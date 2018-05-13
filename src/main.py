from state_tracker import StateTracker
from state_tracking.branch_stack import BranchStack
from state_tracking.branch import Branch 
from state_tracking.interaction_state import InteractionState

testTracker = StateTracker()
branchStack = BranchStack()

frame1 = {"a" : 1, "b" : 2, "c" : 3}
frame2 = {"d" : 4, "b" : 3, "e" : 5}

IS1 = InteractionState(frame1)
IS2 = InteractionState(frame2)

B1 = Branch("N.E.D.", IS1)
B2 = Branch("U.W.S.", IS2)

testTracker.branch_stack.push(B1)
testTracker.branch_stack.push(B2)

testTracker.merge_current_branch_with_parent(["e"])
branchStack.push(1)
branchStack.push(2)
branchStack.push(3)

print(testTracker.get_current_branch().context)
print(testTracker.get_current_branch().latest_state.frame)
print(testTracker.get_current_branch().history[0].frame)