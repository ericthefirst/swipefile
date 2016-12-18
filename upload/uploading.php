<?php
	print("<html>\n\t<head>\n\t\t<title>Uploading file...</title></head><body>");

	$target_dir = "../img/";
	$title = $_POST['title'];
	$target_file = $target_dir . basename($title . ".png");
	print("<h1>Uploading $target_file</h1>");

	$uploadOk = 1;
	$imageFileType = pathinfo($target_file,PATHINFO_EXTENSION);
	
	// Check if image file is a actual image or fake image
	if(isset($_POST["submit"])) {
    	$check = getimagesize($_FILES["add"]["tmp_name"]);
    	if($check !== false) {
        	echo "<p>File is an image of type " . $check["mime"] . ".</p>";
        	$uploadOk = 1;
    	} 
    	else {
        	echo "<p>File is not an image.</p>";
        	$uploadOk = 0;
   		}}

	// Check if $uploadOk is set to 0 by an error
	if ($uploadOk == 0) {
    	echo "<p>Sorry, your file was not uploaded.</p>";
	// if everything is ok, try to upload file
	} else {
    if (move_uploaded_file($_FILES["add"]["tmp_name"], $target_file)) {
       echo "<p>The file ". basename( $_FILES["add"]["name"]). " has been uploaded.<p>";
			 $records = fopen("../records", "a");
			 fwrite($records, $title . "\t" . $_POST['comments']. "\n");
			 fclose($records);
    } else {
        echo "<p>Sorry, there was an error uploading your file.</p>";
    }
	}

	echo '<p><a href="upload_portal.html">Upload another</a><p>';
	echo '<p><a href="../index.cgi">View the collection</a>';
	echo '</form>';
	echo '</body></html>';

?>
