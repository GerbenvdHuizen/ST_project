import datetime

class Branch(object):
    '''A branch that keeps track of all the state history within a certain context'''

    def __init__(self, context, state):
        self._context = context
        self._history = []
        self._latest_state = state
        self._timestamp = datetime.datetime.now()

    @property
    def context(self):
        return self._context

    @property
    def history(self):
        return self._history

    @property
    def latest_state(self):
        return self._latest_state
    
    @property
    def timestamp(self):
        return self._timestamp

    @latest_state.setter
    def latest_state(self, value):
        self._latest_state = value

    def add_to_history (self, value):
        self._history.append(value)
    
    def update_to_next_state(self, state):
        self.add_to_history(self._latest_state)
        self.latest_state = state

