#!/bin/bash

echo "Installing  twilio-python..."
sudo pip install twilio 

echo "Setting Environment..."
echo 'export Twilio_Sid=<twilio sid>' >> ~/.bashrc
echo 'export Twilio_Token=<twilio token>' >> ~/.bashrc
echo 'export Phone_To=<others number>' >> ~/.bashrc
echo 'export Phone_From=<your twilio number>' >> ~/.bashrc
