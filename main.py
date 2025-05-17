import matplotlib.pyplot as plt
import physics_laws
import parameters
import graph_results

parameters= parameters.set_initial_parameters()

velocity, time = physics_laws.get_velocity(parameters["initial_conditions"]["acceleration"], parameters["time_step"], parameters["initial_conditions"]["velocity"], parameters["initial_conditions"]["velocity_threshold"], parameters["number_of_steps"])
print(velocity)
print(time)
graph_results.graph_vt(velocity, time)