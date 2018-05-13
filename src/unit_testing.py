import unittest

from state_tracker import StateTracker
from state_tracking.branch_stack import BranchStack
from state_tracking.branch import Branch 
from state_tracking.interaction_state import InteractionState

class TestStateTracker(unittest.TestCase):
 
    def setUp(self):
        self.testTracker = StateTracker()
        self.branchStack = BranchStack()

        self.frame1 = {"a" : 1, "b" : 2, "c" : 3}
        self.frame2 = {"d" : 4, "b" : 3}

        self.IS1 = InteractionState(self.frame1)
        self.IS2 = InteractionState(self.frame2)

        self.B1 = Branch("N.E.D.", self.IS1)
        self.B2 = Branch("U.W.S.", self.IS2)
 
    def test_add_new_branch(self):
        self.testTracker.add_new_branch("context_test1")
        self.assertEqual((self.testTracker.branch_stack.size()), 1)

        self.testTracker.add_new_branch("context_test2")
        self.assertEqual((self.testTracker.branch_stack.size()), 2)

        self.testTracker.reset_branch_stack()
        self.testTracker.branch_stack.push(self.B1)
        self.testTracker.add_new_branch("context_test3")

        child_branch_frame_size = len(self.testTracker.get_lastest_state().frame)
        parent_branch_frame_size = len(self.testTracker.get_parent_latest_state().frame)

        self.assertEqual(child_branch_frame_size, parent_branch_frame_size)

        self.testTracker.reset_branch_stack()

    def test_merge_dicts(self):
        merged_frame1 = self.testTracker.merge_dicts(self.frame1, self.frame2, [])
        self.assertEqual(merged_frame1, {"a" : 1, "b" : 3, "c" : 3, 'd' : 4})

        merged_frame2 = self.testTracker.merge_dicts(self.frame1, self.frame2, ['b'])
        self.assertEqual(merged_frame2, {"a" : 1, "b" : 2, "c" : 3, 'd' : 4})

    def test_merge_current_branch_with_parent(self):
        self.testTracker.branch_stack.push(self.B1)
        self.testTracker.branch_stack.push(self.B2)

        self.testTracker.merge_current_branch_with_parent()

        self.assertEqual(self.testTracker.branch_stack.size(), 1)
        self.assertEqual(self.testTracker.get_current_branch().context, "N.E.D.")
        self.assertEqual(self.testTracker.get_lastest_state().frame, {"a" : 1, "b" : 3, "c" : 3, "d" : 4})

        self.testTracker.reset_branch_stack()

    def test_commit_to_branch(self):
        self.testTracker.branch_stack.push(self.B1)

        self.testTracker.commit_to_branch({"d" : 4, "e" : 5, "f" : 6, "g" : 7}, ["f"])

        self.assertEqual(self.testTracker.get_lastest_state().frame, {"a" : 1, "b" : 2, "c" : 3, "d" : 4, "e" : 5,
                                                                      "g" : 7 })        

        self.testTracker.reset_branch_stack()


if __name__ == '__main__':
    unittest.main()