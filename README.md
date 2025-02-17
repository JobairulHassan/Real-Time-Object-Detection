# Real-Time Object Detection
## Description
This repository contains Real-Time Object Detection with YOLOv11 and Fast R-CNN model. A simple UI is also build using Tkinter.
## Table of contents
1.  [General Info](#general-info)
2.  [Technologies Used](#technologies-used)
3.  [Dataset](#dataset)
4.  [Installation](#installation)
5.  [License](#license)

## General Info
This project focuses on object detection using a custom dataset of 150 labeled images containing traffic-related objects. Both YOLOv11 and Faster R-CNN models were trained and evaluated for performance comparison. A user-friendly application was developed to process and visualize object detection on video files.

## Technologies Used
  - **Python:** The primary programming language for the project.
  - **Pytorch:** Deep learning framework for implementing and training the object detection models.
  - **Ultralytics YOLOv11:** Object detection model implementation.
  - **Torch Vision:** Provides pre-trained Faster R-CNN model and utilities for image processing.
  - **OpenCV (cv2):** Used for image and video processing tasks, including loading, displaying, and writing video.
  - **LabelImg:** Tool for creating bounding box annotations in Pascal VOC XML and YOLO formats.
  - **Tkinter:** Python library for creating the graphical user interface (GUI).
  - **Matplotlib:** Used for visualizing and plotting data.
## Dataset
  - **Dataset Selection:** A set of 150 images mostly collected from [kitti](https://www.kaggle.com/datasets/klemenko/kitti-dataset) dataset and roboflow public project named [VRU_valid Computer Vision](https://universe.roboflow.com/university-of-jordan/vru_valid) Project. It helps create a robust dataset by including variations such as daylight and nighttime images, as well as different angles of the objects.
  *  **Annotation:**
      * Loading Images:  Each image was loaded into LabelImg for annotation.
      * Creating Bounding Boxes: Multiple bounding boxes is created based on object present in the loaded image. Total 5 different object is detected in the whole project. They are: Traffic sign, Car, Pedestrian, Traffic signal light and bus. 
      * Saving Annotations: Annotations were saved in both Pascal VOC XML format and YOLO format. 

## Installation
1.  **Clone the repository:**

    ```
    git clone https://github.com/JobairulHassan/Real-Time-Object-Detection
    cd [Project Directory]
    ```

2.  **Install Dependencies:**

    It is recommended to create a virtual environment to manage project dependencies.

    ```
    # Create a virtual environment (optional but recommended)
    python -m venv venv
    # Activate the virtual environment
    # On Windows:
    venv\Scripts\activate
    # On macOS and Linux:
    source venv/bin/activate
    ```

    Install the required Python packages:

    ```
    pip install -r requirements.txt
    ```
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
