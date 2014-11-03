from baddie import *


class Queue(object):
    def __init__(self, queue=None):
        if queue is None:
            self.queue = []
        else:
            self.queue = list(queue)

    def dequeue_if_ready(self):
    	
    	running = [item for item in self.queue if item[0] == 0]

    	self.queue = [(item[0]-1, item[1]) for item in self.queue if item[0] != 0 ]

    	for thing in running:
    		thing[1].event(self)

    def enqueue(self, time, object):
        self.queue.append((time,object))


