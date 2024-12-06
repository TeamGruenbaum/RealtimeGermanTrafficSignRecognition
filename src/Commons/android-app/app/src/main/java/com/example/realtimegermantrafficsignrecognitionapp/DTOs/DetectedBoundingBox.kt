package com.example.realtimegermantrafficsignrecognitionapp.DTOs

import android.graphics.Rect

data class DetectedBoundingBox(val topLeft:Point, val topRight: Point, val bottomRight:Point, val bottomLeft:Point, val className:String)