# PiMonitor

## Start PiMonitor (development web server)

`python3 app.py`

## Remote connection to Raspberry Pi

Ensure the Pi has SSH enabled:

`sudo systemctl enable ssh`

`sudo systemctl start ssh`

**Transferring files:**

`scp file.txt pi@raspberrypi:~`

**Connect to terminal (SSH):**

`ssh pi@raspberrypi`

(Substitute `raspberrypi` for the Pi's IP address)