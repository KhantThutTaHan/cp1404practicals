import random

def simulate_gophers(years=10, starting_population=1000):
    print("Welcome to the Gopher Population Simulator!")
    population = starting_population
    print(f"Starting population: {population}")

    for year in range(1, years + 1):
        print(f"\nYear {year}")

        birth_rate = random.uniform(0.10, 0.20)
        death_rate = random.uniform(0.05, 0.25)

        births = int(population * birth_rate)
        deaths = int(population * death_rate)

        population += births - deaths

        # Prevent negative population
        population = max(population, 0)

        print(f"{births} gophers were born. {deaths} died.")
        print(f"Population: {population}")

simulate_gophers()
