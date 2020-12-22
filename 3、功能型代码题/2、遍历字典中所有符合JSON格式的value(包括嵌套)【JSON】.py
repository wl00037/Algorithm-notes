
#假设给定一个字符串：inputstr = json.dumps({"a":{"a1":1},"b":2})，遍历出所有的符合json格式的value，包括嵌套的；

import json

inputstr = json.dumps({"a":{"a1":{"a11":1}},"b":2})     # 生成测试数据，dumps：将字典变成json串

result_list = []
def getJson(inputstr):
    load_data = json.loads(inputstr)    #   loads：将json串转换成字典
    if not isinstance(load_data,dict):
        return
    for key,value in load_data.items():
        if isinstance(value,dict):
            result_list.append(value)
            getJson(json.dumps(value))

getJson(inputstr)
print(result_list)

