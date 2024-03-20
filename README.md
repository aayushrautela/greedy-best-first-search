# Maze Solver

## Overview

This Python program, `maze_solver.py`, is designed to solve mazes using the Greedy Best-First Search algorithm. The program takes as input a 2D grid representing a maze, where the maze includes empty spaces, walls, a start position, and an end position. The objective is to find a path from the start to the end position using the least number of steps possible. This implementation features a step-by-step visualization of the search procedure and incorporates two distinct heuristics to guide the search process.

## Features

- **Greedy Best-First Search Algorithm:** Efficiently finds a path from the start to the end position in a maze.
- **Two Heuristics:** Implements two distinct heuristics to optimize the search process.
- **Visualization:** Provides a console-based step-by-step visualization of the algorithm's search procedure, making it easier to understand how the solution is derived.
- **Test Cases:** Includes various test cases, including corner cases, to ensure the reliability and robustness of the solution.

## Requirements

Before running the program, ensure you have the following prerequisites installed:
- Python 3.6 or later

## Installation

No additional installation is required. Clone or download the repository to get started.

## Usage

To run the program, navigate to the directory containing `maze_solver.py` and execute the following command in your terminal:

```
python maze_solver.py
```

## Heuristics Implemented

The program implements the following two heuristics for the Greedy Best-First Search algorithm:

1. **Euclidean Distance:** Calculates the straight-line distance between the current position and the end position.
2. **Manhattan Distance:** Calculates the sum of the absolute differences of the Cartesian coordinates between the current position and the end position.

## Contributing

We welcome contributions! If you have suggestions for improving the algorithm or adding new features, please feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Algorithm Description and Implementation

### Greedy Best-First Search Algorithm

The Greedy Best-First Search (GBFS) algorithm is a search algorithm that navigates through a space, such as a maze, by selecting the path that appears to be leading most directly towards the goal at each step. Unlike other search algorithms that might consider the distance already traveled (the "cost"), GBFS focuses solely on an estimate of the distance from the current state to the goal. This makes it a "greedy" algorithm, as it prioritizes immediate progress over the total distance traveled.

### Implementation in This Project

In `maze_solver.py`, the GBFS algorithm is implemented with two heuristics to efficiently solve maze puzzles:

- **Euclidean Distance Heuristic:** This heuristic calculates the straight-line distance between two points in the maze. It's used when the path between the start and end points can be diagonal, providing a closer approximation to the actual shortest path in such scenarios.

- **Manhattan Distance Heuristic:** This heuristic calculates the sum of the absolute differences between the X and Y coordinates of two points. It's particularly effective in grid-based mazes where movement is restricted to horizontal and vertical steps, resembling the street layout of Manhattan.

The choice of heuristic can be adjusted based on the characteristics of the maze, allowing for flexibility and optimization in solving various maze configurations.

### Step-by-Step Visualization

To aid in understanding and debugging, the program includes a console-based visualization that displays the maze at each step of the algorithm's execution. This visualization shows the current position, explored paths, and the walls of the maze, offering insight into how the algorithm navigates through the maze towards the goal.

This implementation is structured to be modular, allowing for easy adaptation or expansion. Auxiliary functions are included to support the algorithm's operations, such as functions for generating the maze, updating the visualization, and calculating heuristic distances.

By combining the GBFS algorithm with these heuristics and visualization tools, this project provides a comprehensive solution for solving mazes, demonstrating the practical application of these concepts in a Python environment.
