import TeliaChallenge

solver = TeliaChallenge.TeliaChallenge()

arrs = [
    ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"],
    ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH"],
    ["NORTH", "WEST", "SOUTH", "EAST"],
    [],
    ["NORTH"]
]

reduced_arrs = [solver.pathReduc(x) for x in arrs]

print(reduced_arrs)