import sys
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.abspath("."))
sys.path.append(os.path.abspath(".."))
sys.path.append(os.path.abspath("../MachineLearningImageAnalysis"))
sys.path.append(os.path.abspath("../TraditionalImageAnalysis"))


from Commons.DetectorDrawer import DetectorDrawer
from MachineLearningImageAnalysis.MachineLearningImageAnalysisDetector import MachineLearningImageAnalysisDetector
from TraditionalImageAnalysis.TemplateImage import TemplateImage
from TraditionalImageAnalysis.TraditionalImageAnalysisDetector import TraditionalImageAnalysisDetector

detector_drawer = DetectorDrawer("green", 7, "Arial.ttf", 20, "green")
machine_learning_image_analysis_detector = MachineLearningImageAnalysisDetector(
    model_path='../MachineLearningImageAnalysis/best.pt',
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
    prediction_image_size=640
)
traditional_image_analysis_detector = TraditionalImageAnalysisDetector(
    template_images=[
        TemplateImage('../TraditionalImageAnalysis/traffic_sign_images/Hoechstgeschwindigkeit 20.png', 'Hoechstgeschwindigkeit 20'),
        TemplateImage('../TraditionalImageAnalysis/traffic_sign_images/Hoechstgeschwindigkeit 30.png', 'Hoechstgeschwindigkeit 30'),
        TemplateImage('../TraditionalImageAnalysis/traffic_sign_images/Hoechstgeschwindigkeit 50.png', 'Hoechstgeschwindigkeit 50'),
        TemplateImage('../TraditionalImageAnalysis/traffic_sign_images/Hoechstgeschwindigkeit 60.png', 'Hoechstgeschwindigkeit 60'),
        TemplateImage('../TraditionalImageAnalysis/traffic_sign_images/Hoechstgeschwindigkeit 70.png', 'Hoechstgeschwindigkeit 70'),
        TemplateImage('../TraditionalImageAnalysis/traffic_sign_images/Hoechstgeschwindigkeit 80.png', 'Hoechstgeschwindigkeit 80'),
        TemplateImage('../TraditionalImageAnalysis/traffic_sign_images/Ende Hoechstgeschwindigkeit 80.png', 'Ende Hoechstgeschwindigkeit 80'),
        TemplateImage('../TraditionalImageAnalysis/traffic_sign_images/Hoechstgeschwindigkeit 100.png', 'Hoechstgeschwindigkeit 100'),
        TemplateImage('../TraditionalImageAnalysis/traffic_sign_images/Hoechstgeschwindigkeit 120.png', 'Hoechstgeschwindigkeit 120'),
        TemplateImage('../TraditionalImageAnalysis/traffic_sign_images/Ueberholverbot.png', 'Ueberholverbot'),
        TemplateImage('../TraditionalImageAnalysis/traffic_sign_images/Ueberholverbot für Kfz ueber 3,5t.png', 'Ueberholverbot für Kfz ueber 3,5t'),
        TemplateImage('../TraditionalImageAnalysis/traffic_sign_images/Vorfahrt an der naechsten Kreuzung.png', 'Vorfahrt an der naechsten Kreuzung'),
        TemplateImage('../TraditionalImageAnalysis/traffic_sign_images/Vorfahrtstrasse.png', 'Vorfahrtstrasse'),
        TemplateImage('../TraditionalImageAnalysis/traffic_sign_images/Vorfahrt gewaehren.png', 'Vorfahrt gewaehren'),
        TemplateImage('../TraditionalImageAnalysis/traffic_sign_images/Halt. Vorfahrt gewaehren.png', 'Halt. Vorfahrt gewaehren'),
        TemplateImage('../TraditionalImageAnalysis/traffic_sign_images/Verbot fuer Fahrzeuge aller Art.png', 'Verbot fuer Fahrzeuge aller Art'),
        TemplateImage('../TraditionalImageAnalysis/traffic_sign_images/Verbot für Kfz ueber 3,5t.png', 'Verbot für Kfz ueber 3,5t'),
        TemplateImage('../TraditionalImageAnalysis/traffic_sign_images/Verbot der Einfahrt.png', 'Verbot der Einfahrt'),
        TemplateImage('../TraditionalImageAnalysis/traffic_sign_images/Gefahrstelle.png', 'Gefahrstelle'),
        TemplateImage('../TraditionalImageAnalysis/traffic_sign_images/Kurve links.png', 'Kurve links'),
        TemplateImage('../TraditionalImageAnalysis/traffic_sign_images/Kurve rechts.png', 'Kurve rechts'),
        TemplateImage('../TraditionalImageAnalysis/traffic_sign_images/Doppelkurve links.png', 'Doppelkurve links'),
        TemplateImage('../TraditionalImageAnalysis/traffic_sign_images/Unebene Fahrbahn.png', 'Unebene Fahrbahn'),
        TemplateImage('../TraditionalImageAnalysis/traffic_sign_images/Schleuder- oder Rutschgefahr.png', 'Schleuder- oder Rutschgefahr'),
        TemplateImage('../TraditionalImageAnalysis/traffic_sign_images/Einseitig verenge Fahrbahn.png', 'Einseitig verenge Fahrbahn'),
        TemplateImage('../TraditionalImageAnalysis/traffic_sign_images/Arbeitsstelle.png', 'Arbeitsstelle'),
        TemplateImage('../TraditionalImageAnalysis/traffic_sign_images/Lichtzeichenanlage.png', 'Lichtzeichenanlage'),
        TemplateImage('../TraditionalImageAnalysis/traffic_sign_images/Fußgaenger.png', 'Fußgaenger'),
        TemplateImage('../TraditionalImageAnalysis/traffic_sign_images/Kinder.png', 'Kinder'),
        TemplateImage('../TraditionalImageAnalysis/traffic_sign_images/Radverkehr.png', 'Radverkehr'),
        TemplateImage('../TraditionalImageAnalysis/traffic_sign_images/Schnee- und Eisglatt.png', 'Schnee- und Eisglatt'),
        TemplateImage('../TraditionalImageAnalysis/traffic_sign_images/Wildwechsel.png', 'Wildwechsel'),
        TemplateImage('../TraditionalImageAnalysis/traffic_sign_images/Ende saemtlicher streckenbezogenen Geschwindigkeitsbeschraenkungen und Ueberholverbote.png', 'Ende saemtlicher streckenbezogenen Geschwindigkeitsbeschraenkungen und Ueberholverbote'),
        TemplateImage('../TraditionalImageAnalysis/traffic_sign_images/Rechts.png', 'Rechts'),
        TemplateImage('../TraditionalImageAnalysis/traffic_sign_images/Links.png', 'Links'),
        TemplateImage('../TraditionalImageAnalysis/traffic_sign_images/Geradeaus.png', 'Geradeaus'),
        TemplateImage('../TraditionalImageAnalysis/traffic_sign_images/Geradeaus oder Rechts.png', 'Geradeaus oder Rechts'),
        TemplateImage('../TraditionalImageAnalysis/traffic_sign_images/Geradeaus oder Links.png', 'Geradeaus oder Links'),
        TemplateImage('../TraditionalImageAnalysis/traffic_sign_images/Rechts vorbei.png', 'Rechts vorbei'),
        TemplateImage('../TraditionalImageAnalysis/traffic_sign_images/Links vorbei.png', 'Links vorbei'),
        TemplateImage('../TraditionalImageAnalysis/traffic_sign_images/Kreisverkehr.png', 'Kreisverkehr'),
        TemplateImage('../TraditionalImageAnalysis/traffic_sign_images/Ende des Ueberholverbots.png', 'Ende des Ueberholverbots'),
        TemplateImage('../TraditionalImageAnalysis/traffic_sign_images/Ende des Ueberholverbots fuer Kfz ueber 3,5t.png', 'Ende des Ueberholverbots fuer Kfz ueber 3,5t'),
    ],
    needed_matches=50
)


