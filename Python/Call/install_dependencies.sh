#!/bin/bash

echo "Installing Flask..."
sudo pip install Flask

echo "Install Beautiful Soup"
sudo pip install beautifulsoup4

echo 'Setting Environment Variables....'
echo 'export Twilio_Sid=<twilio sid>' >> ~/.bashrc
echo 'export Twilio_Token=<twilio token>' >> ~/.bashrc
echo 'export  Phone_To=<others number>' >> ~/.bashrc
echo 'export Phone_From=<your twlio number>' >> ~/.bashrc
