import math
import random

total = 0
n_i = 0
sim_pi = 0
while not math.isclose(sim_pi, math.pi, abs_tol=1e-5):
    a = random.random()
    y = random.random()
    d = pow(a**2 + y**2, 0.5)
    total += 1
    if d <= 1:
        n_i += 1
    sim_pi = 4 * n_i / total
print(sim_pi)
print(total)
