#!/usr/bin/bash

#SETUP SCRIPT PSEUDOCODE:
#1. Check if script is run with sudo
#2. Copy service file to /etc/systemd/system/
#3. Reload systemd daemon to recognize new service
#4. Start the service
#5. Enable service to start on boot
#6. Display service status

set -e # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}=== Flask systemd Service Setup ===${NC}\n"

# Check if script is run with sudo
if [ "$EUID" -ne 0 ]; then
    echo -e "${RED}Please run as root or use sudo.${NC}"
    echo "Usage: sudo ./setup.sh"
    exit 1
fi

# get the  actual user (not root) who ran sudo
ACTUAL_USER=${SUDO_USER:-$USER}
USER_HOME=$(eval echo "~$ACTUAL_USER")

# Check if Flask is installed
echo -e "${YELLOW}Checking for Flask...${NC}"
if ! pacman -Qi python-flask &> /dev/null; then
    echo -e "${YELLOW}Flask not found. Installing via pacman...${NC}"
    pacman -S --noconfirm python-flask
else
    echo -e "${GREEN}Flask is already installed${NC}"
fi
# update service file with actual paths
SERVICE_FILE="flask-app.service"
TEMP_SERVICE="/tmp/$SERVICE_FILE.tmp"

echo -e "${YELLOW}Configuring service file...${NC}"
sed "s|%u|$ACTUAL_USER|g; s|%h|$USER_HOME|g" $SERVICE_FILE > $TEMP_SERVICE

#copy sevice file to systemd directory
echo -e "${YELLOW}Installing service file...${NC}"
cp $TEMP_SERVICE /etc/systemd/system/$SERVICE_FILE
rm $TEMP_SERVICE

# Reload systemd to recognize new service
echo -e "${YELLOW}Reloading systemd daemon...${NC}"
systemctl daemon-reload

# Start the service
echo -e "${YELLOW}Starting flask-app service...${NC}"
systemctl start flask-app

# Enable service to start on boot
echo -e "${YELLOW}Enabling flask-app service to start on boot...${NC}"
systemctl enable flask-app



