import weathermodule
import weathernow
import coronadata

import threading


def update():
    weathermodule.run()
    weathernow.run()
    coronadata.run()

    threading.Timer(120,update).start()

update()
