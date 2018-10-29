'''
需求说明：导入一个excel表格，表格表头：【资产编号，标签】，然后将其设置到后台，并输出未成功设置的资产编号。
'''
import openpyxl,time,traceback
from selenium import webdriver
from other_duty.decorator.decorator import decorator_for_log_and_load_file

@decorator_for_log_and_load_file(data_column=2,log_column_name=["资产编号","处理结果"])
def ding_flags(sourcePath,logPath,*,data_list):
    will_ding_assert_list=data_list
    #进入浏览器
    brower = webdriver.Chrome()
    brower.maximize_window()
    brower.implicitly_wait(15)
    brower.get('http://console.zy.youkedao.com/login/')
    brower.find_element_by_xpath('//*[@id="userName"]').send_keys('18800010001')
    brower.find_element_by_xpath('//*[@id="password"]').send_keys('abc123')
    brower.find_element_by_xpath('/html/body/form/div/div[2]/div[4]/input').click()
    brower.find_element_by_xpath('//*[@id="side-menu"]/dl[7]/dd[1]/a').click()
    #抵达微信号管理页面
    access=[]#成功的
    unaccess=[]#失败的
    log=[]
    for one in will_ding_assert_list:
        asset=one[0]
        flags=one[1]
        flags_str = flags.strip()
        flags = flags_str.split(",")
        try:
            __ding_flags_for_wechat(brower,asset,flags)
        except:
            log.append([asset,"失败"])
        else:
            log.append([asset, "成功"])
    brower.quit()
    #打标签结束，返回错误日志
    return log
    pass

def __ding_flags_for_wechat(brower,asset:str,flags:[]):

    '''
    这是一个为某一个具体的设备订标签的方法，如果传入的标签为None，那么将清除此设备的所有标签
    :param asset: 设备资产编号
    :param flags: 要打的标签
    :return:None
    '''
    brower.find_element_by_xpath('//*[@id="compose_keywords"]').clear()
    brower.find_element_by_xpath('//*[@id="compose_keywords"]').send_keys(asset)
    brower.find_element_by_xpath('//*[@id="btn-filter"]/span[2]').click()
    #找到change按钮
    time.sleep(1)
    change=brower.find_element_by_xpath('//i[@onclick="modifyGroup($(this))"]')
    #点击change按钮
    brower.execute_script("$(arguments[0]).click()", change)
    #点击清除按钮
    brower.find_element_by_xpath('//*[@id="group-btn-group-cancel"]/span[1]').click()
    #点击ok按钮
    brower.find_element_by_xpath('//*[@id="group-btn-group-ok"]').click()
    brower.find_element_by_xpath('//*[@id="popup_ok"]').click()
    if not flags:
        return
    # 找到change按钮
    change = brower.find_element_by_xpath('//i[@onclick="modifyGroup($(this))"]')
    # 点击change按钮
    brower.execute_script("$(arguments[0]).click()", change)
    for flag in flags:
        brower.find_element_by_xpath('//span[@class="splitTags"][text()="%s"]' % flag).click()
    brower.find_element_by_xpath('//*[@id="group-btn-group-ok"]').click()  # 点击ok按钮





def out_demo_file(path):

    '''
    输出一个demo文件
    :param path:
    :return:
    '''
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.cell(1,1,"资产编号")
    sheet.cell(1,2,"标签")
    sheet.cell(2,1,"SH-A-02")
    sheet.cell(2,2,"封号,故障")
    wb.save(path)

if __name__=="__main__":
    try:
        ding_flags(r'C:\Users\yk690\OneDrive\桌面\新建 Microsoft Excel 工作表.xlsx',r'C:\Users\yk690\OneDrive\桌面\log.xlsx')
    except BaseException as e:
        print(e)
        time.sleep(10)
