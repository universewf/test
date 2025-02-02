a = [1,1,2,2,3,3,4]
array = []

for i in a:
    if a.count(i)==1:
        array.append(i)
        print(array)