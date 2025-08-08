# alternate-physics

**READ MODEL_GUIDE BEFORE RUNNING THE SIMULATION!**

This is a hypothetical kinematics simulation employing fundamental laws
of physics different from Newton's laws. There are a total of four alternate
physical systems, with most bearing a certain amount of resemblance to real
behavior, albeit at very different scales. Parameter customization is possible.

## New Features: Animated Visualizations

The simulation now includes animated visualizations to better understand the physics models:

### Running the Simulation

**Option 1: Original main.py with animation choice**
```bash
python main.py
```
Choose 'y' when prompted for animated graphs.

**Option 2: Dedicated animated version**
```bash
python main_animated.py
```
This version is specifically designed for animations with more options.

### Animation Types Available

1. **Individual Animated Graphs**: Each graph (velocity-time, position-time, acceleration-time, phase space) is shown separately with animated data points
2. **All Graphs Combined**: All four graphs in a single window, updating simultaneously
3. **Particle Motion Visualization**: Shows a particle moving along a line with position vs time graph below
4. **All Animation Types**: Displays all available animations in sequence

### Animation Features

- **Automatic Speed Scaling**: Animation speed automatically adjusts based on the number of data points to keep reasonable duration
  - ≤100 points: Normal speed (50ms intervals)
  - ≤500 points: 2x faster (25ms intervals)  
  - ≤1000 points: 4x faster (12ms intervals)
  - >1000 points: 8x faster (6ms intervals)
- **Save as GIF**: Option to save animations as GIF files for sharing or presentations
- **Interactive Controls**: All matplotlib animation controls available (pause, step, etc.)
- **Real-time Data Points**: See the current data point highlighted as the animation progresses
- **Data Point Counter**: Each animation shows the total number of points being animated

### Requirements

- matplotlib
- numpy
- pillow (for GIF saving)

All dependencies are automatically installed when using the virtual environment.

