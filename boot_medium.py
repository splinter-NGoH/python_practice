def numRescueBoats(people, limit: int):
    people.sort()
    heavy_pointer = len(people) - 1
    light_pointer = 0
    boats = 0
    while heavy_pointer >= light_pointer:
        if people[heavy_pointer] + people[light_pointer] <= limit:
            boats += 1
            heavy_pointer -= 1
            light_pointer += 1
        else:
            boats += 1
            heavy_pointer -= 1
    return boats


people = [3, 2, 2, 1]

limit = 3

print(numRescueBoats(people, limit))
