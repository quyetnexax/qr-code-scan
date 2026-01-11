package com.qrscanner.utility.ui

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.qrscanner.utility.R
import com.qrscanner.utility.databinding.ActivityPrivacyPolicyBinding

class PrivacyPolicyActivity : AppCompatActivity() {
    
    private lateinit var binding: ActivityPrivacyPolicyBinding
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityPrivacyPolicyBinding.inflate(layoutInflater)
        setContentView(binding.root)
        
        setupToolbar()
        loadPrivacyPolicy()
    }
    
    private fun setupToolbar() {
        setSupportActionBar(binding.toolbar)
        supportActionBar?.setDisplayHomeAsUpEnabled(true)
        supportActionBar?.title = getString(R.string.privacy_policy)
        
        binding.toolbar.setNavigationOnClickListener {
            onBackPressed()
        }
    }
    
    private fun loadPrivacyPolicy() {
        binding.webView.settings.javaScriptEnabled = false
        binding.webView.loadUrl("file:///android_asset/privacy_policy.html")
    }
}
