<html>

<body>

	
	<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
	<video id="video" width="640" height="480" autoplay></video>
	<button class = "round-button" id = "snap">Snap Photo</button>
	<button class = "round-button" id = "upload">upload</button>
	<canvas id="canvas" width="640" height="480"></canvas>

	<script src="script.js"></script>
	<style>
	/* The Modal (background) */
	.round-button {
		
    display:block;
    width:100px;
    height:100px;
    line-height:50px;
    border: 2px solid #f5f5f5;
    border-radius: 50%;
    color:#f5f5f5;
    text-align:center;
    text-decoration:none;
    background: #464646;
    box-shadow: 0 0 3px gray;
    font-size:15px;
    font-weight:bold;
}
.round-button:hover {
    background: #262626;
}

	#snap{
		left:200px;
		top:500px;
		position:absolute;
	}
	#upload{
		left:350px;
		top:500px;
		position:absolute;
	}
	#video{
		top : 50px;
		position : absolute;
		display : block;
	}
	#canvas{
		top : 50px;
		left: 650px;
		position : absolute;
		display : block;
	}
	.modal {
	    display: none;  /*Hidden by default*/ 
	    position: fixed; /* Stay in place */
	    z-index: 1; /* Sit on top */
	    left: 0;
	    top: 0;
	    width: 100%; /* Full width */
	    height: 100%; /* Full height */
	    overflow: auto; /* Enable scroll if needed */
	    background-color: rgb(0,0,0); /* Fallback color */
	    background-color: rgba(0,0,0,0.4); /* Black w/ opacity */
	    -webkit-animation-name: fadeIn; /* Fade in the background */
	    -webkit-animation-duration: 0.4s;
	    animation-name: fadeIn;
	    animation-duration: 0.4s
	}

	/* Modal Content */
	.modal-content {
	    position: fixed;
	    bottom: 0;
	    background-color: #fefefe;
	    width: 100%;
	    -webkit-animation-name: slideIn;
	    -webkit-animation-duration: 0.4s;
	    animation-name: slideIn;
	    animation-duration: 0.4s
	}

	/* The Close Button */
	
	.close:hover,
	.close:focus {
	    color: #000;
	    text-decoration: none;
	    cursor: pointer;
	}

	.modal-header {
	    padding: 2px 16px;
	    background-color: #5cb85c;
	    color: white;
	}

	.modal-body {padding: 2px 16px;}

	.modal-footer {
	    padding: 2px 16px;
	    background-color: #5cb85c;
	    color: white;
	}

	/* Add Animation */
	@-webkit-keyframes slideIn {
	    from {bottom: -300px; opacity: 0} 
	    to {bottom: 0; opacity: 1}
	}

	@keyframes slideIn {
	    from {bottom: -300px; opacity: 0}
	    to {bottom: 0; opacity: 1}
	}

	@-webkit-keyframes fadeIn {
	    from {opacity: 0} 
	    to {opacity: 1}
	}

	@keyframes fadeIn {
	    from {opacity: 0} 
	    to {opacity: 1}
	}
	</style>
	</head>
	<body>
	<!-- The Modal -->
	<div id="myModal" class="modal">

	  <!-- Modal content -->
	  <div class="modal-content">
	    <div class="modal-header">
	      
	      <h2>Please enter your name</h2>
	    </div>
	    <div class="modal-body">
	     <form id="frm1">
	  		 name: <input id = 'hh' type="text" name="name"><br>
 		 <input type="button" onclick="myFunction()" value="Submit">
		</form>
	    </div>
	    <div class="modal-footer">
	      <h3></h3>
	    </div>
	  </div>

	</div>

	
</body>
</html>