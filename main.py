
import physics_laws_1
import physics_laws_2
import physics_laws_3
import physics_laws_4
# Importing the necessary modules

import parameters
import graph_results

print("=== Physics Simulation ===")
animation_mode = input("Would you like animated graphs? (y/n): ")

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

# Display graphs based on user preference
if animation_mode.lower() == 'y':
    print("\nChoose animation type:")
    print("1. Individual animated graphs")
    print("2. All graphs in one view") 
    print("3. Particle motion visualization")
    
    anim_choice = input("Enter choice (1-3) [default: 2]: ")
    if anim_choice not in ["1", "2", "3"]:
        anim_choice = "2"
    
    save_anim = input("Save animations as GIFs? (y/n): ").lower() == 'y'
    
    if anim_choice == "1":
        graph_results.animate_vt(velocity, time, save_animation=save_anim)
        graph_results.animate_xt(position, time, save_animation=save_anim)  
        graph_results.animate_xv(position, velocity, save_animation=save_anim)
        graph_results.animate_at(acceleration, time, save_animation=save_anim)
    elif anim_choice == "2":
        graph_results.animate_all_graphs(velocity, time, acceleration, position, save_animation=save_anim)
    else:
        graph_results.animate_particle_motion(position, time, save_animation=save_anim)
else:
    # Original static graphs
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