import matplotlib.pyplot as plt

def graph_vt(velocity, time):
    # Function to plot velocity vs time
    plt.plot(time, velocity)
    plt.title('Velocity vs Time')
    plt.xlabel('Time')
    plt.ylabel('Velocity')
    plt.grid()
    plt.show()