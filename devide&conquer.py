# CONSTANTS 
TILE = 160
BOARD_SIZE = 480
BG_COLOR = "misty rose"

GOAL = (1,2,3,4,5,6,7,8,0)
DIRS=[(-1,0),(1,0),(0,-1),(0,1)]


# MOVE GENERATOR
def neighbors(state):
    i=state.index(0)
    r,c=divmod(i,3)
    res=[]
    for dr,dc in DIRS:
        nr,nc=r+dr,c+dc
        if 0<=nr<3 and 0<=nc<3:
            j=nr*3+nc
            lst=list(state)
            lst[i],lst[j]=lst[j],lst[i]
            res.append(tuple(lst))
    return res
