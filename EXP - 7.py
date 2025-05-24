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

if __name__ == "__main__":
    goal_f = 'f'
    if backward_chaining(goal_f, facts, rules):
        print(f"The goal '{goal_f}' can be achieved.")
    else:
        print(f"The goal '{goal_f}' cannot be achieved.")

    goal_d = 'd'
    if backward_chaining(goal_d, facts, rules):
        print(f"The goal '{goal_d}' can be achieved.")
    else:
        print(f"The goal '{goal_d}' cannot be achieved.")
