import weathermodule
import weathernow
import coronadata
import air_condition

import threading
import datetime
import traceback
import logging
def update():
    try:
        weathermodule.run()
        weathernow.run()
        coronadata.run()
        threading.Timer(120,update).start()
    except Exception as e:
        logging.error(traceback.format_exc())
        threading.Timer(120,update).start()

update()
