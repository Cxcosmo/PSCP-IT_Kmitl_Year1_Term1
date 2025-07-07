"""a"""
planets = input()
# planets = "Mercury Venus Earth Mars Jupiter Saturn Uranus Neptune Sun"
# planets = "Sun Mercury Venus Earth Mars Jupiter Saturn Uranus Neptune"
# planets = "Mercury Venus Earth Mars Sun Jupiter Saturn Uranus Neptune"
planets = planets.split()

# find Sun
suni = planets.index("Sun")

hots = []
cools = []
if not suni:
    hots.append(planets[1])
    cools.append(planets[-1])
elif suni == len(planets) - 1:
    hots.append(planets[-2])
    cools.append(planets[0])
else:
    hots.append(planets[suni - 1])
    hots.append(planets[suni + 1])
    if abs(planets.index(hots[0]) - suni) == abs(planets.index(hots[1]) - suni) and hots[0] == planets[0] and hots[1] == planets[-1]:
        cools.append(planets[0])
        cools.append(planets[-1])
    elif abs(0 - suni) > abs((len(planets) - 1) - suni):
        cools.append(planets[0])
    elif abs(0 - suni) < abs((len(planets) - 1) - suni):
        cools.append(planets[-1])
    else :
        cools.append(planets[0])
        cools.append(planets[-1])
print("Hot:", " ".join(hots))
print("Cool:", " ".join(cools))
