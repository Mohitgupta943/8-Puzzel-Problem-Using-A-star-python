# 8-Puzzel-Problem-Using-A-star-python3
The code is very simple.I have implemented it recursively so for large puzzels it might give stackoverflow error. you can implement it<br> 
iteratively by small modifications.The main function in the code is:<br>
  astar(a,b,g,bi,bj)<br>
  a=initial state<br>
  b=goal state<br>
  g=levels(initially it is 0)<br>
  bi & bj are position of blank tile that we have to move <br> 

As we know that in A8 algorithm we need to calculate cost at each step by following function <br>
f(n)=h(n)+g(n) <br>
in this g(n) is nothing but the level g that we have passed in astar() function. <br>
h(n) is a function defined in the code and it calculates number of missplaced tiles
