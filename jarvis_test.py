from TimeNormalizer import TimeNormalizer # 引入包
import json
import re


tn = TimeNormalizer()

# res = tn.parse(target='下周三下午两点30分五秒') # target为待分析语句，timeBase为基准时间默认是当前时间
# print(res)
# res = tn.parse(target='2013年二月二十八日下午四点三十分二十九秒 到 2014年二月二十八日下午四点三十分二十九秒', timeBase='2013-02-28 16:30:29') # target为待分析语句，timeBase为基准时间默认是当前时间
# print(res)
# res = tn.parse(target='我需要大概33天2分钟', timeBase='2013-02-28 16:30:29') # target为待分析语句，timeBase为基准时间默认是当前时间
# print(res)
# res = tn.parse(target='1月末') # target为待分析语句，timeBase为基准时间默认是当前时间
# print(res)
# res = tn.parse(target='明天')
# js = json.loads(res)
# print(js)
# print(res)

# res = tn.parse(target='7月10',timeBase='2024-01-01 16:30:29') # target为待分析语句，timeBase为基准时间默认是当前时间
# print(res)

# res = tn.parse(target='7-10',timeBase='2024-01-01 16:30:29') # target为待分析语句，timeBase为基准时间默认是当前时间
# print(res)


res = tn.parse(target='7.10',timeBase='2024-01-01 16:30:29') # target为待分析语句，timeBase为基准时间默认是当前时间
print(res)


##########
#####注意
##########

# 如果需要拓展时间样式，需要修改regex_saas.txt,是之匹配，修改TimeUnit.py中的time_normalization()函数,使之可以解析样式
res = tn.parse(target='7/10',timeBase='2024-01-01 16:30:29') # target为待分析语句，timeBase为基准时间默认是当前时间
print(res)
