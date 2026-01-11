package com.qrscanner.utility.ui

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.qrscanner.utility.R
import com.qrscanner.utility.databinding.ActivityHistoryBinding

class HistoryActivity : AppCompatActivity() {
    
    private lateinit var binding: ActivityHistoryBinding
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityHistoryBinding.inflate(layoutInflater)
        setContentView(binding.root)
        
        setupToolbar()
    }
    
    private fun setupToolbar() {
        setSupportActionBar(binding.toolbar)
        supportActionBar?.setDisplayHomeAsUpEnabled(true)
        supportActionBar?.title = getString(R.string.history)
        
        binding.toolbar.setNavigationOnClickListener {
            onBackPressed()
        }
    }
}
