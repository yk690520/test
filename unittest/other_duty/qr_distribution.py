import os,shutil,openpyxl,random
from other_duty.decorator.decorator import decorator_for_log_and_load_file
#读取文件列表

#获取QR数量
def __qr_count(qr_path:str):
    if not os.path.exists(qr_path):
        raise BaseException("二维码目录不存在")
    if not os.path.isdir(qr_path):
        raise BaseException("所提供的路径不是目录")
    count=0
    for root,dirs,files in os.walk(qr_path):
        for file in files:
            count+=1
    return count
#文件移动方法
def __move_file(number:int,path:str,dscPath:str):
    '''
    :param number: 移动的数量
    :param path: 被移到文件所在目录
    :param dscPath: 移动目的地
    :return:
    '''
    if os.path.exists(dscPath):
        shutil.rmtree(dscPath)
    os.makedirs(dscPath)
    count=0
    for root,dirs,files in os.walk(path):
        for file in files:
            file=os.path.join(root,file)
            fname,fename=os.path.splitext(file)
            fname="%s%s" % (fname,random.randint(1,1000))
            new_filename="%s%s" % (fname,fename)
            os.rename(file,new_filename)
            shutil.move(new_filename,dscPath)
            count+=1
            if count>=number:
                return

#分配二维码
@decorator_for_log_and_load_file(data_column=2,log_column_name=["未分配数量","已分配数量"])
def distr_qr(source_path:str,log_path:str,qr_path,*,data_list):
    '''
    二维码分配方法
    :param source_path:
    :param log_path:
    :return:
    '''
    distr_list=data_list
    count=__qr_count(qr_path)
    if count<=0:
        raise BaseException("二维码目录里无二维码")
    copy_count=count
    log=[]
    now_dir="%s/已分配二维码" % os.getcwd()
    if os.path.exists(now_dir):
        shutil.rmtree(now_dir)
    os.makedirs(now_dir)
    for distr in distr_list:
        asset=distr[0]
        number=int(distr[1])
        count-=number
        __move_file(number,qr_path,"%s/%s" % (now_dir,asset))
    re=[count,copy_count-count]
    log.append(re)
    return log

def output_demo(path:str):

    '''
    输出一个demo文件
    :param path:
    :return:
    '''
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.cell(1,1,"资产编号")
    sheet.cell(1,2,"分配数量")
    sheet.cell(2,1,"YC-A-01")
    sheet.cell(2,2,"8")
    wb.save(path)
if __name__ == '__main__':
    distr_qr(r'C:\Users\yk690\OneDrive\桌面\二维码分配模板.xlsx',"%s/log.xlsx" % os.getcwd(),r"C:\Users\yk690\OneDrive\桌面\360")