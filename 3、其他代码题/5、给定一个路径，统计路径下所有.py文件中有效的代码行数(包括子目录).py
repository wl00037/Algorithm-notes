
# 蚂蚁金服 - 网商银行（一面）
# 题目：给定一个路径，统计出这个路径下（包括子目录下的文件）所有.py文件中有效代码行数；
#       有效代码：不包括import代码行、不包括注释行；

# 注意点：
#   1、要先拿到所有.py文件，并且子目录下也要考虑；
#   2、要考虑到以"#"开头和以"import"开头的行；
#   3、还要保证左侧的空格要去掉；

import os

def getAllFiles(path):
    # 可以用os.walk来实现递归获取path下所有文件
    pyfiles_list = []
    for root,dirs,files in os.walk(path):
        # os.walk实现递归，会将每个子目录作为path进行处理，所以我们可以直接对每一个files分析即可
        # root：当前目录路径（每一个递归的path的路径）
        # dirs：当前路径下所有子目录（每一个递归path下的子目录）
        # files：当前路径下所有非目录子文件（每一个递归path下的文件）
        for file in files:
            if file.endswith(".py"):        # 我们将后缀为.py的文件过滤出来
                pyfiles_list.append(os.path.join(root,file))   # 不能只加文件名，还需要加上对应的路径os.path.join方法
    return pyfiles_list

def getCodeLine(pyfilepath):
    fileLineCount = 0
    with open(pyfilepath,"r") as f:
        linesList = f.readlines()
    for line in linesList:
        if line.lstrip().startswith("#") or line.lstrip().startswith("import") or line == "\n":
            # 过滤回车行数、注释行数、import导入行数
            continue
        fileLineCount += 1
    return fileLineCount

if __name__ == "__main__":
    path = "D:\out"
    pyfilelist = getAllFiles(path)
    AllCount = 0
    for pyfile in pyfilelist:
        LineCount = getCodeLine(pyfile)
        AllCount += LineCount
    print("总行数为：",AllCount)
