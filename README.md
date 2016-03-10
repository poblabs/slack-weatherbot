# Slack weatherbot

A Slack bot that fetches weather data using the Outgoing Webhooks Custom Integrations. 

I have this setup to listen on any Slack channel for "w" as the trigger word. Users can use the phrase "w 90210" to retrieve the weather from zip code 90210. 

This driver requires:
- Python untangle library (e.g. sudo pip install untangle)

## Install
- Copy both the weather.py and weather.php file to a public directory on your webserver. 
- Setup a new Outgoing WebHook in Slack (https://slack.com/apps > Configure > Custom Integrations > Outgoing WebHooks) 
- Set the channel to listen on to your desire. 
- Set the Trigger Word to w
- Set the URL to the public URL the weather.php file will reside
- Copy the Token, we'll need this soon
- Give it a label, and a username
- Click Save
- Open weather.php and enter your token into the `$slack_token` variable
- Update the `exec()` path in weather.php to match the location of weather.py

## Version
1.0 - Initial

## Troubleshooting
- Uncomment the `syslog` lines in both scripts to try and track down any issues. 

I'm open to pull requests!
