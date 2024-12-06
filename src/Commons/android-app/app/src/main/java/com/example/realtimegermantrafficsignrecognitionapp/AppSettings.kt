package com.example.realtimegermantrafficsignrecognitionapp

import android.content.Context
import android.content.SharedPreferences
import com.example.realtimegermantrafficsignrecognitionapp.DTOs.DetectionMode

class AppSettings(context: Context)
{
    private var sharedPreferences: SharedPreferences = context.getSharedPreferences("settings", Context.MODE_PRIVATE)

     var ip: String
        get() = sharedPreferences.getString("ip", null) ?: "192.168.178.1"
        set(value)
        {
            sharedPreferences.edit().apply { putString("ip", value) }.commit()
        }

    var port: Int
        get() = sharedPreferences.getInt("port", 15240)
        set(value)
        {
            sharedPreferences.edit().apply {putInt("port", value) }.commit()
        }

    var detectionMode: DetectionMode
        get() = DetectionMode.valueOf(sharedPreferences.getString("detectionMode", null) ?: DetectionMode.MACHINE_LEARNING.toString())
        set(value)
        {
            sharedPreferences.edit().apply { putString("detectionMode", value.name) }.commit()
        }
}