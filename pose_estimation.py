"""
Version1: 
Generated Skeleton image in Grey Scale with White lines for Skeleton.
Output is stored in output_images directory. 

Version2: 
Added code to store the skeleton image in numpy array and 
create skeleton image with Colors for landmarks and connections.
Output is stored in Color_output_images directory. 

"""



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

    # Draw the pose landmarks on the blank image with colorful, thick lines
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(
            skeleton_image,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=8, circle_radius=2),  # Green for landmarks
            mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=8, circle_radius=2),  # Red for connections
        )

    return skeleton_image




# Function to preprocess the input image
def preprocess_image(image_path):

    # Load the image
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Detect the pose
    pose_image = detect_pose(image)

    # Convert to RGB and resize
    pose_image = cv2.cvtColor(pose_image, cv2.COLOR_BGR2RGB)
    # chnaged from "COLOR_BGR2GRAY" to "COLOR_BGR2RGB" above to keep the RGB Colors
    pose_image = cv2.resize(pose_image, (512, 512))

    # Convert to PIL image
    pose_pil = Image.fromarray(pose_image)
    return pose_pil





# Function to generate the skeleton image
# def generate_pose_image(input_image_path, output_image_path):

#     # Preprocess the input image
#     pose_image = preprocess_image(input_image_path)

#     # Save the skeleton image for debugging
#     pose_image.save(output_image_path)
#     print(f" Output Pose_Image is saved as {output_image_path}")

#     # Save the skeleton image in Numpy Array
#     pose_array = np.array(pose_image)  # Convert to numpy array for further processing

#     # Print basic information
#     print(f"Array shape: {pose_array.shape}")
#     print(f"Data type: {pose_array.dtype}")


from PIL import Image

def generate_pose_image(input_image_path, output_image_path):
    # Load input image (for display)
    input_image = Image.open(input_image_path).convert("RGB")

    # Generate the skeleton image from your function
    pose_image = preprocess_image(input_image_path)

    # Convert both to NumPy arrays
    input_array = np.array(input_image)
    pose_array = np.array(pose_image)

    # Resize to same shape if needed
    if input_array.shape != pose_array.shape:
        pose_array = cv2.resize(pose_array, (input_array.shape[1], input_array.shape[0]))

    # Combine images side-by-side
    combined = np.hstack((input_array, pose_array))

    # Save combined image using OpenCV
    success = cv2.imwrite(output_image_path, cv2.cvtColor(combined, cv2.COLOR_RGB2BGR))

    if success:
        print(f" Output Pose_Image is saved as {output_image_path}")
    else:
        print(f" Failed to save image: {output_image_path}")

    # Print basic info for debugging
    print(f"Array shape: {pose_array.shape}")
    print(f"Data type: {pose_array.dtype}")




import glob
if __name__ == "__main__":

    os.makedirs("input_images", exist_ok=True)
    os.makedirs("output_images", exist_ok=True)

    image_paths = sorted(glob.glob("input_images/*.jpg"))
    print(f"🔍 Found {len(image_paths)} image(s) in 'input_images/'")

    for i, input_image_path in enumerate(image_paths):
        output_image_path = f"output_images/skeleton_image_{i}.png"

        try:
            generate_pose_image(input_image_path, output_image_path)
            print(f"Processed image {i}: Saved to {output_image_path}")
        except Exception as e:
            print(f"Error processing image {i}: {e}")