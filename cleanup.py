testCase = int(input())

def isOddNumber(value):
    return False if value%2==0 else True

def createtaskList(totalNumberOfJobs):
    arr = []
    for i in range(totalNumberOfJobs):
        arr.append(i+1)
    
    return arr

def checKTaskList(TaskList,IndexNoOfAlreadyDoneTasks):
    for i in range(len(IndexNoOfAlreadyDoneTasks)):
        TaskList[IndexNoOfAlreadyDoneTasks[i]-1]=0
    
    return TaskList

def AssignTaskListToAssistant(CheckedTaskList):
    AssistantIndexFlag = 1
    for i in range(len(CheckedTaskList)):
        if(CheckedTaskList[i]<1):
            continue
        else:
            if(isOddNumber(AssistantIndexFlag)):
                CheckedTaskList[i]=-1
            AssistantIndexFlag +=1
    
    return CheckedTaskList

def AssignTaskListToChef(CheckedTaskListAfterAssigningToAssistant):
    for i in range(len(CheckedTaskListAfterAssigningToAssistant)):
        if(CheckedTaskListAfterAssigningToAssistant[i]<1):
            continue
        else:
            CheckedTaskListAfterAssigningToAssistant[i]=-2
    
    return CheckedTaskListAfterAssigningToAssistant

def printResult(FInalTaskList):
    AssistantTasks = []
    ChefTasks = []
    for i in range(len(FinalTaskList)):
        if(FinalTaskList[i]==0):
            continue
        elif(FinalTaskList[i]==-1):
            AssistantTasks.append(i+1)
        elif(FinalTaskList[i]==-2):
            ChefTasks.append(i+1)
    
    print(*AssistantTasks, sep=" ")
    print(*ChefTasks, sep=" ")

            
              

for i in range(testCase):
    totalNumberOfJobsAndNumberOfAlreadyDoneTasks = [int(x) for x in input().split()]
    totalNumberOfJobs = totalNumberOfJobsAndNumberOfAlreadyDoneTasks[0]
    NumberOfAlreadyDoneTasks = totalNumberOfJobsAndNumberOfAlreadyDoneTasks[1]
    TaskList = createtaskList(totalNumberOfJobs)
    IndexNoOfAlreadyDoneTasks = [int(x) for x in input().split()]
    TaskListAfterChecking = checKTaskList(TaskList,IndexNoOfAlreadyDoneTasks)
    TaskListAfterAssigningToAssistant= AssignTaskListToAssistant(TaskListAfterChecking)
    FinalTaskList = AssignTaskListToChef(TaskListAfterAssigningToAssistant)
    printResult(FinalTaskList)
