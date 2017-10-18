<?php
	$ledState = $_GET["ledState"];
	$fanState = $_GET["fanState"];
	
	$file = fopen("state.csv", "w+");
	//$value = "a,b,c,";
	//$value = "{$ledState},{$fanState}','";
	$value = $ledState . "," . $fanState . ",";
	fputcsv($file, explode(',', $value));
	
	fclose($file);

?>
