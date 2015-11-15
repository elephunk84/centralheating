<meta http-equiv="refresh" content="10;url=http://192.168.1.5/test.php" />
<link rel="stylesheet" href="/resources/css/style.css">
<iframe id="forecast_embed" type="text/html" frameborder="0" height="245" width="100%" src="http://forecast.io/embed/#lat=53.3353&lon=-2.7307&units=uk&name=Runcorn England"> </iframe>



<?php
if (isset($_POST['offbutton'])) { exec('echo "" > ./status'); }
if (isset($_POST['onbutton'])) { exec('echo "ON" > ./status'); }
echo file_get_contents( "./status" );
?>
<form action="" method="post" align="center">
    <button type="submit" name="onbutton">Manual Override On</button>
    <button type="submit" name="offbutton">Manual Override Off</button>
</form>
<?php
$db = new PDO ('sqlite:resources/python/templog_raspi-5.db');

$results = $db->query('SELECT * FROM temps');
while ($row = $results->fetchArray())
{
var_dump($row);
}
?>
