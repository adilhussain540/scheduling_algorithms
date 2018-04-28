class Process:
    def __init__(self):
        self.id = 0
        self.arrival_time = 0
        self.burst_time = 0
        self.start_time = 0
        self.end_time = 0
    
    def display(self):
        print("\nProcess ID: ", self.id)
        print("Arrival Time: ", self.arrival_time)
        print("Burst Time: ", self.burst_time)
        print("Start Time: ", self.start_time)
        print("End Time: ", self.end_time)
                                     
def displayProcessList(processes, n):
    for i in range(n):
        processes[i].display()
    
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

count = int(input("Enter number of processes: "))

for i in range(count):
    temp = Process()
    temp.arrival_time = int(input("\nEnter Arrival Time for Process: "))
    temp.burst_time = int(input("Enter Burst Time for Process: "))
    temp.id = i
    bursts.append(temp.burst_time)
    allProcesses.append(temp)
 
sortProcessList(allProcesses,count,"arrival")

while allProcessCompleted(bursts, count) == False:
    while process_index < count and allProcesses[process_index].arrival_time == clock:
        readyProcesses.append(allProcesses[process_index])
        process_index = process_index + 1   
    if readyProcesses:
        sortProcessList(readyProcesses,len(readyProcesses),"burst")
        if readyProcesses[0].burst_time == bursts[readyProcesses[0].id]:
            for i in range(count):
                if readyProcesses[0].id == allProcesses[i].id:
                    allProcesses[i].start_time = clock                            
        bursts[readyProcesses[0].id] = bursts[readyProcesses[0].id] - 1                    
        if bursts[readyProcesses[0].id] == 0:
            for i in range(count):
                if readyProcesses[0].id == allProcesses[i].id:
                    allProcesses[i].end_time = clock + 1
            readyProcesses.pop(0)                
    clock = clock + 1
        
displayProcessList(allProcesses,count)    