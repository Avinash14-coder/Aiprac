
facts = {"rain", "cloudy"}

rules = [
    ({"rain"}, "wet_ground"),
    ({"cloudy"}, "rain"),
    ({"wet_ground"}, "slippery_road")
]

def forward_chaining(facts, rules):
    facts = set(facts)

    while True:
        new_fact_added = False

        for conditions, conclusion in rules:
            if conditions.issubset(facts) and conclusion not in facts:
                facts.add(conclusion)
                print("New fact derived:", conclusion)
                new_fact_added = True

        if not new_fact_added:
            break

    return facts

result = forward_chaining(facts, rules)

print("\nFinal Knowledge Base:")
for fact in result:
    print(fact)
