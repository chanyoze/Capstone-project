<!doctype html>
<html lang="ko">
  <head>
    <meta charset="utf-8">
    <title>제주 카페</title>
    <style>
      body {
        font-family: Consolas, monospace;
        font-family: 12px;
      }
      table {
        width: 100%;
      }
      th, td {
        padding: 10px;
        border-bottom: 1px solid #dadada;
      }
    </style>
  </head>
  <body>
    <h1>제주 카페 정보</h1>
    <table>
      <thead>
        <tr>
          <th>상호명</th>
          <th>지점명</th>
          <th>중분류명</th>
          <th>소분류명</th>
          <th>지번주소</th>
          <th>도로명주소</th>
          <th>신우편번호</th>
        </tr>
      </thead>
      <tbody>
        <?php
        include 'connect.php';
  
          $conn = mysqli_connect( 'localhost', 'phpmyadmin', 'root', 'cafereco' );
          $sql = "SELECT * FROM `jeju_cafe_info`";
          $result = mysqli_query( $conn, $sql );
          
          
          
          while( $row = mysqli_fetch_array( $result ) ) {
            echo
              '<tr><td>'
              . $row[0]
              . "</td><td>"
              . $row[1]
              . "</td><td>"
              . $row[2]
              . "</td><td>"
              . $row[3]
              . "</td><td>"
              . $row[4]
              . "</td><td>"
              . $row[5]
              . "</td><td>"
              . $row[6]
              . '</td></tr>'
            ;
          }
        ?>
      </tbody>
    </table>
  </body>
</html>