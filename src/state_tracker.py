import abc

from branching.branch_stack import BranchStack
from branching.branch import Branch
from tracking.interaction_state import InteractionState

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

    def get_current_branch(self):
        return self.branch_stack.peek_top()
    
    def get_last_parent_branch(self):
        return self.branch_stack.peek_second()
    
    def remove_current_branch(self):
        self.branch_stack.pop()
    
    def replace_current_branch(self, branch):
        self.branch_stack.replace(branch)

    def get_lastest_state(self):
        current_branch = self.get_current_branch()
        return current_branch.latest_state
    
    def get_parent_latest_state(self):
        parent_branch = self.get_last_parent_branch()
        return parent_branch.latest_state

    def get_current_history(self):
        current_branch = self.get_current_branch()
        return current_branch.history

    def add_new_branch(self, new_context):
        last_frame = {}
        if (not self.branch_stack.isEmpty):
            latest_state = self.get_lastest_state()
            last_frame = latest_state.frame

        new_latest_state = InteractionState(last_frame)
        new_branch = Branch(new_context, new_latest_state)
        
        self.branch_stack.push(new_branch)
    
    def merge_dicts(self, frame1, frame2, keyList, keep = "old"):  
        if (keep == "new"):
            filtered_frame = {key: frame1[key] for key in frame1.keys() if key not in keyList}
            merged_frame = {**filtered_frame, **frame2}
        else:
            filtered_frame = {key: frame2[key] for key in frame2.keys() if key not in keyList}
            merged_frame = {**frame1, **filtered_frame}
        
        return merged_frame

    def merge_current_branch_with_parent(self, keyList = []):
        latest_state = self.get_lastest_state()
        parent_latest_state = self.get_parent_latest_state()

        merged_frame = self.merge_dicts(parent_latest_state.frame, latest_state.frame, keyList)

        parent_branch_copy = self.get_last_parent_branch()
        merged_state = InteractionState(merged_frame)
        parent_branch_copy.update_to_next_state(merged_state)

        self.remove_current_branch()
        self.replace_current_branch(parent_branch_copy)
    
    def commit_to_branch(self, keys, keyList = []):
        latest_frame = self.get_lastest_state().frame
        new_frame = self.merge_dicts(latest_frame, keys, keyList)

        new_interaction_state = InteractionState(new_frame)

        current_branch_copy = self.get_current_branch()
        current_branch_copy.update_to_next_state(new_interaction_state)

        self.replace_current_branch(current_branch_copy)

    def reset_branch_stack(self):
        self.branch_stack.empty_stack


