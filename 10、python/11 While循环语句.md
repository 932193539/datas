while (count < 9):
print 'The count is:', count
count = count + 1

在 python 中，while … else 在循环条件为 false 时执行 else 语句块：
 
count = 0
while count < 5:
   print count, " is  less than 5"
   count = count + 1
else:
   print count, " is not less than 5"