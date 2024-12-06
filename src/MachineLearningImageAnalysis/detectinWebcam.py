import sys
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.abspath("."))
sys.path.append(os.path.abspath(".."))
sys.path.append(os.path.abspath("../Commons"))
sys.path.append(os.path.abspath("../TraditionalImageAnalysis"))


import cv2

from MachineLearningImageAnalysis.MachineLearningImageAnalysisDetector import MachineLearningImageAnalysisDetector
from Commons.WebcamDetection import WebcamDetection


machine_learning_image_analysis_detector = MachineLearningImageAnalysisDetector(
    model_path='best.pt',
    class_names=[
        "Hoechstgeschwindigkeit 20",
        "Hochstgeschwindigkeit 30",
        "Hoechstgeschwindigkeit 50",
        "Hoechstgeschwindigkeit 60",
        "Hoechstgeschwindigkeit 70",
        "Hoechstgeschwindigkeit 80",
        "Ende Hoechstgeschwindigkeit 80",
        "Hoechstgeschwindigkeit 100",
        "Hoechstgeschwindigkeit 120",
        "Ueberholverbot",
        "Ueberholverbot fuer Kfz ueber 3,5t",
        "Vorfahrt an der naechsten Kreuzung",
        "Vorfahrtstraße",
        "Vorfahrt gewaehren",
        "Halt. Vorfahrt gewaehren",
        "Verbot fuer Fahrzeuge aller Art",
        "Verbot fuer Kfz ueber 3,5t",
        "Verbot der Einfahrt",
        "Gefahrstelle",
        "Kurve links",
        "Kurve rechts",
        "Doppelkurve links",
        "Unebene Fahrbahn",
        "Schleuder- oder Rutschgefahr",
        "Einseitig verenge Fahrbahn",
        "Arbeitsstelle",
        "Lichtzeichenanlage",
        "Fußgaenger",
        "Kinder",
        "Radverkehr",
        "Schnee- und Eisglaette",
        "Wildwechsel",
        "Ende saemtlicher streckenbezogenen Geschwindigkeitsbeschraenkungen und ueberholverbote",
        "Rechts",
        "Links",
        "Geradeaus",
        "Geradeaus oder Rechts",
        "Geradeaus oder Links",
        "Rechts vorbei",
        "Links vorbei",
        "Kreisverkehr",
        "Ende des Ueberholverbots",
        "Ende des Ueberholverbots fuer Kfz ueber 3,5t"
    ],
    prediction_image_size=256
)

webcam_detection = WebcamDetection(
    detector=machine_learning_image_analysis_detector,
    box_color=(0, 255, 0),
    box_thickness=2,
    font=cv2.FONT_HERSHEY_SIMPLEX,
    font_scale=1,
    font_color=(255, 255, 255),
    font_thickness=2,
    window_name='Deutsche Verkehrszeichen Erkennung',
    window_close_key='q'
)

webcam_detection.start_detection()
