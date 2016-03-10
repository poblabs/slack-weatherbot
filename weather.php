<?php
//
// This file accepts the POST input, and passes it to Python
// where it is then parsed and returned as a readable string
// for the weather information. 
//
// (c) 2016 Pat O'Brien - http://obrienlabs.net
// Licensed under the MIT License. Please include original copyright string in any new works.
//

$slack_token = "YOUR_SLACK_TOKEN";

$data = parse_str( file_get_contents("php://input") );

// As a small method of security, make sure the token in POST matches
if ( $token == $slack_token ) {
    $data = explode(" ", $text);
    if ( strtolower( $data[0] ) == "w" ) {
        // Only run the script if w is the first full word
        //syslog(LOG_INFO, "Slack weatherbot check for ". $data[1] ." by ". $user_name ." from channel #". $channel_name); // Log to the syslog for debugging
        exec("/usr/bin/python /YOUR/PATH/TO/weather.py " . $data[1], $output, $retval);
        header('Content-Type: application/json');
        echo '{ "text": "'.$output[0].'" }';
    } else {
        die();
    }
} else {
    header("HTTP/1.0 404 Not Found");
    die();
}

?>
