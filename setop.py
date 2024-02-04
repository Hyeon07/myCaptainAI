# User input of two sets
print("enter set E: ")
E=set(map(int,input().split()))
print("enter set N: ")
N=set(map(int,input().split()))
# Perform set operations
u = E.union(N)
i = E.intersection(N)
d = E.difference(N)
s = E.symmetric_difference(N)
# Display the results
print(f"Union of E and N is {u}")
print(f"Intersection of E and N is {i}")
print(f"Difference of E and N is {d}")
print(f"Symmetric difference of E and N is {s}")
