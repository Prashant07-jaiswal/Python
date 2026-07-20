import time
from IPython.display import clear_output
import datetime
import zoneinfo

while True:
    clear_output(wait=True)
    tzinfo = zoneinfo.ZoneInfo("Asia/Kolkata")
    current = datetime.datetime.now(tzinfo).strftime("%I:%M:%S %p")
    print("   DOGITAL CLOCK")
    print(current)
    time.sleep(1)







