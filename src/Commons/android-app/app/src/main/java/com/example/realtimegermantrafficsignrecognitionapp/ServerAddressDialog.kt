package com.example.realtimegermantrafficsignrecognitionapp

import android.content.Context
import android.widget.EditText
import android.widget.LinearLayout
import android.widget.TextView
import androidx.appcompat.app.AlertDialog
import androidx.core.view.setPadding
import com.google.android.material.dialog.MaterialAlertDialogBuilder


class ServerAddressDialog(context: Context, private var appSettings: AppSettings) : MaterialAlertDialogBuilder(context)
{
    lateinit var ipEditText: EditText
    lateinit var portEditText: EditText

    init {
        updateDialogContent()
        this
        .setNegativeButton(context.resources.getString(R.string.cancel)) { _, _ ->
            updateEditTexts()
        }
        .setPositiveButton(context.resources.getString(R.string.apply)) { dialog, which ->
            appSettings.ip = ipEditText.text.toString()
            appSettings.port = Integer.parseInt(portEditText.text.toString())
        }
    }

    override fun show(): AlertDialog
    {
        updateDialogContent()
        return super.show()
    }

    private fun updateDialogContent()
    {
        val linearLayout = LinearLayout(context)
        linearLayout.orientation = LinearLayout.VERTICAL
        linearLayout.setPadding(40)
        this.ipEditText = EditText(context)
        this.ipEditText.isSingleLine=true
        this.portEditText = EditText(context)
        this.portEditText.isSingleLine=true
        linearLayout.addView(ipEditText)
        linearLayout.addView(portEditText)

        updateEditTexts()
        this.setView(linearLayout)
    }

    private fun updateEditTexts()
    {
        ipEditText.setText(appSettings.ip, TextView.BufferType.EDITABLE)
        portEditText.setText(appSettings.port.toString(), TextView.BufferType.EDITABLE)
    }
}