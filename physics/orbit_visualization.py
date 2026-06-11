import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation 

EARTH_RADIUS = 6371000

def animate_orbit(orbital_radius, orbital_period):

    theta = np.linspace(0, 2*np.pi, 1000)

    earth_x = EARTH_RADIUS * np.cos(theta)
    earth_y = EARTH_RADIUS * np.sin(theta)

    orbit_x = orbital_radius * np.cos(theta)
    orbit_y = orbital_radius * np.sin(theta)

    fig, ax = plt.subplots(figsize=(8,8))
    ax.set_facecolor("black")
    fig.patch.set_facecolor("black")

    earth = plt.Circle(
    (0, 0),
    EARTH_RADIUS,
    color="royalblue"
)
    ax.add_patch(earth)

    ax.plot(
    orbit_x,
    orbit_y,
    color="white",
    linestyle="--",
    linewidth=1.5,
    alpha=0.7
)

    satellite, = ax.plot(
    [],
    [],
    marker='o',
    color='gold',
    markersize=10
)

    ax.set_aspect('equal')
    ax.axis('off')

    ax.set_title("Satellite Orbit Animation")

    limit = orbital_radius * 1.8
    ax.set_xlim(-limit, limit)
    ax.set_ylim(-limit, limit)

    omega = 2*np.pi / orbital_period

    telemetry = ax.text(
    0.01,
    0.99,
    "",
    transform=ax.transAxes,
    color="white",
    fontsize=11,
    verticalalignment="top",
    family="monospace",
    bbox=dict(
        facecolor="black",
        edgecolor="white",
        alpha=0.9
    )
)

    def update(frame):

        t = frame

        angle = omega * t

        x = orbital_radius * np.cos(angle)
        y = orbital_radius * np.sin(angle)

        telemetry.set_text(

    f"Altitude : {(orbital_radius-EARTH_RADIUS)/1000:.0f} km\n"
    f"Velocity : {np.sqrt(3.986e14/orbital_radius)/1000:.2f} km/s\n"
    f"Period   : {orbital_period/60:.2f} min\n"
    f"Angle    : {np.degrees(angle)%360:.1f}°"
)

        satellite.set_data([x], [y])

        return satellite, telemetry

    ani = FuncAnimation(
        fig,
        update,
        frames=np.arange(0, orbital_period, 20),
        interval=50,
        blit=True,
        repeat=True
    )

    plt.show()