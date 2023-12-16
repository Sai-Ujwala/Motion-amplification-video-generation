import React, { useEffect } from 'react'
import { useState } from 'react';
import Navbar from './Navbar';
import axios from "axios";
//import playButtonImage from '../assets/playButtomImage.jpg';

const Home = () => {
    const videoRef = React.useRef(null);
    // const responseVideoRef = React.useRef(null);
    const [jsonData, setJsonData] = useState({'url': ''});

  const handleVideoInput = async (event) => {
    setJsonData({'url': ''})
    const file = event.target.files[0];
    if (file) {
      const videoURL = URL.createObjectURL(file);
      videoRef.current.src = videoURL;
    }
  
    //sending the input video to the server
    if (file) {
      const formData = new FormData();
      formData.append('video', file);

      try {
        // const response = await fetch('http://127.0.0.1:5000', {
        //   method: 'POST',
        //   // mode: 'no-cors',
        //   body: formData,
          
        // });
        const response = await axios.post('http://localhost:5000', formData);
        // setJsonData({'url': ''})
        console.log(response)
        
        if (response.status===200) {
        //const responseData = await response.blob();
        //   const videoURL = URL.createObjectURL(responseData);
        //   responseVideoRef.current.src = videoURL;
        //   if (responseVideoRef.current) {
        //     responseVideoRef.current.src = videoURL;
        // } else {
        //     console.error('Response video element is null.');
        // }
          const data = response.data;
          console.log(data)
          setJsonData({ url: data.url });
        //   console.log(jsonData.url);
        } else {
          console.error('Failed to upload video');
        }
      } catch (error) {
        console.error('Error uploading video:', error);
      }

    }

  };
console.log(jsonData.url);
  return (
    <div className='home'>
        <Navbar/>
        <header
        style={{
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          padding: '10px',
        //   border: '1px solid #ddd',
        }}
      >
        <div className='input' style={{ flex: 1 }}>
            <input
                type="file"
                accept="video/*"
                onChange={handleVideoInput}
            />

            {/* {videoRef && <img className='preview1' src={playButtonImage} alt="Play Button" />} */}
            <video ref={videoRef} controls width="640" height="480" />
        </div>
      {/* <video ref={responseVideoRef} controls width="640" height="480" /> */}
        <div className='output' style={{ flex: 1, display: 'flex', justifyContent: 'center'}}>
            {/* {!jsonData.url && <img className='preview2' src={playButtonImage} alt="Play Button" />} */}
            <video width="640" height="480" controls>
                
                {jsonData.url && <source src={jsonData.url} type="video/mp4" />}
                Your browser does not support the video tag.
            </video>
        </div>
      </header>
    </div>
  );
    
}

export default Home