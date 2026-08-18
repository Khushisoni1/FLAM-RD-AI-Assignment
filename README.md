# FLAM R&D / AI Assignment

## Objective

The objective of this assignment is to determine the unknown parameters
theta (θ), M and X of the given parametric curve.

## Parametric Curve

The curve is defined by:

x = (t ∗ cos(θ) − eM∣t∣⋅ sin(0.3t) sin(θ) + X)

y = (42 + t ∗ sin(θ) + e ⋅ sin(0.3t) cos(θ) M∣t∣ )
## Parameter Ranges

- 0° < θ < 50°
- -0.05 < M < 0.05
- 0 < X < 100
- 6 < t < 60

## Approach

1. Define the given parametric equations.
2. Load the curve data from xy_data.csv.
3. Generate predicted points using candidate values of θ, M and X.
4. Calculate the L1 distance between the expected and predicted points.
5. Search the permitted parameter ranges for the combination that minimizes
   the L1 distance.
6. Plot the resulting curve for verification.

## Tools Used

- Python
- NumPy
- SciPy
- Matplotlib
- Desmos
- GitHub

## Files

- `solve_assignment.py` - Python program used to estimate the parameters.
- `xy_data.csv` - Provided curve data.
- `curve.png` - Final curve visualization.

## Results

The final values of θ, M and X will be added after processing the provided
curve data.
