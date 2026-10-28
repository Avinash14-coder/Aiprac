
from itertools import product

study_hours = {"Low": 0.4, "High": 0.6}
attendance = {"Low": 0.3, "High": 0.7}

performance = {
    ("Low", "Low"): {"Poor": 0.9, "Good": 0.1},
    ("Low", "High"): {"Poor": 0.6, "Good": 0.4},
    ("High", "Low"): {"Poor": 0.5, "Good": 0.5},
    ("High", "High"): {"Poor": 0.1, "Good": 0.9}
}

print("Bayesian Network: Student Exam Performance")
print("Study Hours -> Performance")
print("Attendance -> Performance")

print("\nProbability of Performance:")

for result in ["Poor", "Good"]:
    probability = 0

    for study, attend in product(study_hours, attendance):
        probability += (
            study_hours[study]
            * attendance[attend]
            * performance[(study, attend)][result]
        )

    print(result, "=", round(probability, 2))

print("\nFor a student with high study hours and high attendance:")
print("Poor =", performance[("High", "High")]["Poor"])
print("Good =", performance[("High", "High")]["Good"])
