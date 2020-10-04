import csv 
f1 = open('train_example.csv','r',newline='')
data = csv.reader(f1)
i = next(data)
data=list(data)
print("Given Dataset: ")
for row in data:
    print(row)
n = len(data[0])
#for row in data:
#   print(row[n-1])
pos1 = [row for row in data if row[n-1]=='Yes']
pos1 = [row[:n-1] for row in pos1]
#print(pos1)
s1=pos1[0]
#print(s1)
pos1=pos1[1:]
#print(pos1)
for row in pos1:
    for i in range(0,n-1):
        if(row[i]==s1[i] or s1[i]=='?'):
            continue
        else:
            s1[i]='?'
print("\nFinal Hypothesis: ",s1)
f1.close()

