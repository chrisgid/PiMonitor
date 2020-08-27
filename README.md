# PiMonitor

A simple network speed monitor designed to run on a Raspberry Pi

## Setup

### Raspberry PI

1. Install speedtest and dependencies:

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

### Windows

1. Download Ookla Speedtest CLI: https://www.speedtest.net/apps/cli

2. Ensure `speedtest` is available on PATH:

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
