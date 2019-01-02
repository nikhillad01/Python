t = int(input())
dl=[]
ml=[]
dandm={}
for t_itr in range(t):
    dm = input().split(" ")

    d = int(dm[0])
    dl.append(d)

    m = int(dm[1])
    ml.append(m)
    dandm.update({d:m})
print(dl," ",ml)
print("dictionary ",dandm)
    #result = taskScheduling(d, m)

