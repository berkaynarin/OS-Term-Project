import datetime
import random

eventType = [["Timer Interrupt", "5"], ["System Call", "1"], ["Memory Operation", "2"], ["I/O Operation", "8"], ["Application Call", "4"]] 
eventQueue = []

def dequeue(queue):
	displayMessage(queue[0][0], queue[0][1])
	queue.pop(0)

def displayMessage(event, time):
    print(f"The event {event} has executed in {time} seconds at {datetime.datetime.now()}")
    f = open("log.txt", "a")
    f.write(f"The event {event} has executed in {time} seconds at {datetime.datetime.now()} \n")
    f.close() 

def createEvent():
	for i in range(0, 5):
		eventQueue.append(eventType[random.randint(0, 4)]) #Type of the event
	

createEvent()

for i in range(0, 5):
	dequeue(eventQueue)


