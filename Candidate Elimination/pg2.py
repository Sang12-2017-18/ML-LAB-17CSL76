import csv 
f1 = open('train_example.csv','r',newline='')
data = csv.reader(f1)
i = next(data)
data=list(data)
print("Given Dataset: ")
for row in data:
    print(row)
n=len(data[0])
pos1 = [row for row in data if row[n-1]=='Yes'].copy()
SB = pos1[0][:-1].copy()
GB = [['?' for i in range(len(SB))] for i in range(len(SB))]
#i=0
for row in data:
    if row[-1]=="Yes":
        for c1 in range(0,n-1):
            if SB[c1]!=row[c1]:
                SB[c1]='?'
                GB[c1][c1]='?'
                #print(SB)
        #print(SB)
    if row[-1]=="No":
        for c1 in range(n-1):
            if row[c1]!=SB[c1]:
                GB[c1][c1]=SB[c1]
            else:
                GB[c1][c1]='?'
    #print("Steps in Candidate Elimination Algorithm: ",i+1)
    #i=i+1
    #print(SB)
    #print(GB)
indices = [i for i,val in enumerate(GB) if val == ['?']*(n-1)]
for i in indices:
    GB.remove(['?']*(n-1))

print("\nFinal Specific Boundary: ", SB)
print("Final General Boundary: ", GB)