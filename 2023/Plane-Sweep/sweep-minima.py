import numpy as np

def sweep_minima(S : np.array):
    q = S[0]
    print (q)
    for i in S:
      if i[1] < q[1]:
        print (i)
        q = i
        
# points have to be sorted by xy-coordinates - upwards
s = np.array([[0,3],[3,3],[7,5],[9,7]])
# use lexsort for that - O(n log n)
sweep_minima(s)