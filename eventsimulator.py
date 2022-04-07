#skeleton of the project
from enum import Enum,unique

import random
## event types for enumeration
@unique
class event_type(Enum):
    Timer_interrupt = 0
    IO_system_call = 1
    Process_exit = 2

#Event messages
def proc_exit():
    return "Exited the process"
def timer_interrupt():
    return "Timer interrupts"
def system_call():
    return "I/O system call"

def main():
 
    event_count = 5
    event_type_count = 3
    #enum event_type 
    events = [None] * event_count
    eventQueue = [None] * event_count

    for i in range(0,event_count): # Random event creation
        events[i] = random.randint(0,event_type_count - 1)
        eventQueue[i] = event_type(random.randint(0,event_type_count - 1))
    
    switcher = {
        0:timer_interrupt,
        1:system_call,
        2:proc_exit
    } 

    def getEvent(event):
        return switcher.get(event)()
           
    for event in events:
        print("Event Number: ",event)
        print(getEvent(event))


if __name__=="__main__":
    main()