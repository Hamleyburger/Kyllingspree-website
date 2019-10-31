<?php

if(isset($_POST['submit']))
{
    /* declaring variables*/
    $name = $_POST['name'];
    $mailFrom = $_POST['email'];
    $message = $_POST['message'];
    $subject = $_POST['subject'];
    
    
    $mailTo = "almatem@roskilde.dk";
    $headers = "From: ".$mailFrom;
    $txt = "You have received an e-mail from ".$name.".\n\n".$message;
    
    /*using variables in already existing functions*/
    mail($mailTo, $subject, $txt, $headers);
    header("Location: contact.php?mailsend");
}
