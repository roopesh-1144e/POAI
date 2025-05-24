facts = {
    'a': True,
    'b': True,
    'c': False
}
rules = [
    ('d', ['a', 'b']),
    ('e', ['b', 'c']),
    ('f', ['d', 'e'])
]
def backward_chaining(goal, facts, rules):
    if goal in facts:
        return facts[goal]
    for rule in rules:
        head, body = rule
        if head == goal:
            if all(backward_chaining(fact, facts, rules) for fact in body):
                return True
    return False

# Test for goal 'f'
goal_f = 'f'
print(f"Expected Output for the Goal '{goal_f}':")
if backward_chaining(goal_f, facts, rules):
    print(f"The goal '{goal_f}' can be achieved.")
else:
    print(f"The goal '{goal_f}' cannot be achieved.")

print() # Add a newline for separation

# Test for goal 'd'
goal_d = 'd'
print(f"Expected Output for the Goal '{goal_d}':")
if backward_chaining(goal_d, facts, rules):
    print(f"The goal '{goal_d}' can be achieved.")
else:
    print(f"The goal '{goal_d}' cannot be achieved.")
