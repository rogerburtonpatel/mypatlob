N = input("Please enter the Nth element you desire")
prev = 1
prev2 = 1
for i in range(N - 2):
    temp = prev + prev2
    prev2 = prev
    prev = temp
print(prev)