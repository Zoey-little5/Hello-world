# Your Code Below
import numpy as np
# from itertools import permutations
from numpy import random
import time
def t2o(t):
    re=[]
    for i in range(len(t[0])):
        re.append(t[0][i]*3+t[1][i])
    return re

def o2t(o):
    # print("o",o)
    re=[int(o/3),o%3]
    return re

def check(bd):

    p1=t2o(np.where(bd==1))
    p2=t2o(np.where(bd==2))
#     print(p1,p2)
    win=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    if len(p1)>2:
        for i in range(len(p1)):
            for j in range(i+1,len(p1)):
                for k in range(j+1,len(p1)):
                    if [p1[i],p1[j],p1[k]] in win:
#                         print(p1[i],p1[j],p1[k])
                        return 1
    if len(p2)>2:
        for i in range(len(p2)):
            for j in range(i+1,len(p2)):
                for k in range(j+1,len(p2)):
                    if [p2[i],p2[j],p2[k]] in win:
#                         print(p2[i],p2[j],p2[k])
                        return 2
    return 0
def check_win(bd):
    p1=t2o(np.where(bd==1))
    p2=t2o(np.where(bd==2))
    win=[[0,1],[0,2],[1,2],[3,4],[3,5],[4,5],[6,7],[6,8],[7,8],[0,3],[0,6],[3,6],[1,4],[1,7],[4,7],[2,5],[2,8],[5,8],[0,4],[0,8],[4,8],[2,4],[2,6],[4,6]]
    win_next=[2,1,0,5,4,3,8,7,6,6,3,0,7,4,1,8,5,2,8,4,0,6,4,2]
    # print("xxxxxxxxxxxx",len(p1))
    if len(p1)>1:
        for i in range(len(p1)):
            for j in range(i+1,len(p1)):
                x=[p1[i],p1[j]]
                y=[p1[j],p1[i]]
                if  x in win:
                    # print("x!!!!",x)
                    plan=win_next[win.index(x)]
                    # print("plan",plan)
                    if plan not in p2:
                        return plan 
                if y in win:
                    # print("y!!!!",y)
                    plan=win_next[win.index(y)]
                    # print("plan",plan)
                    if plan not in p2:
                        return plan 

def check_not_win(bd):
    # print("bd",bd)
    p2=t2o(np.where(bd==1))
    p1=t2o(np.where(bd==2))
    # print(p1)
    # print(p2)
    win=[[0,1],[0,2],[1,2],[3,4],[3,5],[4,5],[6,7],[6,8],[7,8],[0,3],[0,6],[3,6],[1,4],[1,7],[4,7],[2,5],[2,8],[5,8],[0,4],[0,8],[4,8],[2,4],[2,6],[4,6]]
    win_next=[2,1,0,5,4,3,8,7,6,6,3,0,7,4,1,8,5,2,8,4,0,6,4,2]
    # print("xxxxxxxxxxxx",len(p1))
    if len(p1)>1:
        for i in range(len(p1)):
            for j in range(i+1,len(p1)):
                x=[p1[i],p1[j]]
                y=[p1[j],p1[i]]

                if  x in win:
                    # print("x!!!!",x)
                    plan=win_next[win.index(x)]
                    # print(plan)
                    # print("plan",plan)
                    if plan not in p2:
                        return plan 
                if y in win:
                    # print("y!!!!",y)
                    plan=win_next[win.index(y)]
                    # print("plan",plan)
                    if plan not in p2:
                        return plan







start_time=time.time()
win1=0
win2=0
draw=0
# pos=-1
game=0
now=time.time()
while(now-start_time<1):
    
    print(time.time())
    game+=1
    print("New game\n\n\n")
    board=np.zeros((3,3))#initialize the board, step and result
    board = board.astype(int)
#     print(board)
    re=0
    step=0
    first=np.random.randint(2)
    while re==0:
        taken=0
        # a=np.random.randint(3)
        # b=np.random.randint(3)
        # while board[a,b]!=0:
        #     a=np.random.randint(3)
        #     b=np.random.randint(3)
        # if first==0:
        #     if step%2==0:
        #         board[a][b]=1
        #     if step%2==1:
        #         board[a][b]=2   
        # if first==1:
        #     if step%2==0:
        #         board[a][b]=2
        #     if step%2==1:
        #         board[a][b]=1
        pos=None
        if (first==1 and step%2==1) or (first==0 and step%2==0):
            pos=None
            pos=check_win(board)
            if pos!=None:
                pos=o2t(pos)

            if pos==None:
                pos=check_not_win(board)
                if pos!=None:

                    pos=o2t(pos)
                # print("suggest",pos)
        if pos !=None:
            board[pos[0]][pos[1]]=1
            taken=1

        if taken==0:
            a=np.random.randint(3)
            b=np.random.randint(3)
            while board[a,b]!=0:
                a=np.random.randint(3)
                b=np.random.randint(3)
            if first==0:
                if step%2==0:
                    board[a][b]=1
                if step%2==1:
                    board[a][b]=2   
            if first==1:
                if step%2==0:
                    board[a][b]=2
                if step%2==1:
                    board[a][b]=1
        
        

        step+=1
        print("step",step)
        print(board)
        

        re=check(board)
        if re==1:
            # print("1 win")
            win1+=1
            re=1
        if re==2:
            # print("2 win")
            win2+=1
            re=1
        if step==9 and re==0:
            # print("draw")
            draw+=1
            re=1
    now=time.time()
        
# print(win1,win2,draw)
# print(xxxxxxxxxxx,yyyyyyyyyyyy)

print("Probability of 1 wins: ",win1/game)
print("Probability of 2 wins: ",win2/game)
print("Probability of draw: ",draw/game)
print("Games completed: ",game)
print("Simulation time: ",now-start_time,"s")


