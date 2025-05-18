#simulates exponentially increasing acceleration as velocty increases
def velocity_dependent_acceleration(acceleration, velocity):
    acceleration = acceleration + acceleration * ((velocity)/(velocity + 1)) / 100
    return acceleration 

def get_velocity(acceleration, dt, initial_velocity, n):
    velocity_by_step = []
    time = []
    acceleration_by_step = []
    for i in range(n):
        acceleration = velocity_dependent_acceleration(acceleration, initial_velocity)
        print("Acceleration:", acceleration)
        velocity = initial_velocity + acceleration * dt
        velocity_by_step.append(velocity)
        time.append(i * dt)
        acceleration_by_step.append(acceleration)
        initial_velocity = velocity
    return velocity_by_step, time, acceleration_by_step

def get_position(velocity, dt, initial_position, n):
    position_by_step = []
    for i in range(n):
        position = initial_position + velocity[i] * dt
        position_by_step.append(position)
        initial_position = position
    return position_by_step
