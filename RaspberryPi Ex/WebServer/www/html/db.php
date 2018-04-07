<?php
$servername = "localhost"; 
$username = "root";
$password = "Raspberry2018"; 
$dbname = "website";
// Create connection 
$conn = new mysqli($servername, $username, $password, $dbname); 
// Check connection 
if ($conn->connect_error) { die("Connection failed: " . $conn->connect_error); } 
$sql = "SELECT * FROM name"; 
$result = $conn->query($sql);
if ($result->num_rows > 0) { 
// Output data of each row 
while($row = $result->fetch_assoc()) 
{ 
echo $row["FirstName"]." ".$row["FamilyName"]." ".$row["Address"]."<BR>"; } 
} else { 
echo "No results"; 
} 
$conn->close(); 
?>
