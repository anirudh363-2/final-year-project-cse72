import random

# Define constants
NUM_EXAMS = 10  # Number of exams to schedule
NUM_SLOTS = 5  # Number of time slots per day
NUM_DAYS = 5  # Number of days for exams
MAX_HOURS_PER_DAY = 3  # Maximum exam hours per day

# Example data
students = {0: [1, 2], 1: [2, 3], 2: [1, 3]}  # student_id: [exam_ids]
faculty = {0: [1, 2], 1: [2, 3], 2: [1, 3]}  # faculty_id: [exam_ids]
exams = list(range(NUM_EXAMS))

# Representation of a timetable (Chromosome)
def generate_timetable():
    return [random.randint(0, NUM_SLOTS * NUM_DAYS - 1) for _ in range(NUM_EXAMS)]

# Fitness function
def fitness(timetable):
    score = 0

    # Constraint 1: Avoid clashes for students
    for student, student_exams in students.items():
        student_slots = [timetable[exam] for exam in student_exams]
        if len(student_slots) == len(set(student_slots)):
            score += len(student_slots)

    # Constraint 2: Faculty availability
    for fac, faculty_exams in faculty.items():
        faculty_slots = [timetable[exam] for exam in faculty_exams]
        if len(faculty_slots) == len(set(faculty_slots)):
            score += len(faculty_slots)

    # Constraint 3: Max hours per day
    hours_per_day = [0] * NUM_DAYS
    for slot in timetable:
        day = slot // NUM_SLOTS
        hours_per_day[day] += 1
    if all(hours <= MAX_HOURS_PER_DAY for hours in hours_per_day):
        score += 10  # Reward for adhering to this constraint

    return score

# Genetic Algorithm operations
def selection(population):
    return random.choices(population, weights=[fitness(p) for p in population], k=2)

def crossover(parent1, parent2):
    point = random.randint(0, len(parent1) - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

def mutate(timetable, mutation_rate=0.1):
    for i in range(len(timetable)):
        if random.random() < mutation_rate:
            timetable[i] = random.randint(0, NUM_SLOTS * NUM_DAYS - 1)

# Main Genetic Algorithm
def genetic_algorithm(generations=100, population_size=50):
    # Initial population
    population = [generate_timetable() for _ in range(population_size)]

    for generation in range(generations):
        # Evaluate fitness
        population = sorted(population, key=fitness, reverse=True)
        if fitness(population[0]) >= 50:  # Adjust this threshold as needed
            break

        # Selection and reproduction
        new_population = population[:2]  # Elitism: Carry forward the best 2
        while len(new_population) < population_size:
            parent1, parent2 = selection(population)
            child1, child2 = crossover(parent1, parent2)
            mutate(child1)
            mutate(child2)
            new_population.extend([child1, child2])

        population = new_population

        print(f"Generation {generation}: Best Fitness = {fitness(population[0])}")

    return population[0]

# Run the Genetic Algorithm
best_timetable = genetic_algorithm()
print("Best Timetable:", best_timetable)