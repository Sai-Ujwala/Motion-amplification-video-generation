import cv2
import numpy as np
import tqdm
import matplotlib.pyplot as pyplot
import scipy.fftpack

def show_frequencies(vid_data, fps, bounds=None):
    """Graph the average value of the video as well as the frequency strength"""
    averages = []

    if bounds:
        for x in range(1, vid_data.shape[0] - 1):
            averages.append(vid_data[x, bounds[2]:bounds[3], bounds[0]:bounds[1], :].sum())
    else:
        for x in range(1, vid_data.shape[0] - 1):
            averages.append(vid_data[x, :, :, :].sum())

    averages = averages - min(averages)

    charts_x = 1
    charts_y = 2
    pyplot.figure(figsize=(20, 10))
    pyplot.subplots_adjust(hspace=.7)

    pyplot.subplot(charts_y, charts_x, 1)
    pyplot.title("Pixel Average")
    pyplot.xlabel("Time")
    pyplot.ylabel("Brightness")
    pyplot.plot(averages)

    freqs = scipy.fftpack.fftfreq(len(averages), d=1.0 / fps)
    fft = abs(scipy.fftpack.fft(averages))
    idx = np.argsort(freqs)

    pyplot.subplot(charts_y, charts_x, 2)
    pyplot.title("FFT")
    pyplot.xlabel("Freq (Hz)")
    freqs = freqs[idx]
    fft = fft[idx]

    freqs = freqs[len(freqs) // 2 + 1:]
    fft = fft[len(fft) // 2 + 1:]
    pyplot.plot(freqs, abs(fft))

    pyplot.show()
    
def get_capture_dimensions(capture):
    """Get the dimensions of a capture"""
    width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    return width, height
    
capture = cv2.VideoCapture("/content/Eulerian-Video-Magnification/results/motions/baby.avi")
frame_count = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
width, height = get_capture_dimensions(capture)
fps = int(capture.get(cv2.CAP_PROP_FPS))
x = 0
vid_frames = np.zeros((frame_count, height, width, 3), dtype='uint8')
while capture.isOpened():
    ret, frame = capture.read()
    if not ret:
        break
    vid_frames[x] = frame
    x += 1
capture.release()


show_frequencies(vid_frames,fps)