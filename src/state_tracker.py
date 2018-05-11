import abc

from branching.branch_stack import BranchStack

class StateTracker(object):
    '''Keeps track of all the context branches'''

    def __init__(self):
        self._current_context = "No context"
        self._branch_stack = BranchStack() 

    @property
    def current_context(self):
        return self._current_context

    @property
    def branch_stack(self):
        return self._branch_stack

    @current_context.setter
    def current_context(self, value):
        self._current_context = value

    @branch_stack.setter
    def branch_stack(self, value):
        self._branch_stack = value
