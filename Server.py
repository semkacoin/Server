
# coding: utf-8

# In[ ]:


# 我看见你了
# 走开


# In[1]:


import DataModule
import time
import csv
import os
timerequest = 600
DataFileCsv = 'data/checkpoints.csv'
def CHECK_DATA():
    DataPath = os.path.exists(DataFileCsv)
    if DataPath:
        print(' ')
    else:
        print(' ')
    return DataPath
def GET_LAST_CHECKPOINT():
    with open(DataFileCsv, 'r') as fp:
        reader = csv.reader(fp)
        data_read = [row for row in reader]
    last_checkpoint_list_unit = str(data_read[len(data_read)-1])
    last_checkpoint= int(last_checkpoint_list_unit[2:-2])
    return last_checkpoint
def DATA_MEGERING(current_time, last_checkpoint):
    CheckpointMegering = current_time - last_checkpoint
    print(' '+str(CheckpointMegering))
    return CheckpointMegering
def CURRENT_TIME():
    current_time=int(time.time())
    return current_time
def ADD_DATA(checkpoint_csv):
    current_checkpoint=[CURRENT_TIME()]
    with open(checkpoint_csv, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(current_checkpoint)
        print(' ')
    MainDataFile = open('data/'+str(CURRENT_TIME())+'.txt','w')
    MainDataFile.write(str(DataModule.GETCOIN()))
    MainDataFile.close()
    CHECK_TIMER(timerequest)
def CHECK_TIMER(timertime):
    timer_time = timertime
    current_time=0
    while (current_time - GET_LAST_CHECKPOINT()) < timerequest :
        current_time=CURRENT_TIME()
        print('.', end='')
        time.sleep(1)
    ADD_DATA(DataFileCsv)
if CHECK_DATA():
    if GET_LAST_CHECKPOINT() > 0:
        if DATA_MEGERING(CURRENT_TIME(),GET_LAST_CHECKPOINT()) < timerequest:
            print(' ')
            CHECK_TIMER(DATA_MEGERING(CURRENT_TIME(),GET_LAST_CHECKPOINT()))
            print(' ')
        else: 
            print(' ')
            ADD_DATA(DataFileCsv)
    if GET_LAST_CHECKPOINT() <= 0:
        print(' ')
        ADD_DATA(DataFileCsv)
else:
    print(' ')
ADD_DATA(DataFileCsv)
getcheckpoint = int(time.time())
get_checkpoint_csv = "data/checkpoints.csv"
def ADD_DATA(checkpoint, checkpoint_csv):
    current_checkpoint=[checkpoint]
    with open(checkpoint_csv, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(current_checkpoint)
ADD_DATA(getcheckpoint,get_checkpoint_csv)    
def CHECK_TIMER(timertime):
    last_checkpoint=int(time.time())
    timer_time = timertime
    current_time=0
    while (current_time - last_checkpoint) < timer_time :
        current_time=int(time.time())
        print(current_time)
        time.sleep(1)
print(os.path.exists('data/checkpoints.csv'))
def CHECK_DATA():
    DataPath = os.path.exists('data/checkpoints.csv')
    if DataPath:
        print(' ')
    else:
        print(' ')
    return DataPath
def GET_LAST_CHECKPOINT():
    with open('data/checkpoints.csv', 'r') as fp:
        reader = csv.reader(fp)
        data_read = [row for row in reader]
    last_checkpoint_list_unit = str(data_read[len(data_read)-1])
    last_checkpoint= int(last_checkpoint_list_unit[2:-2])
    return last_checkpoint
    
GET_LAST_CHECKPOINT()
current_time=int(time.time())
last_checkpoint=GET_LAST_CHECKPOINT()
def DATA_MEGERING():
    CheckpointMegering = current_time - last_checkpoint
    return CheckpointMegering
DATA_MEGERING()
open(str(CURRENT_TIME())+'.txt','w')
close()
print(DataModule.GETCOIN())

