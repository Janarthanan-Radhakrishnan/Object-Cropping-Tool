import streamlit as st
import os
import zipfile
import shutil
from image_cropper import ImageCropper

def save_uploaded_file(uploaded_file, folder):
    file_path = os.path.join(folder, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return file_path

def extract_zip(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_to)

def zip_output_folder(output_folder, zip_filename):
    shutil.make_archive(zip_filename, 'zip', output_folder)
    return zip_filename + ".zip"

st.title("Automatic Image Cropping Tool")

# Create directories
UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "cropped_images"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Upload ZIP or multiple files
uploaded_files = st.file_uploader("Upload images and annotation files (ZIP or multiple files)",
                                  accept_multiple_files=True, type=["zip", "jpg", "jpeg", "png", "txt", "xml", "json"])

if uploaded_files:
    processing_folder = os.path.join(UPLOAD_FOLDER, "processing")
    os.makedirs(processing_folder, exist_ok=True)
    
    for uploaded_file in uploaded_files:
        file_path = save_uploaded_file(uploaded_file, processing_folder)
        
        # If ZIP file, extract it
        if uploaded_file.name.endswith(".zip"):
            extract_zip(file_path, processing_folder)
            os.remove(file_path)  # Remove the ZIP after extraction
    
    st.success("Files uploaded and extracted successfully!")
    
    # Process images
    cropper = ImageCropper(processing_folder, OUTPUT_FOLDER)
    cropper.crop("yolo")  # Automatically detects YOLO, Pascal, or COCO
    
    # Zip and provide download link
    zip_file = zip_output_folder(OUTPUT_FOLDER, "cropped_output")
    
    with open(zip_file, "rb") as f:
        st.download_button("Download Cropped Images", f, file_name="cropped_images.zip", mime="application/zip")
    
    st.success("Cropping completed! Download your cropped images.")
