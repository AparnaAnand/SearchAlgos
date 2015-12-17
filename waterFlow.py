import re
import sys

from collections import namedtuple
from collections import deque
                
Pipe = namedtuple("Pipe", ['start', 'end', 'length', 'offPeriods'])
Node = namedtuple("Node", ['id','state','parent','depth','cost'])
pipes = []
readInput=open(str(sys.argv[2]),'r').readlines()
#readInput=open("gradingTestCases.txt",'r').readlines()
writeOutput = open('output.txt', 'w')
p = re.compile('(.*)')
for i in range(len(readInput)):
    m=p.match(readInput[i])
    readInput[i]=m.group();
testCaseNum=int(readInput[0])
inputIndex=1
for each in range(testCaseNum):
    pipes=[]
    algoType=readInput[inputIndex]
    inputIndex+=1
    source=readInput[inputIndex]
    inputIndex+=1
    destinations=readInput[inputIndex].split(' ')
    inputIndex+=1
    middles=readInput[inputIndex].split(' ')
    inputIndex+=1
    pipeNum=int(readInput[inputIndex])
    for eachPipe in range(pipeNum):
        inputIndex+=1
        m=re.search('^(\w+?)\s(\w+?)\s(\d+?)\s(\d+?)', readInput[inputIndex])
        st=m.group(1)
        en=m.group(2)
        if algoType=='BFS' or algoType=='DFS':
            l=1
            offNum=0
        else:
            l=int(m.group(3))
            offNum=int(m.group(4))
        pos=0
        offPer=[]
        for eachOff in range(offNum):
            m=re.search('(\d*)-(\d*)',readInput[inputIndex][pos:])
            off1=int(m.group(1))
            off2=int(m.group(2))
            while off1<=off2:
                if off1 not in offPer:
                    offPer.append(off1)
                off1+=1
            pos+=m.end()
        offPer.sort()
        pipes.append(Pipe(st,en,l,offPer))
    inputIndex+=1
    time=int(readInput[inputIndex])
    inputIndex+=2
    openQueue=[]
    idnum=1
    openQueue.append(Node(idnum,source,None,0,time))
    openSt=[]
    openSt.append(source)
    closeSt=[]
    closeQueue=[]
    flag=0
    currTime=0
    while True:
        if not openQueue:
            writeOutput.write("None\n")
            break
        currnode=openQueue.pop(0)
        currSt=openSt.pop(0)
        currTime=currnode.cost%24
        if algoType!='BFS':
            for eachDest in destinations:
                if currSt==eachDest:
                    opVal=str(currSt+" "+str(currTime)+"\n")
                    writeOutput.write(opVal)
                    flag=1
                    break
        if flag==1:
            break
        closeQueue.append(currnode)
        closeSt.append(currSt)
        children=[]
        childLength=[]
        for eachPipe in pipes:
            if eachPipe.start==currSt and (currTime not in eachPipe.offPeriods):
                children.append(eachPipe.end)
                childLength.append(eachPipe.length)
        if algoType=='BFS':
            children.sort()
            for eachChild in children:
                if eachChild not in openSt and eachChild not in closeSt:
                    for eachDest in destinations:
                        if eachChild==eachDest:
                            opVal=str(eachChild+" "+str((currnode.cost+1)%24)+"\n")
                            writeOutput.write(opVal)
                            flag=1
                            break
                    if flag==1:
                        break
                    idnum+=1
                    openQueue.append(Node(idnum,eachChild,currnode.id,currnode.depth+1,currnode.cost+1))
                    openSt.append(eachChild)
            if flag==1:
                break
        elif algoType=='DFS':
            children.sort(reverse=True)
            for eachChild in children:
                if eachChild not in closeSt:
                    idnum+=1
                    openQueue.insert(0,Node(idnum,eachChild,currnode.id,currnode.depth+1,currnode.cost+1))
                    openSt.insert(0,eachChild)
        else:
            for ind in range(len(children)):
                idnum+=1
                if children[ind] not in openSt and children[ind] not in closeSt:
                    openQueue.append(Node(idnum,children[ind],currnode.id,currnode.depth+1,currnode.cost+childLength[ind]))
                    openSt.append(children[ind])
                elif children[ind] in openSt:
                    CI=openSt.index(children[ind])
                    if openQueue[CI].cost>(currnode.cost+childLength[ind]):
                        openQueue.pop(CI)
                        openSt.pop(CI)
                        openQueue.append(Node(idnum,children[ind],currnode.id,currnode.depth+1,currnode.cost+childLength[ind]))
                        openSt.append(children[ind])
        if algoType=='UCS':
            for i in range(1, len(openQueue)):
                j = i
                while j > 0 and openQueue[j].cost < openQueue[j-1].cost:
                    openQueue[j], openQueue[j-1] = openQueue[j-1], openQueue[j]
                    openSt[j], openSt[j-1] = openSt[j-1], openSt[j]
                    j-=1
            i=0
            while i < len(openQueue)-1:
                beg=i
                size=0
                while i<len(openQueue)-1 and openQueue[i].cost==openQueue[i+1].cost:
                    size+=1
                    i+=1
                last=beg+size
                for k in range(beg+1,last+1):
                    j = k
                    while j > beg and openQueue[j].state < openQueue[j-1].state:
                        openQueue[j], openQueue[j-1] = openQueue[j-1], openQueue[j]
                        openSt[j], openSt[j-1] = openSt[j-1], openSt[j]
                        j-=1
                i=last+1
writeOutput.close()
