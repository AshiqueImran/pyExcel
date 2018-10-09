arrs=[]

arrs.append("abc")
arrs.append("def")
arrs.append("xyz")
arrs.append("123")
arrs.append("mno")

print "Hello World!\n"
for arr in arrs:
    print(arr)


for el in arrs:
    if el == "123":
        index=arrs.index(el)
        a=arrs.pop(index)
        print(a)

print "Hello World!\n"
for arr in arrs:
    print(arr)
