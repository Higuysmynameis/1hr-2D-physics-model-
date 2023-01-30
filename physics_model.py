import math
import matplotlib.pyplot as plt
import time
import csv


print("Physics Model 1.0.0")


with open("example.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        t = len(row)


class proj_velocity:
    def velocity(self):
        print(f"Velocity of projectile is {self.rv}")


Falcon_9 = proj_velocity()
Falcon_9.rv = 7.4
Falcon_9_heavy = proj_velocity()
Falcon_9_heavy.rv = 6.7


class proj_environment:
    def environment(self):
        print(f"Current environment has a gravitational field of {self.gf}")


earth = proj_environment()
earth.gf = 9.81
mars = proj_environment()
mars.gf = 3.72
moon = proj_environment()
moon.gf = 1.62


def proj_motion():
    q = input("What is the current environment: ")
    q.lower()
    if q == 'mars':
        mars.environment()
        g = mars.gf
    elif q == 'moon':
        moon.environment()
        g = moon.gf
    elif q == 'earth':
        earth.environment()
        g = earth.gf
    else:
        print("invalid")

    q1 = input("Select projectile type: ")
    q1.lower()
    if q1 == 'falcon 9':
        Falcon_9.velocity()
        v0 = Falcon_9.rv
    elif q1 == 'falcon 9 heavy':
        Falcon_9_heavy.velocity()
        v0 = Falcon_9_heavy.rv
    else:
        print("invalid")

    angle = int(input("angle: "))
    h0 = float(input("height: "))
    t = (2 * v0 * math.sin(angle)) / g
    x = v0 * math.cos(angle) * t

    y = h0 + (v0 * math.sin(angle) * t) - (0.5 * g * t ** 2)

    print("Time of flight: ", t)
    print("Maximum horizontal distance: ", x)
    print("Maximum vertical distance: ", y)
    print("====Graphing===>")

    x_vals = [v0 * math.cos(math.radians(angle)) * t
              for t in range(int(t * 10))]
    y_vals = [h0 + (v0 * math.sin(math.radians(angle)) * t) - (0.5 * g * t ** 2)
              for t in range(int(t * 10))]
    f, ax = plt.subplots()
    ax.plot(x_vals, y_vals)
    ax.set(xlabel='horizontal distance (m)', ylabel='vertical distance (m)',
           title=f'{q1.upper()} projectile motion')
    print(g)
    time.sleep(4)
    plt.show()


proj_motion()
