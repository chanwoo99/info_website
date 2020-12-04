import weathermodule
import weathernow
import coronadata
import air_condition


import threading
import datetime
import traceback
import logging


def update_fuc(module,interval):
    try:
        module.run()
        print("run properly")
        threading.Timer(interval,module).start()
    except:
        print("run error")
        threading.Timer(interval,module).start()


update_fuc(weathermodule,120)
update_fuc(weathernow,120)
update_fuc(coronadata,120)
update_fuc(air_condition,350)
