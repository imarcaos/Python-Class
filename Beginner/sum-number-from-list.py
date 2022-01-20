# Soma os números contidos em uma lista - 20/02/2022

x = [5,10,15,20,25,30]
listSize = len(x)
sumList = 0


while(listSize > 0):
    sumList += x[listSize-1]
    listSize -= 1

# ou simplesmente
# sumList = sum(x)
print("A Soma dos números contidos na lista é -> ", sumList)