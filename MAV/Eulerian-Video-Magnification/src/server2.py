from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from processing import loadVideo, saveVideo
from evm import laplacian_evm
from constants import gaussian_kernel
import uvicorn
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
from twilio.rest import Client
import cloudinary
import cloudinary.uploader
from moviepy.editor import VideoFileClip
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
# origins = [
#    "http://127.0.0.1:5173"
# ]
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://127.0.0.1:5173"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
origins = [
    # "http://localhost.tiangolo.com",
    # "https://localhost.tiangolo.com",
    # "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.post("/")
async def success(video: UploadFile = File(...)):
    contents = await video.read()
    with open(video.filename, "wb") as file:
        file.write(contents)
    
    images, fps = loadVideo(video_path=video.filename)
    output_video =laplacian_evm(images, fps, gaussian_kernel, 6, 30, 16, [0.4, 3], 0.5)
    saveVideo(video=output_video,saving_path="output.avi",fps=fps)
    input_file_path = 'output.avi'
    output_file_path = 'output_video.mp4'

    # Load the video clip
    clip = VideoFileClip(input_file_path)

    # Write the video clip to the output file in MP4 format
    clip.write_videofile(output_file_path, codec='libx264', audio_codec='aac')

    print(f'File {input_file_path} successfully converted to {output_file_path}')

    cap_original = cv2.VideoCapture('output.avi')
    mse_values=[]
    print("hi")
    while cap_original.isOpened():
        ret_orig, frame_orig = cap_original.read()
        if not (ret_orig):
            break
        frame_orig = cv2.resize(frame_orig, (640, 480))
        gray_orig = cv2.cvtColor(frame_orig, cv2.COLOR_BGR2GRAY)
        mse = np.mean((gray_orig ) ** 2)
        mse_values.append(mse)
    average_mse = np.nanmean(mse_values)
    print(f"average{average_mse}")
    if average_mse>1:
        account_sid = "AC6d7c8515de9fbd7cc7b53be32d982cb4"
        auth_token = "57a597156adb8783a7d2c570c1dece1e"

        client = Client(account_sid, auth_token)
        cloudinary.config(
        cloud_name = "dvhdairwt",
        api_key = "279488354499749",
        api_secret = "gp-93BVHEWBycheZnUoIYiH6HBw"
        )
        video_path = 'output_video.mp4'  # Replace with the actual path to your video file
        upload_result = cloudinary.uploader.upload(video_path, resource_type="video")
        cloudinary_url = upload_result['secure_url']
        print(cloudinary_url)
        
        # message = client.messages.create(
        #     body = cloudinary_url,
        #     from_ = "+19384440025",
        #     to = "+919441995960"
        #)

    print(str(cloudinary_url))
    return {"url":cloudinary_url}
    # return {"data":"Tempo"}
if __name__ == "__main__":
    uvicorn.run(app,host="localhost",port=5000)