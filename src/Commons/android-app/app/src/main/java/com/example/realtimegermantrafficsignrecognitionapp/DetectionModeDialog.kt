package com.example.realtimegermantrafficsignrecognitionapp

import android.content.Context
import androidx.appcompat.app.AlertDialog
import com.example.realtimegermantrafficsignrecognitionapp.DTOs.DetectionMode
import com.google.android.material.dialog.MaterialAlertDialogBuilder

class DetectionModeDialog(context: Context, private var appSettings: AppSettings) : MaterialAlertDialogBuilder(context)
{
    private var selectedDetectionMode:DetectionMode=appSettings.detectionMode

    init {
        updateSingleChoiceItems()
        this
        .setNegativeButton(context.resources.getString(R.string.cancel)) { _, _ ->
            selectedDetectionMode=appSettings.detectionMode
        }
        .setPositiveButton(context.resources.getString(R.string.apply)) { dialog, which ->
            appSettings.detectionMode=selectedDetectionMode
        }
    }

    override fun show(): AlertDialog
    {
        updateSingleChoiceItems()
        return super.show()
    }

    private fun updateSingleChoiceItems()
    {
        this.setSingleChoiceItems(
                arrayOf(
                    "Traditional Image Detection",
                    "Machine Learning Image Detection"
                ), if (selectedDetectionMode == DetectionMode.TRADITIONAL) 0 else 1
            )
            { _, selectedItem ->
                selectedDetectionMode = if (selectedItem == 0) DetectionMode.TRADITIONAL else DetectionMode.MACHINE_LEARNING
            }
    }
}