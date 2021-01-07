
#   打开一个英文的文本文件,将该文件中的每个字母加密后写入到一个新文件。
#   加密的方法如下：
#       将A变成B , B变成C, … Y变成Z , Z变成A；
#       a变成b,b变成…z变成a；
#       其他字符不变化；

with open("English.txt","r") as f:
    OldString = f.read()    #   每个字符，那么就全读出来就可以了；

NewString = ""

for i in OldString:
    temp = ord(i)           #   ord函数用来返回字符对应的ASCII码
    if temp in  range(65,91):       #   处理小写字母：小写字母的ascii在65-90
        if temp == 90:
            char_new = chr(temp-25)     #   z -> a
            NewString = NewString + char_new
        else:
            char_new = chr(temp+1)
            NewString = NewString + char_new
    elif temp in range(97,123):     #   处理大写字母：大写字母的ascii在97-122
        if temp == 122:
            char_new = chr(temp-25)     #   z -> a
            NewString = NewString + char_new
        else:
            char_new = chr(temp+1)
            NewString = NewString + char_new
    else:                           #   处理非字母字符
        NewString = NewString + i

print(NewString)
