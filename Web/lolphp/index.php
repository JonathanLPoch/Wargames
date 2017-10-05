<?php
    if ($_SERVER['REQUEST_METHOD'] === 'GET' && isset($_GET['thing1']) && isset($_GET['thing2'])) {
        if ($_GET['thing1'] == $_GET['thing2']) {
            die("thing1 and thing2 must be different!");
        } else if (hash('sha256', $_GET['thing1']) === hash('sha256', $_GET['thing2'])) {
            echo "Correct!\n";
            echo file_get_contents("/flag.txt");
            die();
        } else {
            die("Hashes don't match!");
        }
    }
?>
<html>
    <body>
        <p>Your job is simple. Give me 2 different inputs that hash (sha256) to the same value.</p>
        <form method="GET">
            <input type="text" name="thing1" placeholder="Thing 1" /><br/>
            <input type="text" name="thing2" placeholder="Thing 2" /><br/>
            <input type="submit" value="Submit" />
        </form>
    </body>
</html>
