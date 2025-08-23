# Q : Dict comprehension: map numbers 1–10 to their cubes.

cube_of_numbers = { x:x**3 for x in range(1,11)}

for number in cube_of_numbers:
    print(f"{number} : {cube_of_numbers[number]}")