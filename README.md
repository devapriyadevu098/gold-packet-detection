 Automatic Gold Packet Counter

Project Overview

The Automatic Gold Packet Counter is a computer vision-based application designed to automatically detect and count gold packets using the RT-DETR (Real-Time Detection Transformer) object detection model.

The system processes uploaded images containing gold packets, identifies individual packets, displays bounding boxes around detected objects, and provides the total packet count.

 Objectives

- Automate the process of gold packet detection and counting.
- Reduce manual counting efforts.
- Improve counting efficiency and accuracy.
- Provide a simple and user-friendly interface for image-based detection.

Technologies Used

- **Programming Language:** Python
- **Object Detection Model:** RT-DETR
- **Deep Learning Framework:** Ultralytics
- **Web Framework:** Flask
- **Dataset and Annotation:** Roboflow
- **Frontend:** HTML, CSS, JavaScript
- **Development Environment:** Visual Studio Code
 Key Features

- Image-based gold packet detection.
- Automatic counting of detected packets.
- Bounding box visualization.
- User-friendly web interface.
- Separate display of uploaded and processed images.
- Supports JPG, JPEG, PNG, and WEBP formats.
- Maximum image upload size: 10 MB.

System Workflow

1. Upload an image containing gold packets.
2. The uploaded image is displayed in the preview area.
3. Click the Detect Packets button.
4. The RT-DETR model processes the image.
5. Detected packets are highlighted with bounding boxes.
6. The total number of detected packets is displayed.

Installation and Execution

1. Clone the Repository

git clone https://github.com/devapriyadevu098/gold-packet-detection.git


 2. Navigate to the Project Directory


cd gold-packet-detection

 3. Install Dependencies

If a requirements.txt file is available:

pip install -r requirements.txt

4. Run the Application

python app.py


Open the local URL displayed in your terminal to access the application.

 Future Enhancements

- Improve detection accuracy under different lighting conditions.
- Enhance performance for images containing densely arranged packets.
- Extend the system for real-time conveyor belt detection.
- Develop a database for storing detection results.

Author

Devapriya Prejith

MCA Mini Project – 2026
