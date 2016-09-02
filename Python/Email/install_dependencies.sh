#!/bin/bash

echo 'Installing pygmail....'
sudo pip install pygmail

echo 'Setting Environment Variables....'
echo 'export Gmail_ID=your gmail id' >> ~/.bashrc
echo 'export Gmail_Password=your gmail password' >> ~/.bashrc


