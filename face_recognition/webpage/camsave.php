&lt;?php
$rawData = $_POST['imgBase64'];
$filteredData = explode(',', $rawData);
$unencoded = base64_decode($filteredData[1]);
$randomName = rand(0, 99999);;
echo "hello"
//Create the image 
$fp = fopen($randomName.'.png', 'w');
fwrite($fp, $unencoded);
fclose($fp);
?&gt;