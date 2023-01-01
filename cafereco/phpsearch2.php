<!doctype html>
<html lang="ko">
  <head>
    <meta charset="utf-8">
    <title>서울 카페</title>
    <style>
      body {
        font-family: Consolas, monospace;
        font-family: 11.5px;
        background-color: #DBCABE;
      }
      table {
        width: 100%;
        text-align: center;
        border: 1px solid #fff;
        border-spacing: 1px;
        font-family: 'Cairo', sans-serif;
        margin: auto;
        border: 1px solid;
      }

      table caption {
        text-align: left;
        font-weight: bold;
        font-size: 60pt;
      }

      th, td {
        padding: 10px;
        border-bottom: 1px solid #dadada;
      }

      table td {
        padding: 10px;
        background-color: #eee;
      }

      table th {
        background-color: #333;
        color: #fff;
        padding: 10px;
      }

      caption { 
        display: table-caption;
        text-align: center;
      }

      tr:nth-child(2n){
        background-color: red;
      }

    </style>
  </head>
  <body>
  </body>
</html> 

<?php
ini_set('memory_limit','-1');
$search = $_POST['search'];

$servername = "localhost";
$username = "root";
$password = "root";
$db = "cafereco";

$conn = new mysqli($servername, $username, $password, $db);

if ($conn->connect_error){
	die("Connection failed: ". $conn->connect_error); 
}

/*$sql = "SELECT * FROM `incheon_cafe_info` WHERE 상호명 LIKE '%$search%' OR 도로명주소 LIKE '%$search%' ORDER BY `incheon_cafe_info`.`평균별점` DESC";*/
$sql = "SELECT * FROM `seoul_cafe_info` WHERE 키워드 LIKE '%$search%' ORDER BY `seoul_cafe_info`.`평균별점` DESC";


$result = $conn->query($sql);

if ($result->num_rows > 0){
  echo "<table>
  <caption>검색 키워드: $search</caption>
  <tr>
  <th>상호명</th>
  <th>지점명</th>
  <th>평균별점</th>
  <th>중분류</th>
  <th>소분류</th>
  <th>지번주소</th>
  <th>도로명주소</th>
  <th>새우편번호</th>
  </tr>";
while($row = $result->fetch_assoc() ){
  echo "<tr>
  <td>".$row["상호명"]."</td>
  <td>".$row["지점명"]."</td>
  <td>".$row["평균별점"]."</td>
  <td>".$row["중분류"]."</td>
  <td>".$row["소분류"]."</td>
  <td>".$row["지번주소"]."</td>
  <td>".$row["도로명주소"]."</td>
  <td>".$row["우편번호"]."</td>
  </tr>";
}
echo "</table>";
} else {
	echo "0 records";
}

$conn->close();
?>

