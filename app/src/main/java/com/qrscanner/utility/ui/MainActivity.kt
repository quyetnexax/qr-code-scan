package com.qrscanner.utility.ui

import android.Manifest
import android.animation.ObjectAnimator
import android.animation.ValueAnimator
import android.app.Activity
import android.content.Intent
import android.content.pm.PackageManager
import android.graphics.Bitmap
import android.graphics.ImageDecoder
import android.net.Uri
import android.os.Build
import android.os.Bundle
import android.os.Vibrator
import android.provider.MediaStore
import android.view.View
import android.view.animation.LinearInterpolator
import android.widget.Toast
import androidx.activity.result.contract.ActivityResultContracts
import androidx.appcompat.app.AppCompatActivity
import androidx.camera.core.*
import androidx.camera.lifecycle.ProcessCameraProvider
import androidx.core.app.ActivityCompat
import androidx.core.content.ContextCompat
import com.google.mlkit.vision.barcode.BarcodeScanning
import com.google.mlkit.vision.barcode.common.Barcode
import com.google.mlkit.vision.common.InputImage
import com.qrscanner.utility.R
import com.qrscanner.utility.databinding.ActivityMainBinding
import java.util.concurrent.ExecutorService
import java.util.concurrent.Executors

class MainActivity : AppCompatActivity() {
    
    private lateinit var binding: ActivityMainBinding
    private lateinit var cameraExecutor: ExecutorService
    private var imageAnalyzer: ImageAnalysis? = null
    private var isScanning = true
    private var lastScanTime = 0L
    private var scanLineAnimator: ObjectAnimator? = null
    
    private val imagePickerLauncher = registerForActivityResult(
        ActivityResultContracts.StartActivityForResult()
    ) { result ->
        if (result.resultCode == Activity.RESULT_OK) {
            result.data?.data?.let { uri ->
                processImageFromGallery(uri)
            }
        }
    }
    
