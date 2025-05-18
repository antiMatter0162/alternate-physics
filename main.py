import matplotlib.pyplot as plt
import physics_laws_1
import parameters
import graph_results

parameters= parameters.set_initial_parameters()

velocity, time = physics_laws_1.get_velocity(parameters["initial_conditions"]["acceleration"], parameters["time_step"], parameters["initial_conditions"]["velocity"], parameters["initial_conditions"]["velocity_threshold"], parameters["number_of_steps"])

position = physics_laws_1.get_position(velocity, parameters["time_step"], parameters["initial_conditions"]["position"], parameters["number_of_steps"])

graph_results.graph_vt(velocity, time)

graph_results.graph_xt(position, time)

graph_results.graph_xv(position, velocity)