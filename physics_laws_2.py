#simulates quasi - relativistic effects at much lower speeds
def velocity_dependent_force(force, velocity, f_0):
    c = 50.0
    if velocity > c:
        velocity = c
    #c is the hypothetical maximum speed limit
    force = f_0 * (1 - velocity**2 / c**2)**0.5
    return force

def force_law(mass, force):     
    acceleration = force / mass
    return acceleration

def get_velocity(acceleration, dt, initial_velocity, n, force, mass):
    velocity_by_step = []
    time = []
    acceleration_by_step = []
    f_0 = force
    #f_0 is the force constant equal to the initial force
    gamma = 1.0
    for i in range(n):
        velocity = initial_velocity + acceleration * dt * gamma
        force = velocity_dependent_force(force, velocity, f_0)
        if velocity > 50.0:
            velocity = 50.0
        if mass == 0:
            print("Mass is zero, stopping simulation.")
            break
        acceleration = force_law(mass, force)
        acceleration_by_step.append(acceleration)
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