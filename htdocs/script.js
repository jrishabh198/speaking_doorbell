// Put event listeners into place
		window.addEventListener("DOMContentLoaded", function() {
			// Grab elements, create settings, etc.
            var canvas = document.getElementById('canvas');
            var context = canvas.getContext('2d');
            var video = document.getElementById('video');
            var mediaConfig =  { video: true };
            

            var errBack = function(e) {
            	console.log('An error has occurred!', e)
            };


			// Put video listeners into place
            if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
                navigator.mediaDevices.getUserMedia(mediaConfig).then(function(stream) {
                    video.src = window.URL.createObjectURL(stream);
                    video.play();
                });
            }

            /* Legacy code below! */
            else if(navigator.getUserMedia) { // Standard
				navigator.getUserMedia(mediaConfig, function(stream) {
					video.src = stream;
					video.play();
				}, errBack);
			} else if(navigator.webkitGetUserMedia) { // WebKit-prefixed
				navigator.webkitGetUserMedia(mediaConfig, function(stream){
					video.src = window.webkitURL.createObjectURL(stream);
					video.play();
				}, errBack);
			} else if(navigator.mozGetUserMedia) { // Mozilla-prefixed
				navigator.mozGetUserMedia(mediaConfig, function(stream){
					video.src = window.URL.createObjectURL(stream);
					video.play();
				}, errBack);
			}

			// Trigger photo take
			document.getElementById('snap').addEventListener('click', function() {
				context.drawImage(video, 0, 0, 640, 480);
			});
		}, false);
		function myFunction() {
			var modal = document.getElementById('myModal');

			modal.style.display = "none";
			$.ajax({
			type: "POST",

			url: "http://172.25.34.202:5000/setname",
			data: { 
				name : document.getElementById("hh").value
				// data1 : 'value'
			},
			// dataType: 'json'
			}).done(function(msg) {

			console.log('saved');
			
			// var msg2 = new SpeechSynthesisUtterance('hello ');
			var modal = document.getElementById('myModal');
			
				// window.speechSynthesis.speak(msg2);
				var msg1 = new SpeechSynthesisUtterance(msg);
				window.speechSynthesis.speak(msg1);
			

			
		});
   			 
		}

		document.getElementById("upload").addEventListener("click", function(){
		var dataUrl = canvas.toDataURL();
		$.ajax({
			type: "POST",

			url: "http://172.25.34.202:5000/upload",
			data: { 
				imgBase64: dataUrl
				// data1 : 'value'
			},
			// dataType: 'json'
			}).done(function(msg) {
			console.log('saved');
			
			// var msg2 = new SpeechSynthesisUtterance('hello ');
			var modal = document.getElementById('myModal');
			if(msg=="naam pucho"){
				modal.style.display = "block";
			}
			else{
				// window.speechSynthesis.speak(msg2);
				var msg1 = new SpeechSynthesisUtterance(msg);
				window.speechSynthesis.speak(msg1);
			}

			
		});
	});



