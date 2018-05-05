class process:
    def __init__(self):
        self.id = 0
        self.arrival_time = 0
        self.burst_time = 0
        self.start_time = 0
        self.finish_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0

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
        
def sortProcessList(processes, n):
    for i  in range(0,n-1):
        for j  in range(i+1,n):
            if processes[j].arrival_time < processes[i].arrival_time:
                processes[j], processes[i] = processes[i], processes[j]
            elif processes[j].arrival_time == processes[i].arrival_time:
                if processes[j].burst_time < processes[i].burst_time:
                    processes[j], processes[i] = processes[i], processes[j]

                    
def allProcessCompleted(bursts, n):
    check = True
    for i in range(n):
        if bursts[i] != 0:
            check = False
    return check        
	
# main code starting here	
allProcesses = []
readyProcesses = []
bursts = []
process_index = 0
avg_waiting_time = 0
avg_turnaround_time = 0
clock = 0


count = int(input("Enter Number of Processes: "))

#taking input from user and inserting in our process array
for index in range(int(count)):
    temp = process()
    temp.arrival_time = int(input("\nEnter Arrival Time: "))
    temp.burst_time = int(input("Enter Burst Time: "))
    temp.id = index
    bursts.append(temp.burst_time)
    allProcesses.append(temp)

#sorting processes on bases of arrival and burst time
sortProcessList(allProcesses,count)

print("\n. = idle\n- = running\nC = completed\n\n")
while allProcessCompleted(bursts, count) == False:
    #new processes
    while process_index < count and allProcesses[process_index].arrival_time == clock:
        readyProcesses.append(allProcesses[process_index])
        process_index = process_index + 1
    
    if not readyProcesses:
        print(". ", end="")
        clock = clock + 1
    elif readyProcesses:
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

