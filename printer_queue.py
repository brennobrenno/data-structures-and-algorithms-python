from queue import Queue
import random


class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self, newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60/self.pagerate


class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp


def simulation(numSeconds, pagesPerMinute):

    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waiting_times = []

    for currentSecond in range(numSeconds):

      if newPrintTask():
         task = Task(currentSecond)
         printQueue.enqueue(task)

      if (not labprinter.busy()) and (not printQueue.isEmpty()):
        next_task = printQueue.dequeue()
        waiting_times.append(next_task.waitTime(currentSecond))
        labprinter.startNext(next_task)

      labprinter.tick()

    averageWait = sum(waiting_times)/len(waiting_times)
    print("Average Wait %6.2f secs %3d tasks remaining." % (averageWait, printQueue.size()))


def newPrintTask():
    num = random.randrange(1, 181)
    return num == 180


for i in range(10):
    simulation(3600, 10)
