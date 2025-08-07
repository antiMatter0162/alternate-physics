import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

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

# Animated versions of the graphing functions
def animate_vt(velocity, time, interval=50, save_animation=False):
    """Animated velocity vs time plot"""
    fig, ax = plt.subplots()
    ax.set_xlim(min(time), max(time))
    ax.set_ylim(min(velocity) - abs(min(velocity)) * 0.1, max(velocity) + abs(max(velocity)) * 0.1)
    ax.set_xlabel('Time')
    ax.set_ylabel('Velocity')
    ax.set_title('Velocity vs Time (Animated)')
    ax.grid(True)
    
    line, = ax.plot([], [], 'b-', label='Velocity', linewidth=2)
    point, = ax.plot([], [], 'ro', markersize=8)
    ax.legend()
    
    def animate(frame):
        if frame < len(time):
            line.set_data(time[:frame+1], velocity[:frame+1])
            point.set_data([time[frame]], [velocity[frame]])
        return line, point
    
    anim = animation.FuncAnimation(fig, animate, frames=len(time), 
                                 interval=interval, blit=True, repeat=True)
    
    if save_animation:
        anim.save('velocity_time_animation.gif', writer='pillow', fps=20)
        print("Animation saved as 'velocity_time_animation.gif'")
    
    plt.show()
    return anim

def animate_xt(position, time, interval=50, save_animation=False):
    """Animated position vs time plot"""
    fig, ax = plt.subplots()
    ax.set_xlim(min(time), max(time))
    ax.set_ylim(min(position) - abs(min(position)) * 0.1, max(position) + abs(max(position)) * 0.1)
    ax.set_xlabel('Time')
    ax.set_ylabel('Position')
    ax.set_title('Position vs Time (Animated)')
    ax.grid(True)
    
    line, = ax.plot([], [], 'orange', label='Position', linewidth=2)
    point, = ax.plot([], [], 'ro', markersize=8)
    ax.legend()
    
    def animate(frame):
        if frame < len(time):
            line.set_data(time[:frame+1], position[:frame+1])
            point.set_data([time[frame]], [position[frame]])
        return line, point
    
    anim = animation.FuncAnimation(fig, animate, frames=len(time), 
                                 interval=interval, blit=True, repeat=True)
    
    if save_animation:
        anim.save('position_time_animation.gif', writer='pillow', fps=20)
        print("Animation saved as 'position_time_animation.gif'")
    
    plt.show()
    return anim

def animate_at(acceleration, time, interval=50, save_animation=False):
    """Animated acceleration vs time plot"""
    fig, ax = plt.subplots()
    ax.set_xlim(min(time), max(time))
    ax.set_ylim(min(acceleration) - abs(min(acceleration)) * 0.1, max(acceleration) + abs(max(acceleration)) * 0.1)
    ax.set_xlabel('Time')
    ax.set_ylabel('Acceleration')
    ax.set_title('Acceleration vs Time (Animated)')
    ax.grid(True)
    
    line, = ax.plot([], [], 'red', label='Acceleration', linewidth=2)
    point, = ax.plot([], [], 'ro', markersize=8)
    ax.legend()
    
    def animate(frame):
        if frame < len(time):
            line.set_data(time[:frame+1], acceleration[:frame+1])
            point.set_data([time[frame]], [acceleration[frame]])
        return line, point
    
    anim = animation.FuncAnimation(fig, animate, frames=len(time), 
                                 interval=interval, blit=True, repeat=True)
    
    if save_animation:
        anim.save('acceleration_time_animation.gif', writer='pillow', fps=20)
        print("Animation saved as 'acceleration_time_animation.gif'")
    
    plt.show()
    return anim

def animate_xv(position, velocity, interval=50, save_animation=False):
    """Animated position vs velocity plot (phase space)"""
    fig, ax = plt.subplots()
    ax.set_xlim(min(velocity) - abs(min(velocity)) * 0.1, max(velocity) + abs(max(velocity)) * 0.1)
    ax.set_ylim(min(position) - abs(min(position)) * 0.1, max(position) + abs(max(position)) * 0.1)
    ax.set_xlabel('Velocity')
    ax.set_ylabel('Position')
    ax.set_title('Position vs Velocity (Animated Phase Space)')
    ax.grid(True)
    
    line, = ax.plot([], [], 'green', label='Phase Trajectory', linewidth=2)
    point, = ax.plot([], [], 'ro', markersize=8)
    ax.legend()
    
    def animate(frame):
        if frame < len(velocity):
            line.set_data(velocity[:frame+1], position[:frame+1])
            point.set_data([velocity[frame]], [position[frame]])
        return line, point
    
    anim = animation.FuncAnimation(fig, animate, frames=len(velocity), 
                                 interval=interval, blit=True, repeat=True)
    
    if save_animation:
        anim.save('position_velocity_animation.gif', writer='pillow', fps=20)
        print("Animation saved as 'position_velocity_animation.gif'")
    
    plt.show()
    return anim

