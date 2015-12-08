<html>

<head>
<meta http-equiv="refresh" content="10">
<link rel="stylesheet" href="/resources/css/style.css">
<link href='https://fonts.googleapis.com/css?family=Open+Sans' rel='stylesheet' type='text/css'>
<title>Iains Central Heating Control</title>
</head>

<body>
<div class="weather" align="left">
<iframe id="forecast_embed" type="text/html" frameborder="0" height="245" width="100%" src="http://forecast.io/embed/#lat=53.3353&lon=-2.7307&units=uk&name=Runcorn England"> </iframe>
</div>
<div class="leftbar">
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
    ?>

</br>

    <?php
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

</br></br>
Schedule Program - 

    <?php
    $schedule=fgets(fopen( "resources/run_schedule", 'r'));
    switch ($schedule) {
        case (strlen(schedule) > 1):
            $run_schedule = "ON";
            echo $run_schedule;
        break;
        case (strlen(schedule) == 0):
            $run_schedule = "OFF";
            echo $run_schedule;
        break;
    };
    ?>

</br>

    <?php

    switch ($run_schedule) {
        case "ON":
        break;
        case "OFF":
            $next_run=fgets(fopen( "resources/next_run", 'r'));
            echo "</br>Next Program - </br>";
            echo $next_run;
        break;
    };
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
    ON:- <?php echo $firstline;?>
    </br>
    OFF:- <?php echo $lastline;?>
    </br>
    -------------------------------------
    <?php
    };
    ?>

</br>
</h3>
<h2 align="center">
Manual Override is - 

    <?php
    if (filesize("resources/status") <= 1 )
    {
    echo "OFF";
    }
    echo file_get_contents( "./resources/status" );
    ?>

</h2>

    <?php
    if (isset($_POST['offbutton'])) { exec('echo "" > ./resources/status'); }
    if (isset($_POST['onbutton'])) { exec('echo "ON" > ./resources/status'); }
    $status=fgets(fopen( "./resources/status", 'r'));
    var_dump($_POST);
    if (isset($_POST['advance'])){ 
    switch ($status){
        case "ON":
            exec('echo "" > ./resources/status');
            break;
        case "":
            exec('echo "ON" > ./resources/status');
            break;
    };
    }
    ?>

<form action="" method="post" align="center">
    <button type="submit" name="onbutton">Manual Override On</button>
    <button type="submit" name="offbutton">Manual Override Off</button>
    <button type="submit" name="advance">Advance</button>
</form>

<h2 align="center">
Holiday Mode is - 

    <?php
    if (filesize("resources/holiday") <= 1 )
    {
    echo "OFF";
    }
    echo file_get_contents( "./resources/holiday" );
    ?>

</h2>


    <?php
    if (isset($_POST['offholiday'])) { exec('echo "OFF" > ./resources/holiday'); }
    if (isset($_POST['onholiday'])) { exec('echo "ON" > ./resources/holiday'); }
    ?>

<form action="" method="post" align="center">
    <button type="submit" name="onholiday">Holiday Mode On</button>
    <button type="submit" name="offholiday">Holiday Mode Off</button>
</form>

</div>
</body>

</html>
