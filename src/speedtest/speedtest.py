from datetime import datetime
from json import loads
from subprocess import Popen, PIPE



def run_speedtest():
    process = Popen(['speedtest', "--format=json"], stdout=PIPE)
    (output, err) = process.communicate()
    exit_code = process.wait()

    if exit_code == 0:
        return Speedtest.from_json(output)
    else:
        return Speedtest(datetime.now)



class Speedtest(object):
    def __init__(self, timestamp: datetime, download: int=0, upload: int=0, latency: float=0, packet_loss: float=0):
        self.timestamp = timestamp
        self.download = download
        self.upload = upload
        self.latency = latency
        self.packet_loss = packet_loss


    @classmethod
    def from_json(cls, json: str):
        speed_dict = loads(json)
        timestamp = datetime.strptime(speed_dict["timestamp"], "%Y-%m-%dT%H:%M:%SZ")
        if speed_dict.get("type") != "result":
            return cls(timestamp)
        
        download = speed_dict["download"]["bandwidth"]
        upload = speed_dict["upload"]["bandwidth"]
        latency = speed_dict["ping"]["latency"]
        packet_loss = speed_dict["packetLoss"]
        return cls(timestamp, download, upload, latency, packet_loss)


    def as_tuple(self) -> tuple:
        return (
            self.timestamp, 
            self.download, 
            self.upload,
            self.latency
        )