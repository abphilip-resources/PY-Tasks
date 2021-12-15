import sched
import time
import winsound as ws

def alarm(t, a, m):
    s = sched.scheduler(time.time, time.sleep)
    s.enterabs(t, 1, print, argument=(m,))
    s.enterabs(t, 1, ws.PlaySound, argument=(a, ws.SND_FILENAME))
    print('Alarm set for', time.asctime(time.localtime(t)))
    s.run() 

alarm(time.time()+5, 'data/alarm.wav', 'Wake up!')