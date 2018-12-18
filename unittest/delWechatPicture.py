import os
import time
while True:
    dirss=[]
    des=r"C:\Users\root\Documents\WeChat Files"
    if not os.path.exists(des):
        des=r"C:\Users\Administrator\Documents\WeChat Files"
    for root,dirs,files in os.walk(des):
        for dir in dirs:
            temp=os.path.join(root,dir)
            print(temp)
            dirss.append(temp)
        break
    for dir in dirss:
        cmd=r'del /f /s /q "%s\Video\*.*"' % dir
        resault=os.popen(cmd)
        print(resault.read())
    print("间隔1小时后将再次清理，请勿关闭此窗口")
    time.sleep(3600)