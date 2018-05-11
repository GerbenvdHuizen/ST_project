import datetime

from frame import Frame

class InteractionState(object):
    '''The InteractionState holds a snapshot of a situation that occured during an interaction'''

    def __init__(self, frame = Frame()):
        self._frame = frame
        self._timestamp = datetime.datetime.now()

    @property
    def frame(self):
        return self._frame

    @property
    def timestamp(self):
        return self._timestamp

    @frame.setter
    def frame(self, value):
        self._frame = value

