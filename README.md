# PythonPractice

* 字符串不能直接拼接数字
``` python
count = 0
print("一共"+str(count)+"个")  # 字符串不能直接拼接数字
```

- 获取最新一天的干货 
例如： http://gank.io/api/today 


## 编码问题

- 使用urllib的response中文显示成unicode码，如："\u60a8\u597d"

```python
# 解决unicode码问题
print(response.read().decode('unicode-escape'))

```