map<int, string> mapStudent;  
mapStudent.insert(pair<int, string>(1, "student_one"));  
mapStudent.insert(pair<int, string>(2, "student_two"));  

map<int, string>::iterator iter;  
for(iter = mapStudent.begin(); iter != mapStudent.end(); iter++)  
   cout<<iter->first<<' '<<iter->second<<endl;  

//输出如下
1, student_one
2, student_two
3, student_three

Int nSize = mapStudent.size();
int n = mapStudent.erase(1);//如果删除了会返回1，否则返回0  

//一下代码把整个map清空  
mapStudent.clear(） 

//如果要删除1,用迭代器删除  
map<int, string>::iterator iter;  
iter = mapStudent.find(1);  
mapStudent.erase(iter);  

begin()         返回指向map头部的迭代器
clear(）        删除所有元素
count()         返回指定元素出现的次数
empty()         如果map为空则返回true
end()           返回指向map末尾的迭代器
equal_range()   返回特殊条目的迭代器对
erase()         删除一个元素
find()          查找一个元素
get_allocator() 返回map的配置器
insert()        插入元素
key_comp()      返回比较元素key的函数
lower_bound()   返回键值>=给定元素的第一个位置
max_size()      返回可以容纳的最大元素个数
rbegin()        返回一个指向map尾部的逆向迭代器
rend()          返回一个指向map头部的逆向迭代器
size()          返回map中元素的个数
swap()           交换两个map
upper_bound()    返回键值>给定元素的第一个位置
value_comp()     返回比较元素value的函数
