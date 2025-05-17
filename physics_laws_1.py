def get_energy(mass, velocity):
    # Calculates kinetic energy based on mass and velocity
    return 0.5 * mass * velocity ** 2
def get_momentum(mass, velocity):
    # Calculates momentum based on mass and velocity
    return mass * velocity

def acceleration_dependent_velocity(acceleration, dt, initial_velocity, v_threshold):
    if initial_velocity < v_threshold:
        velocity = initial_velocity + acceleration * dt * (initial_velocity/v_threshold)
        acceleration = acceleration * (initial_velocity/v_threshold)
    else:
        velocity = initial_velocity - acceleration * dt * (initial_velocity/v_threshold)
        acceleration = - acceleration * (initial_velocity/v_threshold)
    return velocity

def get_velocity(acceleration, dt, initial_velocity, v_threshold, n):
    # Calculates velocity based on acceleration and time step
    velocity_by_step = []
    time = []
    for i in range(n):
        velocity = acceleration_dependent_velocity(acceleration, dt, initial_velocity, v_threshold)
        velocity_by_step.append(velocity)
        # Store the velocity for each step
        initial_velocity = velocity
        # Store the time for each step
        time.append(i * dt)
        # Update the initial velocity for the next iteration
    return velocity_by_step, time