source_gtsrb_folder_path_string = "/Users/stevensolleder/Desktop/source/gtsrb"
source_gtsdb_folder_path_string = "/Users/stevensolleder/Desktop/source/gtsdb"

detector_drawer.draw_bounding_boxes_and_class_names_in_images(
    detector=machine_learning_image_analysis_detector,
    source_folder_path_string=source_gtsrb_folder_path_string,
    results_folder_path_string="/Users/stevensolleder/Desktop/result/machine_learning_image_analysis_detector",
    content_names_in_file_name=True
)
detector_drawer.draw_bounding_boxes_and_class_names_in_images(
    detector=machine_learning_image_analysis_detector,
    source_folder_path_string=source_gtsdb_folder_path_string,
    results_folder_path_string="/Users/stevensolleder/Desktop/result/machine_learning_image_analysis_detector"
)

detector_drawer.draw_bounding_boxes_and_class_names_in_images(
    detector=traditional_image_analysis_detector,
    source_folder_path_string=source_gtsrb_folder_path_string,
    results_folder_path_string="/Users/stevensolleder/Desktop/result/traditional_image_analysis_detector",
    content_names_in_file_name=False
)
detector_drawer.draw_bounding_boxes_and_class_names_in_images(
    detector=traditional_image_analysis_detector,
    source_folder_path_string=source_gtsdb_folder_path_string,
    results_folder_path_string="/Users/stevensolleder/Desktop/result/traditional_image_analysis_detector"
)
