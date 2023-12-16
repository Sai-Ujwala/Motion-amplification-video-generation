from distutils.log import debug 
from fileinput import filename 
from flask import *  
# from flask_cors import CORS
from flask_cors import CORS, cross_origin
from processing import (getGaussianOutputVideo, getLaplacianOutputVideo,
                        loadVideo, saveVideo)
from evm import laplacian_evm
from constants import gaussian_kernel

app = Flask(__name__)  
# # CORS(app, resources={r"/": {"origins": ""}})
# CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
  
@app.route('/', methods=['POST', 'OPTIONS'])   
async def success():   
    if request.method == 'POST':   
        f = request.files['video'] 
        f.save(f.filename)  
        images, fps = loadVideo(video_path=f.filename)

        output_video=await laplacian_evm(images,fps,gaussian_kernel,6,30,16,[0.4,3],0.5)
        output_video.save("output.mp4")




        return {"message":"received"}
  
if __name__ == '__main__':   
    app.run(debug=True)