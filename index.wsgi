# -*- coding: utf-8 -*-
import os
from AutoQ import AutoQ
import httplib, urllib2,json,random,time,threading
jue1='QSMY_M_9000_30=%7B%22userId%22%3A49129%2C%22plat%22%3A24%2C%22platId%22%3A%2232342370%22%2C%22name%22%3A%22%5Cu300e%5Cu5fa1%5Cu98ce%5Cu300f%5Cu73cf%22%2C%22mCode%22%3A%2202DBA835D-BECC-4F09-9781-B13D35D549C3%22%2C%22sysType%22%3A%22ios%22%2C%22eqType%22%3A%22iPhone6%2C2_Darwin_15.0.0%22%2C%22ip%22%3A%22218.29.102.110%22%2C%22sig%22%3A%22f8d521cfc25c4ae0daeb929b50b6b2c6%22%7D'
    #jue2
jue2='QSMY_M_9000_30=%7B%22userId%22%3A49149%2C%22plat%22%3A24%2C%22platId%22%3A%2232365111%22%2C%22name%22%3A%22%5Cu73cf2%22%2C%22mCode%22%3A%2202DBA835D-BECC-4F09-9781-B13D35D549C3%22%2C%22sysType%22%3A%22ios%22%2C%22eqType%22%3A%22iPhone6%2C2_Darwin_15.0.0%22%2C%22ip%22%3A%22218.29.102.114%22%2C%22sig%22%3A%22a101f57889bf0c991202a0ebd9493864%22%7D'                        



def hello():
    return "Hello, world! - Bottle"


def hunt_jue1():
    m = AutoQ()
    m.usercookie=jue1
    m.hunt()
    return "hunt_jue1_done"


def hunt_jue2():
    m = AutoQ()
    m.usercookie=jue2
    m.hunt()
    return "hunt_jue2_done"


def tower_jue1():
    m = AutoQ()
    m.usercookie=jue1
    m.tower()
    return "tower_jue1_done"



def tower_jue2():
    m = AutoQ()
    m.usercookie=jue2
    m.tower()
    return "tower_jue2_done"


def explore_jue1():
    m = AutoQ()
    m.usercookie=jue1
    try:
        m.explore()
    except Exception, e:
        return e
    return "explore_jue1_done"


def explore_jue2():
    m = AutoQ()
    m.zj=16
    m.gk=6
    m.usercookie=jue2
    try:
        m.explore()
    except Exception, e:
        return e
    return "explore_jue2_done"

if __name__=='__main__':
    threads = []
    threads.append(threading.Thread(target=hunt_jue1))
    threads.append(threading.Thread(target=hunt_jue2))
    threads.append(threading.Thread(target=tower_jue1))
    threads.append(threading.Thread(target=tower_jue2))
    threads.append(threading.Thread(target=explore_jue1))
    threads.append(threading.Thread(target=explore_jue2))
    for t in threads:
        t.setDaemon(True)
        t.start()
    print '狩魂begin'
    raw_input('preess any key to kill\n')
