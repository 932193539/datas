在c++中，vector是一个十分有用的容器，下面对这个容器做一下总结。
1 基本操作
(1)头文件#include<vector>.
(2)创建vector对象，vector<int> vec;
(3)尾部插入数字：vec.push_back(a);
(4)使用下标访问元素，cout<<vec.at(0)<<endl;记住下标是从0开始的。
(5)使用迭代器访问元素.
vector<int>::iterator it;
for(it=vec.begin();it!=vec.end();it++)  //直接 auto it 就可以
    cout<<*it<<endl;
(6)插入元素：    vec.insert(vec.begin()+i,a);在第i+1个元素前面插入a;
(7)删除元素：    vec.erase(vec.begin()+2);删除第3个元素
vec.erase(vec.begin()+i,vec.end()+j);删除区间[i,j-1];区间从0开始
(8)向量大小:vec.size();
(9)清空:vec.clear();
(10)vec.getIndex(*it) 得到 *it 这个元素的id 也就是插入顺序id

2  算法
(1) 使用reverse将元素翻转：需要头文件#include<algorithm>
reverse(vec.begin(),vec.end());将元素翻转(在vector中，如果一个函数中需要两个迭代器，
一般后一个都不包含.)
(2)使用sort排序：需要头文件#include<algorithm>，
sort(vec.begin(),vec.end());(默认是按升序排列,即从小到大).

vector<int>::iterator it;//声明一个迭代器
for(it=iVec.begin();it!=iVec.end();)
{
    if(*it % 3 ==0)
        it=iVec.erase(it);    //删除元素，返回值指向已删除元素的下一个位置    
    else
        ++it;    //指向下一个位置29    
    
}



