# CPU-Scheduling-Processes-Using-Threading
This repository contains a Python implementation of four CPU scheduling algorithms: First Come First Serve (FCFS), Shortest Job First (SJF), High Response Ratio Next (HRRN), and Round Robin (RR). The main file (Main.py) orchestrates the execution of these algorithms using threads.

# CPU Scheduling Algorithms

This repository contains a Python implementation of various CPU scheduling algorithms, including **First Come First Serve (FCFS)**, **Shortest Job First (SJF)**, **High Response Ratio Next (HRRN)**, and **Round Robin (RR)**. The main file (`Main.py`) orchestrates the execution of these algorithms using threads.

## Algorithms Implemented

1. **FCFS:**
   - First Come First Serve scheduling algorithm.
   - Calculates completion time, response time, and waiting time.
   - Generates Gantt Chart for visualization.

2. **SJF:**
   - Shortest Job First scheduling algorithm.
   - Considers both arrival time and burst time.
   - Computes average response time and waiting time.
   - Presents Gantt Chart for better understanding.

3. **HRRN:**
   - High Response Ratio Next scheduling algorithm.
   - Utilizes response ratio for process prioritization.
   - Computes average response time and waiting time.
   - Displays Gantt Chart for visualization.

4. **RR:**
   - Round Robin scheduling algorithm with user-defined time slice.
   - Generates Gantt Chart to visualize the execution.
   - Calculates average response time and waiting time.

## Usage

1. Run the `Main.py` file to execute and compare the performance of the implemented CPU scheduling algorithms.
2. Enter the arrival time and burst time details as prompted.
3. Provide the time slice for Round Robin when prompted.

## File Structure

- `FCFS.py`, `SJF.py`, `HRRN.py`, and `RR.py` contain the respective algorithm implementations.
- `Main.py` orchestrates the execution of all algorithms using threads.

## Contributing

Feel free to explore, experiment, and contribute to the project! If you have any improvements or new algorithms to add, open an [issue](https://github.com/R-Y-N-36/CPU-Scheduling-Processes-Using-Threading/issues) or submit a [pull request](https://github.com/R-Y-N-36/CPU-Scheduling-Processes-Using-Threading/pulls).

## License

This project is licensed under the [MIT License](LICENSE).
