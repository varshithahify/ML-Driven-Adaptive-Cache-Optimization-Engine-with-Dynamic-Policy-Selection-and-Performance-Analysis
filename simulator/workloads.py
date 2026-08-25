#phase 4
import random
# Sequential pattern
def sequential_workload(size):
    return list(range(size))
# Repetitive pattern
def repetitive_workload(size):
    base = [1, 2, 3]
    return [random.choice(base) for _ in range(size)]
# Random pattern
def random_workload(size):
    return [random.randint(1, 20) for _ in range(size)]
# Mixed pattern
def mixed_workload(size):
    data = []

    for _ in range(size):

        choice = random.choice(["seq", "rep", "rand"])

        if choice == "seq":
            data.append(random.randint(1, 50))

        elif choice == "rep":
            data.append(random.choice([1, 2, 3]))

        else:
            data.append(random.randint(1, 20))

    return data