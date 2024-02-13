# AI Traffic Eye

The project involved 5 phases 
- Data collection, cleaning and procesing : Uses web scarped data by selenium , manually annotated using Roboflow.
- Model Buidling and training : Custom trained on YoloV8n model from Ultralytics hub
- Deployment : Deployed in Streamlit community cloud.

**The application is deployed in streamlit cloud, try it for yourself!!**

**Link** -- https://yolov8nestedobjectdetection-akxeu4mb6zecb6mupmc57o.streamlit.app/

### 1.Data Collection 
I utilized the Selenium library in Python for automating web scraping. The scraping process posed challenges due to frequent Chrome updates that hindered traditional methods. The most demanding aspect involved configuring the chromedriver to navigate through thumbnails and identify the image source to prevent downloading of the thumbnails.

[Code for scrapping](https://github.com/kailas711/YoloV5_Nested_Object_Detection/blob/main/Data_Collection.py)


![Data_collection](https://github.com/kailas711/YoloV5_Nested_Object_Detection/assets/89206677/21f41239-620c-4706-ac3b-db86154de4cb)



### 2.Data Cleannig and Processing
Around 307 images were carefully selected and manually inspected. To ensure consistent input dimensions for the YOLO model, resizing was performed on all images. Roboflow was utilized to manually draw bounding boxes. Additionally, image augmentation techniques were employed to expand the training dataset, enhancing the model's learning capabilities.

![Annotation](https://github.com/kailas711/YoloV5_Nested_Object_Detection/assets/89206677/2257ed62-02ab-4a8b-8f04-a9553b00e2b4)


### 3.Model Buidling and training
The Ultralytics YoloV8 nano model custom trained on dataset via Roboflow API dairectly on T4 GPU in Google Colab.

[YoloV8n model](https://github.com/kailas711/YoloV5_Nested_Object_Detection/blob/main/YoloV8%20Training.ipynb)


### 4.Deployment 
![image](https://github.com/kailas711/AI-Traffic-Eye/blob/main/assets/streamlit.jpeg?raw=true)

