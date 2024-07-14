# Set the number of processes
n = 3

# Initialize a dictionary to store process information
d = dict()
print()

# Get user input for process details
for i in range(n):
    key = "P" + str(i + 1)
    a = int(input("Enter arrival time of process " + str(i + 1) + ": "))
    b = int(input("Enter CBT time of process " + str(i + 1) + ": "))
    print()
    l = [a, b]
    d[key] = l

# Convert dictionary items to a list and sort by arrival time and burst time
c = list(d.items())
d = sorted(d.items(), key=lambda item: (item[1][0], item[1][1]))

# Display the input table
print("\nYour Table is as Follows:\n")
print("Process | Arrival | CBT")
for i in range(n):
    print(" ", c[i][0], "   |   ", c[i][1][0], "   | ", c[i][1][1])

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
