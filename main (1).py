#PROBLEM 2
T = int(input("enter ur repetetion"))
for i in range(T):
    X = int(input("Enter height of alice:"))
    Y = int(input("Enter height of Bob:"))
    if X>Y:
        print("alice is longer than Bob")
    else:
        print("Bob is longer than alice")
    