class process:
    p_no = 0
    arrival_time = 0
    burst_time = 0
    start_time = 0
    end_time = 0
    priorty = 0
	
#array to hold processes
processes = []

avg_waiting_time = 0
avg_turnaround_time = 0
idle_time = 0;

count = int(input("Enter Number of Processes: "))

#taking input from user and inserting in our process array
for index in range(int(count)):
    temp = process()
    temp.arrival_time = int(input("\nEnter Arrival Time of Process: "))
    temp.burst_time = int(input("Enter Burst Time of Process: ",))
    temp.priorty = int(input("Enter Priorty of Process: ",))
    temp.p_no = index+1
    processes.append(temp)

#now we have to select 1st process and in Priorty Scheduling 1st process is on basis of FCFS and priorty
#let 1st process is at starting index
first_procoess_arrival = processes[0].arrival_time
first_process_index = 0

#now comparing 1st process with remaining processes on the basis of arrival time and priorty
for i in range(1,int(count)):
    if processes[i].arrival_time<first_procoess_arrival:
        first_process_arrival = processes[i].arrival_time
        first_process_index = i
#if arrival time is equal, compare on the basis of priorty
    elif processes[i].arrival_time==first_procoess_arrival:
            if processes[i].priorty < processes[first_process_index].priorty:
                first_process_arrival = processes[i].arrival_time
                first_process_index = i

#placing best suitable 1st process at starting index			
processes[first_process_index], processes[0] = processes[0], processes[first_process_index]

#sorting remaining processes on bases of priorty
for i in range(1,int(count)-1):
    for j  in range(i+1,int(count)):
        if processes[j].arrival_time<processes[i].arrival_time:
            processes[j], processes[i] = processes[i], processes[j]
        elif processes[j].arrival_time==processes[i].arrival_time:
            if processes[j].priorty<processes[i].priorty:
                processes[j], processes[i] = processes[i], processes[j]    

#we already know start time and end time of our 1st process
processes[0].start_time = processes[0].arrival_time
processes[0].end_time =  processes[0].burst_time + processes[0].arrival_time

#calculating start time and end time of remaining processes
for index in range(1,int(count)):
    if processes[index].arrival_time > processes[index-1].arrival_time:
        idle_time = processes[index].arrival_time - processes[index-1].end_time
        if idle_time < 0:
            idle_time = 0
    else:
        idle_time = 0
    processes[index].start_time = processes[index-1].start_time + processes[index-1].burst_time + + idle_time
    processes[index].end_time = processes[index].start_time + processes[index].burst_time


#diplaying each process info plus calculating  average waiting time and turnaround time
for index in range(count):
    print ('\nProcess', processes[index].p_no)
    print ('Arrived at:', processes[index].arrival_time)
    print ('Started at:', processes[index].start_time)
    print ('Ended at:', processes[index].end_time)
    avg_waiting_time = avg_waiting_time + (processes[index].start_time - processes[index].arrival_time)
    avg_turnaround_time = avg_turnaround_time + (processes[index].end_time - processes[index].arrival_time)

avg_waiting_time = float(float(avg_waiting_time) / float(count))	
avg_turnaround_time = float(float(avg_turnaround_time) / float(count))	


print ('\n\nAverage waiting time: ', avg_waiting_time)
print ('Average turnaround time: ', avg_turnaround_time)
	
	

