#imports user answers from txt doc labeled MyAnswers.txt and stores them in array myAnswers, stored as one asnwers 
myAnswers = []
with open('MyAnswers.txt') as f:
    myAnswers = f.readlines()

for i in range(len(myAnswers)):
    myAnswers[i] = myAnswers[i].rstrip().lower()
#print(myAnswers)

#imports answer key from txt doc labeled key.txt and stores them in array myAnswers, stored as one asnwers 
key = []
with open('Key.txt') as f:
    key = f.readlines()

seperator = input("Type in what seperates the number form the answer for that number ex:(1-a) you type '-' : ")
for i in range(len(key)):
    splitIndex = key[i].find(seperator) + 1
    key[i] = key[i][splitIndex:].rstrip()
#print(key)

#calculates the score by comparing the answers between each index of myAnswers and key
count = 0
qWrong = []
for i in range(len(key)):
    if(myAnswers[i] == key[i]):
        count+=1
    else:
        qWrong.append(i)
print("Score: " + str(count) +"/" +  str(len(myAnswers)))
print("Questions you got wrong: " + str(qWrong))