dis=eval(input())
if dis<0:
    print("请输入正确的公里数进行计算,程序结束")
elif 0<dis<2:
    print("8")
elif 2<dis<=12:
    dis=8+(dis-2)*1.2
    print(dis)
else:
    dis=8+10*1.2+(dis-12)*1.5
    print(dis)

#解题思路:由少至多,分段计算费用

'''题目:
要求：循环输入公里数，自动计算所需费用，费用计算公式如下

0.公里数小于等于0时输出：
  请输入正确的公里数进行计算，程序结束

1.出租车起步价8元，包含2公里
2.超过两公里的部分，每公里收取1.2元
3.超过12公里的部分，每公里收取1.5元'''