<?php
class MyDB extends SQLite3
{
  function __construct()
  {
     $this->open('/resources/python/templog_raspi-6.db');
  }
}
$db = new MyDB();
if(!$db){
  echo $db->lastErrorMsg();
} else {
  echo "Opened database successfully\n";
}
?>
<html >
  <head>
    <meta charset="UTF-8">
    <title>Fancy Mobile Flat Navigation</title>
      <link rel="stylesheet" href="resources/css/menustyle.css">
</head>

  <body>


  </body>
</html>
