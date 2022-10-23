setTimeout(function(){
    window.location.reload(1);
 }, 10000);
 var datetime = new Date();
 console.log(datetime);
 document.getElementById("time").textContent = datetime; //it will print on html page 

 var userImageLink = 
 "https://media.geeksforgeeks.org/wp-content/cdn-uploads/20200714180638/CIP_Launch-banner.png";
             var time_start, end_time;
             
             // The size in bytes
             var downloadSize = 5616998;
             var downloadImgSrc = new Image();
   
             downloadImgSrc.onload = function () {
                 end_time = new Date().getTime();
                 displaySpeed();
             };
             time_start = new Date().getTime();
             downloadImgSrc.src = userImageLink;
   
             function displaySpeed() {
                 var timeDuration = (end_time - time_start) / 1000;
                 var loadedBits = downloadSize * 8;
                 
                 /* Converts a number into string
                    using toFixed(2) rounding to 2 */
                 var bps = (loadedBits / timeDuration).toFixed(2);
                 var speedInKbps = (bps / 1024).toFixed(2);
                 var speedInMbps = (speedInKbps / 1024).toFixed(2);
                 document.getElementById('wifi_speed').innerHTML = speedInMbps;
             }