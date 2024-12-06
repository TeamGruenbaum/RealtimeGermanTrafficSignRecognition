package com.example.realtimegermantrafficsignrecognitionapp.DTOs

import kotlinx.serialization.Serializable

@Serializable
class ServerResponse(val imageDetectionResults:Array<ImageDetectionResult>, val requestId:Int?)