    companion object {
        private const val CAMERA_PERMISSION_REQUEST = 100
        private const val SCAN_DELAY = 2000L // 2 seconds between scans
    }
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)
        
        setupToolbar()
        setupButtons()
        startScanLineAnimation()
        cameraExecutor = Executors.newSingleThreadExecutor()
        
        if (checkCameraPermission()) {
            startCamera()
        } else {
            requestCameraPermission()
        }
    }
    
    private fun setupToolbar() {
        // No toolbar in new design
    }
    
    private fun setupButtons() {
        binding.btnHistory.setOnClickListener {
            startActivity(Intent(this, HistoryActivity::class.java))
        }
        
        binding.btnSettings.setOnClickListener {
            startActivity(Intent(this, SettingsActivity::class.java))
        }
        
        binding.btnScan.setOnClickListener {
            openImagePicker()
        }
    }
    
    private fun openImagePicker() {
        val intent = Intent(Intent.ACTION_PICK)
        intent.type = "image/*"
        imagePickerLauncher.launch(intent)
    }
    
    private fun processImageFromGallery(uri: Uri) {
        try {
            val bitmap = if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.P) {
                ImageDecoder.decodeBitmap(ImageDecoder.createSource(contentResolver, uri))
            } else {
                @Suppress("DEPRECATION")
                MediaStore.Images.Media.getBitmap(contentResolver, uri)
            }
            
            val image = InputImage.fromBitmap(bitmap, 0)
            val scanner = BarcodeScanning.getClient()
            
            scanner.process(image)
                .addOnSuccessListener { barcodes ->
                    if (barcodes.isNotEmpty()) {
                        val barcode = barcodes[0]
                        barcode.rawValue?.let { rawValue ->
                            handleQRCodeFromImage(rawValue, barcode)
                        }
                    } else {
                        Toast.makeText(
                            this,
                            "Không nhận diện được QR, hãy thử lại",
                            Toast.LENGTH_LONG
                        ).show()
                    }
                }
                .addOnFailureListener {
                    Toast.makeText(
                        this,
                        "Không nhận diện được QR, hãy thử lại",
                        Toast.LENGTH_LONG
                    ).show()
                }
        } catch (e: Exception) {
            Toast.makeText(
                this,
                "Không nhận diện được QR, hãy thử lại",
                Toast.LENGTH_LONG
            ).show()
        }
    }
    
    private fun handleQRCodeFromImage(rawValue: String, barcode: Barcode) {
        // Vibrate
        val vibrator = getSystemService(VIBRATOR_SERVICE) as Vibrator
        vibrator.vibrate(100)
        
        runOnUiThread {
            openResultActivity(rawValue)
        }
    }
    
    private fun checkCameraPermission(): Boolean {
        return ContextCompat.checkSelfPermission(
            this,
            Manifest.permission.CAMERA
        ) == PackageManager.PERMISSION_GRANTED
    }
    
    private fun requestCameraPermission() {
        ActivityCompat.requestPermissions(
            this,
            arrayOf(Manifest.permission.CAMERA),
            CAMERA_PERMISSION_REQUEST
        )
    }
    
    override fun onRequestPermissionsResult(
        requestCode: Int,
        permissions: Array<out String>,
        grantResults: IntArray
    ) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults)
        if (requestCode == CAMERA_PERMISSION_REQUEST) {
            if (grantResults.isNotEmpty() && grantResults[0] == PackageManager.PERMISSION_GRANTED) {
                startCamera()
            } else {
                Toast.makeText(
                    this,
                    getString(R.string.camera_permission_required),
                    Toast.LENGTH_LONG
                ).show()
                finish()
            }
        }
    }
    
    private fun startCamera() {
        val cameraProviderFuture = ProcessCameraProvider.getInstance(this)
        
        cameraProviderFuture.addListener({
            val cameraProvider = cameraProviderFuture.get()
            
            val preview = Preview.Builder()
                .build()
                .also {
                    it.setSurfaceProvider(binding.previewView.surfaceProvider)
                }
            
            imageAnalyzer = ImageAnalysis.Builder()
                .setBackpressureStrategy(ImageAnalysis.STRATEGY_KEEP_ONLY_LATEST)
                .build()
                .also {
                    it.setAnalyzer(cameraExecutor, QRCodeAnalyzer())
                }
            
            val cameraSelector = CameraSelector.DEFAULT_BACK_CAMERA
            
            try {
                cameraProvider.unbindAll()
                cameraProvider.bindToLifecycle(
                    this,
                    cameraSelector,
                    preview,
                    imageAnalyzer
                )
            } catch (e: Exception) {
                Toast.makeText(this, "Camera initialization failed", Toast.LENGTH_SHORT).show()
            }
            
        }, ContextCompat.getMainExecutor(this))
    }
    
    private inner class QRCodeAnalyzer : ImageAnalysis.Analyzer {
        private val scanner = BarcodeScanning.getClient()
        
        @androidx.camera.core.ExperimentalGetImage
        override fun analyze(imageProxy: ImageProxy) {
            val mediaImage = imageProxy.image
            if (mediaImage != null && isScanning) {
                val currentTime = System.currentTimeMillis()
                if (currentTime - lastScanTime > SCAN_DELAY) {
                    val image = InputImage.fromMediaImage(
                        mediaImage,
                        imageProxy.imageInfo.rotationDegrees
                    )
                    
                    scanner.process(image)
                        .addOnSuccessListener { barcodes ->
                            for (barcode in barcodes) {
                                handleQRCode(barcode)
                            }
                        }
                        .addOnCompleteListener {
                            imageProxy.close()
                        }
                } else {
                    imageProxy.close()
                }
            } else {
                imageProxy.close()
            }
        }
    }
    
    private fun handleQRCode(barcode: Barcode) {
        lastScanTime = System.currentTimeMillis()
        val rawValue = barcode.rawValue ?: return
        
        // Vibrate on successful scan
        val vibrator = getSystemService(VIBRATOR_SERVICE) as Vibrator
        vibrator.vibrate(100)
        
        runOnUiThread {
            // Open Result Activity
            openResultActivity(rawValue)
        }
    }
    
    private fun openResultActivity(content: String) {
        val intent = Intent(this, ResultActivity::class.java)
        intent.putExtra("QR_CONTENT", content)
        startActivity(intent)
    }
    
    private fun startScanLineAnimation() {
        binding.scanLine.post {
            // Lấy kích thước khung QR
            val qrFrameHeight = binding.qrFrame.height.toFloat()
            
            if (qrFrameHeight > 0) {
                // Animation di chuyển từ trên xuống trong khung QR
                scanLineAnimator = ObjectAnimator.ofFloat(
                    binding.scanLine,
                    "translationY",
                    -qrFrameHeight / 2,
                    qrFrameHeight / 2
                ).apply {
                    duration = 2000 // 2 giây
                    repeatCount = ValueAnimator.INFINITE
                    repeatMode = ValueAnimator.REVERSE
                    interpolator = LinearInterpolator()
                    start()
                }
            }
        }
    }
    
    override fun onDestroy() {
        super.onDestroy()
        scanLineAnimator?.cancel()
        cameraExecutor.shutdown()
    }
    
    override fun onPause() {
        super.onPause()
        scanLineAnimator?.pause()
        isScanning = false
    }
    
    override fun onResume() {
        super.onResume()
        scanLineAnimator?.resume()
        isScanning = true
    }
}
