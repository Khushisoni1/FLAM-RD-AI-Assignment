import os
import numpy as np
from scipy.optimize import differential_evolution


# --------------------------------------------------
# FLAM R&D / AI Assignment
# Find theta, M and X
# --------------------------------------------------


def curve(t, theta_deg, M, X):
    """
    Parametric curve from the assignment.
    """

    theta = np.radians(theta_deg)

    exponential = np.exp(M * np.abs(t))
    sine_term = np.sin(0.3 * t)

    x = (
        t * np.cos(theta)
        - exponential * sine_term * np.sin(theta)
        + X
    )

    y = (
        42
        + t * np.sin(theta)
        + exponential * sine_term * np.cos(theta)
    )

    return x, y


# --------------------------------------------------
# Check for the data file
# --------------------------------------------------

if not os.path.exists("xy_data.csv"):

    print("----------------------------------------")
    print("FLAM R&D / AI ASSIGNMENT")
    print("----------------------------------------")
    print()
    print("xy_data.csv was not found.")
    print()
    print("The solver is ready.")
    print("Place xy_data.csv in this folder")
    print("when the data file is available.")
    print()

else:

    print("xy_data.csv found.")
    print("Loading data...")

    data = np.loadtxt(
        "xy_data.csv",
        delimiter=",",
        skiprows=1
    )

    x_expected = data[:, 0]
    y_expected = data[:, 1]

    print("Data loaded successfully.")
    print("Number of points:", len(data))

    # --------------------------------------------------
    # Objective function
    # --------------------------------------------------

    def objective(params):

        theta, M, X = params

        # Uniformly sample t from the assignment range
        t = np.linspace(6, 60, len(data))

        x_predicted, y_predicted = curve(
            t,
            theta,
            M,
            X
        )

        # L1 distance
        error = np.sum(
            np.abs(x_expected - x_predicted)
            + np.abs(y_expected - y_predicted)
        )

        return error


    # --------------------------------------------------
    # Parameter ranges from assignment
    # --------------------------------------------------

    bounds = [
        (0, 50),       # theta in degrees
        (-0.05, 0.05), # M
        (0, 100)       # X
    ]


    # --------------------------------------------------
    # Optimization
    # --------------------------------------------------

    print()
    print("Searching for best parameters...")
    print()

    result = differential_evolution(
        objective,
        bounds,
        seed=42,
        polish=True
    )


    # --------------------------------------------------
    # Results
    # --------------------------------------------------

    theta, M, X = result.x

    print("----------------------------------------")
    print("BEST PARAMETERS")
    print("----------------------------------------")
    print(f"Theta = {theta:.8f} degrees")
    print(f"M     = {M:.8f}")
    print(f"X     = {X:.8f}")
    print(f"L1 Error = {result.fun:.8f}")
    print("----------------------------------------")