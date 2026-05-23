def display_state(state):
    for row in state:
        print(row)
    print()
def compare_states(initial, goal):
    if initial == goal:
        print("The two states are the same.")
    else:
        print("The two states are different.")
initial_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 0, 8]
]
print("Initial State:")
display_state(initial_state)
print("Goal State:")
display_state(goal_state)
compare_states(initial_state, goal_state)