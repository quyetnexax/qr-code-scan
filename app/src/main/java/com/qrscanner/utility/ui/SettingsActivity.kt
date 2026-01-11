package com.qrscanner.utility.ui

import android.content.Intent
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.qrscanner.utility.R
import com.qrscanner.utility.databinding.ActivitySettingsBinding

class SettingsActivity : AppCompatActivity() {
    
    private lateinit var binding: ActivitySettingsBinding
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivitySettingsBinding.inflate(layoutInflater)
        setContentView(binding.root)
        
        setupToolbar()
        setupButtons()
    }
    
    private fun setupToolbar() {
        setSupportActionBar(binding.toolbar)
        supportActionBar?.setDisplayHomeAsUpEnabled(true)
        supportActionBar?.title = getString(R.string.settings)
        
        binding.toolbar.setNavigationOnClickListener {
            onBackPressed()
        }
    }
    
    private fun setupButtons() {
        binding.btnPrivacyPolicy.setOnClickListener {
            startActivity(Intent(this, PrivacyPolicyActivity::class.java))
        }
        
        binding.tvVersion.text = "Version ${getAppVersion()}"
    }
    
    private fun getAppVersion(): String {
        return try {
            packageManager.getPackageInfo(packageName, 0).versionName ?: "1.0.0"
        } catch (e: Exception) {
            "1.0.0"
        }
    }
}
