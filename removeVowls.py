myStr = input("Enter myString: ")
newmyStr = myStr

for i in myStr.lower():
    if i in ('a', 'e', 'i', 'o', 'u'):
        newmyStr = newmyStr.replace(i, "")

print(newmyStr)