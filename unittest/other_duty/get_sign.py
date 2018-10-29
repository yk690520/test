#此模块用来生成签名
import requests
import csv,os
from lxml.html import fromstring

type_list={
    "情侣":"qinglv","超拽":"chaozhuai","伤感":"shanggan","经典":"jingdian",
    "励志":"lizhi","心情":"xinqing","艺术":"yishu","爱情":"aiqing","幸福":"xingfu","唯美":"weimei","无奈":"wunai"
}
def __getDataFromWebsite(link):

    '''
    从网址获取签名数据
    :param link:
    :return: 返回一个数据的list
    '''
    response=requests.get(link)
    response.encoding='utf-8'
    doc=fromstring(response.text)
    temp=doc.xpath("//ul[@class='list']//p")
    list=[text.text_content() for text in doc.xpath("//ul[@class='list']//p")]
    if list and len(list)>0:

        return list

def __writeCsv(list,path):
    '''
    写入数据
    :param list:
    :return:
    '''
    with open(path,'a+',newline='',errors='ignore') as file:
        csv_w=csv.writer(file)
        for data in list:
            if len(data)<30:
                print(data)
                csv_w.writerow([data])

def print_type():

    '''
    输出可使用的类型
    :return:
    '''
    global type_list
    print("")
    print("请输入可使用的【类型】，可使用的【类型】有以下，请直接输入：")
    count=1
    for type in type_list.keys():
        if count%5==0:
            print()
        print(type,end="  ")
        count+=1
def get_sign(path,type):
    global type_list
    if not type in type_list.keys():
        return "请检查输入的【类型】是否有误"
    type_py=type_list[type]
    if os.path.exists(path) and os.path.isfile(path):
        os.remove(path)
    for count in range(1,100):
        list=__getDataFromWebsite('http://www.qqgexingqianming.com/%s/%s.htm' % (type_py,count))
        if list:
            __writeCsv(list,'%s/【%s】签名导出集合.csv' % (path,type))

if __name__=="__main__":
    get_sign(os.getcwd(),"情侣")