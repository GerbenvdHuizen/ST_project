
class Frame(object):
    '''Holds all information relevant to the InteractionState'''

    def __init__(self, slots = {}):
        self._frame_slots = slots

    @property
    def frame_slots(self):
        return self._frame_slots

    @frame_slots.setter
    def frame_slots(self, value):
        self._frame_slots = value

