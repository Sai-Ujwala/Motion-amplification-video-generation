import requests

url = 'http://127.0.0.1:5000/'  # Replace with the appropriate URL

files = {'video': open('result1.avi', 'rb')}  # Replace with the path to your video file

try:
    response = requests.post(url, files=files)
    if response.status_code == 200:
        print("File successfully sent to the server.")
    else:
        print(f"Failed to send the file. Status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
