
import air_condition

import threading
import datetime
import traceback
import logging
def update():
    try:
        air_condition.run()
        threading.Timer(300,update).start()
    except Exception as e:
        logging.error(traceback.format_exc())
        threading.Timer(300,update).start()
update()
