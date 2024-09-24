from numpy import*
from random import*
from time import*
from keyboard import*
def show_platform():
    global jum,gt,lost,s_time,speed
    if jum==True:
        print("\n\n\n\n                                                                                                ██████████████  \n                                                                                              ████░░████████████\n                                                                                              ██████████████████\n                                                                                              ██████████████████\n                                                                                              ██████████████████\n                                                                                              ████████          \n                                                                                              ████████████████  \n                                                                                              ██████            \n                                                                          ██              ██████████            \n                                                                          ████        ██████████████████        \n                                                                          ██████      ██████████████  ██        \n                                                                          ██████████████████████████            \n                                                                          ██████████████████████████            \n                                                                            ██████████████████████              \n                                                                                ██████████████████              \n                                                                                ████████████████                \n                                                                                  ██████████████                \n                                                                                    ████      ██                \n                                                                                    ██        ██                \n                                                                                    ██        ██                ")
        jum=False
    elif jum==False:
        if gt[3]=="cactus":
            lost=True
        else:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            gt[3]="dinasor"
    #print zone
    w=""
    for i in range(20):
        for j in range(16):
            if gt[j]=="cactus":
                w=w+cac[(25*i):(25*(i+1)-1)]
            elif gt[j]=="dinasor":
                w=w+dina[(41*i):(41*(i+1)-1)]
            else:
                w=w+gt[j]
        w=w+"\n"
    print(w)
    #time delay
    tc=time()+speed
    while tc>time():
        if gt[3]=="dinasor":
            jump()
def jump():
    global gt,jum
    if is_pressed("up"):
        gt[3]=es
        jum=True
def move_cactus(t):
    i=0
    while (i<16):
        if t[i]=="cactus":
            if i==0:
                t[i]=es
            else:  
                t[i]=es
                t[i-1]="cactus"
                i=i+1
        i=i+1
    return t
#variables_&_const
cac="""          ████          
  ██    ██▒▒▒▒██        
██▒▒██  ██▒▒▒▒██        
██▒▒██  ██▒▒▒▒██        
██▒▒██  ██▒▒▒▒██        
██▒▒██  ██▒▒▒▒██    ██  
██▒▒██  ██▒▒▒▒██  ██▒▒██
██▒▒▒▒████▒▒▒▒██  ██▒▒██
  ██▒▒▒▒▒▒▒▒▒▒██  ██▒▒██
    ██▒▒▒▒▒▒▒▒██  ██▒▒██
      ████▒▒▒▒████▒▒▒▒██
        ██▒▒▒▒▒▒▒▒▒▒██  
        ██▒▒▒▒▒▒▒▒██    
        ██▒▒▒▒████      
        ██▒▒▒▒██        
        ██▒▒▒▒██        
        ██▒▒▒▒██        
        ██▒▒▒▒██        
        ██▒▒▒▒██        
        ██▒▒▒▒██        """
dina="""                        ██████████████  
                      ████░░████████████
                      ██████████████████
                      ██████████████████
                      ██████████████████
                      ████████          
                      ████████████████  
                      ██████            
  ██              ██████████            
  ████        ██████████████████        
  ██████      ██████████████  ██        
  ██████████████████████████            
  ██████████████████████████            
    ██████████████████████              
        ██████████████████              
        ████████████████                
          ██████████████                
            ████      ██                
            ██        ██                
            ██        ██                """
es="                        "
jum=False
lost=False
s_time=time()
speed=0.3
goal=100
gt=array([es]*16,dtype="<U1000")
#start menu
print("\n∧")
for i in range(5):
    print("|")
print("|                Please make sure that your shell is in the right height than press 's'")
for i in range(4):
    print("|")
print("∨")
while not(is_pressed("s")):
    True
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
#start
while lost==False:
    gt[15]="cactus"
    for i in range(randint(2,7)):
        gt=move_cactus(gt)
        show_platform()
        if int((time()-s_time)*100)>=goal:
            speed-=0.01
            goal+=100