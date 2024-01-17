# Import necessary modules
from threading import Thread, Lock

lock = Lock()
# Set the number of processes
n = 3

# Initialize a dictionary to store process information
d = dict()
print()

# Get user input for process details
for i in range(n):
    key = "P"+str(i+1)
    a = int(input("Enter Arrival Time of Process "+str(i+1)+": "))
    b = int(input("Enter CBT Time of Process "+str(i+1)+": "))
    print()
    l = []
    l.append(a)
    l.append(b)
    d[key] = l

# Get time slice for Round Robin
r = int(input("**Enter your Time Slice**: "))

# Display the input table
c = list(d.items())
print("\nYour Table is as Follows:\n")
print("Process | Arrival | CBT")
for i in range(n):
    print(" ",c[i][0],"   |   ",c[i][1][0],"   | ",c[i][1][1])

# Function to execute First Come First Serve (FCFS) algorithm
def FCFS():
    global d, n

    # Convert dictionary items to a list and sort by arrival time
    d = sorted(d.items(), key=lambda item: item[1][0])

    # Initialize lists to store completion time(ET), response time(RT) and waiting time(WT)
    ET = []
    RT = []
    WT = []

    # Calculate completion time(ET), response time(RT) and waiting time(WT) for each process
    for i in range(n):
        if i == 0:
            ET.append(d[i][1][1] + int(d[i][1][0]))
        else:
            ET.append(ET[i-1] + d[i][1][1])

        RT.append(ET[i] - d[i][1][0])

        if i == 0:
            WT.append(int(d[i][1][0]))
        else:
            WT.append(ET[i-1] - d[i][1][0])

    # Calculate average response time and waiting time
    avg_RT = sum(RT) / n
    avg_WT = sum(WT) / n

    # Format average response time and waiting time to two decimal places
    avg_RT = f"{avg_RT:.2f}"
    avg_WT = f"{avg_WT:.2f}"

    # Add spaces and "|" for Gantt Chart representation
    if d[1][1][0] > d[0][1][1]:
        e = d[1][1][0]
        f = "|"
    else:
        e = " "
        f = " "

    if d[2][1][0] > d[0][1][1] + d[1][1][1] + d[0][1][1]:
        g = d[2][1][0]
        h = "|"
    else:
        g = " "
        h = " "

    if d[0][1][0] + d[0][1][1] >= d[1][1][0]:
        j = d[0][1][0] + d[0][1][1] + d[1][1][1]
    else:
        j = d[1][1][0] + d[1][1][1]

    if j >= d[2][1][0]:
        k = j + d[2][1][1]
    else:
        k = d[2][1][0] + d[2][1][1]

    # Display Gantt Chart and performance metrics for FCFS
    print("\nGantt Chart of First Come First Serve *(FCFS)* CPU Scheduling is as Follows:")
    print("\n|   ", d[0][0], "   |", f, "", d[1][0], "   |", h, "", d[2][0], "   |   ")
    print(d[0][1][0], "        ", d[0][1][0] + d[0][1][1], e, "      ", j, g, "      ", k)
    print("\nAverage Waiting Time of *(FCFS)*: ", avg_WT)
    print("Average Response Time of *(FCFS)*: ", avg_RT, "\n")


# Function to execute Shortest Job First (SJF) algorithm
def SJF():
    global d, n

   # Convert dictionary items to a list and sort by arrival time and burst time
    d = sorted(d, key=lambda item: (item[1][0], item[1][1]))

    # If processes have the same arrival time, sort by their burst time
    if d[1][1][0] <= d[0][1][1] and d[2][1][0] <= d[0][1][1]:
        if d[1][1][1] > d[2][1][1]:
            d[1], d[2] = d[2], d[1]
        else:
            pass

    # Initialize lists to store completion time(ET), response time(RT) and waiting time(WT)
    ET = []
    RT = []
    WT = []

    # Calculate completion time(ET), response time(RT) and waiting time(WT) for each process
    for i in range(n):
        if i == 0:
            ET.append(d[i][1][1] + int(d[i][1][0]))
        else:
            ET.append(ET[i-1] + d[i][1][1])

        RT.append(ET[i] - d[i][1][0])

        if i == 0:
            WT.append(int(d[i][1][0]))
        else:
            WT.append(ET[i-1] - d[i][1][0])

    # Calculate average response time and waiting time
    avg_RT = sum(RT) / n
    avg_WT = sum(WT) / n

    # Format average response time and waiting time to two decimal places
    avg_RT = f"{avg_RT:.2f}"
    avg_WT = f"{avg_WT:.2f}"

    # Add spaces and "|" for Gantt Chart representation
    if d[1][1][0] > d[0][1][1]:
        e = d[1][1][0]
        f = "|"
    else:
        e = " "
        f = " "

    if d[2][1][0] > d[0][1][1] + d[1][1][1] + d[0][1][1]:
        g = d[2][1][0]
        h = "|"
    else:
        g = " "
        h = " "

    if d[0][1][0] + d[0][1][1] >= d[1][1][0]:
        j = d[0][1][0] + d[0][1][1] + d[1][1][1]
    else:
        j = d[1][1][0] + d[1][1][1]

    if j >= d[2][1][0]:
        k = j + d[2][1][1]
    else:
        k = d[2][1][0] + d[2][1][1]

    # Display Gantt Chart and performance metrics for SJF
    print("\nGantt Chart of Shortest Job First *(SJF)* CPU Scheduling is as Follows:")
    print("\n|   ", d[0][0], "   |", f, "", d[1][0], "   |", h, "", d[2][0], "   |   ")
    print(d[0][1][0], "        ", d[0][1][0] + d[0][1][1], e, "      ", j, g, "      ", k)
    print("\nAverage Waiting Time of *(SJF)*: ", avg_WT)
    print("Average Response Time of *(SJF)*: ", avg_RT, "\n")