def animate_particle_motion(position, time, interval=50, save_animation=False):
    """Animated visualization of particle motion in 1D"""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    
    # Top plot: particle position on a line
    ax1.set_xlim(min(position) - abs(max(position) - min(position)) * 0.1, 
                 max(position) + abs(max(position) - min(position)) * 0.1)
    ax1.set_ylim(-0.5, 0.5)
    ax1.set_xlabel('Position')
    ax1.set_title('Particle Motion (1D)')
    ax1.grid(True, alpha=0.3)
    ax1.axhline(y=0, color='k', linewidth=1)
    
    # Bottom plot: position vs time with current point highlighted
    ax2.set_xlim(min(time), max(time))
    ax2.set_ylim(min(position) - abs(min(position)) * 0.1, max(position) + abs(max(position)) * 0.1)
    ax2.set_xlabel('Time')
    ax2.set_ylabel('Position')
    ax2.set_title('Position vs Time')
    ax2.grid(True)
    
    # Elements to animate
    particle, = ax1.plot([], [], 'ro', markersize=15, label='Particle')
    trail, = ax1.plot([], [], 'r-', alpha=0.3, linewidth=1)
    pos_line, = ax2.plot([], [], 'b-', linewidth=2)
    current_point, = ax2.plot([], [], 'ro', markersize=8)
    
    ax1.legend()
    
    def animate(frame):
        if frame < len(time):
            # Update particle position
            particle.set_data([position[frame]], [0])
            
            # Update trail (show last few positions)
            trail_length = min(20, frame + 1)
            trail_positions = position[max(0, frame - trail_length + 1):frame + 1]
            trail_y = [0] * len(trail_positions)
            trail.set_data(trail_positions, trail_y)
            
            # Update position vs time plot
            pos_line.set_data(time[:frame+1], position[:frame+1])
            current_point.set_data([time[frame]], [position[frame]])
            
        return particle, trail, pos_line, current_point
    
    anim = animation.FuncAnimation(fig, animate, frames=len(time), 
                                 interval=interval, blit=True, repeat=True)
    
    if save_animation:
        anim.save('particle_motion_animation.gif', writer='pillow', fps=20)
        print("Animation saved as 'particle_motion_animation.gif'")
    
    plt.tight_layout()
    plt.show()
    return anim

def animate_all_graphs(velocity, time, acceleration, position, interval=50, save_animation=False):
    """Show all animated graphs in a single figure with subplots"""
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
    
    # Set up each subplot
    # Velocity vs Time
    ax1.set_xlim(min(time), max(time))
    ax1.set_ylim(min(velocity) - abs(min(velocity)) * 0.1, max(velocity) + abs(max(velocity)) * 0.1)
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Velocity')
    ax1.set_title('Velocity vs Time')
    ax1.grid(True)
    
    # Position vs Time
    ax2.set_xlim(min(time), max(time))
    ax2.set_ylim(min(position) - abs(min(position)) * 0.1, max(position) + abs(max(position)) * 0.1)
    ax2.set_xlabel('Time')
    ax2.set_ylabel('Position')
    ax2.set_title('Position vs Time')
    ax2.grid(True)
    
    # Acceleration vs Time
    ax3.set_xlim(min(time), max(time))
    ax3.set_ylim(min(acceleration) - abs(min(acceleration)) * 0.1, max(acceleration) + abs(max(acceleration)) * 0.1)
    ax3.set_xlabel('Time')
    ax3.set_ylabel('Acceleration')
    ax3.set_title('Acceleration vs Time')
    ax3.grid(True)
    
    # Phase Space (Position vs Velocity)
    ax4.set_xlim(min(velocity) - abs(min(velocity)) * 0.1, max(velocity) + abs(max(velocity)) * 0.1)
    ax4.set_ylim(min(position) - abs(min(position)) * 0.1, max(position) + abs(max(position)) * 0.1)
    ax4.set_xlabel('Velocity')
    ax4.set_ylabel('Position')
    ax4.set_title('Phase Space (Position vs Velocity)')
    ax4.grid(True)
    
    # Create line and point objects for each subplot
    v_line, = ax1.plot([], [], 'b-', linewidth=2)
    v_point, = ax1.plot([], [], 'ro', markersize=6)
    
    x_line, = ax2.plot([], [], 'orange', linewidth=2)
    x_point, = ax2.plot([], [], 'ro', markersize=6)
    
    a_line, = ax3.plot([], [], 'red', linewidth=2)
    a_point, = ax3.plot([], [], 'ro', markersize=6)
    
    phase_line, = ax4.plot([], [], 'green', linewidth=2)
    phase_point, = ax4.plot([], [], 'ro', markersize=6)
    
    def animate(frame):
        if frame < len(time):
            # Update all plots
            v_line.set_data(time[:frame+1], velocity[:frame+1])
            v_point.set_data([time[frame]], [velocity[frame]])
            
            x_line.set_data(time[:frame+1], position[:frame+1])
            x_point.set_data([time[frame]], [position[frame]])
            
            a_line.set_data(time[:frame+1], acceleration[:frame+1])
            a_point.set_data([time[frame]], [acceleration[frame]])
            
            phase_line.set_data(velocity[:frame+1], position[:frame+1])
            phase_point.set_data([velocity[frame]], [position[frame]])
            
        return v_line, v_point, x_line, x_point, a_line, a_point, phase_line, phase_point
    
    anim = animation.FuncAnimation(fig, animate, frames=len(time), 
                                 interval=interval, blit=True, repeat=True)
    
    if save_animation:
        anim.save('all_graphs_animation.gif', writer='pillow', fps=20)
        print("Animation saved as 'all_graphs_animation.gif'")
    
    plt.tight_layout()
    plt.show()
    return anim