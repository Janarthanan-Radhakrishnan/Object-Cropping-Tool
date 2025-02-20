import cv2
import os
import xml.etree.cElementTree as ET
import json

class ImageCropper:
    def __init__(self, image_folder, output_folder):
        self.image_folder = image_folder
        self.output_folder = output_folder
        os.makedirs(self.output_folder, exist_ok=True)

    def _create_output_subfolder(self, image_name):
        image_output_folder = os.path.join(self.output_folder, image_name)
        os.makedirs(image_output_folder, exist_ok=True)
        return image_output_folder

    def _get_image_files(self):
        return [f for f in os.listdir(self.image_folder) if f.lower().endswith((".jpg", ".jpeg", ".png"))]

    def yolo_crop(self):
        image_files = self._get_image_files()
        
        for image_file in image_files:
            image_path = os.path.join(self.image_folder, image_file)
            label_path = os.path.join(self.image_folder, os.path.splitext(image_file)[0] + ".txt")
            
            if not os.path.exists(label_path):
                print(f"Label file not found for {image_file}, skipping...")
                continue
            
            image = cv2.imread(image_path)
            height, width, _ = image.shape
            image_output_folder = self._create_output_subfolder(os.path.splitext(image_file)[0])
            
            with open(label_path, "r") as f:
                labels = f.readlines()
            
            for idx, label in enumerate(labels):
                parts = label.strip().split()
                class_id = int(parts[0])
                x_center, y_center, bbox_width, bbox_height = map(float, parts[1:])
                x_min = int((x_center - bbox_width / 2) * width)
                y_min = int((y_center - bbox_height / 2) * height)
                x_max = int((x_center + bbox_width / 2) * width)
                y_max = int((y_center + bbox_height / 2) * height)
                x_min, y_min = max(0, x_min), max(0, y_min)
                x_max, y_max = min(width, x_max), min(height, y_max)
                cropped_img = image[y_min:y_max, x_min:x_max]
                cv2.imwrite(os.path.join(image_output_folder, f"{image_file}_crop_{idx+1}.jpg"), cropped_img)

    def pascal_crop(self):
        image_files = self._get_image_files()
        
        for image_file in image_files:
            image_path = os.path.join(self.image_folder, image_file)
            label_path = os.path.join(self.image_folder, os.path.splitext(image_file)[0] + ".xml")
            
            if not os.path.exists(label_path):
                print(f"Label file not found for {image_file}, skipping...")
                continue
            
            image = cv2.imread(image_path)
            height, width, _ = image.shape
            image_output_folder = self._create_output_subfolder(os.path.splitext(image_file)[0])
            
            tree = ET.parse(label_path)
            root = tree.getroot()
            
            for i, obj in enumerate(root.findall("object")):
                bndbox = obj.find("bndbox")
                xmin, ymin, xmax, ymax = map(int, [bndbox.find(tag).text for tag in ["xmin", "ymin", "xmax", "ymax"]])
                xmin, ymin = max(0, xmin), max(0, ymin)
                xmax, ymax = min(width, xmax), min(height, ymax)
                cropped_img = image[ymin:ymax, xmin:xmax]
                cv2.imwrite(os.path.join(image_output_folder, f"{image_file}_crop_{i+1}.jpg"), cropped_img)

    def coco_crop(self):
        image_files = self._get_image_files()
        
        for image_file in image_files:
            image_path = os.path.join(self.image_folder, image_file)
            annotation_path = os.path.join(self.image_folder, os.path.splitext(image_file)[0] + ".json")
            
            if not os.path.exists(annotation_path):
                print(f"Annotation file not found for {image_file}, skipping...")
                continue
            
            image = cv2.imread(image_path)
            height, width, _ = image.shape
            image_output_folder = self._create_output_subfolder(os.path.splitext(image_file)[0])
            
            with open(annotation_path, 'r') as f:
                annotations = json.load(f)
            
            for i, annotation in enumerate(annotations['objects']):
                xmin, ymin, w, h = annotation['bbox']
                xmax, ymax = xmin + w, ymin + h
                xmin, ymin = max(0, int(xmin)), max(0, int(ymin))
                xmax, ymax = min(width, int(xmax)), min(height, int(ymax))
                cropped_img = image[ymin:ymax, xmin:xmax]
                cv2.imwrite(os.path.join(image_output_folder, f"{image_file}_crop_{i+1}.jpg"), cropped_img)

    def crop(self, format_type):
        if format_type == "yolo":
            self.yolo_crop()
        elif format_type == "pascal":
            self.pascal_crop()
        elif format_type == "coco":
            self.coco_crop()
        else:
            print("Unsupported format. Choose from 'yolo', 'pascal', or 'coco'.")
