import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim

# Read the original and motion-amplified videos
cap_original = cv2.VideoCapture('data\baby.mp4')
cap_amplified = cv2.VideoCapture('result1.avi')

# Define variables for MSE and SSIM
mse_values = []
ssim_values = []

while cap_original.isOpened() and cap_amplified.isOpened():
    print(1)
    ret_orig, frame_orig = cap_original.read()
    ret_ampl, frame_ampl = cap_amplified.read()
    if not (ret_orig and ret_ampl):
        break

    frame_orig = cv2.resize(frame_orig, (640, 480))
    frame_ampl = cv2.resize(frame_ampl, (640, 480))

    # Convert frames to grayscale
    gray_orig = cv2.cvtColor(frame_orig, cv2.COLOR_BGR2GRAY)
    gray_ampl = cv2.cvtColor(frame_ampl, cv2.COLOR_BGR2GRAY)

    # Calculate MSE and SSIM
    mse = np.mean((gray_orig - gray_ampl) ** 2)
    ssim_score = ssim(gray_orig, gray_ampl)

    # Append values to the lists
    mse_values.append(mse)
    ssim_values.append(ssim_score)
print(mse_values)
print(ssim_values)
# Calculate the average MSE and SSIM values
average_mse = np.mean(mse_values)
average_ssim = np.mean(ssim_values)

# Print the results
print(f'Average MSE: {average_mse}')
print(f'Average SSIM: {average_ssim}')

# Release the video captures
cap_original.release()
cap_amplified.release()
