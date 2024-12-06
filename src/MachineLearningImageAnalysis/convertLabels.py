import csv
import os

def convert_to_yolo_format(width, height, x1, y1, x2, y2):
    x_center = (x1 + x2) / (2 * width)
    y_center = (y1 + y2) / (2 * height)
    box_width = (x2 - x1) / width
    box_height = (y2 - y1) / height
    return x_center, y_center, box_width, box_height

csv_file_path = "dataset-information-class-0.csv"
class_id = "0"

output_folder = "labels"
os.makedirs(output_folder, exist_ok=True)

with open(csv_file_path, 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile, delimiter=';')

    for row in csv_reader:
        filename = row['Filename']
        width = float(row['Width'])
        height = float(row['Height'])
        x1 = float(row['Roi.X1'])
        y1 = float(row['Roi.Y1'])
        x2 = float(row['Roi.X2'])
        y2 = float(row['Roi.Y2'])

        x_center, y_center, box_width, box_height = convert_to_yolo_format(width, height, x1, y1, x2, y2)

    output_file_path = os.path.join(output_folder,
                                    f"{filename.split('.')[0]}.txt")

    with open(output_file_path, 'w') as output_file:
        output_file.write(f"{class_id}{x_center}{y_center}{box_width}{box_height}\n")