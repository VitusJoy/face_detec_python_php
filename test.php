<?php
$command = escapeshellcmd('faced.py');
$output = shell_exec($command);
echo $output;
?>