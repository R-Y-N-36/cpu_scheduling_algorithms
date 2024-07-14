# Set the number of processes
n = 3

# Initialize a dictionary to store process information
d = dict()
print()

# Get user input for process details
for i in range(n):
    key = "P"+str(i+1)
    a = int(input("Enter arrival time of process "+str(i+1)+": "))
    b = int(input("Enter CBT time of process "+str(i+1)+": "))
    print()
    l = [a, b]
    d[key] = l

# Get time slice for Round Robin
r = int(input("**Enter your Time Slice**: "))

# Convert dictionary items to a list and sort by arrival time
c = list(d.items())
d = sorted(d.items(), key=lambda item: item[1][0])

# Display the input table
print("\nYour Table is as Follows:\n")
print("Process | Arrival | CBT")
for i in range(n):
    print(" ",c[i][0],"   |   ",c[i][1][0],"   | ",c[i][1][1])

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