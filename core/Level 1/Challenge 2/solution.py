import pickle
ch=input("Do you want to enter values in the file")
while ch=='y' or ch=='Y':
    file = open("data.pkl", "ab")
    dict1 = {}
    ch = 'y'
    rn = []
    score = []
    n = int(input("Number of entries "))
    for i in range(0, n):
        rn_ele = int(input("Enter Registration Number: "))
        sc_ele = float(input("Enter the scored marks: "))
        rn.append(rn_ele)
        score.append(sc_ele)

    dict1["Rno"] = rn
    dict1["score"] = score
    pickle.dump(dict1, file)
    file.close()
    ch=input("Still want to enter values in the file")

print("Contents in the file")
file = open("data.pkl", 'rb')
file.seek(0)
while True:
    try:
        data = pickle.load(file)
        print(data)
    except EOFError:
        break

file.close()

file = open("data.pkl", 'rb+')
file.seek(0)
temp = int(input("Enter the registration number of the student whose marks should be modified: "))
f = 0
data = pickle.load(file)
for line in data:
    pos = file.tell()
    n = len(data["Rno"])
    for i in range(n):
        if (data["Rno"][i]) == temp:

            s = int(input("Enter the score to be modified"))
            data["score"][i] = s
            file.seek(pos)
            pickle.dump(data, file)
            print("Data has been successfully modified")
            f = 1
            break
    if f == 1:
        break

if f == 0:
    print("Data not found")

file.close()
file = open("data.pkl", 'rb')
while True:
    try:
        data = pickle.load(file)
        print(data)
    except EOFError:
        break
