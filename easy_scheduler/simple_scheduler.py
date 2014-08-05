__author__ = 'SOROOSH'

from abc import ABCMeta, abstractmethod
import logging
import multiprocessing
from time import sleep
import uuid
import threading


class Scheduler:
    __metaclass__ = ABCMeta

    def __init__(self, seconds, code, *args, **kwargs):
        self.seconds = seconds
        self.code = code
        self._stopped = False
        if kwargs.has_key('deamon'):
            self.deamon = kwargs['deamon']
        else:
            self.deamon = False

    def _decorate_task(self):
        def result():
            while (not self._stopped):
                try:
                    self.code()
                except Exception as e:
                    print 'Exception: %s occured. Scheduler continues its job.' % e.message

                sleep(self.seconds)


        return result

    def stop(self):
        self._stopped = True

    def resume(self):
        self._stopped = False
        self.run()

    @abstractmethod
    def run(self):
        pass


class SimpleThreadScheduler(Scheduler):
    def run(self):
        print 'scheduler started'
        thread = threading.Thread(name='SCHEDULER-' + str(uuid.uuid4()), target=self._decorate_task())
        thread.daemon = self.deamon
        thread.start()
        return thread


class SimpleProcessScheduler(Scheduler):
    def run(self):
        process = multiprocessing.Process(name='SCHEDULER-' + str(uuid.uuid4()), target=self._decorate_task())
        process.daemon = self.deamon
        process.start()
        return process






