from datetime import datetime
from json import loads


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
