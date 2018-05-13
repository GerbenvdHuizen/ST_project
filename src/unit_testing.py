import unittest

from state_tracking.state_tracker import StateTracker
from state_tracking.branch_stack import BranchStack
from state_tracking.branch import Branch 
from state_tracking.interaction_state import InteractionState

class TestStateTracker(unittest.TestCase):
 
    def setUp(self):
        self.testTracker = StateTracker()
        self.branchStack = BranchStack()

        self.frame1 = {"a" : 1, "b" : 2, "c" : 3}
        self.frame2 = {"d" : 4, "b" : 3, "e" : 5}

        self.IS1 = InteractionState(self.frame1)
        self.IS2 = InteractionState(self.frame2)

        self.B1 = Branch("N.E.D.", self.IS1)
        self.B2 = Branch("U.W.S.", self.IS2)
 
    def test_add_new_branch(self):
        self.testTracker.add_new_branch("test1")
        self.assertEqual((self.testTracker.branch_stack.size()), 1)

 
    def test_merge_dicts(self):
        print("test")
    
    def test_merge_current_branch_with_parent(self):
        print("test")
    
    def test_commit_to_branch(self):
        print("test")
 
if __name__ == '__main__':
    unittest.main()