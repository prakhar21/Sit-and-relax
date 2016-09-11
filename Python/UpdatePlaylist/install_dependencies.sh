#!/bin/bash

echo 'Installing Pafy...'
sudo pip install pafy

echo 'Installing Convertor...'
sudo apt-get install pacpl

echo 'Installing Dropbox...'
sudo pip install dropbox

echo 'Installing PyUSB...'
sudo pip install pyusb --pre

echo "Installing the Media transfer Protocol file system..."
sudo apt-get install mtpfs

echo "Creating mount point..."
sudo mkdir /media/onex

echo "Setting Permission to r/w"
sudo chmod 775 /media/onex
sudo mtpfs -o allow_other /media/onex

echo "Opening (rules) file and setting the authentication..."
#sudo gedit /etc/udev/rules.d/51-android.rules
#SUBSYSTEM=="usb", SYSFS{idVendor}=="0bb4", MODE="0666"

echo "Restarting service..."
sudo service udev restart

echo 'Setting Environment Variables...'
echo "export Playlist_Location='https://www.youtube.com/watch?v=SjahQsqSLLY&index=1&list=PLINP9i2Sqbf-vCwVXXfEvJOTnco5GOjMf'" >> ~/.bashrc





