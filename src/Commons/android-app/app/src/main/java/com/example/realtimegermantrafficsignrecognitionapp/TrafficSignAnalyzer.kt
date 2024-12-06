package com.example.realtimegermantrafficsignrecognitionapp

import android.graphics.Bitmap
import android.graphics.Bitmap.CompressFormat
import android.graphics.Matrix
import android.graphics.Rect
import android.media.Image
import android.speech.tts.TextToSpeech
import android.util.Log
import android.widget.Toast
import androidx.annotation.OptIn
import androidx.camera.core.ExperimentalGetImage
import androidx.camera.core.ImageAnalysis
import androidx.camera.core.ImageProxy
import androidx.camera.view.PreviewView
import com.example.realtimegermantrafficsignrecognitionapp.DTOs.DetectedBoundingBox
import com.example.realtimegermantrafficsignrecognitionapp.DTOs.DetectionMode
import com.example.realtimegermantrafficsignrecognitionapp.DTOs.Point
import com.example.realtimegermantrafficsignrecognitionapp.DTOs.ServerResponse
import io.ktor.client.*
import io.ktor.client.call.body
import io.ktor.client.engine.android.*
import io.ktor.client.plugins.contentnegotiation.*
import io.ktor.client.request.*
import io.ktor.client.request.forms.formData
import io.ktor.client.request.forms.submitFormWithBinaryData
import io.ktor.client.statement.HttpResponse
import io.ktor.http.Headers
import io.ktor.http.HttpHeaders
import io.ktor.serialization.kotlinx.json.*
import kotlinx.coroutines.runBlocking
import java.io.ByteArrayOutputStream


class TrafficSignAnalyzer (val detectionOverlay:DetectionOverlay, val appSettings: AppSettings, var previewView: PreviewView, var textToSpeech: TextToSpeech): ImageAnalysis.Analyzer
{
    private val client:HttpClient
    private lateinit var matrix:Matrix
    private lateinit var detectedClassNames:List<String>

    private val requestServerAddress:String
        get() = "http://${appSettings.ip}:${appSettings.port}/"
    private val requestDetectionMode:String
        get() = if (appSettings.detectionMode == DetectionMode.MACHINE_LEARNING) "machine-learning-image-analysis/image-detection-results" else "traditional-image-analysis/image-detection-results"


    init
    {
        client = HttpClient(Android)
        {
            install(ContentNegotiation)
            {
                json()
            }
        }
    }

    @OptIn(ExperimentalGetImage::class) override fun analyze(imageProxy: ImageProxy)
    {
        imageProxy.use{
            it.image ?: return@use

            if (!this::matrix.isInitialized) matrix = createMatrix(it, previewView)

            val (imageByteArray:ByteArray?, croppedBitmap:Bitmap) = convertBitmapToByteArray(it.toBitmap(), it.cropRect, matrix)
            if(imageByteArray==null) return@use

            try
            {
                runBlocking {
                    val httpResponse: HttpResponse = client.submitFormWithBinaryData(
                        url = requestServerAddress + requestDetectionMode,
                        formData = formData {
                            append("image", imageByteArray, Headers.build {
                                append(HttpHeaders.ContentType, "image/png")
                                append(HttpHeaders.ContentDisposition, "filename=\"image.png\"")
                            })
                        }
                    )

                    if (httpResponse.status.value in 200..299)
                    {
                        val serverResponse:ServerResponse = httpResponse.body()
                        detectedClassNames = serverResponse.imageDetectionResults.map { it.content }

                        detectionOverlay.drawDetectedBoundingBoxes(serverResponse.imageDetectionResults.map {
                            DetectedBoundingBox(
                                Point(
                                    ((it.frameCoordinates.topLeft.x/croppedBitmap.width.toFloat())*(detectionOverlay.width)).toInt(),
                                    ((it.frameCoordinates.topLeft.y/croppedBitmap.height.toFloat())*(detectionOverlay.height)).toInt()
                                ),
                                Point(
                                    ((it.frameCoordinates.topRight.x/croppedBitmap.width.toFloat())*(detectionOverlay.width)).toInt(),
                                    ((it.frameCoordinates.topRight.y/croppedBitmap.height.toFloat())*(detectionOverlay.height)).toInt()
                                ),
                                Point(
                                    ((it.frameCoordinates.bottomRight.x/croppedBitmap.width.toFloat())*(detectionOverlay.width)).toInt(),
                                    ((it.frameCoordinates.bottomRight.y/croppedBitmap.height.toFloat())*(detectionOverlay.height)).toInt()
                                ),
                                Point(
                                    ((it.frameCoordinates.bottomLeft.x/croppedBitmap.width.toFloat())*(detectionOverlay.width)).toInt(),
                                    ((it.frameCoordinates.bottomLeft.y/croppedBitmap.height.toFloat())*(detectionOverlay.height)).toInt()
                                ),
                                it.content
                            )
                        })
                    }
                }
            }
            catch (exception: Exception)
            {
                Log.d("Problem","Can't connect to server.")
            }
        }
    }

    fun readOutDetectedClassNames()
    {
        if (this::detectedClassNames.isInitialized && !detectedClassNames.isEmpty())
        {
            detectedClassNames.forEach { textToSpeech.speak(it, TextToSpeech.QUEUE_ADD, null,"") }
        }
    }

    private fun convertBitmapToByteArray(bitmap: Bitmap, cropRect:Rect, matrix:Matrix):Pair<ByteArray?, Bitmap>
    {
        val bitmapWithoutAlpha = Bitmap.createBitmap(bitmap, cropRect.left, cropRect.top, cropRect.width(), cropRect.height(), matrix, false).copy(Bitmap.Config.RGB_565, false)
        val stream = ByteArrayOutputStream()
        bitmapWithoutAlpha.compress(CompressFormat.PNG, 80, stream)
        return Pair(stream.toByteArray(), bitmapWithoutAlpha)
    }

    private fun createMatrix(imageProxy: ImageProxy, previewView: PreviewView) : Matrix
    {
        val sourceArray:FloatArray = imageProxy.cropRect.run { floatArrayOf(left.toFloat(), top.toFloat(), right.toFloat(), top.toFloat(), right.toFloat(), bottom.toFloat(), left.toFloat(), bottom.toFloat()) }
        val destinationArray:FloatArray = floatArrayOf(0f, 0f, previewView.width.toFloat(), 0f, previewView.width.toFloat(), previewView.height.toFloat(), 0f, previewView.height.toFloat())

        val clonedDestinationArray:FloatArray = destinationArray.clone()
        for (index in sourceArray.indices) destinationArray[index] = clonedDestinationArray[(index + imageProxy.imageInfo.rotationDegrees / 90 * 2) % sourceArray.size]

        return Matrix().apply {setPolyToPoly(sourceArray, 0, destinationArray, 0, 4)}
    }
}