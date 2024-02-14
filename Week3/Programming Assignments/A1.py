
def solution(marks):
    ### Enter your solution below this line
    ### Indent your entire code by one unit (4 spaces) to the right
    n = len(marks)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if(marks[j] > marks[j+1]):
                marks[j], marks[j+1] = marks[j+1], marks[j]
    if n % 2 == 1:
        median = marks[n//2]
    else:
        m1 = marks[(n-1)//2]
        m2 = marks[n//2]
        median = (m1 + m2)/2