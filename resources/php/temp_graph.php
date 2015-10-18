<?php

## Put todays date into a variable for later use...

$date= date("d-m-Y");

## Tell PHP the location of our datafile for the current date...
## file_get_contents() retrieves the contents and places it into a 
## variable as a string.

###$txt_file= file_get_contents('temp_log_' .$date. '.txt');
$txt_file= file_get_contents('../python/log.log');

## Do a little error checking and display a message if the text 
## file is missing...

if(!$txt_file) {
echo "<br>ERROR - There is no information for this date.";

## If the file is present lets get going...

} else {

## Retrieve each row from the file.  The explode() function
## in this instance is using each new line ("\n") as a delimiter
## and assigning the entire file to a variable ($rows)...
 
$rows= explode("\n", $txt_file);

## As the explode() function will treat the last line as a new 
## record, we need to remove the last record (which is a blank line).  
## array_pop() does this for us automatically...

array_pop($rows);

## Setup two blank arrays for our data.  One for the time and one
## for the temperatures...

$temp=array();
$time=array();

## Now we use a foreach statement to parse each row so that we can 
## process them and sort our data. We assign each row to a 
## variable ($data)...

foreach($rows as $row => $data)
{

## Break down the individual record using (,) as delimiter.

$total= explode(",", $data);

## Extract the time from the record and make it loo pretty...

$t= explode(":", $total[1]);
$time[]= "$t[0]:$t[1]";

## Extract the temperature data from the record...
## floor() rounds the number down to the nearest integer.  
## We then multiply this by 100 and divide the rounded down 
## figure by 100.  This gives our temperature in a huma 
## readable fashion with the correct decimal places... 

$temp[]= floor($total[2] * 100) / 100;

## Notice that within this foreach statement I have 
## used the two variables $temp & $time with [] appended 
## to the end.  Doing this saves our new, re-fashioned 
## readings back to the variable turning it into an array of 
## all the data...

## then we end the foreach statement...

}

## Now we use the implode function to accumulate each row 
## that we have processed and save it back to an array.  
## We use (,) as our delimiter again...

$tempa= implode(",", $temp);
$timea= implode(",", $time);

## We have two, human-readable, arrays of data that we can 
## now pass to our graph...
?>
