class process:
    def __init__(self):
        self.id = 0
        self.arrival_time = 0
        self.burst_time = 0
        self.start_time = 0
        self.finish_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0
        self.belongs_to = 0

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
                if processes[j].arrival_time < processes[i].arrival_time:
                    processes[j], processes[i] = processes[i], processes[j]
            elif basis == "queue":
                if processes[j].belongs_to < processes[i].belongs_to:
                    processes[j], processes[i] = processes[i], processes[j]
            
def allProcessCompleted(bursts):
    check = True
    for i in range(len(bursts)):
        if bursts[i] != 0:
            check = False       
    return check        
	
	
# main code starting here
allProcesses = []
readyProcesses = []
bursts = []
process_index = 0
index_1 = 0
index_2 = 0
index_3 = 0
avg_waiting_time = 0
avg_turnaround_time = 0
clock = 0


count = int(input("Enter Number of Processes: "))

# all three logical queues are FCFS (belongs_to variable helps in logical division)
# division is on basis of burst time
# processes with burst time between 1-3 will be queue_1, 4-6 in queue_2 and 7-9 in queue_3
# priorty of queues is queue_1 > queue_2 > queue_3

for index in range(int(count)):
    temp = process()
    temp.arrival_time = int(input("\nEnter Arrival Time: "))
    temp.burst_time = int(input("Enter Burst Time: "))
    temp.id = index
    if temp.burst_time < 4:
        temp.belongs_to = 1;
    elif temp.burst_time < 7 and temp.burst_time > 3:
        temp.belongs_to = 2;
    elif temp.burst_time < 10 and temp.burst_time > 6:
        temp.belongs_to = 3;
    
    bursts.append(temp.burst_time)
    allProcesses.append(temp)

#sorting processes on bases of arrival time
sortProcessList(allProcesses, count, "arrival")


print("\n. = idle\n- = running\nC = completed\n\n")
while allProcessCompleted(bursts) == False:
    # new processes
    while process_index < count and allProcesses[process_index].arrival_time == clock:
        readyProcesses.append(allProcesses[process_index])
        process_index = process_index + 1
    
    if not readyProcesses:
        print(". ", end="")
        clock = clock + 1
    elif readyProcesses:
        #sorting on basis of queues priorty
        sortProcessList(readyProcesses, len(readyProcesses), "queue")
        
        #processes started execution
        if readyProcesses[0].burst_time == bursts[readyProcesses[0].id]:
            for i in range(count):
                if readyProcesses[0].id == allProcesses[i].id:
                    allProcesses[i].start_time = clock
                    
        bursts[readyProcesses[0].id] = bursts[readyProcesses[0].id] - 1
        clock = clock + 1
        print("- ", end="")
        
        #processes completed execution
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
      
    
print("\n\n")
avg_waiting_time = float(avg_waiting_time)/float(count)
avg_turnaround_time = float(avg_turnaround_time)/float(count)
displayProcessList(allProcesses,count)

print("\nAverage Waiting Time : ", avg_waiting_time)
print("Average Turnaround Time : ", avg_turnaround_time)
