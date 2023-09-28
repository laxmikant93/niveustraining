<?php
// Database connection details
$servername = "34.68.3.172"; // Replace with your MySQL server address
$username = "laxmikant"; // Replace with your MySQL username
$password = "password"; // Replace with your MySQL password
$dbname = "laxmikantdb"; // Replace with the name of your MySQL database

// Create a database connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check for connection errors
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Check if the form has been submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Parameters from the form
    $name = $_POST['name'];
    $password = $_POST['password'];
    $email = $_POST['email'];

    // Hash the password
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

    // Check if password meets minimum length requirement
    if (strlen($password) < 8) {
        echo "Password must be at least 8 characters long";
    } else {
        // SQL query to insert data into the user registration table
        $sql = "INSERT INTO users (username, password, email) VALUES ('$name', '$hashedPassword', '$email')";

        if ($conn->query($sql) === TRUE) {
            echo "User data submitted successfully";
        } else {
            echo "Error: " . $sql . "<br>" . $conn->error;
        }
    }
}

// Close the database connection
$conn->close();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to Niveus</title>
    <style>
        /* Your CSS styles here */
    </style>
</head>
<body>
    <div class="container">
        <h2>Welcome to Niveus</h2>
        <form action="index.php" method="post">
            <div class="form-group">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
            </div>
            <div class="form-group">
                <label for="password">Password (minimum 8 characters):</label>
                <input type="password" id="password" name="password" required>
            </div>
            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
            </div>
            <button type="submit">Register</button>
        </form>
    </div>
</body>
</html>

