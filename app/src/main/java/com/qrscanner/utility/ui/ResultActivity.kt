package com.qrscanner.utility.ui

import android.content.ClipData
import android.content.ClipboardManager
import android.content.Intent
import android.net.Uri
import android.os.Bundle
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.qrscanner.utility.R
import com.qrscanner.utility.databinding.ActivityResultBinding

class ResultActivity : AppCompatActivity() {
    
    private lateinit var binding: ActivityResultBinding
    private var qrContent: String = ""
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityResultBinding.inflate(layoutInflater)
        setContentView(binding.root)
        
        qrContent = intent.getStringExtra("QR_CONTENT") ?: ""
        
        setupUI()
        setupButtons()
    }
    
    private fun setupUI() {
        binding.tvQrContent.text = qrContent
    }
    
    private fun setupButtons() {
        binding.btnCopy.setOnClickListener {
            copyToClipboard()
        }
        
        binding.btnOpenLink.setOnClickListener {
            openLink()
        }
        
        binding.btnClose.setOnClickListener {
            finish()
        }
    }
    
    private fun copyToClipboard() {
        val clipboard = getSystemService(CLIPBOARD_SERVICE) as ClipboardManager
        val clip = ClipData.newPlainText("QR Code", qrContent)
        clipboard.setPrimaryClip(clip)
        Toast.makeText(this, getString(R.string.copied_to_clipboard), Toast.LENGTH_SHORT).show()
    }
    
    private fun openLink() {
        if (qrContent.startsWith("http://") || qrContent.startsWith("https://")) {
            try {
                val intent = Intent(Intent.ACTION_VIEW, Uri.parse(qrContent))
                startActivity(intent)
            } catch (e: Exception) {
                Toast.makeText(this, "Cannot open link", Toast.LENGTH_SHORT).show()
            }
        } else {
            Toast.makeText(this, "Not a valid URL", Toast.LENGTH_SHORT).show()
        }
    }
}
