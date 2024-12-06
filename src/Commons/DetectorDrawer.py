import os

import cv2
import numpy
import pathlib
import PIL

from Commons.AbstractDetector import AbstractDetector

class DetectorDrawer:
    def __init__(self, box_color: str, box_thickness: int, font_path_string: str, font_size: int, font_color):
        self.__box_color = box_color
        self.__box_thickness = box_thickness
        self.__font_path_string = font_path_string
        self.__font_size = font_size
        self.__font_color = font_color

    def draw_bounding_boxes_and_class_names_in_images(self, detector: AbstractDetector, source_folder_path_string: str, results_folder_path_string: str, content_names_in_file_name: bool=False) -> None:
        source_folder_path = pathlib.Path(source_folder_path_string)
        results_folder_path = pathlib.Path(results_folder_path_string)

        source_image_paths = [file for file in source_folder_path.iterdir() if file.is_file() and file.suffix.lower() in ['.jpg', '.png', '.jpeg']]

        results_folder_path.mkdir(parents=True, exist_ok=True)

        for source_image_path in source_image_paths:
            content_names = []
            
            source_image = PIL.Image.open(source_image_path)
            image_detection_results = detector.detect(cv2.cvtColor(numpy.array(source_image), cv2.COLOR_RGB2BGR))

            drawable_source_image = PIL.ImageDraw.Draw(source_image)

            for image_detection_result in image_detection_results:
                content_names.append(image_detection_result.content)

                drawable_source_image.polygon(
                    [
                        (image_detection_result.frame_coordinates.top_left.x, image_detection_result.frame_coordinates.top_left.y),
                        (image_detection_result.frame_coordinates.top_right.x, image_detection_result.frame_coordinates.top_right.y),
                        (image_detection_result.frame_coordinates.top_right.x, image_detection_result.frame_coordinates.top_right.y),
                        (image_detection_result.frame_coordinates.bottom_right.x, image_detection_result.frame_coordinates.bottom_right.y),
                        (image_detection_result.frame_coordinates.bottom_right.x, image_detection_result.frame_coordinates.bottom_right.y),
                        (image_detection_result.frame_coordinates.bottom_left.x, image_detection_result.frame_coordinates.bottom_left.y),
                        (image_detection_result.frame_coordinates.bottom_left.x, image_detection_result.frame_coordinates.bottom_left.y),
                        (image_detection_result.frame_coordinates.top_left.x, image_detection_result.frame_coordinates.top_left.y),
                    ],
                    outline=self.__box_color,
                    width=self.__box_thickness
                )

                text_position_point_tuple = (image_detection_result.frame_coordinates.bottom_left.x, image_detection_result.frame_coordinates.bottom_left.y + 5)
                drawable_source_image.text(text_position_point_tuple, f"{image_detection_result.content} ({image_detection_result.confidence})", fill=self.__font_color, font=PIL.ImageFont.truetype(self.__font_path_string, self.__font_size))

            file_name = source_image_path.name

            if content_names_in_file_name:
                base_name, extension = os.path.splitext(file_name)
                file_name = base_name + ("_[" + ", ".join(content_names) + "]") + extension

            source_image.save(results_folder_path.joinpath(file_name))
            source_image.close()
