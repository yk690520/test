"""
此功能用来删除设备号的资产编号
"""
from other_duty.decorator.decorator import decorator_for_log_and_load_file
import requests,openpyxl,json

@decorator_for_log_and_load_file(data_column=4,log_column_name=["设备编号","处理结果"])
def update_asset(source_path,log_path,*,data_list=None):
    """
    具体设置的方法
    :param source_path:
    :return:
    """
    log=[]
    asset_device_list=data_list
    for asset_device in asset_device_list:
        url = asset_device[3]
        asset_device={"fdevice":str(asset_device[0]),"isv_id":asset_device[1],"fdevice_asset":asset_device[2]}

        try:
            __update_asset(asset_device,url)
        except BaseException as e:
            log.append([asset_device["fdevice"],"修改失败"])
        else:
            log.append([asset_device["fdevice"],"修改成功"])
    return log

def __update_asset(asset_and_device,url):
    asset_and_device=json.dumps(asset_and_device)
    rb=requests.post(url,data=asset_and_device)
    re=json.loads(rb.text)
    if re['code']!="0":
        raise BaseException("失败")

def out_demo_file(path):
    '''
    输出一个demo文件
    :param path:
    :return:
    '''
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.cell(1,1,"设备号")
    sheet.cell(1,2,"isv_id")
    sheet.cell(1, 3, "资产编号")
    sheet.cell(1,4,"处理网址")
    sheet.cell(2,1,"99000740060892")
    sheet.cell(2,2,"1792")
    sheet.cell(2,4,"http://console.zy.youkedao.com/ykdweb//ykd/asset/update")
    sheet.cell(2,5,"自营环境")
    sheet.cell(3, 1, "99000740060892")
    sheet.cell(3, 2, "1792")
    sheet.cell(3, 4, "http://console.yk.yijuchelian.com/ykdweb//ykd/asset/update")
    sheet.cell(3,5,"车联网环境")
    wb.save(path)
if __name__ == "__main__":
    __update_asset({'fdevice': '99000740060892', 'isv_id': '1792', 'fdevice_asset': ''})
    pass