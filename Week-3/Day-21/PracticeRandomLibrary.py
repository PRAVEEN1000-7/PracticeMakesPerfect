import random as rd

# Returns a float between 0.0 and 1.0.
print(rd.random())

# Returns a random integer between a and b (inclusive).
print(rd.randint(1,10))

# Returns a float between a and b.
print(rd.uniform(1,10))

# Picks one random element.
game = ['rock','paper','scissor']
print(rd.choice(game))

# Picks n random elements with replacement.
print(rd.choices(game,k=2))

# Picks n unique random elements (no repetition).
print(rd.sample(game,k=2))

# Shuffles a list in-place.
rd.shuffle(game)
print(game)

# Sets the seed so results are reproducible.
rd.seed(42)
print(rd.random())