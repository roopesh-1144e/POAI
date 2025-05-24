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
def forward_chaining(facts_dict, rules, goal):
    inferred_facts = {fact for fact, value in facts_dict.items() if value is True}
    changed = True
    while changed:
        changed = False
        for rule_head, rule_body in rules:
            all_conditions_met = all(condition in inferred_facts for condition in rule_body)
            if all_conditions_met and rule_head not in inferred_facts:
                inferred_facts.add(rule_head)
                changed = True
    return goal in inferred_facts

goals_to_test = ['f', 'e', 'd']

for goal in goals_to_test:
    if forward_chaining(facts, rules, goal):
        print(f"The goal '{goal}' can be achieved.")
    else:
        print(f"The goal '{goal}' cannot be achieved.")
