<?php 



  ini_set('display_errors', 1); error_reporting(E_ALL); 



  // 1. Create connection to database



  mysql_connect('10.6.185.42','myt1301008195275','VTC2@mel') or die('Could not connect to mysql: <hr>'.mysql_error());



  // 2. Select database



  mysql_select_db("myt1301008195275") or die('Could not connect to database:<hr>'.mysql_error());





  // 3. Assign variables (after connection as required by escape string)



      $age=mysql_real_escape_string($_POST['age']);





  // 4. Insert data into table



  mysql_query("INSERT INTO people (age) VALUES ('$age')"); 



  Echo 'Your information has been successfully added to the database.';  



  print_r($_POST);



  mysql_close()



?> 