# Function to execute High Response Ratio Next (HRRN) algorithm
def HRRN():
    global d, n

    # Convert dictionary items to a list and sort by arrival time
    d = sorted(d, key=lambda item: (item[1][1]), reverse = True)

    # If processes have the same arrival time, sort by their burst time
    if d[0][1][0] == d[1][1][0] == d[2][1][0]:
        d = sorted(d, key=lambda item: (item[1][1]), reverse=True)

    # Calculate ratio of remaining processes
    ratio = []
    for i in range(n):
        if i == 0:
            d = sorted(d, key=lambda item: (item[1][0]))
            for j in range(i + 1, n):
                if d[i][1][0] == d[j][1][1]:
                    if d[i][1][1] > d[j][1][1]:
                        d[i], d[j] = d[j], d[i]
                    else:
                        continue
                else:
                    continue
        else:
            response_ratio = (((d[0][1][1] + d[0][1][0]) - d[i][1][0]) + d[i][1][1]) / d[i][1][1]
            ratio.append(response_ratio)

    if ratio[1] > ratio[0]:
        d[1], d[2] = d[2], d[1]
    else:
        pass

    # Initialize lists to store completion time(ET), response time(RT) and waiting time(WT)
    ET = []
    RT = []
    WT = []

    # Calculate completion time(ET), response time(RT) and waiting time(WT) for each process
    for i in range(n):
        if i == 0:
            ET.append(d[i][1][1] + int(d[i][1][0]))
        else:
            ET.append(ET[i - 1] + d[i][1][1])

        RT.append(ET[i] - d[i][1][0])

        if i == 0:
            WT.append(int(d[i][1][0]))
        else:
            WT.append(ET[i - 1] - d[i][1][0])

    # Calculate average response time and waiting time
    avg_RT = sum(RT) / n
    avg_WT = sum(WT) / n

    # Format average response time and waiting time to two decimal places
    avg_RT = f"{avg_RT:.2f}"
    avg_WT = f"{avg_WT:.2f}"

    # Add spaces and "|" for Gantt Chart representation
    if d[1][1][0] > d[0][1][1]:
        e = d[1][1][0]
        f = "|"
    else:
        e = " "
        f = " "

    if d[2][1][0] > d[0][1][1] + d[1][1][1] + d[0][1][1]:
        g = d[2][1][0]
        h = "|"
    else:
        g = " "
        h = " "

    if d[0][1][0] + d[0][1][1] >= d[1][1][0]:
        j = d[0][1][0] + d[0][1][1] + d[1][1][1]
    else:
        j = d[1][1][0] + d[1][1][1]

    if j >= d[2][1][0]:
        k = j + d[2][1][1]
    else:
        k = d[2][1][0] + d[2][1][1]

    # Display Gantt Chart and performance metrics for HRRN
    print("\nGantt Chart of High Response Ratio Next *(HRRN)* CPU Scheduling is as Follows:")
    print("\n|   ", d[0][0], "   |", f, "", d[1][0], "   |", h, "", d[2][0], "   |   ")
    print(d[0][1][0], "        ", d[0][1][0] + d[0][1][1], e, "      ", j, g, "      ", k)
    print("\nAverage Waiting Time of *(HRRN)*: ", avg_WT)
    print("Average Response Time of *(HRRN)*: ", avg_RT, "\n")

