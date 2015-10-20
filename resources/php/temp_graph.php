<?php
require_once "/pChart/class/pDraw.class.php";
require_once "/pChart/class/pImage.class.php";
require_once "/pChart/class/pData.class.php";

$db = new PDO 'sqlite:resources/python/templog_raspi-6.db';
$table = "temps";
$request = "SELECT * FROM $table";
while ($row = sqlite3_fetch_array($request))
{$myDataset = AddPoint($row["value"],"timestamp"); }
q$myImage = new pImage(500, 300, $myData);
$myImage->setFontProperties(array(
    "FontName" => PCHART_PATH . "/fonts/GeosansLight.ttf";
    "FontSize" => 15));
$myImage->setGraphArea(25,25, 475,275);
$myImage->drawScale();
$myImage->drawBarChart();
header("Content-Type: image/png");
$myImage->Render(null);
?>
