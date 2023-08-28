""" This file includes the object detection performed 
    in images using custom - trained yolov8 model"""

import PIL
import streamlit as st 
from ultralytics import YOLO
import cv2
import numpy 

# model_path = "weights\\best.pt"
# checking_model = "weights\\yolov8m.pt"

model_path = "best.pt"
checking_model = "yolov8m.pt"


# Setting page layout
st.set_page_config(
    page_title="Images",  # Setting page title
    page_icon="🤖",     # Setting page icon
    layout="wide",      # Setting layout to wide
    initial_sidebar_state="expanded"    # Expanding sidebar by default
)

# Creating sidebar
with st.sidebar:
    st.header("Image/Video Config")     # Adding header to sidebar
    # Adding file uploader to sidebar for selecting images
    source_img = st.file_uploader(
        "Choose an image...", type=("jpg", "jpeg", "png", 'bmp', 'webp'))
    
    # model confidence 
    confidence = float(st.slider(
        "Select Model Confidence", 25,100,40)) / 100
    
st.title("Detection on images")

col1,col2 = st.columns(2)

# Adding image to the first column if image is uploaded
with col1:
    if source_img:
        # Opening the uploaded image
        uploaded_image = PIL.Image.open(source_img)
        # Adding the uploaded image to the page with a caption
        st.image(source_img,
                 caption="Uploaded Image",
                 use_column_width=True
                 )
        
try:
    model = YOLO(model_path)
except Exception as e:
    st.error(
        f"Unable to open Yolo weights"
    )
    st.error(e)

if st.sidebar.button("Detect Objects"):
    res = model.predict(uploaded_image,
                        conf = confidence)
    boxes = res[0].boxes
    res_plotted = res[0].plot()[:, :, ::-1]
    box = boxes.xywh[0].tolist()
    box = [int(x) for x in box]
    x, y, w, h = box

    image = cv2.cvtColor(numpy.array(uploaded_image), cv2.COLOR_RGB2BGR)

    roi_x = int(x - w / 2)
    roi_y = int(y - h/ 2)
    roi_width = int(w)
    roi_height = int(h)

    roi = image[roi_y:roi_y+roi_height, roi_x:roi_x+roi_width]
    # Convert array of Roi into PIL Image
    cropped_img = PIL.Image.fromarray(roi)
    # Checking for number of passengers , The Nested Object detection 
    model_2 = YOLO(checking_model)
    names = model_2.names
    res = model_2(cropped_img, conf = 0.5)
    for r in res:
        count = 0
        for c in r.boxes.cls:
            if names[int(c)] == 'person':
                count+=1

    st.write("The Number of passengers " , count)

    with col2:
        st.image(res_plotted,
                 caption = "Detected Image",
                 use_column_width = True)
        
        try:
            with st.expander("detection results"):
                for box in boxes:
                    st.write(box.xywh)
        except Exception as e:
            st.write("No image uploaded")

