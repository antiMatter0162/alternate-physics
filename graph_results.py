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
    plt.plot(velocity, position, label='Position vs Velocity', color='green')
    plt.legend()
    plt.title('Position vs Velocity')
    plt.xlabel('Velocity')
    plt.ylabel('Position')
    plt.grid()
    plt.show()