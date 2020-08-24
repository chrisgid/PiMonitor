from datetime import datetime
from json import loads
from subprocess import Popen, PIPE
from sys import platform


def run_speedtest():
    executable_name = ''

    if platform == 'linux' or platform == 'linux2':
        ## Assume on raspberry pi
        executable_name = 'speedtest_arm32'
    elif platform == "win32":
        executable_name = 'speedtest.exe'
    else:
        print("Unsupported platform")


    process = Popen([executable_name, "--format=json"], stdout=PIPE)
    (output, err) = process.communicate()
    exit_code = process.wait()

    if exit_code == 0:
        return Speedtest(output)
        ## return a Speedtest
    else:
        print("Error")
        ## return a zero-value Speedtest


class Speedtest:
    def __init__(self, json: str):
        self.raw = json
        self.speed_dict = loads(self.raw)


    @property
    def timestamp(self) -> datetime:
        return datetime.strptime(self.speed_dict["timestamp"], "%Y-%m-%dT%H:%M:%SZ")


    @property
    def download(self) -> int:
        """Download speed of the speedtest in bytes per second"""
        if not self.is_result:
            return 0

        return self.speed_dict["download"]["bandwidth"]


    @property
    def upload(self) -> int:
        """Upload speed of the speedtest in bytes per second"""
        if not self.is_result:
            return 0
        
        return self.speed_dict["upload"]["bandwidth"]


    @property
    def latency(self) -> float:
        """Latency of the speedtest in milliseconds"""
        if not self.is_result:
            return 0
        
        return self.speed_dict["ping"]["latency"]


    @property
    def packet_loss(self) -> int:
        """Packet loss as a percentage in the speedtest"""
        if not self.is_result:
            return 0
        
        return self.speed_dict["packetLoss"]
    

    @property
    def is_result(self) -> bool:
        """True if the speedtest is a result, false if it's an error"""
        return self.speed_dict.get("type") == "result"
