from moviepy.editor import VideoFileClip

# Define the paths for the input and output files
input_file_path = 'output.avi'
output_file_path = 'output_video.mp4'

# Load the video clip
clip = VideoFileClip(input_file_path)

# Write the video clip to the output file in MP4 format
clip.write_videofile(output_file_path, codec='libx264', audio_codec='aac')

print(f'File {input_file_path} successfully converted to {output_file_path}')
