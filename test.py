ls=[1,2,3,4,5,6,7]

for i in ls:
    if i%2==0:
        ls.remove(i)


print(ls)