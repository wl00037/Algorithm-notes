
#   找到S中的一个连续子串，要包涵L中的所有元素(不限制元素在S中的顺序和次数)

l = ['a', 'c', 'b', 'd']
s = "fjiaidjabacdefkl"


def ISTrue():
    l = ['a', 'c', 'b', 'd']
    s = "fjiaidjabacdefkl"

    for i in range(0, len(s) - 1):
        if s[i] not in l[:]:
            continue

        start = i
        tmp = l[:]
        removed = []
        while (start < len(s)):
            if s[start] in tmp:
                removed.append(s[start])
                tmp.remove(s[start])
                start += 1
                if len(tmp) == 0:
                    return i
                else:
                    continue
            elif s[start] in removed:
                start += 1
                continue
            else:
                break
    return -1

print(ISTrue())