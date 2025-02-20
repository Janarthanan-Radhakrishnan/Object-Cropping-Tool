import streamlit as st
import os
import tempfile
import zipfile
from tkinter import Tk, filedialog
from image_cropper import ImageCropper

# Streamlit app title
st.title("Automatic Object Cropping Tool")

# Function to open folder selection dialog
def select_folder(title="Select Folder"):
    root = Tk()
    root.withdraw()  # Hide the root window
    root.attributes('-topmost', True)  # Bring the dialog to the front
    folder_path = filedialog.askdirectory(title=title)
    root.destroy()
    return folder_path

# Input folder selection
if st.button("Select Input Folder"):
    input_folder = select_folder(title="Select Input Folder")
    if input_folder:
        st.session_state.input_folder = input_folder
        st.success(f"Input folder selected: {input_folder}")

# Output folder selection
if st.button("Select Output Folder"):
    output_folder = select_folder(title="Select Output Folder")
    if output_folder:
        st.session_state.output_folder = output_folder
        st.success(f"Output folder selected: {output_folder}")

# Display selected folders
if "input_folder" in st.session_state:
    st.write(f"**Input Folder:** {st.session_state.input_folder}")
if "output_folder" in st.session_state:
    st.write(f"**Output Folder:** {st.session_state.output_folder}")

def find_label_format(folder):
    """Detect annotation format from files in folder"""
    txt_labels = [f for f in os.listdir(folder) if f.endswith(".txt")]
    xml_labels = [f for f in os.listdir(folder) if f.endswith(".xml")]
    json_labels = [f for f in os.listdir(folder) if f.endswith(".json")]

    if txt_labels:
        return "yolo"
    elif xml_labels:
        return "pascal"
    elif json_labels:
        return "coco"
    else:
        return "unknown"

if st.button("Crop Images"):
    if "input_folder" not in st.session_state:
        st.error("Please select an input folder!")
    elif "output_folder" not in st.session_state:
        st.error("Please select an output folder!")
    else:
        input_folder = st.session_state.input_folder
        output_folder = st.session_state.output_folder

        # Detect annotation format
        detected_format = find_label_format(input_folder)
        
        if detected_format == "unknown":
            st.error("No valid annotation files found! Supported formats: YOLO, Pascal VOC, COCO")
        else:
            with st.spinner(f"Processing {detected_format.upper()} format..."):
                try:
                    cropper = ImageCropper(input_folder, output_folder)
                    cropper.crop(detected_format)
                    st.success(f"Successfully cropped images to {output_folder}")
                    st.balloons()
                except Exception as e:
                    st.error(f"Error during processing: {str(e)}")
