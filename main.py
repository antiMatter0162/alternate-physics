
import physics_laws_1
import physics_laws_2
import physics_laws_3
import physics_laws_4
# Importing the necessary modules

import parameters
import graph_results
model_to_use = input("Select alternate model number: ")

while model_to_use not in ["1", "2", "3", "4"]:
    print("Invalid model number. Please select a valid model.")
    model_to_use = input("Select alternate model number: ")

parameters= parameters.set_initial_parameters(model_to_use)
if model_to_use == "1":
    print("Using model 1")
    velocity, time, acceleration = physics_laws_1.get_velocity(parameters["initial_conditions"]["acceleration"], 0.1, parameters["initial_conditions"]["velocity"], parameters["initial_conditions"]["velocity_threshold"], parameters["number_of_steps"])
    position = physics_laws_1.get_position(velocity, 0.1, parameters["initial_conditions"]["position"], parameters["number_of_steps"])
elif model_to_use == "2":
    print("Using model 2")
    velocity, time, acceleration = physics_laws_2.get_velocity(parameters["initial_conditions"]["acceleration"], 0.001, parameters['initial_conditions']['velocity'], parameters["number_of_steps"], parameters["simulation_parameters"]["mass"] * parameters['initial_conditions']['acceleration'], parameters["simulation_parameters"]["mass"])
    position = physics_laws_2.get_position(velocity, 0.001, parameters["initial_conditions"]["position"], parameters["number_of_steps"])
elif model_to_use == "3":
    print("Using model 3")
    velocity, time, acceleration = physics_laws_3.get_velocity(parameters["initial_conditions"]["acceleration"], 0.001, parameters["initial_conditions"]["velocity"], parameters["number_of_steps"], parameters["simulation_parameters"]["mass"] * parameters['initial_conditions']['acceleration'], parameters["simulation_parameters"]["mass"])
    position = physics_laws_3.get_position(velocity, 0.001, parameters["initial_conditions"]["position"], parameters["number_of_steps"])
elif model_to_use == "4":
    print("Using model 4")
    velocity, time, acceleration = physics_laws_4.get_velocity(parameters["initial_conditions"]["acceleration"], 0.001, parameters["initial_conditions"]["velocity"], parameters["number_of_steps"])
    position = physics_laws_4.get_position(velocity, 0.001, parameters["initial_conditions"]["position"])

    
graph_results.graph_vt(velocity, time)

graph_results.graph_xt(position, time)

graph_results.graph_xv(position, velocity)

graph_results.graph_at(acceleration, time)

graph_results.give_max_values(velocity, acceleration)


save_results = input("Would you like to save the results? (y/n) ")
if save_results.lower() == 'y':
    graph_results.save_results(velocity, time, acceleration, position)
    print("Results saved.")
else:
    print("Results not saved.")