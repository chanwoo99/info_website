import weathermodule
import weathernow
import coronadata
import air_condition


import threading
import datetime


def update_fuc1():
    weathermodule.run()
    weathernow.run()
    coronadata.run()
    print("run properly")
    threading.Timer(120,update_fuc1).start()

def update_fuc2():
    air_condition.run()
    print("run properly")
    threading.Timer(300,update_fuc2).start()

update_fuc1()
update_fuc2()
