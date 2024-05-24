word = input()
a = len(word)
b = -1
mylist = [None] * a
while b >= -a:
    x = (abs(b)-1)
    mylist[x] = word[b]
    b = b-1
output = ''.join(mylist)
print (output)
