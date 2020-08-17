import random
from datetime import datetime
from datetime import timedelta

class Result:
    UP = "up"
    DOWN = "down"

    def __init__(self, timestamp, bytesPerSecond, upDown):
        self.timestamp = timestamp
        self.bytesPerSecond = bytesPerSecond
        self.type = upDown

def get_results(test=False):
    if (test):
        return get_test_results()
    else:
        raise Exception("Actual results not yet impemented")

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