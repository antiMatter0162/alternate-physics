#simulates quasi - relativistic effects at much lower speeds
def velocity_dependent_mass(mass, velocity):
    alpha = 0.5
    m_0 = 1.0
    mass = m_0 * (1 + velocity**2 * alpha)
    return mass

def force_law(mass, force):     
    acceleration = force / mass
    return acceleration

def get_velocity(acceleration, dt, initial_velocity, n, force, mass):
    velocity_by_step = []
    time = []
    gamma = 30.0
    for i in range(n):
        velocity = initial_velocity + acceleration * dt * gamma
        mass = velocity_dependent_mass(mass, velocity)
        if mass == 0:
            print("Mass is zero, stopping simulation.")
            break
        acceleration = force_law(mass, force)
        velocity_by_step.append(velocity)
        initial_velocity = velocity
        time.append(i * dt)
    return velocity_by_step, time

def get_position(velocity, dt, initial_position, n_steps):
    position_by_step = []
    n_steps = len(velocity)
    for i in range(n_steps):
        # Debugging line to check velocity values
        position = initial_position + velocity[i] * dt
        position_by_step.append(position)
        initial_position = position
    return position_by_step