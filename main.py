
from skyfield.api import load, EarthSatellite
from datetime import datetime, timedelta, timezone
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import requests

def fetch_iss_tle():
    url = "https://celestrak.org/NORAD/elements/stations.txt"
    response = requests.get(url)
    lines = response.text.splitlines()

    for i in range(len(lines)):
        if "ISS (ZARYA)" in lines[i]:
            return lines[i+1], lines[i+2]

    raise ValueError("ISS TLE not found")

plt.style.use("dark_background")

def draw_earth(ax, radius=6371):
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)

    x = radius * np.outer(np.cos(u), np.sin(v))
    y = radius * np.outer(np.sin(u), np.sin(v))
    z = radius * np.outer(np.ones(np.size(u)), np.cos(v))

    ax.plot_surface(x, y, z, color="blue", alpha=0.3)
line1, line2 = fetch_iss_tle()


satellite = EarthSatellite(line1, line2, "ISS")

ts = load.timescale()
start_time = datetime.now(timezone.utc)

times = [
    ts.utc(start_time + timedelta(minutes=i))
    for i in range(0, 90, 2)
]

positions = [satellite.at(t).position.km for t in times]

x = [p[0] for p in positions]
y = [p[1] for p in positions]
z = [p[2] for p in positions]

fig = plt.figure(figsize=(9, 9))
ax = fig.add_subplot(111, projection="3d")

draw_earth(ax)


ax.plot(x, y, z, color="cyan", linewidth=5, alpha=0.2)
ax.plot(x, y, z, color="cyan", linewidth=2, label="ISS Orbit")

sat_point, = ax.plot([], [], [], 'ro', markersize=6, label="ISS")

print("Using FIXED update() function")

def update(frame):
    sat_point.set_data([x[frame]], [y[frame]])
    sat_point.set_3d_properties([z[frame]])
    return sat_point,

ani = FuncAnimation(
    fig,
    update,
    frames=len(x),
    interval=100,   
    blit=False
)

ax.legend()
plt.show()


