""" This file includes the object detection and tracking performed 
    in video frames using custom - trained yolov8 model"""

import cv2 
import streamlit as st 
from ultralytics import YOLO
import torch 

model_path = "best.pt"
checking_model_path = "yolov8m.pt"

# Setting page layout
st.set_page_config(
    page_title="Videos",  # Setting page title
    page_icon="🤖",     # Setting page icon
    layout="wide",      # Setting layout to wide
    initial_sidebar_state="expanded"    # Expanding sidebar by default
)

st.title("Detection on video")
content = """ You can limit the number of allowded passengers in a two wheeler before raising a flag """

st.markdown(content)

number = st.number_input(' ', min_value=0, max_value=3)

# Creating sidebar
with st.sidebar:
    st.header("Image/Video Config")     # Adding header to sidebar
    # Adding file uploader to sidebar for selecting images
    source_vid = st.sidebar.selectbox(
        "Choose an video...", ["videos/video_1.mp4","videos/video_2.mp4"])
    
    # model confidence 
    confidence = float(st.slider(
        "Select Model Confidence", 25,100,40)) / 100
    
# splitting screen to 2 columns. 
    
col1,col2 = st.columns(2)
count = 0

try:
    model = YOLO(model_path)
    checking_model = YOLO(checking_model_path)
except Exception as e:
    st.error(
        f"Unable to open Yolo weights"
    )
    st.error(e)

with col1:

    if source_vid is not True:
        with open(str(source_vid),'rb') as video_file:
            video_bytes = video_file.read()

        if video_bytes:
            st.video(video_bytes)

        if st.sidebar.button('Detect Objects'):
            vid_cap = cv2.VideoCapture(
                #'videos/video_1.mp4'
                source_vid)

            st_frame = st.empty()
            while(vid_cap.isOpened()):
                sucess, image = vid_cap.read()
                if sucess:
                    image = cv2.resize(image,(720,int(720*(9/16))))
                    res = model.predict(image,conf = confidence)
                    result_tensor = res[0].boxes
                    res_plotted = res[0].plot()

                    # print("Any detections -----" , torch.any(result_tensor.xywh))
                    
                    if torch.any(result_tensor.xywh):

                        vehicle_region= result_tensor.xywh[0].tolist()
                        x, y, w, h = [int(x) for x in vehicle_region]

                        roi_x = int(x - w / 2)
                        roi_y = int(y - h/ 2)
                        roi_width = int(w)
                        roi_height = int(h)

                        roi = image[roi_y:roi_y+roi_height, roi_x:roi_x+roi_width]

                        check = checking_model.predict(roi, conf = confidence)
                        names = checking_model.names

                        with col2:
                            for r in check:
                                count = 0
                                for c in r.boxes.cls:
                                    if names[int(c)] == 'person':
                                        count+=1

                                    if count > number:
                                            st_frame.image(res_plotted,
                                                    caption = 'Detected Video',
                                                    channels = "BGR",
                                                    use_column_width = False)
                                    else:
                                        st_frame.image(image,
                                                caption = 'Detected Video',
                                                channels = "BGR",
                                                use_column_width = False)
                                                                                
                else:
                    vid_cap.release()
                    # display passenger count 
                    st.subheader(f"The Number of passengers {count}")
                    break



