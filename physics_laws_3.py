#no idea what this is, but it looks funny

import math
def sinuosoidal_law(force, mass, time):
    factor = math.sin(force / mass * time)
    return factor

def get_velocity(acceleration, dt, initial_velocity, n, force, mass):
    velocity_by_step = []
    time = []
    gamma = 1.0
    acceleration_by_step = []
    a_0 = acceleration
    for i in range(n):
        acceleration = a_0 * sinuosoidal_law(force, mass, dt * i)
        acceleration_by_step.append(acceleration)
        velocity = initial_velocity + acceleration * dt * gamma
        if mass == 0:
            print("Mass is zero, stopping simulation.")
            break
        velocity_by_step.append(velocity)
        initial_velocity = velocity
        time.append(i * dt)
    return velocity_by_step, time, acceleration_by_step

def get_position(velocity, dt, initial_position, n_steps): 
    position_by_step = []
    n_steps = len(velocity)
    for i in range(n_steps):
        # Debugging line to check velocity values
        position = initial_position + velocity[i] * dt
        position_by_step.append(position)
        initial_position = position
    return position_by_step