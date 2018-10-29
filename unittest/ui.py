#此为功能的一个集合
#打标签功能
from other_duty import create_flag, ding_flags_for_wechat, recharge, get_momo_picture, get_sign, update_asset,qr_distribution
from airtest.core.android.constant import (DEFAULT_ADB_PATH, IP_PATTERN,
                                           SDK_VERISON_NEW)
import os,traceback,shutil

while True:
    os.system("cls")
    print("请输入你要执行的功能：")
    print("【1】打标签")
    print("【2】更新资产编号")
    print("【3】生成签名")
    print("【4】根据链接获取陌陌图片")
    print("【5】创建标签")
    print("【6】给手机充话费")
    print("【7】分配二维码")
    print("【0】退出")
    duty=input("请输入：")
    if duty=="1":
        os.system("cls")
        while True:
            print("欢迎进入打标签界面")
            print("【1】输出样例文件")
            print("【2】开始打标签")
            print("【0】返回上一级")
            choice=input("请选择：")
            path=os.getcwd()
            if choice=="1":
                ding_flags_for_wechat.out_demo_file("%s/打标签样例文件.xlsx" % path)
                os.system("cls")
                print("样例文件输出成功")
            elif choice=="2":
                os.system("cls")
                print("请在此键入需要处理设备的excl路径，如果使用样例文件，且未更改名字与位置，请直接回车")
                tpath=input("请输入：")
                try:
                    if not tpath:
                        ding_flags_for_wechat.ding_flags("%s/打标签样例文件.xlsx" % path, "%s/打标签结果.xlsx" % path)
                    else:
                        ding_flags_for_wechat.ding_flags(tpath, "%s/打标签结果.xlsx" % path)
                except BaseException as e:
                    traceback.print_stack()
                    print("处理出错，错误信息已显示")
                else:
                    os.system("cls")
                    print("已处理完成，且生成了打标签结果.xlsx报告，欢迎查看")
            elif choice=="0":
                break
            else:
                os.system("cls")
                continue
    elif duty=="2":
        os.system('cls')
        while True:
            print("欢迎进入更新资产编号界面")
            print("【1】输出样例文件")
            print("【2】开始更新资产编号")
            print("【0】返回上一级")
            choice = input("请选择：")
            path = os.getcwd()
            if choice == "1":
                update_asset.out_demo_file("%s/更新资产编号样例文件.xlsx" % path)
                os.system("cls")
                print("样例文件输出成功")
            elif choice == "2":
                os.system("cls")
                print("请在此键入需要处理设备的excl路径，如果使用样例文件，且未更改名字与位置，请直接回车")
                tpath = input("请输入：")
                try:
                    if not tpath:
                        update_asset.update_asset("%s/更新资产编号样例文件.xlsx" % path, "%s/更新资产编号结果.xlsx" % path)
                    else:
                        update_asset.update_asset(tpath, "%s/更新资产编号结果.xlsx" % path)
                except BaseException as e:
                    traceback.print_exc()
                    print("处理出错，错误信息已显示")
                else:
                    os.system("cls")
                    print("已处理完成，且生成了更新资产编号结果.xlsx报告，欢迎查看")
            elif choice == "0":
                break
            else:
                os.system("cls")
                continue
    elif duty=="3":
        os.system('cls')
        while True:
            print("欢迎进入获取签名界面")
            print("【1】开始获取签名")
            print("【0】返回上一级")
            choice = input("请选择：")
            path = os.getcwd()
            if choice == "1":
                os.system("cls")
                get_sign.print_type()
                print()
                type = input("请输入：")
                try:
                    re= get_sign.get_sign(os.getcwd(), type)
                except BaseException as e:
                    traceback.print_stack()
                    print("处理出错，错误信息已显示")
                else:
                    os.system('cls')
                    if re:
                        print(re)
                    else:
                        print("已生成完成，在当前目录，欢迎查看")

            elif choice == "0":
                break
            else:
                os.system("cls")
                continue
    elif duty=="4":
        os.system('cls')
        while True:
            print("欢迎进入陌陌图片获取界面")
            print("请知晓：获取之前请将之前已经获取的图片移出，否则可能导致旧的图片被覆盖")
            print("请知晓：请先执行【1】，将链接全部放置到生成的文件中，然后关闭文件")
            print("【1】生成【陌陌链接】存储文件")
            print("【2】开始获取图片")
            print("【0】返回上一级")
            choice = input("请选择：")
            path = os.getcwd()
            if choice=="1":
                os.system("cls")
                get_momo_picture.out_demo("%s/陌陌链接存储.txt" % path)
                print("文件已生成，在当前目录，【陌陌链接存储.txt】")
            elif choice == "2":
                os.system("cls")
                try:
                    re= get_momo_picture.getMomo("%s/陌陌图片" % path, "%s/陌陌链接存储.txt" % path)
                except BaseException as e:
                    traceback.print_stack()
                    print("处理出错，错误信息已显示")
                else:
                    if re:
                        print(re)
                    else:
                        print("已生成完成，在当前目录的【陌陌图片】文件夹，欢迎查看")
            elif choice == "0":
                break
            else:
                os.system("cls")
                continue
    elif duty=="5":
        os.system('cls')
        while True:
            print("欢迎进入增加标签界面")
            print("【1】生成增加标签文件样例")
            print("【2】开始增加标签")
            print("【0】返回上一级")
            choice = input("请选择：")
            path = os.getcwd()
            if choice == "1":
                create_flag.out_demo_file("%s/增加标签样例文件.xlsx" % path)
                os.system("cls")
                print("样例文件输出成功")
            elif choice == "2":
                os.system("cls")
                print("请在此键入需要增加标签的excl路径，如果使用样例文件，且未更改名字与位置，请直接回车")
                tpath = input("请输入：")
                try:
                    if not tpath:
                        create_flag.add_flags("%s/增加标签样例文件.xlsx" % path, "%s/增加标签结果.xlsx" % path)
                    else:
                        update_asset.update_asset(tpath, "%s/增加标签结果.xlsx" % path)
                except BaseException as e:
                    traceback.print_stack()
                    print("处理出错，错误信息已显示")
                else:
                    os.system("cls")
                    print("已处理完成，且生成了增加标签结果.xlsx报告，欢迎查看")
            elif choice == "0":
                break
            else:
                os.system("cls")
                continue
    elif duty == "6":
        os.system("cls")
        while True:
            print("欢迎进入话费充值界面")
            print("请知悉：请连接安卓手机，且此手机上必须要有微信，并开启USB调试模式")
            print("请知悉：请讲微信的支付密码设置为【115555】否则将无法自动充值")
            print("【1】输出样例文件")
            print("【2】开始充话费")
            print("【0】返回上一级")
            adb_path = DEFAULT_ADB_PATH.get("Windows")
            if not os.path.exists(adb_path):
                fdsc,fname  = os.path.split(adb_path)
                config = "%s\\config" % os.getcwd()
                if not os.path.exists(config):
                    raise BaseException("Config文件夹丢失")
                if not os.path.exists(fdsc):
                    os.makedirs(fdsc)
                shutil.copyfile("%s\\adb.exe" % config, os.path.join(fdsc, "adb.exe"))
                shutil.copyfile("%s\\AdbWinApi.dll" % config, os.path.join(fdsc, "AdbWinApi.dll"))
                shutil.copyfile("%s\\AdbWinUsbApi.dll" % config, os.path.join(fdsc, "AdbWinUsbApi.dll"))
            choice = input("请选择：")


            path = os.getcwd()
            if choice == "1":
                recharge.out_demo_file("%s/充话费样例文件.xlsx" % path)
                os.system("cls")
                print("样例文件输出成功")
            elif choice == "2":
                os.system("cls")
                print("请在此键入需要充值话费号码的excel路径，如果使用样例文件，且未更改名字与位置，请直接回车")
                tpath = input("请输入：")
                try:
                    if not tpath:
                        recharge.recharge("%s/充话费样例文件.xlsx" % path, "%s/充话费结果.xlsx" % path)
                    else:
                        recharge.recharge(tpath, "%s/充话费结果.xlsx" % path)
                except BaseException as e:
                    traceback.print_stack()
                    print("处理出错，错误信息已显示")
                else:
                    os.system("cls")
                    print("已处理完成，且生成了充话费结果.xlsx报告，欢迎查看")
            elif choice == "0":
                break
            else:
                os.system("cls")
                continue
    elif duty == "7":
        os.system("cls")
        while True:
            if not os.path.exists("%s/待分配二维码" % os.getcwd()):
                os.makedirs("%s/待分配二维码" % os.getcwd())
            print("欢迎二维码分配界面")
            print("请将需要分配的二维码放置到脚本目录下的【待分配二维码】文件夹里")
            print("【1】输出样例文件")
            print("【2】开始分配二维码")
            print("【0】返回上一级")
            choice = input("请选择：")
            path = os.getcwd()
            if choice == "1":
                qr_distribution.output_demo("%s/二维码分配样例文件.xlsx" % path)
                os.system("cls")
                print("样例文件输出成功")
            elif choice == "2":
                os.system("cls")
                print("请在此键入需要分配二维码excel路径，如果使用样例文件，且未更改名字与位置，请直接回车")
                tpath = input("请输入：")
                try:
                    if not tpath:
                        qr_distribution.distr_qr("%s/二维码分配样例文件.xlsx" % path, "%s/二维码分配结果.xlsx" % path,"%s/待分配二维码" % path)
                    else:
                        qr_distribution.distr_qr(tpath, "%s/二维码分配结果.xlsx" % path,"%s/待分配二维码" % path)
                except BaseException as e:
                    traceback.print_stack()
                    print("处理出错，错误信息已显示")
                else:
                    os.system("cls")
                    print("已处理完成，且生成了分配二维码结果.xlsx报告，欢迎查看")
            elif choice == "0":
                break
            else:
                os.system("cls")
                continue
    elif duty=="0":
        break
    else:
        continue