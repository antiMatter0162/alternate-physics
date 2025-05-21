import matplotlib.pyplot as plt

def graph_vt(velocity, time):
    # Function to plot velocity vs time
    plt.plot(time, velocity, label='Velocity')
    plt.legend()
    plt.title('Velocity vs Time')
    plt.xlabel('Time')
    plt.ylabel('Velocity')
    plt.grid()
    plt.show()

def graph_xt(position, time):
    # Function to plot position vs time
    plt.plot(time, position, label='Position', color='orange')
    plt.legend()
    plt.title('Position vs Time')
    plt.xlabel('Time')
    plt.ylabel('Position')
    plt.grid()
    plt.show()

def graph_xv(position, velocity):
    # Function to plot position vs velocity
    # Not particularly useful in practice
    plt.plot(velocity, position, label='Position vs Velocity', color='green')
    plt.legend()
    plt.title('Position vs Velocity')
    plt.xlabel('Velocity')
    plt.ylabel('Position')
    plt.grid()
    plt.show()

def graph_at(acceleration, time):
    # Function to plot acceleration vs time
    plt.plot(time, acceleration, label='Acceleration', color='red')
    plt.legend()
    plt.title('Acceleration vs Time')
    plt.xlabel('Time')
    plt.ylabel('Acceleration')
    plt.grid()
    plt.show()

def give_max_values(velocity, acceleration):
    # Function to give max values of velocity and acceleration
    max_velocity = max(velocity)
    max_acceleration = max(acceleration)
    print(f"Max Velocity: {max_velocity}")
    print(f"Max Acceleration: {max_acceleration}")

def save_results(velocity, time, acceleration, position):
    # Function to save results to a file
    with open('results.txt', 'w') as f:
        f.write("Time, Velocity, Acceleration, Position\n")
        for t, v, a, p in zip(time, velocity, acceleration, position):
            f.write(f"{t}, {v}, {a}, {p}\n")
    print("Results saved to results.txt")