import pexpect
import threading
import timeit
import time
import sys
import random
import argparse
from functools import reduce



# arguments 
parser = argparse.ArgumentParser()
parser.add_argument("-client","--clientsCount")
parser.add_argument("-parallel","--parllel")
args = parser.parse_args()
clientsCount=int(args.clientsCount)

#Generating the port number
port=random.randrange(6000,10000)
#port=6000


def random_messages(i):
    while(True):
        allterminals[i].sendline("sendgroup 1 testmessage")  
def see_the_messages(i):
    while(True):
        print(allterminals[i].readline())


allterminals=[]
threads=[]

#creating all the terminals
allterminals.append(pexpect.spawn("./server",args=[str(port)],use_poll=True))

for i in range(clientsCount):
    allterminals.append(pexpect.spawn("./client",args=[str(i),str(port)],use_poll=True))


creationCommand=reduce((lambda x,y: str(x)+" "+str(y)),range(1,(clientsCount)+1))
allterminals[-1].sendline("creategroup testgrp "+str(clientsCount)+ " "+creationCommand)

#creating parellel threads
if(args.parllel=='1'):
    for i in range(1,len(allterminals)-2):
        x=(threading.Thread(target=random_messages,args=(i,),daemon=True))
        threads.append(x)
        x.start()

'''
y=(threading.Thread(target=observe,args=(-1,)))
threads.append(y)
z=(threading.Thread(target=observe,args=(0,)))
threads.append(z)
#map(lambda x: x.join(), threads)
'''

#y=(threading.Thread(target=observe,args=(-1,)))
#threads.append(y)
#y.start()
start=time.clock()
#start=timeit.timeit()
allterminals[-2].sendline("sendgroup 1 catchmessage")
if(allterminals[-1].expect(['catchmessage'],timeout=120)==0):
    end=time.clock()
    #end=timeit.timeit()
    print("time taken " + str((end-start)*1000)+" ms")
#print("here")

time.sleep(5)
map(lambda x:x._stop() , threads)
map(lambda x:x.close() , allterminals)
sys.exit()