#!/bin/bash

echo 'Installing Pafy...'
sudo pip install pafy

echo 'Installing Convertor...'
sudo apt-get install pacpl

echo 'Installing PyUSB...'
sudo pip install pyusb --pre

#sudo apt-get install go-mtpfs
#sudo apt-get install libmtp
#sudo apt-get install mtpfs mtp-tools

echo 'Setting Environment Variables...'
echo "export Playlist_Location='https://www.youtube.com/watch?v=SjahQsqSLLY&index=1&list=PLINP9i2Sqbf-vCwVXXfEvJOTnco5GOjMf'" >> ~/.bashrc





