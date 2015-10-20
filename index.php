<html>
<meta http-equiv="refresh" content="10">

  <head>
    <meta charset="UTF-8">
    <title>Iains Heating Control</title>
      <link rel="stylesheet" href="resources/css/menustyle.css">
</head>

  <body>
<?php
try
  {
    //open the database
    $db = new PDO('sqlite:/home/pi/GitRepo/centralheating/resources/python/templog_raspi-5.db');

    //now output the data to a simple html table...
    print "<table border=1>";
    print "<tr><td>Living Room</td><td>Temp</td>";
    $result = $db->query('SELECT * FROM temps ORDER BY ROWID DESC LIMIT 1;');
    foreach($result as $row)
    {


      print "<tr><td>".$row['timestamp']."</td>";
      print "<td>".$row['temp']."</td>";
    }
    print "</table>";

    // close the database connection
    $db = NULL;
  }
  catch(PDOException $e)
  {
    print 'Exception : '.$e->getMessage();
  }
try
  {
    //open the database
    $db = new PDO('sqlite:/home/pi/GitRepo/centralheating/resources/python/templog_raspi-6.db');

    //now output the data to a simple html table...
    print "<table border=1>";
    print "<tr><td>Bedroom</td><td>Temp</td>";
    $result = $db->query('SELECT * FROM temps ORDER BY ROWID DESC LIMIT 1;');
    foreach($result as $row)
    {


      print "<tr><td>".$row['timestamp']."</td>";
      print "<td>".$row['temp']."</td>";
    }
    print "</table>";

    // close the database connection
    $db = NULL;
  }
  catch(PDOException $e)
  {
    print 'Exception : '.$e->getMessage();
  }
?>


  </body>
</html>
