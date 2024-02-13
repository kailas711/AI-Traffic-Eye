"""This is the main file of the project that contains the streamlit app
   This file defines the layout of the application which includes the 
   image uploader , video uploader , an interface etc"""

import streamlit as st

# Setting page layout
st.set_page_config(
    page_title="Home",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)
# Main page heading
content = """ # Traffic-EYE
Detecting an object inside an object , My first end-to-end computer vision project, starting from data collection to deployment in a webapp. The idea is to find traffic rule violations by 2 wheelers by detecting motorbies carrying more than 2 persons on road. The number of person is arbitary and can be customized.  

### Nested Object Detection Concept. 
![image](https://github.com/kailas711/AI-Traffic-Eye/blob/main/assets/Nested%20Object%20Detection%20(Custom).png?raw=true)

The project involved 5 phases 
- Data collection, cleaning and procesing : Uses web scarped data by selenium , manually annotated using Roboflow.
- Model Buidling and training : Custom trained on YoloV8n model from Ultralytics hub
- Deployment : Deployed in Streamlit community cloud.

"""

st.markdown(content)
