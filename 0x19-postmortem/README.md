# Postmorterm

<img src="postmorterm.jpeg" alt="error image" width="400"/>

## Issue Summary
The company's server had a downtime for 8 minutes on December 3rd 2022. The incident occurred from 2:00pm WAT till 2:08pm WAT. GET requests resulted in a 500 internal server error and all users were affected. After a minor update to the app, a script accidentally stopped the web server nginx from running.

## Timeline
The issue was detected 5 minutes after deployment (2:05pm WAT) after a customer complained of not being able to gain access to the app. The error logs were checked and it showed that nginx was not running. Nginx was restarted and the server was up again.

## Root cause and resolution
During deployment, a script was accidentally run which stopped the nginx server. The script was found and removed. The nginx server was restarted again and the error was resolved.

## Corrective and preventative measures
The devops team had a meeting and agreed that after each deployment, the status of the server should always be checked.
