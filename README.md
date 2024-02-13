# AI Traffic Eye

**The application is deployed in streamlit cloud, try it for yourself!!**

**Link** -- https://ai-traffic-eye.streamlit.app/

### 1.Data Collection 
I utilized the Selenium library in Python for automating web scraping. The scraping process posed challenges due to frequent Chrome updates that hindered traditional methods. The most demanding aspect involved configuring the chromedriver to navigate through thumbnails and identify the image source to prevent downloading of the thumbnails.

[Code for scrapping](https://github.com/kailas711/YoloV5_Nested_Object_Detection/blob/main/Data_Collection.py)


![Data_collection](https://github.com/kailas711/AI-Traffic-Eye/blob/main/assets/Data%20Collection.gif?raw=true)



### 2.Data Cleannig and Processing
Around 307 images were carefully selected and manually inspected. To ensure consistent input dimensions for the YOLO model, resizing was performed on all images. Roboflow was utilized to manually draw bounding boxes. Additionally, image augmentation techniques were employed to expand the training dataset, enhancing the model's learning capabilities.

![Annotation](https://github.com/kailas711/AI-Traffic-Eye/blob/main/assets/Data%20Annotation.gif?raw=true)


### 3.Model Buidling and training
The Ultralytics YoloV8 nano model custom trained on dataset via Roboflow API dairectly on T4 GPU in Google Colab.

[YoloV8n model](https://github.com/kailas711/YoloV5_Nested_Object_Detection/blob/main/YoloV8%20Training.ipynb)


### 4.Deployment 
![image](https://github.com/kailas711/AI-Traffic-Eye/blob/main/assets/streamlit.jpeg?raw=true)

