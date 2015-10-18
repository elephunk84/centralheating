<!DOCTYPE HTML>
<html lang="en">
<head>
 <meta http-equiv="refresh" content="5" />
<link rel="stylesheet" href="/resources/css/style.css">
<?php 
if (isset($_POST['RedON']))
{
exec("python /var/www/pifaceon.py");
}

if (isset($_POST['RedOFF']))
{
exec("python /var/www/pifaceoff.py");
}

if (isset($_POST['plugon']))
{
exec("/usr/local/bin/tdtool -n 1");
}
if (isset($_POST['plugoff']))
{
exec("/usr/local/bin/tdtool -f 1");
}

if (isset($_POST['plugon1']))
{
exec("/usr/local/bin/tdtool -n 101");
}

if (isset($_POST['plugoff1']))
{
exec("/usr/local/bin/tdtool -f 101");
}

if (isset($_POST['allon']))
{
exec("python /var/www/pifaceon.py");
exec("/usr/local/bin/tdtool -n 1");
exec("/usr/local/bin/tdtool -n 101");
}
if (isset($_POST['alloff']))
{
exec("/usr/local/bin/tdtool -f 1");
exec("/usr/local/bin/tdtool -f 101");
exec("/usr/local/bin/tdtool -f 4");
exec("python /var/www/pifaceoff.py");
}

if (isset($_POST['microon']))
{
exec("/usr/local/bin/tdtool -n 7");
}

if (isset($_POST['microoff']))
{
exec("/usr/local/bin/tdtool -f 7");
}

if (isset($_POST['livingroom']))
{
exec("/usr/local/bin/tdtool -n 4");
}

if (isset($_POST['livingroom']))
{
exec("/usr/local/bin/tdtool -f 4");
}




?>

  <title>Iain's Central Control</title>
</head>
<body>
<h1 style="text-align: center;">Control Center Home</h1>

<div class="container">
    <div class="de">
        <div class="den">
          <div class="dene">
            <div class="denem">
              <div class="deneme">
            <span><?php
$line = '';

$f = fopen('./resources/python/log.log', 'r');
$cursor = -2;

fseek($f, $cursor, SEEK_END);
$char = fgetc($f);

/**
 * Trim trailing newline chars of the file
 */
while ($char === "\n" || $char === "\r") {
    fseek($f, $cursor--, SEEK_END);
    $char = fgetc($f);
}

/**
 * Read until the start of file or first newline char
 */
while ($char !== false && $char !== "\n" && $char !== "\r") {
    /**
     * Prepend the new char
     */
    $line = $char . $line;
    fseek($f, $cursor--, SEEK_END);
    $char = fgetc($f);
}

echo $line;
?></span>
              </div>
            </div>
          </div>
        </div>
    </div>
</div>


<p>Select the device you wish to turn on and off?</p>
<br>
<?
//$ipaddress = $_SERVER["SERVER_NAME"];
//echo $ipaddress;
?>
<form method="post">
  <table
 style="width: 75%; text-align: left; margin-left: auto; margin-right: auto;"
 border="0" cellpadding="2" cellspacing="2">
    <body>

</div>


<div height: 50%;>
      <tr>
        <td style="text-align: center;"><b>Device On</b></td>
        <td style="text-align: center;"><b>Device Off</b></td>
    
      </tr>
      <tr>
        <td style="text-align: center;"><button class="button" name="RedON">Lamp On</button></td>
        <td style="text-align: center;"><button class="button" name="RedOFF">Lamp Off</button></td>
<tr/>
<tr>
        <td style="text-align: center;"><button class="button" name="plugon">Downstairs TV On</button></td>
        <td style="text-align: center;"><button class="button" name="plugoff">Downstairs TV Off</button></td>
      </tr>

<tr>
        <td style="text-align: center;"><button class="button" name="plugon1">Upstairs TV On</button></td>
        <td style="text-align: center;"><button class="button" name="plugoff1">Upstairs TV Off</button></td>
      </tr>
<tr>
        <td style="text-align: center;"><button class="button" name="allon">Coming Home On</button></td>
        <td style="text-align: center;"><button class="button" name="alloff">Going Out Off</button></td>
      </tr>

<tr>
        <td style="text-align: center;"><button class="button" name="microon">Nuke the food</button></td>
        <td style="text-align: center;"><button class="button" name="microoff">No Nukes, No Nukes</button></td>
      </tr>

<tr>
    <td style="text-align: center;"><button class="button" name="livingroom">Livingroom On</button></td>
        <td style="text-align: center;"><button class="button" name="livingroom">Livingroom Off</button></td>
      </tr>
<tr>
        <td style="text-align: center;"><button class="button" name="livingroom1">Youtube On</button></td>
        <td style="text-align: center;"><button class="button" name="livingroom1">Youtube Off</button></td>
      </tr>
    </body>
  </table>
</form>

<p>

<?

?>
</p>
</div>

</body>
</html>

