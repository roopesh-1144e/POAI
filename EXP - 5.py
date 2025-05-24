def minimum(x, y):
    if x <= y:
        return x
    else:
        return y

def maximum(x, y):
    if x >= y:
        return x
    else:
        return y

class KnowledgeBase:
    def __init__(self):
        self.facts = set()

    def add_fact(self, subject, obj):
        self.facts.add((subject, obj))

    def infer(self):
        new_facts_derived = True
        while new_facts_derived:
            new_facts_derived = False
            current_facts_count = len(self.facts)
            derived_in_this_iteration = set()

            for s, o in list(self.facts):
                if s == "mary":
                    if ("john", o) not in self.facts and ("john", o) not in derived_in_this_iteration:
                        derived_in_this_iteration.add(("john", o))

            for s, o in list(self.facts):
                if o == "wine":
                    if ("john", s) not in self.facts and ("john", s) not in derived_in_this_iteration:
                        derived_in_this_iteration.add(("john", s))

            for s, o in list(self.facts):
                if s == o:
                    if ("john", s) not in self.facts and ("john", s) not in derived_in_this_iteration:
                        derived_in_this_iteration.add(("john", s))
            
            if derived_in_this_iteration:
                self.facts.update(derived_in_this_iteration)

            if len(self.facts) > current_facts_count:
                new_facts_derived = True

    def query_specific(self, subject, obj):
        return (subject, obj) in self.facts

    def query_general(self, subject):
        results = set()
        for s, o in self.facts:
            if s == subject:
                results.add(o)
        return sorted(list(results))

print("--- Minimum and Maximum Examples ---")
min_val = minimum(5, 10)
print(f"minimum(5, 10, Min). -> Min = {min_val}")

max_val = maximum(5, 10)
print(f"maximum(5, 10, Max). -> Max = {max_val}")

min_val_2 = minimum(8, 3)
max_val_2 = maximum(8, 3)
print(f"minimum(8, 3, Min), maximum(8, 3, Max). -> Min = {min_val_2}, Max = {max_val_2}")
print("-" * 30)

kb = KnowledgeBase()

kb.add_fact("mary", "food")
kb.add_fact("mary", "wine")
kb.add_fact("john", "wine")
kb.add_fact("john", "mary")

kb.infer()

print("\n--- Knowledge Representation Examples ---")

result_john_food_bool = kb.query_specific("john", "food")
output_john_food_str = "yes" if result_john_food_bool else "no"
print(f"Query: ?- likes(john, food).\nOutput: {output_john_food_str}")

result_john_wine_bool = kb.query_specific("john", "wine")
output_john_wine_str = "yes" if result_john_wine_bool else "no"
print(f"\nQuery: ?- likes(john, wine).\nOutput: {output_john_wine_str}")

print(f"\nQuery: ?- likes(john, food). (implicitly testing 'if Mary likes food')\nOutput: {output_john_food_str}")

john_likes_who = kb.query_general("john")
print(f"\nQuery: ?- likes(john, Y).\nOutput: Y = " + " ; ".join(john_likes_who) if john_likes_who else "false.")
print("-" * 30)
