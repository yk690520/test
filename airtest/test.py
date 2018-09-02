# -*- encoding=utf8 -*-
__author__ = "admin"

from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
import random

auto_setup(__file__)



def battle(boolearn):
    while boolearn:
        if poco(text="离开").exists():
            break
        try:
            poco("StarRoot").click()
            poco("RoleInfoBox1").click()
            
        except:
            continue
    if poco("Confirm").exists():
        print(poco("Lbl_Content").get_text())
        poco("btn_close").click()
    poco(text="离开").wait_for_appearance()
    poco("quan01").click()   #副本战斗
    
    
def clicktime(flag_1=0,flag_2=0):
    for i in range(flag_1):
        poco("quan01").click()
        sleep(1)
    for i in range(flag_2):
        poco(texture="GuideView_WordBG").click()
        sleep(2)
    
def Logginguide():
    guide = [("Country1"),poco("Country2"),poco("Country3")]
    ran = random.randint(0,2)
    guide[ran].click()  #随机选择阵营
    poco("okBtn").click()#确定
    sleep(2)
    poco("icon").wait_for_appearance()
    sleep(3)
    poco(texture="GuideView_WordBG").click()
    clicktime(2)
    sleep(5)
    poco(text="眼下城中资源十分紧缺，应当先修建一些资源建筑。").wait_for_appearance()
    clicktime(flag_2=3)  #循环3次
    buildlist=[poco("5(Clone)"),poco("2(Clone)"),poco("4(Clone)"),poco("3(Clone)")]
    for build in buildlist:
        poco(type="Button").click()
        build.click()
        poco("quan01").click()
        poco("BuildingFunctionHint(Clone)").click()
        poco(texture="GuideView_WordBG").click()
    sleep(2)
    poco(texture="GuideView_WordBG").click()
    sleep(2)
    clicktime(2)  #循环2次
    sleep(6)
    poco("quan01").click()
    poco("icon").wait_for_appearance()
    clicktime(flag_2=2)
    poco("close").click()
    clicktime(3)  #quan3次
    poco(texture="GuideView_WordBG").click()
    poco("Btn_UpgradeImmediate(Clone)").click()
    poco(texture="GuideView_WordBG").click()
    poco("close").click()
    poco(texture="MainView_FormationIcon").click()
    clicktime(2)
    poco("close").click()
    poco(texture="GuideView_WordBG").click()
    poco(texture="Duplicate").click()
    clicktime(3)  #quan3次
    sleep(6)
    while True:
        if poco(text="离开").exists():
            break
        poco("StarRoot").click()
        if poco(text="反国逆贼，何不早降！").exists():
            sleep(10)
    if poco("Confirm").exists():
        print(poco("Lbl_Content").get_text())   #捕获md5报错
        poco("btn_close").click()
    poco("iconBack").wait_for_appearance()
    poco("quan01").click()
    sleep(3)
    poco(texture="GuideView_WordBG").click()
    poco("quan01").click()
    sleep(7)
    clicktime(flag_2=2)
    poco(texture="wine_shop_inner_purple").wait_for_appearance()
    poco("quan01").click()
    poco(texture="GuideView_WordBG").click()
    poco(texture="MainView_FormationIcon").click()
    poco("10013").child("ActiveNode").child("BuildingStateHint").child("Lock").click()
    poco("quan01").click()
    poco("close").click()
    poco(texture="GuideView_WordBG").click()
    poco("RightCorner").click()
    sleep(5)
    poco("icon").wait_for_appearance()
    poco(texture="GuideView_WordBG").click()
    clicktime(3,0)  #quan3次
    poco("icon").wait_for_appearance()
    sleep(2)
    poco(texture="GuideView_WordBG").click()
    poco("Button(Clone)").click()
    poco("quan01").click()
    if not poco("PropGrid").child("BagItem")[0].exists():
        print('无首次奖励')
    poco("closeBtn(Clone)").child("close").click()
    poco("close").click()
    sleep(3)
    poco(texture="GuideView_WordBG").click()
    poco("ShowBtn(Clone)").child("Image").click()
    poco(texture="MainView_HeroIcon").click()
    poco("quan01").click()
    poco("0(Clone)").click()
    poco("quan01").click()
    poco("closeBtn").child("close").click()
    poco("close").click()
    sleep(3)
    poco(texture="GuideView_WordBG").click()
    poco(texture="Duplicate").click()
    clicktime(2)
    poco(texture="MainView_CountryIcon").click()
    sleep(5)
    battle(True)
    sleep(2)
    poco("quan01").click()
    poco(texture="GuideView_WordBG").click()
    poco("ShowBtn(Clone)").child("Image").click()
    poco(texture="MainView_FormationIcon").click()
    poco("quan01").click()
    poco(texture="GuideView_WordBG").click()
    poco("close").click()
    poco(texture="Duplicate").click()
    clicktime(2)
    poco(texture="MainView_CountryIcon").click()
    sleep(5)
    battle(True)
    sleep(5)
    poco(texture="GuideView_WordBG").click()
    poco("quan01").click()
    poco("RightCorner").click()
    sleep(5)
    poco("quan01").click()
    poco("Btn3(Clone)").click()
    poco("quan01").click()
    sleep(3)
    poco(texture="GuideView_WordBG").click()
    sleep(3)
    poco(texture="GuideView_WordBG").click()
    clicktime(3)  #quan3次
    poco("close").click()
    poco(texture="GuideView_WordBG").wait_for_appearance()
    poco(texture="GuideView_WordBG").click()
    if poco("HelpBtn").exists():
        poco("HelpBtn").click()
    else:
        sleep(10)
    poco(texture="GuideView_WordBG").wait_for_appearance()
    clicktime(flag_2=2)
    poco(texture="MainView_CircleBt_2").click()   #新手引导

