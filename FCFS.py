class process:
    p_no = 0
    arrival_time = 0
    burst_time = 0
    start_time = 0
    end_time = 0
	
#array to hold processes
processes = []

waiting_time = 0
turnaround_time = 0
idle_time = 0;

count = int(input("Enter Number of Processes: "))

#taking input from user and inserting in our process array
for index in range(int(count)):
    temp = process()
    temp.arrival_time = int(input("\nEnter Arrival Time for Process: "))
    temp.burst_time = int(input("Enter Burst Time for Process: "))
    temp.p_no = index
    processes.append(temp)


#sorting remaining processes on bases of arrival time
for i  in range(0,int(count)-1):
    for j  in range(i+1,int(count)):
    	if processes[j].arrival_time<processes[i].arrival_time:
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
    processes[index].start_time = (processes[index-1].start_time + processes[index-1].burst_time) + idle_time
    processes[index].end_time = processes[index].start_time + processes[index].burst_time


#diplaying each process info plus calcutilang  average waiting time and turnaround time
for index in range(count):
    print ('\nProcess', processes[index].p_no)
    print ('Arrived at:', processes[index].arrival_time)
    print ('Started at:', processes[index].start_time)
    print ('Ended at:', processes[index].end_time)
    waiting_time = waiting_time + (processes[index].start_time - processes[index].arrival_time)
    turnaround_time = turnaround_time + (processes[index].end_time - processes[index].arrival_time)

waiting_time = float(float(waiting_time) / float(count))	
turnaround_time = float(float(turnaround_time) / float(count))	


print ('\n\nAverage waiting time: ', waiting_time)
print ('Average turnaround time: ', turnaround_time)
