# CPU-Scheduling-Processes-Using-Threading
This repository contains a Python implementation of four CPU scheduling algorithms: First Come First Serve (FCFS), Shortest Job First (SJF), High Response Ratio Next (HRRN), and Round Robin (RR). The main file (Main.py) orchestrates the execution of these algorithms using threads.

CPU Scheduling Algorithms
This repository contains a Python implementation of various CPU scheduling algorithms, including First Come First Serve (FCFS), Shortest Job First (SJF), High Response Ratio Next (HRRN), and Round Robin (RR). The main file (Main.py) orchestrates the execution of these algorithms using threads.

Algorithms Implemented
FCFS:

First Come First Serve scheduling algorithm.
Calculates completion time, response time, and waiting time.
Generates Gantt Chart for visualization.
SJF:

Shortest Job First scheduling algorithm.
Considers both arrival time and burst time.
Computes average response time and waiting time.
Presents Gantt Chart for better understanding.
HRRN:

High Response Ratio Next scheduling algorithm.
Utilizes response ratio for process prioritization.
Computes average response time and waiting time.
Displays Gantt Chart for visualization.
RR:

Round Robin scheduling algorithm with user-defined time slice.
Generates Gantt Chart to visualize the execution.
Calculates average response time and waiting time.
Usage
Run the Main.py file to execute and compare the performance of the implemented CPU scheduling algorithms.
Enter the arrival time and burst time details as prompted.
Provide the time slice for Round Robin when prompted.
File Structure
FCFS.py, SJF.py, HRRN.py, and RR.py contain the respective algorithm implementations.
Main.py orchestrates the execution of all algorithms using threads.
Contributing
Feel free to explore, experiment, and contribute to the project! If you have any improvements or new algorithms to add, open an issue or submit a pull request.

License
This project is licensed under the MIT License.
