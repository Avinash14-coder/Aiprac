from itertools import product

study_hour={"high":0.6,"low":0.4}
attendence={"high":0.7,"low":0.3}

performance={
    ("low","low"):{"poor":0.9, "Good":0.1},
    ("low","high"):{"poor":0.6, "Good":0.4},
       ("high", "low"): {"poor": 0.5, "Good": 0.5},
        ("high", "high"): {"poor": 0.1, "Good": 0.9}
}

print("Bayesin Netowrk for Student Perfromance: ")
print("Study Hours : performace ")
print("attendance Hours : performace ")

for res in ["poor","Good"]:
    probability=0
    for study,attend in product(study_hour,attendence):
        probability+=( study_hour[study]*attendence[attend]*performance[(study,attend)][res])

    print("Result =", probability)

print("For students with high study hours and attendence")

print("Poor=",performance[("high", "high")]["poor"])
print("Good=",performance[("high", "high")]["Good"])