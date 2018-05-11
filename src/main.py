from state_tracker import StateTracker
from branching.branch_stack import BranchStack

testTracker = StateTracker()
branchStack = BranchStack()

testTracker.current_context = "heyhey"
branchStack.push(1)
branchStack.push(2)
branchStack.push(3)

print(testTracker.current_context)
print(branchStack.peek())