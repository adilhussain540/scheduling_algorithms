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
        self.io_burst = 0
    
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

def processFinishedWaiting(returnTimes, n, clock):
    index = -1
    for i in range(n):
        if returnTimes[i] == clock:
            index = i
    return index        


# main code starting here
allProcesses = []
bursts = []
readyProcesses = []
waitingProcesses = []
returnTimeFromIO = []
clock = 0
process_index = 0
avg_waiting_time = 0
avg_turnaround_time = 0

count = int(input("Enter number of processes: "))
time_quantum = int(input("Enter time quantum: "))
io_bound = input("Which process must go for IO(even or odd): ")
io_after = 2

for i in range(count):
    temp = Process()
    temp.arrival_time = int(input("\nEnter Arrival Time: "))
    temp.burst_time = int(input("Enter Burst Time: "))
    if io_bound == "even":
        if i%2 == 0:
            temp.io_burst = int(input("Enter IO Burst: "))
    elif io_bound == "odd":
        if i%2 != 0:
            temp.io_burst = int(input("Enter IO Burst: "))
    temp.id = i
    bursts.append(temp.burst_time)
    allProcesses.append(temp)
 
sortProcessList(allProcesses,count,"arrival")

print("\n. = idle\n- = running\nC = completed\nNC = swapped out\nIO = waiting for input/output\n")
while allProcessCompleted(bursts, count) == False:
    while process_index < count and allProcesses[process_index].arrival_time == clock:
        allProcesses[process_index].time_quantum = time_quantum
        readyProcesses.append(allProcesses[process_index])
        process_index = process_index + 1
        
    if waitingProcesses:
        while processFinishedWaiting(returnTimeFromIO, len(returnTimeFromIO), clock) != -1:
            index = processFinishedWaiting(returnTimeFromIO, len(returnTimeFromIO), clock)
            readyProcesses.append(waitingProcesses.pop(index))
            returnTimeFromIO.pop(index)
    
    if not readyProcesses:
        print(". ", end="")
    elif readyProcesses:
        if readyProcesses[0].burst_time == bursts[readyProcesses[0].id]:
            for i in range(count):
                if readyProcesses[0].id == allProcesses[i].id:
                    allProcesses[i].start_time = clock
                    
        readyProcesses[0].time_quantum = readyProcesses[0].time_quantum - 1
        bursts[readyProcesses[0].id] = bursts[readyProcesses[0].id] - 1
        #ensuring no execution symbol if current process is going for IO
        #if readyProcesses[0].start_time != clock - io_after:
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
    
    if readyProcesses and readyProcesses[0].io_burst != 0:
            if readyProcesses[0].time_quantum % io_after == 0:
                temp = readyProcesses.pop(0)
                waitingProcesses.append(temp)
                returnTimeFromIO.append(clock + temp.io_burst)
                print("P",temp.id,"(IO)", end="", sep="")
    
    
print("\n\n")
avg_waiting_time = float(avg_waiting_time)/float(count)
avg_turnaround_time = float(avg_turnaround_time)/float(count)
displayProcessList(allProcesses,count)

print("\nAverage Waiting Time : ", avg_waiting_time)
print("Average Turnaround Time : ", avg_turnaround_time)


