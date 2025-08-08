import physics_laws_1
import physics_laws_2
import physics_laws_3
import physics_laws_4
# Importing the necessary modules

import parameters
import graph_results

print("=== Animated Physics Simulation ===")
print("This version creates animated visualizations of the physics models.")
print("")

model_to_use = input("Select alternate model number (1-4): ")

while model_to_use not in ["1", "2", "3", "4"]:
    print("Invalid model number. Please select a valid model.")
    model_to_use = input("Select alternate model number (1-4): ")

# Get parameters
parameters_dict = parameters.set_initial_parameters(model_to_use)

# Run the selected physics model
if model_to_use == "1":
    print("Using model 1")
    velocity, time, acceleration = physics_laws_1.get_velocity(
        parameters_dict["initial_conditions"]["acceleration"], 
        0.1, 
        parameters_dict["initial_conditions"]["velocity"], 
        parameters_dict["initial_conditions"]["velocity_threshold"], 
        parameters_dict["number_of_steps"]
    )
    position = physics_laws_1.get_position(
        velocity, 
        0.1, 
        parameters_dict["initial_conditions"]["position"], 
        parameters_dict["number_of_steps"]
    )
    
elif model_to_use == "2":
    print("Using model 2")
    velocity, time, acceleration = physics_laws_2.get_velocity(
        parameters_dict["initial_conditions"]["acceleration"], 
        0.001, 
        parameters_dict['initial_conditions']['velocity'], 
        parameters_dict["number_of_steps"], 
        parameters_dict["simulation_parameters"]["mass"] * parameters_dict['initial_conditions']['acceleration'], 
        parameters_dict["simulation_parameters"]["mass"]
    )
    position = physics_laws_2.get_position(
        velocity, 
        0.001, 
        parameters_dict["initial_conditions"]["position"], 
        parameters_dict["number_of_steps"]
    )
    
elif model_to_use == "3":
    print("Using model 3")
    velocity, time, acceleration = physics_laws_3.get_velocity(
        parameters_dict["initial_conditions"]["acceleration"], 
        0.001, 
        parameters_dict["initial_conditions"]["velocity"], 
        parameters_dict["number_of_steps"], 
        parameters_dict["simulation_parameters"]["mass"] * parameters_dict['initial_conditions']['acceleration'], 
        parameters_dict["simulation_parameters"]["mass"]
    )
    position = physics_laws_3.get_position(
        velocity, 
        0.001, 
        parameters_dict["initial_conditions"]["position"], 
        parameters_dict["number_of_steps"]
    )
    
elif model_to_use == "4":
    print("Using model 4")
    velocity, time, acceleration = physics_laws_4.get_velocity(
        parameters_dict["initial_conditions"]["acceleration"], 
        0.001, 
        parameters_dict["initial_conditions"]["velocity"], 
        parameters_dict["number_of_steps"]
    )
    position = physics_laws_4.get_position(
        velocity, 
        0.001, 
        parameters_dict["initial_conditions"]["position"]
    )

print("\nSimulation complete! Choose your animation type:")
print("1. Individual animated graphs")
print("2. All graphs in one animated view")
print("3. Particle motion visualization") 
print("4. All animation types")

animation_choice = input("Enter your choice (1-4): ")

while animation_choice not in ["1", "2", "3", "4"]:
    print("Invalid choice. Please select 1, 2, 3, or 4.")
    animation_choice = input("Enter your choice (1-4): ")

# Ask about saving animations
save_choice = input("Would you like to save the animations as GIF files? (y/n): ")
save_animations = save_choice.lower() == 'y'

# Show animation speed info
print(f"\nAnimation speed automatically scaled for {len(time)} data points")
print("(More data points = faster animation to keep reasonable duration)")

if animation_choice == "1":
    print("Showing individual animated graphs...")
    print("Close each window to proceed to the next animation.")
    
    print("1. Animating Velocity vs Time...")
    graph_results.animate_vt(velocity, time, save_animation=save_animations)
    
    print("2. Animating Position vs Time...")
    graph_results.animate_xt(position, time, save_animation=save_animations)
    
    print("3. Animating Acceleration vs Time...")
    graph_results.animate_at(acceleration, time, save_animation=save_animations)
    
    print("4. Animating Phase Space (Position vs Velocity)...")
    graph_results.animate_xv(position, velocity, save_animation=save_animations)

elif animation_choice == "2":
    print("Showing all graphs in one animated view...")
    graph_results.animate_all_graphs(velocity, time, acceleration, position, save_animation=save_animations)

elif animation_choice == "3":
    print("Showing particle motion visualization...")
    graph_results.animate_particle_motion(position, time, save_animation=save_animations)

elif animation_choice == "4":
    print("Showing all animation types...")
    print("Close each window to proceed to the next animation.")
    
    print("1. All graphs in one view...")
    graph_results.animate_all_graphs(velocity, time, acceleration, position, save_animation=save_animations)
    
    print("2. Particle motion visualization...")
    graph_results.animate_particle_motion(position, time, save_animation=save_animations)
    
    print("3. Individual graphs...")
    graph_results.animate_vt(velocity, time, save_animation=save_animations)
    graph_results.animate_xt(position, time, save_animation=save_animations)
    graph_results.animate_at(acceleration, time, save_animation=save_animations)
    graph_results.animate_xv(position, velocity, save_animation=save_animations)

# Show max values
print("\n=== Simulation Results ===")
graph_results.give_max_values(velocity, acceleration)

# Option to save results to file
save_results = input("\nWould you like to save the numerical results to a file? (y/n): ")
if save_results.lower() == 'y':
    graph_results.save_results(velocity, time, acceleration, position)
    print("Numerical results saved to 'results.txt'.")
else:
    print("Numerical results not saved.")

print("\nAnimation complete! Thank you for using the animated physics simulation.")
