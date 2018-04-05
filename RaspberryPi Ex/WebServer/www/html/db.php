<?php
$servername = "localhost"; 
$username = "root";
$password = "password"; 
$dbname = "my_db";
// Create connection $conn = new mysqli($servername, $username, $password, $dbname); // Check connection if ($conn->connect_error) { die("Connection failed: " . $conn->connect_error); } 
$sql = "SELECT * FROM tabella"; 
$result = $conn->query($sql);
if ($result->num_rows > 0) { 
// Output data of each row 
while($row = $result->fetch_assoc()) 
{ 
echo $row["colonna2"]." ".$row["colonna3"]." ".$row["colonna4"]."<BR>"; } 
} else { 
echo "No results"; 
} 
$conn->close(); 
?>
