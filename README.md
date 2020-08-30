# PiMonitor

A simple network speed monitor designed to be run on a Raspberry Pi

## Setup

### Raspberry PI

1. Install Ookla Speedtest CLI and it's dependencies: (as shown here https://www.speedtest.net/apps/cli)

```
sudo apt-get install gnupg1 apt-transport-https dirmngr
export INSTALL_KEY=379CE192D401AB61
export DEB_DISTRO=$(lsb_release -sc)
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys $INSTALL_KEY
echo "deb https://ookla.bintray.com/debian ${DEB_DISTRO} main" | sudo tee  /etc/apt/sources.list.d/speedtest.list
sudo apt-get update
sudo apt-get install speedtest
```

2. Install requirements:

    `$ pip3 install -r requirements.txt`

3. Run (development web server):

    `$ python3 app.py`

    **Note:** Using `python3 app.py` to start a server is perfectly fine for development, but if you'd like PiMonitor to be up and running constantly on your Raspberry Pi, a production server should be set up. You can do this using NGINX and uWSGI with the help of [this guide](https://www.raspberrypi-spy.co.uk/2018/12/running-flask-under-nginx-raspberry-pi/).

4. Set up a cron job to run a speedtest and store the results every 30 minutes:

    `$ crontab -e`

    Then add `*/30 * * * * cd /home/pi/pimonitor/src && python3 runner.py` to the end of the file.

### Windows

1. Download Ookla Speedtest CLI: https://www.speedtest.net/apps/cli

2. Ensure `speedtest` is available on PATH:

    (if it's not, use `set PATH=%PATH%;C:\your\path\here\` where `C:\your\path\here\` is the path to the directory containing `speedtest.exe`)

```
C:\>speedtest

   Speedtest by Ookla

     Server: TNP Ltd. - Manchester (id = 3504)
        ISP: TalkTalk
    Latency:     8.07 ms   (8.25 ms jitter)
   Download:    32.46 Mbps (data used: 18.4 MB)
     Upload:     8.63 Mbps (data used: 8.0 MB)
Packet Loss:     0.0%
```

3. Install requirements:

    `>pip3 install -r requirements.txt`

4. Run (development web server):

    `>cd PiMonitor/src`

    `>python3 app.py`
