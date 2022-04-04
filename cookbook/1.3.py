from collections import deque

# helpful pattern when you want fast removal and addition
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
q

q.append(4)
q

q.appendleft(5)
q
