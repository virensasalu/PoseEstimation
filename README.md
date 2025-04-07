# PoseEstimation 

FashionFlux is an innovative virtual try-on platform that leverages cutting-edge AI technologies to revolutionize the online shopping experience. This repository focuses on the **Pose Estimation** module, a critical component of the FashionFlux system, enabling accurate garment overlay and dynamic fit simulation based on user posture.

## Overview

The **Pose Estimation** module is designed to detect and track keypoints of the human body, enabling garments to adapt naturally to different user postures. By integrating this module with other components of FashionFlux, users can visualize how clothing items fit and look on them in real-time.

### File Structure

```
PoseEstimation/
├── requirements.txt         # Python dependencies needed to run the project
├── .env                     # Environment variables  — excluded from version control # gitignored
├── .gitignore               # Specifies files and folders Git should ignore (e.g. .env, venvs)
├── poseenv/                 # Python virtual environment folder # gitignored
├── pose_estimation.py       # Main script to run pose detection and save output images
├── output_images/           # Folder where processed pose images are saved # gitignored
│   ├── skeleton_image_1.png # Pose output for input image 1
│   ├── skeleton_image_2.png # Pose output for input image 2
│   ├── skeleton_image_3.png # Pose output for input image 3
├── input_images/            # Folder containing raw input images to process # gitignored
│   ├── Img_1.jpg            # Example input image 1
│   ├── Img_2.jpg            # Example input image 2
│   ├── Img_3.jpg            # Example input image 3  
└── README.md                # Project overview, usage instructions, and documentation
```

### Key Objectives
- Detect and track human body keypoints with high accuracy.
- Enable dynamic garment overlay that conforms to user posture.
- Provide a seamless and interactive virtual try-on experience.


## Features

- **Real-Time Pose Estimation**: Uses the MediaPipe library for detecting and tracking body keypoints efficiently.
- **Dynamic Fit Simulation**: Ensures garments adapt naturally to user posture and body shape.
- **High Accuracy**: Achieves pose alignment accuracy of ~85–90% based on keypoint matching.
- **Scalable Architecture**: Designed to handle high volumes of concurrent users without compromising performance.


## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/virensasalu/PoseEstimation.git
   cd PoseEstimation

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source poseenv/bin/activate

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

## Usage

1. Upload an image of a person.
2. The system detects body keypoints using the MediaPipe library.
3. Visualize the Pose of the given image.

## Sample Skeleton Pose Output Images for the corresponding input images 

![alt text](image.png)


Feel free to explore, use, and contribute to this project.



   
