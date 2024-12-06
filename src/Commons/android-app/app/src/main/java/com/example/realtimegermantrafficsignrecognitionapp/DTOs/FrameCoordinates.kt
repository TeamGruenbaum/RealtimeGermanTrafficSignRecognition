package com.example.realtimegermantrafficsignrecognitionapp.DTOs
import kotlinx.serialization.*

@Serializable
data class FrameCoordinates(val bottomLeft:Point, val bottomRight:Point, val topLeft:Point, val topRight:Point)