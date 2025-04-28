# Import packages
import numpy as np
import matplotlib.pyplot as plt

# Configuration options
DISPLAY_NUMERICAL = True
PLOT_TRAJECTORIES = True
ONE_PLOT = True
FRAME = [1, 2]  # Only used if PLOT_TRAJECTORIES = False

# Initial state
x = np.array([1, 0.5, 1, 0])  # Initial values for x1, x2, x3, x4
t = [0]
dt = 0.1
t_end = 10
num_steps = int(t_end / dt)

# System matrix A
A = np.array([
    [-1, 0.2, 0.1, 0],
    [0, -1, 0.6, 0.4],
    [0.5, 0, -1, 0.5],
    [0.1, 0.2, 0.7, -1]
])

# Store trajectories
trajectories = [x.copy()]

# Define the system derivative
def f(x):
    return A @ x  # Matrix multiplication

# Runge-Kutta 4th Order Integration
for step in range(num_steps):
    k1 = f(x)
    k2 = f(x + (dt/2) * k1)
    k3 = f(x + (dt/2) * k2)
    k4 = f(x + dt * k3)
    x = x + (dt/6) * (k1 + 2*k2 + 2*k3 + k4)
    
    t.append(t[-1] + dt)
    trajectories.append(x.copy())

# Convert trajectories list into numpy array for easier slicing
trajectories = np.array(trajectories).T  # Shape: (num_variables, num_steps+1)

# Display numerical results
if DISPLAY_NUMERICAL:
    for idx, xi in enumerate(trajectories):
        print(f"X{idx+1} = {xi}")

# Plotting
t = np.array(t)

if PLOT_TRAJECTORIES:
    markers = ['*-k', '-or', '-xg', '->b', '-<c', '-^m']  # Extendable if more variables
    if ONE_PLOT:
        plt.figure(figsize=(10, 6))
        for i in range(trajectories.shape[0]):
            marker = markers[i % len(markers)]
            plt.plot(t, trajectories[i], marker, label=f'X{i+1}')
        plt.xlabel('Time')
        plt.ylabel('Value')
        plt.title('State Trajectories Over Time')
        plt.legend()
        plt.grid(True)
    else:
        fig, axes = plt.subplots(trajectories.shape[0], 1, figsize=(8, 2*trajectories.shape[0]))
        for i, ax in enumerate(axes):
            marker = markers[i % len(markers)]
            ax.plot(t, trajectories[i], marker)
            ax.set_ylabel(f'X{i+1}')
            ax.grid(True)
        axes[-1].set_xlabel('Time')
        plt.tight_layout()
else:
    i, j = FRAME[0]-1, FRAME[1]-1
    plt.plot(trajectories[i], trajectories[j], 'k-*')
    plt.xlabel(f'X{FRAME[0]}')
    plt.ylabel(f'X{FRAME[1]}')
    plt.title(f'Trajectory in X{FRAME[0]} vs X{FRAME[1]} Plane')
    plt.grid(True)

plt.show()
