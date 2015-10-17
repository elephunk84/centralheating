<?php
$output=shell_exec('/usr/bin/python3 ./python/read_temp.py');
echo "<pre>";
print_r($output);
echo "</pre>";
?>
