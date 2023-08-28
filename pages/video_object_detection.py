""" This file includes the object detection and tracking performed 
    in video frames using custom - trained yolov8 model"""

import cv2 
import streamlit as st 
from ultralytics import YOLO
import torch 
import time 

model_path = "best.pt"
checking_model_path = "yolov8m.pt"

# Setting page layout
st.set_page_config(
    page_title="Videos",  # Setting page title
    page_icon="🤖",     # Setting page icon
    layout="wide",      # Setting layout to wide
    initial_sidebar_state="expanded"    # Expanding sidebar by default
)

# Creating sidebar
with st.sidebar:
    st.header("Image/Video Config")     # Adding header to sidebar
    # Adding file uploader to sidebar for selecting images
    source_vid = st.sidebar.selectbox(
        "Choose an video...", ["videos/video_1.mp4","videos/video_2.mp4"])
    
    # model confidence 
    confidence = float(st.slider(
        "Select Model Confidence", 25,100,40)) / 100
    
st.title("Detection on video")


try:
    model = YOLO(model_path)
    checking_model = YOLO(checking_model_path)
except Exception as e:
    st.error(
        f"Unable to open Yolo weights"
    )
    st.error(e)

st.subheader('You can limit the number of allowded passengers') 
st.subheader(' in a two wheeler before raising a flag')
number = st.number_input(' ', min_value=0, max_value=3)

if source_vid is not True:
    with open(str(source_vid),'rb') as video_file:
        video_bytes = video_file.read()

    if video_bytes:
        st.video(video_bytes)

    if st.sidebar.button('Detect Objects'):
        vid_cap = cv2.VideoCapture(
            #'videos/video_3.mp4'
            source_vid
        )

        st_frame = st.empty()
        while(vid_cap.isOpened()):
            sucess, image = vid_cap.read()
            if sucess:
                image = cv2.resize(image,(720,int(720*(9/16))))
                res = model.predict(image,conf = confidence)
                result_tensor = res[0].boxes
                res_plotted = res[0].plot()
                
                if torch.any(result_tensor.xywh):

                    vehicle_region= result_tensor.xywh[0].tolist()
                    x, y, w, h = [int(x) for x in vehicle_region]

                    roi_x = int(x - w / 2)
                    roi_y = int(y - h/ 2)
                    roi_width = int(w)
                    roi_height = int(h)

                    roi = image[roi_y:roi_y+roi_height, roi_x:roi_x+roi_width]
                    check = checking_model.predict(roi, conf = 0.5)
                    names = checking_model.names


                    for r in check:
                        count = 0
                        for c in r.boxes.cls:

                            if names[int(c)] == 'person':
                                count+=1
                                print("The count --- ", count)

                            if count > number:
                                    st_frame.image(res_plotted,
                                            caption = 'Detected Video',
                                            channels = "BGR",
                                            use_column_width = True)
                            else:
                                st_frame.image(image,
                                        caption = 'Detected Video',
                                        channels = "BGR",
                                        use_column_width = True)
            else:
                vid_cap.release()
                break
