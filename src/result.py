import random
from datetime import datetime
from datetime import timedelta
from storage import Database


class Result:
    UP = "up"
    DOWN = "down"
    LATENCY = "latency"

    def __init__(self, timestamp, value, result_type):
        self.timestamp = timestamp
        self.value = value
        self.type = result_type

    def as_dict(self):
        return self.__dict__


def get_results(start: datetime=None, end: datetime=None, test=False, all_results=False):
    if test:
        return get_test_results()

    db = Database.from_config()
    db.connect()

    results = []

    if all_results:
        speedtests = db.get_all_speedtests()
    else:
        speedtests = db.get_speedtests(start, end)

    for speedtest in speedtests:
        results.append(Result(speedtest.timestamp, speedtest.download, Result.DOWN).as_dict())
        results.append(Result(speedtest.timestamp, speedtest.upload, Result.UP).as_dict())
        results.append(Result(speedtest.timestamp, speedtest.latency, Result.LATENCY).as_dict())

    return results


def get_test_results():
    results = []

    startTime = datetime.now()

    for i in range(30):
        timestamp = (startTime-timedelta(hours=i)).isoformat()
        bytesPerSecond = random.randrange(3000000, 5000000)
        upDown = Result.DOWN

        result = Result(timestamp, bytesPerSecond, upDown)
        results.append(result.__dict__)

    for i in range(30):
        timestamp = (startTime-timedelta(hours=i)).isoformat()
        bytesPerSecond = random.randrange(500000, 2000000)
        upDown = Result.UP

        result = Result(timestamp, bytesPerSecond, upDown)
        results.append(result.__dict__)    

    return results