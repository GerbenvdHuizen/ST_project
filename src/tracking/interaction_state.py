import datetime

class InteractionState(object):
    '''The InteractionState holds a snapshot of a situation that occured during an interaction'''

    def __init__(self, frame = {}):
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

    def get_frame_slot(self, key):
        return self.frame[key]

    def set_frame_slot(self, key, value):
        self.frame[key] = value

    def del_frame_slot(self, key):
        del self.frame[key]
