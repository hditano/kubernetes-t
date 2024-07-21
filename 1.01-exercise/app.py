import time
import uuid
from datetime import datetime


class LogOutput:
    def __init__(self):
        self.random_string = str(uuid.uuid4())

    def log(self):
        while True:
            timestamp = datetime.utcnow().isoformat() + "Z"
            print(f"{timestamp}: {self.random_string}")
            time.sleep(5)


if __name__ == "__main__":
    log_output = LogOutput()
    log_output.log()
