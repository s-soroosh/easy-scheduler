__author__ = 'SOROOSH'

from abc import ABCMeta, abstractmethod
import logging
import multiprocessing
from time import sleep
import uuid
import threading


class Scheduler:
    __metaclass__ = ABCMeta

    def __init__(self, seconds, code):
        self.seconds = seconds
        self.code = code

    def _decorate_task(self):
        def result():
            while (True):
                try:
                    self.code()
                except Exception as e:
                    print 'Exception: %s occured. Scheduler continues its job.' % e.message
                    sleep(self.seconds)


        return result

    @abstractmethod
    def run(self):
        pass


class ThreadSimpleScheduler(Scheduler):
    def run(self):
        print 'scheduler started'
        thread = threading.Thread(name='SCHEDULER-' + str(uuid.uuid4()), target=self._decorate_task())
        thread.daemon = True
        thread.start()
        return thread


class ProcessSimpleScheduler(Scheduler):
    def run(self):
        process = multiprocessing.Process(name='SCHEDULER-' + str(uuid.uuid4()), target=self._decorate_task())
        process.daemon = True
        process.start()
        return process


# if __name__ == "__main__":
# logging.basicConfig(level=logging.INFO,
#                         format="[%(threadName)-15s] %(message)s")
#
#     def say_hi():
#         logging.info('hi')
#
#     logging.info("Running...")
#     # ts = ThreadSimpleScheduler(2, say_hi)
#     # ts.run()
#     # print threading.active_count()
#     # sleep(10)
#     # print threading.active_count()
#
#     ps = ProcessSimpleScheduler(2, say_hi)
#     ps.run()
#     children = multiprocessing.active_children()
#     print multiprocessing.cpu_count()
#     # multiprocessing.
#     print len(children)





