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
total=0

for x in new_data:
    total=total+x

mean=total/n

print("Mean of Height :"+ str(mean))



    
