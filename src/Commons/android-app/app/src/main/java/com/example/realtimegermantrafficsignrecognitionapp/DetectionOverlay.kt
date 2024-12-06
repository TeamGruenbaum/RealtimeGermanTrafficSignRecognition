package com.example.realtimegermantrafficsignrecognitionapp

import android.content.Context
import android.graphics.Canvas
import android.graphics.Color
import android.graphics.Paint
import android.graphics.Path
import android.util.AttributeSet
import android.view.View
import com.example.realtimegermantrafficsignrecognitionapp.DTOs.DetectedBoundingBox

class DetectionOverlay constructor(context: Context?, attributeSet: AttributeSet?): View(context, attributeSet)
{
    private val detectedBoundingBoxes: MutableList<DetectedBoundingBox> = mutableListOf()
    private val boxPaint = Paint().apply {
        style = Paint.Style.STROKE
        color = Color.GREEN
        strokeWidth = 10f
    }
    private val textPaint = Paint().apply {
        style = Paint.Style.STROKE
        color = Color.GREEN
        strokeWidth = 6f
        textSize = 55f
    }

    override fun onDraw(canvas: Canvas)
    {
        super.onDraw(canvas)
        detectedBoundingBoxes.forEach {

            canvas.drawPath(
                Path().apply {
                    moveTo(it.topLeft.x.toFloat(), it.topLeft.y.toFloat())
                    lineTo(it.topRight.x.toFloat(), it.topRight.y.toFloat())
                    lineTo(it.bottomRight.x.toFloat(), it.bottomRight.y.toFloat())
                    lineTo(it.bottomLeft.x.toFloat(), it.bottomLeft.y.toFloat())
                    close()
                },
                boxPaint
            )

            canvas.drawText(it.className, it.bottomLeft.x.toFloat(), it.bottomLeft.y.toFloat() + 70f, textPaint)
        }
    }

    fun drawDetectedBoundingBoxes(detectedBoundingBoxes: List<DetectedBoundingBox>)
    {
        this.detectedBoundingBoxes.clear()
        this.detectedBoundingBoxes.addAll(detectedBoundingBoxes)
        invalidate()
    }
}