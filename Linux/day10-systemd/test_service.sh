#!/usr/bin/bash

#TEST SCRIPT PSEUDOCODE:
#1. Test service status
#2. Test HTTP endpoint with curl
#3. Test stop and start
#4. Test restart functionality
#5. Test auto-restart by killing the process
#6. View recent logs

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

SEVICE_NAME="flask-app"
URL="http://localhost:5000"

echo -e "${BLUE}╔═══════════════════════════════════════╗${NC}"
echo -e "${BLUE}║  Flask systemd Service Test Suite    ║${NC}"
echo -e "${BLUE}╚═══════════════════════════════════════╝${NC}\n"

#test 1: sevice status
echo -e "${YELLOW}[TEST 1]${NC}Checking service status..."
if systemctl is-active --quiet $SEVICE_NAME; then
    echo -e "${GREEN}✓ Service is active${NC}\n"
else
    echo -e "${RED}✗ Service is not active${NC}\n"
    exit 1
fi

#test 2: http endpoint
echo -e "${YELLOW}[TEST 2]${NC}Checking HTTP endpoint..."
if curl -s $URL | grep -q "running"; then
    echp -e "${GREEN}✓ HTTP endpoint responding${NC}\n"
    curl -s $URL | python3 -m json.tool
else
    echo -e "${RED}✗ HTTP endpoint not responding${NC}\n"
    exit 1
fi

#test 3: Health check
echo -e "${YELLOW}[Test 3]${NC} Testing health endpoint..."
if curl -s $URL/health | grep -q "healthy"; then
    echo -e "${GREEN}✓ Health check passed${NC}\n"
else
    echo -e "${RED}✗ Health check failed${NC}\n"
    exit 1
fi

#test 4: stop and start
echo -e "${YELLOW}[TEST 4]${NC}Testing stop and start..."
sudo systemctl stop $SEVICE_NAME
sleep 2
if systemctl is-active --quiet $SEVICE_NAME; then
    echo -e "${RED}✗ Service did not stop${NC}\n"
    exit 1
else
    echo -e "${GREEN}✓ Service stopped successfully${NC}"
fi

sudo systemctl start $SEVICE_NAME
sleep 2
if systemctl is-active --quiet $SEVICE_NAME; then
    echo -e "${GREEN}✓ Service started successfully${NC}\n"
else
    echo -e "${RED}✗ Service did not start${NC}\n"
    exit 1
fi

#test 6: Auto-restart on failure
echo -e "${YELLOW}[TEST 6]${NC}Testing auto-restart on failure..."
PID=$(systemctl show -p MainPID $SEVICE_NAME | cut -d= -f2)
echo "Current PID: $PID"
echo "Killing process with SIGKILL..."
sudo kill -9 $PID
sleep 6 # wait for restartsec + buffer

if systemctl is-active --quiet $SEVICE_NAME; then
    NEW_PID=$(systemctl show -p MainPID $SEVICE_NAME | cut -d= -f2)
    echo "New PID: $NEW_PID"
    if [ "$PID" != "$NEW_PID" ]; then
        echo -e "${GREEN}✓ Auto-restart successful${NC}\n"
    else
        echo -e "${RED}✗ Auto-restart failed${NC}\n"
        exit 1
    fi
else
    echo -e "${RED}✗ Auto-restart failed${NC}\n"
    exit 1
fi

#test 7: check boot enable status
echo -e "${YELLOW}[TEST 7]${NC}Checking boot enable status..."
if systemctl is-enabled --quiet $SEVICE_NAME; then
    echo -e "${GREEN}✓ Boot enable status is enabled${NC}\n"
else
    echo -e "${RED}✗ Boot enable status is not enabled${NC}\n"
    exit 1
fi

#test 8: view recent logs
echo -e "${YELLOW}[TEST 8]${NC} Recent logs(last 10 lines):"
journalctl -u $SEVICE_NAME -n 10 --no-pager

echo -e "\n${BLUE}╔═══════════════════════════════════════╗${NC}"
echo -e "${BLUE}║     All Tests Passed! ✓ ✓ ✓          ║${NC}"
echo -e "${BLUE}╚═══════════════════════════════════════╝${NC}"