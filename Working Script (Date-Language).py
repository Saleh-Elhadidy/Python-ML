import csv
import langid
with open('test.csv', 'r') as f:
  reader = csv.reader(f)
  your_list = list(reader)
listLangs = [] # Reads a csv file with 4 fields,date,place,text,lang and counts
listCount = [] # the count of every language occurence,hour of post occurence
listTimePost = [0] *24
for x in range(1,len(your_list)): 
        fullTime = your_list[x][0] # Getting the count of time of tweet of every user's tweets
        wholeTime = fullTime.split(" ")
        time = wholeTime[1].split(":")
        hour = time[0]
        
        listTimePost[int(hour)]+=1
        if your_list[x][3] in listLangs:  # Getting the count every language in a user's tweet
            index = listLangs.index(your_list[x][3])
            listCount[index]+=1
        else:
            listLangs.append(your_list[x][3])
            listCount.append(1)
                    

          
                   
               
print("List Langs:")
print(listLangs)

print("List Counts:")
print(listCount)

               
print("List Hours of posting:")
print(listTimePost)

with open('test2.csv', 'r') as b:
  reader = csv.reader(b)
  your_list2 = list(reader)

print((your_list2[1][3] in listLangs))
