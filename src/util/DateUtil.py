import time

class DateUtil:
    def __init__(self):
        pass

    @property
    def current_time_in_millis(self):
        current_milli_time = int(round(time.time() * 1000))
        return current_milli_time

    @property
    def delayed_time(self):
        time.sleep(0.01)
        return self.current_time_in_millis