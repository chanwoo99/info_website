import weathermodule
import weathernow
import coronadata

import threading
import datetime

def update():
    weathermodule.run()
    weathernow.run()
    coronadata.run()

    threading.Timer(120,update).start()

while(True):
    try:
        update()
    except:
        err=str(datetime.datetime.now())
        print(err+"에 오류 발생")
