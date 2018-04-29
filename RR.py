class Process:
    def __init__(self):
        self.id = 0
        self.arrival_time = 0
        self.burst_time = 0
        self.start_time = 0
        self.finish_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0
        self.time_quantum = 0
    
    def display(self):
        print(self.id, end=" "*20)
        print(self.arrival_time, end=" "*20)
        print(self.start_time, end=" "*15)
        print(self.finish_time, end=" "*15)
        print(self.waiting_time, end=" "*20)
        print(self.turnaround_time, end="")
                                     
def displayProcessList(processes, n):
    print("Process ID   |   Arrival Time   |   Start Time   |   Finish Time   |   Waiting Time   |   Turnaround Time")
    for i in range(n):
        processes[i].display()
        print()
    
def sortProcessList(processes, n, basis):
    for i  in range(0,n-1):
        for j  in range(i+1,n):
            if basis == "arrival":
                if processes[j].arrival_time<processes[i].arrival_time:
                    processes[j], processes[i] = processes[i], processes[j]
            elif basis == "burst":
                if processes[j].burst_time<processes[i].burst_time:
                    processes[j], processes[i] = processes[i], processes[j]
                    
def allProcessCompleted(bursts, n):
    check = True
    for i in range(n):
        if bursts[i] != 0:
            check = False
    return check


# main code starting here
allProcesses = []
bursts = []
readyProcesses = []
clock = 0
process_index = 0
avg_waiting_time = 0
avg_turnaround_time = 0

count = int(input("Enter number of processes: "))
time_quantum = int(input("Enter time quantum: "))

for i in range(count):
    temp = Process()
    temp.arrival_time = int(input("\nEnter Arrival Time for Process: "))
    temp.burst_time = int(input("Enter Burst Time for Process: "))
    temp.id = i
    bursts.append(temp.burst_time)
    allProcesses.append(temp)
 
sortProcessList(allProcesses,count,"arrival")

print("\n. = idle\n- = running\nC = completed\nNC = swapped out\n")
while allProcessCompleted(bursts, count) == False:
    while process_index < count and allProcesses[process_index].arrival_time == clock:
        allProcesses[process_index].time_quantum = time_quantum
        readyProcesses.append(allProcesses[process_index])
        process_index = process_index + 1
    if not readyProcesses:
        print(". ", end="")
    elif readyProcesses:
        if readyProcesses[0].burst_time == bursts[readyProcesses[0].id]:
            for i in range(count):
                if readyProcesses[0].id == allProcesses[i].id:
                    allProcesses[i].start_time = clock
        readyProcesses[0].time_quantum = readyProcesses[0].time_quantum - 1
        bursts[readyProcesses[0].id] = bursts[readyProcesses[0].id] - 1
        print("- ", end="")
        if bursts[readyProcesses[0].id] == 0:
            for i in range(count):
                if readyProcesses[0].id == allProcesses[i].id:
                    allProcesses[i].finish_time = clock + 1
                    allProcesses[i].waiting_time = allProcesses[i].finish_time - allProcesses[i].arrival_time - allProcesses[i].burst_time
                    allProcesses[i].turnaround_time = allProcesses[i].finish_time - allProcesses[i].arrival_time
                    avg_waiting_time = avg_waiting_time + allProcesses[i].waiting_time
                    avg_turnaround_time = avg_turnaround_time + allProcesses[i].turnaround_time
            print("P",readyProcesses[0].id,"(C)", end="", sep="")
            readyProcesses.pop(0)                
        elif readyProcesses[0].time_quantum == 0 and bursts[readyProcesses[0].id] != 0:
            temp = readyProcesses.pop(0)
            temp.time_quantum = time_quantum
            print("P",temp.id,"(NC)", end="", sep="")
            readyProcesses.append(temp)
    clock = clock + 1
print("\n\n")
avg_waiting_time = float(avg_waiting_time)/float(count)
avg_turnaround_time = float(avg_turnaround_time)/float(count)
displayProcessList(allProcesses,count)

print("\nAverage Waiting Time : ", avg_waiting_time)
print("Average Turnaround Time : ", avg_turnaround_time)

