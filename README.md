# YoloV5_Nested_Object_Detection
My first end-to-end computer vision project, starting from data collection to deployment in a webapp.
The project involves 5 steps 
- Data Collection 
- Data cleaning and procesing 
- Model Buidling and training 
- Deployment 

### 1.Data Collection 
I utilized the Selenium library in Python for automating web scraping. The scraping process posed challenges due to frequent Chrome updates that hindered traditional methods. The most demanding aspect involved configuring the chromedriver to navigate through thumbnails and identify the image source to prevent downloading of the thumbnails.

code for scrapping -- 
{gif}

### 2.Data Cleannig 
Around 175 images were carefully selected and manually inspected. To ensure consistent input dimensions for the YOLO model, resizing was performed on all images. Roboflow was utilized to manually draw bounding boxes. Additionally, image augmentation techniques were employed to expand the training dataset, enhancing the model's learning capabilities.
{gif}

### 3.Model Buidling and training 
----under-works-----

### 4.Deployment 
----under-works----
