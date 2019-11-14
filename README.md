# 8-Puzzel-Problem-Using-A-star-python3
The code is very simple.I have implemented it recursively so for large puzzels it might give stackoverflow error. you can implement it 
iteratively by small modifications.The main function in the code is:
astar(a,b,g,bi,bj):
a=initial state
b=goal state
g=levels(initially it is 0)
bi & bj are position of blank tile that we have to move 

As we know that in A8 algorithm we need to calculate cost at each step by following function:
f(n)=h(n)+g(n)
in this g(n) is nothing but the level g that we have passed in astar() function.
h(n) is a function defined in the code and it calculates number of missplaced tiles
