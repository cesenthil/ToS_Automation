from datetime import datetime

def Four_PM_Check():

    Time_Now  = datetime.now()
    Time_04PM = datetime.now().replace(hour=16,minute=0,second=0,microsecond=0)

    while Time_Now < Time_04PM:
        Time_Now = datetime.now()