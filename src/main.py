from state_tracker import StateTracker
from branching.branch_stack import BranchStack
from branching.branch import Branch 
from tracking.interaction_state import InteractionState

testTracker = StateTracker()
branchStack = BranchStack()

x = {"a" : 1, "b" : 2, "c" : 3}
y = {"d" : 4, "b" : 3, "e" : 5}

IS1 = InteractionState(x)
IS2 = InteractionState(y)

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