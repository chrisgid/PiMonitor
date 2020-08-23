from datetime import datetime
from json import loads
from subprocess import Popen, PIPE
from sys import platform


def run_speedtest():

    if platform == 'linux' or platform == 'linux2':
        print("On linux")
        ## run linux speedtest
    elif platform == "win32":
        print("On windows")
        ## run windows speedtest
    else:
        print("Unsupported platform")


    process = Popen(['speedtest.exe', "--format=json"], stdout=PIPE)
    (output, err) = process.communicate()
    exit_code = process.wait()

    if exit_code == 0:
        print("Success!")
        ## return a Speedtest
    else:
        print("Error")
        ## return a zero-value Speedtest


class Speedtest:
    def __init__(self, json: str):
        self.raw = json
        self.speedtest = loads(self.raw)


    @property
    def timestamp(self) -> datetime:
        return datetime.strptime(self.speedtest["timestamp"], "%Y-%m-%dT%H:%M:%SZ")


    @property
    def download(self) -> int:
        """Download speed of the speedtest in bytes per second"""
        if not self.is_result:
            return 0

        return self.speedtest["download"]["bandwidth"]


    @property
    def upload(self) -> int:
        """Upload speed of the speedtest in bytes per second"""
        if not self.is_result:
            return 0
        
        return self.speedtest["upload"]["bandwidth"]


    @property
    def latency(self) -> float:
        """Latency of the speedtest in milliseconds"""
        if not self.is_result:
            return 0
        
        return self.speedtest["ping"]["latency"]


    @property
    def packet_loss(self) -> int:
        """Number of packets lost in the speedtest"""
        if not self.is_result:
            return 0
        
        return self.speedtest["packetLoss"]
    

    @property
    def is_result(self) -> bool:
        """True if the speedtest is a result, false if it's an error"""
        return self.speedtest.get("type") == "result"
