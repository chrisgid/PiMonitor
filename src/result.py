import random

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

    for i in range(10):
        timestamp = '2020-08-14T0' + str(i) + ':00:00Z'
        bytesPerSecond = random.randrange(3000000, 5000000)
        upDown = Result.DOWN

        result = Result(timestamp, bytesPerSecond, upDown)
        results.append(result.__dict__)

    for i in range(10):
        timestamp = '2020-08-14T0' + str(i) + ':00:00Z'
        bytesPerSecond = random.randrange(500000, 2000000)
        upDown = Result.UP

        result = Result(timestamp, bytesPerSecond, upDown)
        results.append(result.__dict__)    

    return results