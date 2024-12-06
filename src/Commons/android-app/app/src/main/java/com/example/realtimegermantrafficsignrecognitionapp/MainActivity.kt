package com.example.realtimegermantrafficsignrecognitionapp

import android.content.pm.PackageManager
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.speech.tts.TextToSpeech
import android.view.MenuItem
import android.view.View
import android.widget.PopupMenu
import android.widget.Toast
import androidx.annotation.MenuRes
import androidx.camera.core.CameraSelector
import androidx.camera.core.ImageAnalysis
import androidx.camera.core.Preview
import androidx.camera.core.UseCaseGroup
import com.google.common.util.concurrent.ListenableFuture
import androidx.camera.lifecycle.ProcessCameraProvider
import androidx.core.app.ActivityCompat
import androidx.core.content.ContextCompat
import androidx.lifecycle.LifecycleOwner
import com.example.realtimegermantrafficsignrecognitionapp.databinding.ActivityMainBinding
import com.google.android.material.dialog.MaterialAlertDialogBuilder
import java.util.Locale
import java.util.concurrent.ExecutorService
import java.util.concurrent.Executors

class MainActivity : AppCompatActivity(), TextToSpeech.OnInitListener
{
    private lateinit var activityMainBinding:ActivityMainBinding
    private lateinit var cameraExecutor:ExecutorService
    private lateinit var detectionModeDialog:MaterialAlertDialogBuilder
    private lateinit var serverAddressDialog:MaterialAlertDialogBuilder
    private lateinit var textToSpeach:TextToSpeech

    override fun onCreate(savedInstanceState: Bundle?)
    {
        super.onCreate(savedInstanceState)
        activityMainBinding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(activityMainBinding.root)

        val appSettings:AppSettings = AppSettings(this)

        textToSpeach = TextToSpeech(this, this)
        val trafficSignAnalyzer:TrafficSignAnalyzer = TrafficSignAnalyzer(activityMainBinding.detectionOverlay, appSettings, activityMainBinding.previewView, textToSpeach)

        activityMainBinding.settingsButton.setOnClickListener { view: View -> showMenu(view, R.menu.settings_menu) }
        activityMainBinding.textToSpeechButton.setOnClickListener { trafficSignAnalyzer.readOutDetectedClassNames() }

        serverAddressDialog = ServerAddressDialog(this, appSettings)
        detectionModeDialog = DetectionModeDialog(this, appSettings)

        if (ContextCompat.checkSelfPermission(this, android.Manifest.permission.CAMERA) == PackageManager.PERMISSION_DENIED)
        {
            ActivityCompat.requestPermissions(this, arrayOf(android.Manifest.permission.CAMERA), 0);
        }

        cameraExecutor = Executors.newSingleThreadExecutor()

        val cameraSelector:CameraSelector = CameraSelector.Builder()
            .requireLensFacing(CameraSelector.LENS_FACING_BACK)
            .build()

        val preview:Preview = Preview.Builder().build()
        preview.setSurfaceProvider(activityMainBinding.previewView.surfaceProvider)

        val imageAnalysis:ImageAnalysis = ImageAnalysis.Builder()
            .setOutputImageFormat(ImageAnalysis.OUTPUT_IMAGE_FORMAT_RGBA_8888)
            .setBackpressureStrategy(ImageAnalysis.STRATEGY_KEEP_ONLY_LATEST)
            .build()
            .apply { this.setAnalyzer(cameraExecutor, trafficSignAnalyzer) }

        val cameraProviderFuture:ListenableFuture<ProcessCameraProvider> = ProcessCameraProvider.getInstance(this)
        cameraProviderFuture.addListener(
        {
            val useCaseGroup=UseCaseGroup.Builder()
                .addUseCase(imageAnalysis)
                .addUseCase(preview)
                .setViewPort(activityMainBinding.previewView.viewPort!!)
                .build()

            cameraProviderFuture.get().bindToLifecycle(
                this as LifecycleOwner,
                cameraSelector,
                useCaseGroup
            )
        }, ContextCompat.getMainExecutor(this))
    }

    override fun onInit(status: Int)
    {
        textToSpeach.setLanguage(Locale.GERMAN)
    }

    private fun showMenu(view:View, @MenuRes menuResource:Int)
    {
        val menu = PopupMenu(this, view)
        menu.menuInflater.inflate(menuResource, menu.menu)

        menu.setOnMenuItemClickListener { menuItem: MenuItem ->
            when (menuItem.itemId) {
                R.id.change_detection_mode -> {
                    detectionModeDialog.show()
                    true
                }
                R.id.change_address -> {
                    serverAddressDialog.show()
                    true
                }
                R.id.developer_information -> {
                    Toast.makeText(this, "Developer information", Toast.LENGTH_SHORT).show()
                    true
                }
                else -> false
            }
        }
        menu.show()
    }

    override fun onDestroy()
    {
        super.onDestroy()
        if (this::textToSpeach.isInitialized)
        {
            textToSpeach.stop()
            textToSpeach.shutdown()
        }
        cameraExecutor.shutdown()
    }
}