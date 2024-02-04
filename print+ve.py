def printpositive(l):
  numbers = [i for i in l if i > 0]
  print(f"Input: {l}\n Output: {numbers}")
print("Enter numbers separated by spaces: ")
l=list(map(int,input().split()))
printpositive(l)
