from audioop import reverse
from enum import Enum,unique
import numpy as np
import random

processArray = [None] * 6
processTime = [None] * 6
#Event types for enumeration
@unique
class event_type(Enum):
    Timer_interrupt = 0
    IO_system_call = 1
    Process_exit = 2
    process_1 = 3
    process_2 = 4
    process_3 = 5

#Creating processes with random times
def createProcess(processTime,processArray):  
    for i in range(6):
        rand = event_type(random.randint(0,5))
        rand = rand.value
        processName = getEvent(rand) 
        processArray[i] = processName
        randomTime = random.randint(1,15)
        processTime[i] = randomTime #Assigning random time
    print(f"Processes: {processArray}")
        
#Finding total execution time
def getTotalTime(processTime):
    sum = 0
    for i in range(0,np.size(processTime)):
        sum += processTime[i]
    return sum

#Longest Job First Scheduling Algorithm
def LJF(processTime, sum):
    processCount = np.size(processArray)
    
    while sum != 0:
        i = 0      
        while i < processCount:      
            if processTime[i] == 0:
                print(f"Status: '{processArray[i]}' is finished")
                processCount = processCount - 1
                i = i + 1
                continue
            else:
                print(f"Status: '{processArray[i]}' is running")
                processTime[i] = processTime[i] - 1
                sum = sum - 1
                i = i + 1
        
        print(f"Status: '{processArray[0]}' is finished") #When the last process is finished


#Event messages
def proc_exit():
    return "Exited the process"
def timer_interrupt():
    return "Timer interrupts"
def system_call():
    return "I/O system call"
def process_1():
    return "process_1"
def process_2():
    return "process_2"
def process_3():
    return "process_3"


switcher = {
    0:timer_interrupt,
    1:system_call,
    2:proc_exit,
    3:process_1,
    4:process_2,
    5:process_3 
} 

def getEvent(event):
    return switcher.get(event)()

createProcess(processTime,processArray)
sum = getTotalTime(processTime)

processTime.sort(reverse=True) #To be able to work with LJF, processes should be sorted in descending order
print(f"Execution Times: {processTime}" )
LJF(processTime, sum)
