<?php
function debug_to_console( $data ) {

    if ( is_array( $data ) )
        $output = "<script>console.log( 'Debug Objects: " . implode( ',', $data) . "' );</script>";
    else
        $output = "<script>console.log( 'Debug Objects: " . $data . "' );</script>";

    echo $output;
}
debug_to_console( "Test" );
$rawData = $_POST['imgBase64'];
$filteredData = explode(',', $rawData);
$unencoded = base64_decode($filteredData[1]);
$randomName = rand(0, 99999);
echo "hello";
//Create the image 
$fp = fopen($randomName.'.png', 'w');
fwrite($fp, $unencoded);
fclose($fp);
?>