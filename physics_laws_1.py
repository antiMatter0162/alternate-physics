
# simulates a "lagging" effect in velocity with discretized time steps
def acceleration_dependent_velocity(acceleration, dt, initial_velocity, v_threshold):
    gamma = 1.5
    a_0 = 1.5
    # Gamma is a constant that determines the effect of acceleration on velocity
    if initial_velocity < v_threshold:
        velocity = initial_velocity + acceleration * dt * (1 - initial_velocity/v_threshold) * gamma
        acceleration = a_0 * (initial_velocity/v_threshold) * gamma
    else:
        velocity = initial_velocity - acceleration * dt * (1 - initial_velocity/v_threshold) * gamma
        acceleration = - a_0 * (initial_velocity/v_threshold) * gamma
        v_threshold = v_threshold * 1.01
    return velocity, v_threshold, acceleration

def get_velocity(acceleration, dt, initial_velocity, v_threshold, n):
    # Calculates velocity based on acceleration and time step
    velocity_by_step = []
    time = []
    acceleration_by_step = []
    for i in range(n):
        velocity, v_threshold, acceleration = acceleration_dependent_velocity(acceleration, dt, initial_velocity, v_threshold)
        velocity_by_step.append(velocity)
        acceleration_by_step.append(acceleration)
        # Store the velocity for each step
        initial_velocity = velocity
        # Store the time for each step
        time.append(i * dt)
        # Update the initial velocity for the next iteration
    return velocity_by_step, time, acceleration_by_step

def get_position(velocity, dt, initial_position, n):
    # Calculates position based on velocity and time step
    gamma = 15.0
    position_by_step = []
    for i in range(n):
        position = initial_position + velocity[i] * dt * gamma
        position_by_step.append(position)
        # Store the position for each step
        initial_position = position
    return position_by_step



