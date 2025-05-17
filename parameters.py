
def set_initial_parameters():
    """
    Set initial parameters for the simulation.
    """
    initial_parameters = {
        "number_of_steps": 100,
        "time_step": 0.01,
        "initial_conditions": {
            "position": 0.0,
            "velocity": 2.4,
            "velocity_threshold": 2.5,
            "acceleration": 1.5

        },
        "simulation_parameters": {
            "gravity": 9.81,
            "mass": 1.0
        }
    }
    return initial_parameters
