from easy_scheduler.simple_scheduler import ThreadSimpleScheduler

seconds = 10  # We want to do something on every 10 seconds


def do_it():
    print 'Printed from a thread based scheduler'


scheduler = ThreadSimpleScheduler(seconds, do_it, deamon=False)
scheduler.run()