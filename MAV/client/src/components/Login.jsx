import { useEffect } from "react";

const YourComponentName = () => {
    function handleCallbackResponse(response){
        console.log("Encoded JWT ID tokens: " + response.credential);
        // var userObject = jwt_decode(response.credential);
        // console.log(userObject);
        // setUser(userObject);
        document.getElementById("signInDiv").hidden = true;
        // history.push('/phoneno');
      }
    
    //   function handleSignOut(event){
    //     //setUser({});
    //     document.getElementById("signInDiv").hidden = false;
    //   }
    
      useEffect(() => {
        google.accounts.id.initialize({
          client_id: "714584002082-25u0p44a65h6dufqp6jr8upgjurupavg.apps.googleusercontent.com",
          callback: handleCallbackResponse
        });
    
        google.accounts.id.renderButton(
          document.getElementById("signInDiv"),
          {theme:"outline", size:"large"}
        );
    
        // google.accounts.id.prompt();
      }, []);
    return (
      <div>
      
      </div>
    );
  };
  
  export default YourComponentName;