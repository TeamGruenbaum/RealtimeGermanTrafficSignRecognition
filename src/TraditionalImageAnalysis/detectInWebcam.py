import sys
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.abspath("."))
sys.path.append(os.path.abspath(".."))
sys.path.append(os.path.abspath("../Commons"))
sys.path.append(os.path.abspath("../MachineLearningImageAnalysis"))


import cv2

from TraditionalImageAnalysis.TemplateImage import TemplateImage
from TraditionalImageAnalysis.TraditionalImageAnalysisDetector import TraditionalImageAnalysisDetector
from Commons.WebcamDetection import WebcamDetection


traditional_image_analysis_detector = TraditionalImageAnalysisDetector(
    template_images=[
        TemplateImage('./traffic_sign_images/Hoechstgeschwindigkeit 20.png', 'Hoechstgeschwindigkeit 20'),
        TemplateImage('./traffic_sign_images/Hoechstgeschwindigkeit 30.png', 'Hoechstgeschwindigkeit 30'),
        TemplateImage('./traffic_sign_images/Hoechstgeschwindigkeit 50.png', 'Hoechstgeschwindigkeit 50'),
        TemplateImage('./traffic_sign_images/Hoechstgeschwindigkeit 60.png', 'Hoechstgeschwindigkeit 60'),
        TemplateImage('./traffic_sign_images/Hoechstgeschwindigkeit 70.png', 'Hoechstgeschwindigkeit 70'),
        TemplateImage('./traffic_sign_images/Hoechstgeschwindigkeit 80.png', 'Hoechstgeschwindigkeit 80'),
        TemplateImage('./traffic_sign_images/Ende Hoechstgeschwindigkeit 80.png', 'Ende Hoechstgeschwindigkeit 80'),
        TemplateImage('./traffic_sign_images/Hoechstgeschwindigkeit 100.png', 'Hoechstgeschwindigkeit 100'),
        TemplateImage('./traffic_sign_images/Hoechstgeschwindigkeit 120.png', 'Hoechstgeschwindigkeit 120'),
        TemplateImage('./traffic_sign_images/Ueberholverbot.png', 'Ueberholverbot'),
        TemplateImage('./traffic_sign_images/Ueberholverbot für Kfz ueber 3,5t.png', 'Ueberholverbot für Kfz ueber 3,5t'),
        TemplateImage('./traffic_sign_images/Vorfahrt an der naechsten Kreuzung.png', 'Vorfahrt an der naechsten Kreuzung'),
        TemplateImage('./traffic_sign_images/Vorfahrtstrasse.png', 'Vorfahrtstrasse'),
        TemplateImage('./traffic_sign_images/Vorfahrt gewaehren.png', 'Vorfahrt gewaehren'),
        TemplateImage('./traffic_sign_images/Halt. Vorfahrt gewaehren.png', 'Halt. Vorfahrt gewaehren'),
        TemplateImage('./traffic_sign_images/Verbot fuer Fahrzeuge aller Art.png', 'Verbot fuer Fahrzeuge aller Art'),
        TemplateImage('./traffic_sign_images/Verbot für Kfz ueber 3,5t.png', 'Verbot für Kfz ueber 3,5t'),
        TemplateImage('./traffic_sign_images/Verbot der Einfahrt.png', 'Verbot der Einfahrt'),
        TemplateImage('./traffic_sign_images/Gefahrstelle.png', 'Gefahrstelle'),
        TemplateImage('./traffic_sign_images/Kurve links.png', 'Kurve links'),
        TemplateImage('./traffic_sign_images/Kurve rechts.png', 'Kurve rechts'),
        TemplateImage('./traffic_sign_images/Doppelkurve links.png', 'Doppelkurve links'),
        TemplateImage('./traffic_sign_images/Unebene Fahrbahn.png', 'Unebene Fahrbahn'),
        TemplateImage('./traffic_sign_images/Schleuder- oder Rutschgefahr.png', 'Schleuder- oder Rutschgefahr'),
        TemplateImage('./traffic_sign_images/Einseitig verenge Fahrbahn.png', 'Einseitig verenge Fahrbahn'),
        TemplateImage('./traffic_sign_images/Arbeitsstelle.png', 'Arbeitsstelle'),
        TemplateImage('./traffic_sign_images/Lichtzeichenanlage.png', 'Lichtzeichenanlage'),
        TemplateImage('./traffic_sign_images/Fußgaenger.png', 'Fußgaenger'),
        TemplateImage('./traffic_sign_images/Kinder.png', 'Kinder'),
        TemplateImage('./traffic_sign_images/Radverkehr.png', 'Radverkehr'),
        TemplateImage('./traffic_sign_images/Schnee- und Eisglatt.png', 'Schnee- und Eisglatt'),
        TemplateImage('./traffic_sign_images/Wildwechsel.png', 'Wildwechsel'),
        TemplateImage('./traffic_sign_images/Ende saemtlicher streckenbezogenen Geschwindigkeitsbeschraenkungen und Ueberholverbote.png', 'Ende saemtlicher streckenbezogenen Geschwindigkeitsbeschraenkungen und Ueberholverbote'),
        TemplateImage('./traffic_sign_images/Rechts.png', 'Rechts'),
        TemplateImage('./traffic_sign_images/Links.png', 'Links'),
        TemplateImage('./traffic_sign_images/Geradeaus.png', 'Geradeaus'),
        TemplateImage('./traffic_sign_images/Geradeaus oder Rechts.png', 'Geradeaus oder Rechts'),
        TemplateImage('./traffic_sign_images/Geradeaus oder Links.png', 'Geradeaus oder Links'),
        TemplateImage('./traffic_sign_images/Rechts vorbei.png', 'Rechts vorbei'),
        TemplateImage('./traffic_sign_images/Links vorbei.png', 'Links vorbei'),
        TemplateImage('./traffic_sign_images/Kreisverkehr.png', 'Kreisverkehr'),
        TemplateImage('./traffic_sign_images/Ende des Ueberholverbots.png', 'Ende des Ueberholverbots'),
        TemplateImage('./traffic_sign_images/Ende des Ueberholverbots fuer Kfz ueber 3,5t.png', 'Ende des Ueberholverbots fuer Kfz ueber 3,5t'),
    ],
    needed_matches=50
)

webcam_detection = WebcamDetection(
    detector=traditional_image_analysis_detector,
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
