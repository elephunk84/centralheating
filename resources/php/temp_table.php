<?php

  try
  {
    //open the database
    $db = new PDO('sqlite:/home/pi/GitRepo/centralheating/resources/python/templog_raspi-6.db');

    //now output the data to a simple html table...
    print "<table border=1>";
    print "<tr><td>Date & Time</td><td>Temp</td>";
    $result = $db->query('SELECT * FROM temps');
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
