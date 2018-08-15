<?php
$command = escapeshellcmd('python faced.py');
$output = shell_exec($command);
// echo $output;
if ($output == 1) {
	echo "face detected";
}else{
	echo "No face detected";
}
?>