# Function to execute Round Robin (RR) algorithm
def RR():
    global d, n, r

    # Convert dictionary items to a list and sort by arrival time
    d = sorted(d, key=lambda item: item[1][0])

    # Round Robin scheduling algorithm
    Time = []
    Operations = []
    i = j = 0
    while d[0][1][1] + d[1][1][1] + d[2][1][1] != 0:
        for i in range(n):
            if i == 0 and j==0:
                Time.append(d[0][1][0])
                Time.append(d[0][1][0] + r)
                Operations.append(d[i][0])
                d[0][1][1] = d[0][1][1] - r
            
            else:
                Time.append(Time[(((3*j)+i)-1)+1] + r if d[i][1][1] >= r  else Time[(((3*j)+i)-1)+1] + d[i][1][1])
                Operations.append(d[i][0] if d[i][1][1] > 0 else 0)
                d[i][1][1] = d[i][1][1] - r if d[i][1][1] > r  else 0
        j += 1

    # Remove duplicate time values
    New_Time = []
    for i in range(len(Time) - 1):
        if Time[i] != Time[i + 1]:
            New_Time.append(Time[i])

    # Append the last element (since it doesn't have a next element to compare)
    New_Time.append(Time[-1])

    New_Operations = []
    for i in range(len(Operations)):
        if Operations[i] != 0:
            New_Operations.append(Operations[i])
        else:
            pass
    
    # Remove the last two duplicate operations
    for i in range (n-1):
        if New_Operations[-1] == New_Operations[-2]:
            del New_Operations[-2]
            del New_Time[-2]
        else:
            break

    # Initialize lists to store completion time(ET), response time(RT) and waiting time(WT) and their operations
    ET = []
    ET_Operations = []
    RT = []
    RT_Operations = []
    WT = []
    WT_Operations = []
    k = 0

    # Calculate completion time(ET), response time(RT) and waiting time(WT) for each process
    for i in range(len(New_Operations)):
        if (i==0):
            k = New_Time[i+1]
            for j in range(i + 1, len(New_Operations)):
                if New_Operations[i] == New_Operations[j]:
                    k = k + New_Time[j+1]
                    ET_Operations.append(New_Operations[i])
                else:
                    pass
            ET.append(k)
            k = 0

        else:
            if New_Operations[i] not in ET_Operations:
                k = New_Time[i+1]
                ET_Operations.append(New_Operations[i])
                for j in range(i + 1, len(New_Operations)):
                    if New_Operations[i] == New_Operations[j]:
                        k = k + New_Time[j+1]
                    else:
                        ET_Operations.append(New_Operations[i])
                ET.append(k)
                k = 0
            else:
                pass

    for i in range(len(New_Operations)):
        if New_Operations[i] not in RT_Operations:
                RT_Operations.append(New_Operations[i])
                k = New_Time[i+1] - d[i][1][0]
                for j in range(i + 1, len(New_Operations)):
                    if New_Operations[i] == New_Operations[j]:
                        k = New_Time[j+1] - d[i][1][0]
                    else:
                        pass
                RT.append(k)
                k = 0
        else:
            pass

    for i in range(len(New_Operations)):
        if New_Operations[i] not in WT_Operations:
                WT_Operations.append(New_Operations[i])
                k = New_Time[i] - d[i][1][0]
                for j in range(i + 1, len(New_Operations)):
                    if New_Operations[i] == New_Operations[j]:
                        k = k + (New_Time[j] - New_Time[i+1])
                        for l in range(j + 1, len(New_Operations)):
                            if New_Operations[j] == New_Operations[l]:
                                k = k + (New_Time[l] - New_Time[j+1])
                                break
                            else:
                                pass
                        break
                    else:
                        pass
                WT.append(k)
                k = 0
        else:
            pass
    
    # Calculate average response time and waiting time
    avg_RT = 0
    for i in RT:
        avg_RT += i
    avg_RT = (avg_RT/n)
    
    avg_WT = 0
    for i in WT:
        avg_WT += i
    avg_WT = (avg_WT/n)

    # Format average response time and waiting time to two decimal places
    avg_RT = f"{avg_RT:.2f}"
    avg_WT = f"{avg_WT:.2f}"

    # Display Gantt Chart and performance metrics for HRRN
    print("\nGaant Chart of Round Robin *(RR)* CPU Scheduling is as Follows:\n")
    for i in range(len(New_Operations)):
        print("|   ", New_Operations[i], "   ", end="")

    # Add a newline at the end to separate from the next line of output
    print()

    for i in range(len(New_Time)):
        print(New_Time[i], "        ", end=" ")

    # Add a newline at the end to separate from the next line of output
    print()

    print("\nAverage Waiting Time of *(RR)*: ",avg_WT)
    print("Average Response Time of *(RR)*: ",avg_RT,"\n")

# Define a function for executing the algorithms(using lock for getting proper form of gantt chart is necessary)
def execution(function, lock):
    lock.acquire()
    function()
    lock.release()

# Create threads for each algorithm
Threads = [
    Thread(target=execution, args=(FCFS, lock)),
    Thread(target=execution, args=(SJF, lock)),
    Thread(target=execution, args=(HRRN, lock)),
    Thread(target=execution, args=(RR, lock))
]

# Start the threads and join them together for executing in the same time
for thread in Threads:
    thread.start()

for thread in Threads:
    thread.join()
