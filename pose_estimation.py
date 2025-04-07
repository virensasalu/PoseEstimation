
import torch

from PIL import Image
import cv2
import numpy as np
import mediapipe as mp
import os


# Function to detect the pose using Mediapipe
def detect_pose(image):
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose(static_image_mode=True)
    mp_drawing = mp.solutions.drawing_utils

    # Convert the image to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Perform pose detection
    results = pose.process(image_rgb)

    # Create a blank image for the skeleton
    skeleton_image = np.zeros_like(image)

    # Draw the pose landmarks on the blank image
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(
            skeleton_image,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=2, circle_radius=2),
            mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=2, circle_radius=2),
        )

    return skeleton_image




# Function to preprocess the input image
def preprocess_image(image_path):

    # Load the image
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Detect the pose
    pose_image = detect_pose(image)

    # Convert to grayscale and resize
    pose_image = cv2.cvtColor(pose_image, cv2.COLOR_BGR2GRAY)
    pose_image = cv2.resize(pose_image, (512, 512))

    # Convert to PIL image
    pose_pil = Image.fromarray(pose_image)
    return pose_pil




# Function to generate the skeleton image
def generate_pose_image(input_image_path, output_image_path):

    # Preprocess the input image
    pose_image = preprocess_image(input_image_path)

    # Save the skeleton image for debugging
    pose_image.save(output_image_path)
    print(f" Output Pose_Image is saved as {output_image_path}")


"""
if __name__ == "__main__":
    input_image_path = "input_images/4.jpg"  # Replace with the path to your input image
    output_image_path = "output_images/skeleton_image_4.png"  # Replace with the desired output path
    generate_pose_image(input_image_path, output_image_path) 
"""

if __name__ == "__main__":
# Ensure the input and output directories exist
    os.makedirs("input_images", exist_ok=True)
    os.makedirs("output_images", exist_ok=True)

    # Looping through the 5 input images
    for i in range(1, 6):
        # Construct the input and output paths dynamically
        input_image_path = f"input_images/{i}.jpg"  # Input image path
        output_image_path = f"output_images/skeleton_image_{i}.png"  # Output image path

        # Call the function for each image
        try:
            generate_pose_image(input_image_path, output_image_path)
            print(f"Processed image {i}: Saved to {output_image_path}")
        except Exception as e:
            print(f"Error processing image {i}: {e}")