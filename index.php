<html>

<head>
<meta http-equiv="refresh" content="10">
<link rel="stylesheet" href="/resources/css/style.css">
<iframe id="forecast_embed" type="text/html" frameborder="0" height="245" width="100%" src="http://forecast.io/embed/#lat=53.3353&lon=-2.7307&units=uk&name=Runcorn England"> </iframe>
<link href='https://fonts.googleapis.com/css?family=Open+Sans' rel='stylesheet' type='text/css'>
<title>Iains Central Heating Control</title>
</head>

<body>

<h1 align="center">
Current Temperature is - 
<?php
echo file_get_contents( "resources/temp" );
?>
&deg;C
</h1>
<h2 align="center">
Central Heating is -
<?php
echo file_get_contents( "resources/webstatus" );
?></br><?php
$status=fgets(fopen( "resources/webstatus", 'r'));
switch ($status) { 
    case "ON":
        $image = "resources/images/GREENLED.png";
    break;
    case ($status=="OFF"):
        $image = "resources/images/REDLED.png";
    break;
};

echo "<img src=\"$image\" height=\"48\"  width=\"48\"/>";
?>
</br>
Schedule Program - 
<?php
if (filesize('resources/run_schedule') <= 1 )
{
echo "OFF";
}
if (filesize('resources/run_schedule') >= 1 )
{
echo "ON";
}
?>
</h2>
<h3 align="center">
<?php
if (filesize('resources/run_schedule') >= 1)
{
?>
--------Active Program--------
</br>
<?php
$firstline = fgets(fopen("resources/run_schedule", 'r'));
$file = escapeshellarg("resources/run_schedule");
$lastline = `tail -n 1 $file`;
?>
ON:- 
<?php
echo $firstline;
?>
</br>
OFF:- 
<?php
echo $lastline;
?>
</br>
-------------------------------------
<?php
}
?>
</br>
</h3>
</br>
<h2 align="center">
Manual Override is - 
<?php
if (filesize('resources/status') <= 1 )
{
echo "OFF";
}
echo file_get_contents( "./resources/status" );
?>
</h2>
<?php
if (isset($_POST['offbutton'])) { exec('echo "" > ./resources/status'); }
if (isset($_POST['onbutton'])) { exec('echo "ON" > ./resources/status'); }
?>
<form action="" method="post" align="center">
    <button type="submit" name="onbutton">Manual Override On</button>
    <button type="submit" name="offbutton">Manual Override Off</button>
</form>
<?php
?>

</body>

</html>
