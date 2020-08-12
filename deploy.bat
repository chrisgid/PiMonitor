ssh pi@raspberrypi "mkdir pimonitor"
scp -r src requirements.txt pi@raspberrypi:~/pimonitor
ssh pi@raspberrypi "cd pimonitor; pip3 install -r requirements.txt;"