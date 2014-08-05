from time import sleep
from easy_scheduler.simple_scheduler import SimpleThreadScheduler

seconds = 1  # We want to do something on every 10 seconds


def do_it():
    print 'Printed from a process based scheduler'


scheduler = SimpleThreadScheduler(seconds, do_it, deamon=False)
scheduler.run()

sleep(10)
scheduler.stop()
sleep(10)
scheduler.resume()
sleep(10)
