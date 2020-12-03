import weathermodule
import weathernow
import coronadata
import air_condition

import threading
import datetime
import traceback
import logging
def update():
    weathermodule.run()
    weathernow.run()
    coronadata.run()


    threading.Timer(120,update).start()


while(True):
    try:
        update()
    except Exception as e:
        logging.error(traceback.format_exc()) #로깅