poco = UnityPoco()
poco("InputID").click()  #入口
text('byl5')   #修改账号
poco("InputID").click()
if poco("LeftRegionNameWriting").get_text()=="国服-patch": #在这里修改要进的服务器
    poco("LoginnButton").click()
else:
    poco("SeverSelector").child("BGAdd").click()  #选择服务器

    while not poco(text="国服-patch").exists():
        poco("Background").swipe([0,-0.2])
        sleep(2)
    try :
        poco("22").child("ItemBG").click()
    except :
        print('有些地方错了') 
    poco(text='确定').click()
    poco("LoginnButton").click()

sleep(5)
if poco("skipBtn").exists():
    poco("skipBtn").click()
else:
    sleep(35)
poco(texture="GuideView_WordBG").click()
poco("icon").wait_for_appearance()
poco(texture="GuideView_WordBG").click()
poco("icon").wait_for_appearance()
sleep(2)
poco("icon").click()
poco(texture="GuideView_WordBG").click()
sleep(15)
if not poco(texture="GuideView_npc2").exists():
    sleep(20)
poco(texture="GuideView_npc2").wait_for_appearance()
poco(texture="GuideView_npc2").click()
poco("RoleInfoBox1").child("Panel").child("Full_effect").child("nuqizhandou_effect").child("effect").child("kuang02").click()
poco(texture="GuideView_npc2").wait_for_appearance()
poco("BG").click()
poco("quan01").click()
sleep(10)


skill =True
while True:
    if not poco("RoleInfoBox0").exists():
        break
    
    if skill == True:
        poco("StrategyGrid").child("1").child("CD").click()
        skill = False
        sleep(10)

        
    if poco("RoleInfoBox0").exists():
        try:
            poco("RoleInfoBox0").click()
            poco("RoleInfoBox1").click()
            poco("RoleInfoBox2").click()  
            poco("RoleInfoBox3").click()
        except:
            continue
    
    
sleep(3)      
poco(texture="GuideView_WordBG").click()
sleep(3)
poco(texture="GuideView_WordBG").click()
sleep(4)
poco(texture="GuideView_WordBG").click()
poco("Placeholder").click()
text('byl')    #修改名称
poco("MainLayer").click()
poco("Btn_Sure").click()
nameflag = 1
while poco(texture="Panelm_Middle_1").exists():   #名字重复判定操作
    if not poco(texture="Panelm_Middle_1").exists():
        break
    poco(texture="Button_Green_1").click()
    poco("Placeholder").click()
    text('%s%s'%(poco("InputField").child('Text').get_text(),nameflag))   
    sleep(2)
    poco("MainLayer").click()
    poco("Btn_Sure").click()
    if poco(texture="Panelm_Middle_1").exists():
        poco(texture="Button_Green_1").click()
        poco("Btn_Random").click()
        poco("Btn_Sure").click()
    
sleep(3)
poco("BG").click()
Logginguide()
        
        
        
        

        
        

    
    



    












    



    




    


    
    






    


















    
    
    



    














    



    


        

    
           
    







    































    

































