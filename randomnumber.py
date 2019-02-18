from os import system,name
def clear():
    if name=='nt':
        _ = system('cls')

def matrix_generator():
    import random
    l=random.sample(range(1,16),15)
    m=[]
    for x in range(4):
        k=[]    
        for y in range(4):
           try:   
              k+=[l.pop(0)]
           except:
               pass
        m+=[k]
    m[3].append(0)
    return m


def matrix_show(m):
    for x in range(4):
        print("--------------------------")
        for y in range(4):

            try:
              if y==0:
                  print("|",end='')
              if m[x][y]==0:
                  print("    :" ,end=' ')
              else:
                  print(" %2d :" %m[x][y],end=' ')
              if y==3:
                  print("|",end='')
            except:
                pass
        print('\n')
    print("--------------------------")


def shiftLeft(l):
      zf=0  
      for x in range(4):
        for y in range(4):
            if k[x][y]==0:
                zf=1
                break
        if zf==1:
            break
      if y==3:
          a=0
          return l,a
      else:
          a=1
          temp=l[x][y]
          l[x][y]=l[x][y+1]
          l[x][y+1]=temp
          return l,a
def shiftRight(l):
      zf=0  
      for x in range(4):
        for y in range(4):
            if k[x][y]==0:
                zf=1
                break
        if zf==1:
            break
      if y==0:
          a=0
          return l,a
      else:
          a=1
          temp=l[x][y]
          l[x][y]=l[x][y-1]
          l[x][y-1]=temp
          return l,a

def shiftUp(l):
      zf=0  
      for x in range(4):
        for y in range(4):
            if k[x][y]==0:
                zf=1
                break
        if zf==1:
            break
      if x==3:
          a=0
          return l,a
      else:
          a=1
          temp=l[x][y]
          l[x][y]=l[x+1][y]
          l[x+1][y]=temp
          return l,a


def shiftDown(l):
      zf=0,  
      for x in range(4):
        for y in range(4):
            if k[x][y]==0:
                zf=1
                break
        if zf==1:
            break
      if x==0:
          a=0
          return l,a
      else:
          a=1
          temp=l[x][y]
          l[x][y]=l[x-1][y]
          l[x-1][y]=temp
          return l,a

        
def checkWin(l):
    a=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
    if a==l:
        return 1
    else:
        return 0

move=500      
k=matrix_generator()

while move!=0:
    try:
        clear()
        print("keys: a-left, d-right, w-up, s-down")
        print("moves remaining:%d" %move)
        if (checkWin(k)):
            print("you won")
            input("press enter")
            break
        matrix_show(k)
        x=ord(input())
        if x==97 or x==65:
             k,a=shiftLeft(k)    
             if a==1:
                 move-=1
                
        elif x==100 or x==68:
             k,a=shiftRight(k)    
             if a==1:
                 move-=1
                
        elif x==115 or x==83:
             k,a=shiftDown(k)    
             if a==1:
                 move-=1
                
        elif x==119 or x==87:
             k,a=shiftUp(k)    
             if a==1:
                 move-=1
        else:
            pass
        
    except:
        pass

if move==0:
    print("You lost")
    input("enter to quit")

                    
























