1.������:�ڼ������������У���������ǿ������ԣ���ָ����ȷ�������õĶ��󲻻ᱻ�������������յ����á�һ��������ֻ�������������ã�����Ϊ�ǲ��ɷ��ʣ������ɷ��ʣ��ģ�����˿������κ�ʱ�̱����ա�һЩ�����������ջ��Ƶ�����

 
local testa = {}
tbl_key = {}
testa[tbl_key] = 1
tbl_key = {}
testa[tbl_key] = 2
 
--��������
collectgarbage()
 
local function PrintInfo()
 
	for k, v in pairs(testa) do
		print(k, "===", v)
	end
 
end
 
PrintInfo()

--�������
table: 004FB890	===	1
table: 004FB8E0	===	2


--lua������Ҫ��ɾ��key����value��table��һ��Ԫ����
--Ԫ�����__mode�ֶΰ���k����v��k��ʾkeyΪ�����ã�v��ʾvalueΪ������

local testa = {}
local mt = {__mode = 'k'}
setmetatable(testa,mt)
 
tbl_key = {}
testa[tbl_key] = 1
tbl_key = {}
testa[tbl_key] = 2
 
--��������
collectgarbage()
 
local function PrintInfo()
 
	for k, v in pairs(testa) do
		print(k, "===", v)
	end
 
end
 
PrintInfo()

--�������
table: 006EB930	===	2




ͨ��key�������ã�������keyΪkey_table��ֵ��û�������ط������ã����Ա����յ���
(�������:ȫ�ֱ���tbl_key��һ�ζ���ʱ�������ǿ������,�������ᱻ����,����������������������ڶ������¶�����,���ڻ���ʱ�ͻ���յ�һ�ζ����)


local test = {1}
local test = {2}
ע��:�������ζ����test�ǿ����������ڴ�ռ�ģ�ͨ��ǿ�����ǿ��Եõ�value = 1��2 ������ֵ��


