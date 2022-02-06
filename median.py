import csv

with open("height-weight.csv",newline='') as f:
    reader= csv.reader(f)
    file_data=list(reader)


file_data.pop(0) #to remove title
#print(file_data)
new_data=[] #to store all height

#get height from file_data
for i in range(len(file_data)):
    n_num=file_data[i][1]
    new_data.append(float(n_num)) 

#mean =total/n
n=len(new_data)
new_data.sort()

if n%2 == 0:
    median1 = float(new_data[n//2])
    median2 = float(new_data[n//2-1])
    median = (median1+median2)/2
else:
    median = float(new_data[n//2])

print(median)