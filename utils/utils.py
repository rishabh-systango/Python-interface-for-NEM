import time
import math



def get_timestamp():
    initial_timestamp = 1427587585000
    current_time = int(round(time.time() * 1000))
    timestamp = math.floor( current_time / 1000 - initial_timestamp / 1000)
    return timestamp


def get_deadline(timestamp = None):
    if timestamp is None:
        timestamp = get_timestamp()
    deadline = timestamp + 1000
    return deadline
