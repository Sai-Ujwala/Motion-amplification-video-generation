import React, { useState, useRef, useEffect } from 'react';
import Navbar from './Navbar';

const Home = () => {
  const videoRef = useRef(null);
  const [jsonData, setJsonData] = useState({ url: '' });

  const handleVideoInput = (event) => {
    const file = event.target.files[0];
    if (file) {
      const videoURL = URL.createObjectURL(file);
      videoRef.current.src = videoURL;
    }
  };

  useEffect(() => {
    console.log("running")
    const fetchData = async () => {
      try {
        console.log("inside try")
        const file = videoRef.current.src;
        if (file) {
          const formData = new FormData();
          formData.append('video', file);

          const response = await fetch('http://127.0.0.1:5000/', {
            method: 'POST',
            body: formData,
          });

          setJsonData({ url: '' });

          if (response.ok) {
            const data = await response.json();
            console.log(data); // Check the content of the response
            setJsonData({ url: data.url }); // Set the URL correctly
          } else {
            console.error('Failed to upload video');
          }
        }
      } catch (error) {
        console.error('Error uploading video:', error);
      }
    };

    fetchData();
  }, [videoRef]);

  console.log(jsonData.url);

  return (
    <div className="home">
      <Navbar />
      <header
        style={{
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          padding: '10px',
        }}
      >
        <div className="input" style={{ flex: 1 }}>
          <input type="file" accept="video/*" onChange={handleVideoInput} />
         
          <video ref={videoRef} controls width="640" height="480" />
        </div>
        <div className="output" style={{ flex: 1, display: 'flex', justifyContent: 'center' }}>
         
          <video width="640" height="480" controls>
            {jsonData.url && <source src={jsonData.url} type="video/mp4" />}
            Your browser does not support the video tag.
          </video>
        </div>
      </header>
    </div>
  );
};

export default Home;
