package com.example.realtimegermantrafficsignrecognitionapp.DTOs

import kotlinx.serialization.Serializable

@Serializable
data class ImageDetectionResult(val frameCoordinates: FrameCoordinates, val content: String, val confidence: Float?)