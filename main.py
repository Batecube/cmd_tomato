import threading
import time
import random
import sys
import datetime #导入相关库
sys.setrecursionlimit(1000000) #增加递归上限
f3=open("data.txt","r",encoding="utf-8-sig")
rdln = f3.readlines()
rdln = [i.rstrip() for i in rdln]
lnwdorg =(eval(rdln[1]))
lnwdmn =(eval(rdln[2]))
rvwdorg =(eval(rdln[3]))
rvwdmn =(eval(rdln[4]))
fswdorg =(eval(rdln[5]))
fswdmn =(eval(rdln[6])) #读取用户数据
lnmode = "ln"
tmtgs = 0
gettmttime = 25
getrsttime = 5
gettmttime2 = gettmttime
getrsttime2 = getrsttime
tnum = 0
starttime=0
lnwdlen=len(lnwdorg)+len(rvwdorg)+len(fswdorg) #以上均为初始化

def startsave(): #保存部分
    global gettmttime, getrsttime, getretime, tmtgs, gettmttime2, getrsttime2, tnum, lnwdlen, rvwdorg, fswdorg, data, getdata, rvwdmn, fswdmn, lnwdmn, lnmode, lnwdorg
    print("*保存中...")
    f3 = open("data.txt", "w", encoding="utf-8-sig")
    data[0] = tmtgs
    expdata = ','.join([str(word) for word in data])
    expdata1 = "','".join([str(word1) for word1 in lnwdorg])
    expdata2 = "','".join([str(word2) for word2 in lnwdmn])
    expdata3 = "','".join([str(word3) for word3 in rvwdorg])
    expdata4 = "','".join([str(word4) for word4 in rvwdmn])
    expdata5 = "','".join([str(word5) for word5 in fswdorg])
    expdata6 = "','".join([str(word6) for word6 in fswdmn])
    if lnwdorg == []:
        d1 = ""
    else:
        d1 = "'"
    if lnwdmn == []:
        d2 = ""
    else:
        d2 = "'"
    if rvwdorg == []:
        d3 = ""
    else:
        d3 = "'"
    if rvwdmn == []:
        d4 = ""
    else:
        d4 = "'"
    if fswdorg == []:
        d5 = ""
    else:
        d5 = "'"
    if fswdmn == []:
        d6 = ""
    else:
        d6 = "'"
    f3.write(
        "[" + expdata + "]\n" + "["+d1+ expdata1 +d1+"]\n" + "["+d2+ expdata2 +d2+"]\n" +"["+d3+ expdata3 +d3+"]\n" + "["+d4+ expdata4 +d4+"]\n" + "["+d5+ expdata5 +d5+"]\n" +"["+d6+ expdata6 +d6+"]\n")
    #以上为在文件中构造多项列表
    f3.close()
    print("保存成功")


def starttmt(): #判断当前学习模式部分
    global gettmttime, getrsttime, getretime, tmtgs, gettmttime2, getrsttime2, lnmode,data
    gettmttime = gettmttime2
    getrsttime = getrsttime2
    if lnmode == "ln" and getretime > 0:
        print("*番茄开始(学习)！")
        gettmttime *= 60
        while gettmttime > 0:
            time.sleep(1)#建议修改以改变时间，减少测试时间
            gettmttime -= 1
            if lnmode=="quit":
                getretime=0
                break
        if not lnmode=="quit":
            lnmode = "restafln"
    elif lnmode == "restafln" and getretime > 0:
        print("*学习时间已结束，进入" + str(getrsttime) + "分钟休息时间\n[警告]请不要对键盘进行任何操作，否则可能导致一些无法预料到的结果！！")
        getrsttime *= 60
        while getrsttime > 0:
            time.sleep(1)#建议修改以改变时间，减少测试时间
            getrsttime -= 1
        tmtgs += 1
        print("*休息时间已结束，获得1个番茄,进入下一轮回")
        getretime -= 1
        lnmode = "rv"
        print("*还剩" + str(getretime) + "次轮回")
    elif lnmode == "rv" and getretime > 0:
        print("*番茄开始（复习）！")
        gettmttime *= 60
        while gettmttime > 0:
            time.sleep(1)#建议修改以改变时间，减少测试时间
            gettmttime -= 1
            if lnmode=="quit":
                getretime=0
                break
        if not lnmode == "quit":
            lnmode = "restafrv"
    elif lnmode == "restafrv" and getretime > 0:
        print("*复习时间已结束，进入" + str(getrsttime) + "分钟休息时间\n[警告]请不要对键盘进行任何操作，否则可能导致一些无法预料到的结果！！")
        getrsttime *= 60
        while getrsttime > 0:
            time.sleep(1)#建议修改以改变时间，减少测试时间
            getrsttime -= 1
        tmtgs += 1
        print("*休息时间已结束，获得1个番茄,进入下一轮回")
        getretime -= 1
        lnmode = "ln"
        print("*还剩" + str(getretime) + "次轮回")


def startln(): #学习复习主要逻辑部分
    time.sleep(0.1)
    global lnwdorg, lnwdmn, lnmode, getretime, tst, rectst,rvwdorg,rvwdmn,lnwdlen,fswdmn,fswdorg
    recordtruere = getretime
    time.sleep(0.1)
    if lnmode == "ln":
        print("*现在开始学习，剩余" + str(len(lnwdorg)) + "个单词")
        while len(lnwdorg) != 0 and lnmode == "ln" and recordtruere == getretime:
            wantchoosewd = random.randint(0, len(lnwdorg) - 1)
            print("[进度"+str(lnwdlen-len(lnwdorg))+"/"+str(lnwdlen)+"][剩余时间："+str(gettmttime)+"(sec)]"+lnwdorg[wantchoosewd])
            def tryget():
                global lnwdorg, lnwdmn, lnmode, getretime, tst, rectst, rvwdorg, rvwdmn, lnwdlen
                getuserrepeat=str(input("请输入:1.认识 2.不认识： "))
                if getuserrepeat=="1":
                    rvwdorg.append(lnwdorg[wantchoosewd])
                    rvwdmn.append(lnwdmn[wantchoosewd])
                    print("释义："+lnwdmn[wantchoosewd])
                    del lnwdorg[wantchoosewd]
                    del lnwdmn[wantchoosewd]
                elif getuserrepeat=="2":
                    print("释义：" + lnwdmn[wantchoosewd])
                elif getuserrepeat=="":
                    tryget()
                elif getuserrepeat[0]=='''/''':
                    if getuserrepeat=='''/time''':
                        today = datetime.datetime.today()
                        if today.hour<10:
                            hour = ("0"+str(today.hour))
                        else:
                            hour = str(today.hour)
                        if today.minute<10:
                            mint = ("0"+str(today.minute))
                        else:
                            mint = str(today.minute)
                        if today.second < 10:
                            sec = ("0" + str(today.second))
                        else:
                            sec = str(today.second)
                        print("*现在时间：{}:{}.{}".format(hour,mint,sec))
                        tryget()
                    elif getuserrepeat == '''/tmt''':
                        if gettmttime<=0:
                            print("*时间已结束")
                            tryget()
                        else:
                            print("*剩余时间："+str(gettmttime)+"(sec)")
                            tryget()
                    elif getuserrepeat == '''/quit''':
                        print("*尝试强制退出，本次学习你不会得到番茄")
                        lnmode="quit"
                    else:
                        print("*未知命令！")
                        tryget()
                else:
                    tryget()
            tryget()
        if len(lnwdorg) == 0:
            print("[进度"+str(lnwdlen-len(lnwdorg))+"/"+str(lnwdlen)+"][剩余时间："+str(gettmttime)+"(sec)]"+"*你已经将词书中的内容学习完成了\n[警告]请不要对键盘进行任何操作，否则可能导致一些无法预料到的结果！！")
    elif lnmode == "rv": 
        rvwdlen=len(rvwdorg)+len(fswdorg)
        print("现在开始复习，剩余" + str(len(rvwdorg)) + "个单词")
        while len(rvwdorg) != 0 and lnmode == "rv" and recordtruere == getretime:
            wantchoosewd = random.randint(0, len(rvwdorg) - 1)
            print("[进度"+str(rvwdlen-len(rvwdorg))+"/"+str(rvwdlen)+"][剩余时间："+str(gettmttime)+"(sec)]"+rvwdorg[wantchoosewd])
            def tryget1():
                global lnwdorg, lnwdmn, lnmode, getretime, tst, rectst, rvwdorg, rvwdmn, lnwdlen,fswdorg,fswdmn
                getinput=input("*返回回车或任意值查看释义，即表示已过目")
                if getinput=="":
                    fswdorg.append(rvwdorg[wantchoosewd])
                    fswdmn.append(rvwdmn[wantchoosewd])
                    print("释义：" + rvwdmn[wantchoosewd])
                    del rvwdorg[wantchoosewd]
                    del rvwdmn[wantchoosewd]
                elif getinput[0]== '''/''':
                    if getinput=='''/time''':
                        today = datetime.datetime.today()
                        if today.hour < 10:
                            hour = ("0" + str(today.hour))
                        else:
                            hour = str(today.hour)
                        if today.minute < 10:
                            mint = ("0" + str(today.minute))
                        else:
                            mint = str(today.minute)
                        if today.second < 10:
                            sec = ("0" + str(today.second))
                        else:
                            sec = str(today.second)
                        print("*现在时间：{}:{}.{}".format(hour, mint, sec))
                        tryget1()
                    elif getinput == '''/tmt''':
                        if gettmttime<=0:
                            print("*时间已结束")
                            tryget1()
                        else:
                            print("*剩余时间："+str(gettmttime)+"(sec)")
                            tryget1()
                    elif getinput == '''/quit''':
                        print("*尝试强制退出，本次学习你不会得到番茄")
                        lnmode = "quit"
                    else:
                        print("*未知命令！")
                        tryget1()
            tryget1()
        if len(rvwdorg) == 0:
            print("[进度"+str(rvwdlen-len(rvwdorg))+"/"+str(rvwdlen)+"][剩余时间："+str(gettmttime)+"(sec)]"+"*你已完成了本次复习,开始复习已完成的单词")
            while len(fswdorg) != 0 and lnmode == "rv" and recordtruere == getretime:
                wantchoosewd = random.randint(0, len(fswdorg) - 1)
                print("[已完成][剩余时间：" + str(gettmttime) + "(sec)]" + fswdorg[wantchoosewd])
                def tryget2():
                    global lnwdorg, lnwdmn, lnmode, getretime, tst, rectst, rvwdorg, rvwdmn, lnwdlen,fswdorg,fswdmn
                    getinput=input("*返回回车或任意值查看释义，即表示已过目")
                    if getinput == "":
                        print("释义：" + fswdmn[wantchoosewd])
                    elif getinput[0] == '''/''':
                        if getinput == '''/time''':
                            today = datetime.datetime.today()
                            if today.hour < 10:
                                hour = ("0" + str(today.hour))
                            else:
                                hour = str(today.hour)
                            if today.minute < 10:
                                mint = ("0" + str(today.minute))
                            else:
                                mint = str(today.minute)
                            if today.second < 10:
                                sec = ("0" + str(today.second))
                            else:
                                sec = str(today.second)
                            print("现在时间：{}:{}.{}".format(hour, mint, sec))
                            tryget2()
                        elif getinput == '''/tmt''':
                            if gettmttime<=0:
                                print("*时间已结束")
                                tryget2()
                            else:
                                print("*剩余时间："+str(gettmttime)+"(sec)")
                                tryget2()
                        elif getinput == '''/quit''':
                            print("*尝试强制退出，本次学习你不会得到番茄")
                            lnmode = "quit"
                        else:
                            print("*未知命令！")
                            tryget2()
                tryget2()
    if lnmode=="quit":
        pass

def get_tmt_num(): #判断用户所输入的番茄个数部分
    global getretime,lnwdorg,rvwdorg,lnmode
    if len(lnwdorg)==0:
        if len(rvwdorg)==0:
            print("[警告]你已完成所有单词，不支持设置番茄个数，直接开始复习模式！！")
            lnmode = "rv"
            getretime=1
        else:
            print("[警告]你已学完所有单词，不支持设置番茄个数，直接开始复习已完成单词模式！！")
            lnmode = "rv"
            getretime = 1
    else:
        try:
            getretime = int(input("请设置番茄的个数\n*必须为偶数：第一个番茄为学习时间，第二个番茄为复习时间，其中番茄专注时间为25min，休息时间为5min：\n"))
        except ValueError:
            print("[提示]输入值内容不规范，请重新输入")
            get_tmt_num()
        else:
            if getretime % 2 == 0 and getretime != 0:
                pass
            else:
                print("[提示]输入值内容不规范，请重新输入")
                get_tmt_num()

def ProgramStart(): #总程序主控部分
    global starttime
    if starttime==0:
        f5 = open("logo.txt", "r")
        logo = f5.read()
        print(logo)
        starttime+=1
    print("主页\n")
    global gettmttime, getrsttime, getretime, tmtgs, gettmttime2, getrsttime2, tnum,lnwdlen,rvwdorg,fswdorg,data,getdata,rvwdmn,fswdmn,lnwdmn,lnmode,lnwdorg,tmtgs
    lnmode="ln"
    f3 = open("data.txt", "r", encoding="utf-8-sig")
    getdata = f3.readline()
    data = eval(getdata)
    tmtgs=data[0]
    f3.close()
    if tmtgs==0:
        print('*欢迎使用番茄背单词，如是第一次使用，建议先查阅"README.md"说明文档')
    if len(lnwdorg)==0:
        if len(rvwdorg)==0:
            print("[提示]你已完成所有的单词了，如需重新学习，请输入'3'以清除数据")
        else:
            print("[提示]你已学习所有的单词了，但仍有"+str(len(rvwdorg))+"个单词需复习")
            lnmode = "rv"
    getstartmode = str(input("选择模式：\n1.开始学习\n2.查看状态\n3.智能翻译\n4.清除数据\n5.获取帮助\n6.安全退出\n"))
    if getstartmode == "1":
        get_tmt_num()
        def ThreadStart(): #启用多线程部分
            global tmtgs,data,getdata
            if getretime > 0:
                threads = []
                t1 = threading.Thread(target=startln)
                threads.append(t1)
                t2 = threading.Thread(target=starttmt)
                threads.append(t2)
                if __name__ == "__main__":
                    for t in threads:
                        t.start()
                    for t in threads:
                        t.join()
                startsave()
                ThreadStart()
            else:
                ProgramStart()
        ThreadStart()
    elif getstartmode == "2":
        print("你的状态：\n所有单词："+str(lnwdlen)+"\n已学习单词："+str(len(rvwdorg)+len(fswdorg)))
        print("未复习单词：" + str(len(rvwdorg)) + "\n已完成单词：" + str(len(fswdorg)))
        print("你现在拥有的番茄：" + str(tmtgs))
        ProgramStart()
    elif getstartmode == "3":
        print('*由于开源不再开放')
        ProgramStart()
    elif getstartmode == "4":
        def gettruere():
            global gettmttime, getrsttime, getretime, tmtgs, gettmttime2, getrsttime2, tnum, lnwdlen, rvwdorg, fswdorg, data, getdata, rvwdmn, fswdmn, lnwdmn, lnmode,lnwdorg
            qcnd=str(input("请问要清除哪些数据？\n1.仅学习进度\n2.全部数据\n3.取消\n"))
            if qcnd=="1":
                gettrue = str(input("该操作将清楚所有用户数据！！是否继续？\n1.我明白我在做什么 2.取消: "))
                if gettrue == "1":
                    rvwdorg = []
                    rvwdmn = []
                    fswdorg = []
                    fswdmn = []
                    f1 = open("lnwdorg.txt", "r", encoding="utf-8-sig")
                    f2 = open("lnwdmn.txt", "r", encoding="utf-8-sig")
                    lnwdorg = f1.readlines()
                    lnwdorg = [i.rstrip() for i in lnwdorg]
                    lnwdmn = f2.readlines()
                    lnwdmn = [j.rstrip() for j in lnwdmn]
                    f1.close()
                    f2.close()
                    lnmode = "ln"
                    gettmttime = 25
                    getrsttime = 5
                    gettmttime2 = gettmttime
                    getrsttime2 = getrsttime
                    tnum = 0
                    lnwdlen = len(lnwdorg)
                    f3 = open("data.txt", "w", encoding="utf-8-sig")
                    data[0] = tmtgs
                    expdata = ','.join([str(word) for word in data])
                    expdata1 = "','".join([str(word1) for word1 in lnwdorg])
                    expdata2 = "','".join([str(word2) for word2 in lnwdmn])
                    expdata3 = "','".join([str(word3) for word3 in rvwdorg])
                    expdata4 = "','".join([str(word4) for word4 in rvwdmn])
                    expdata5 = "','".join([str(word5) for word5 in fswdorg])
                    expdata6 = "','".join([str(word6) for word6 in fswdmn])
                    if not lnwdorg:
                        d1 = ""
                    else:
                        d1 = "'"
                    if not lnwdmn:
                        d2 = ""
                    else:
                        d2 = "'"
                    if not rvwdorg:
                        d3 = ""
                    else:
                        d3 = "'"
                    if not rvwdmn:
                        d4 = ""
                    else:
                        d4 = "'"
                    if not fswdorg:
                        d5 = ""
                    else:
                        d5 = "'"
                    if not fswdmn:
                        d6 = ""
                    else:
                        d6 = "'"
                    f3.write(
                        "[" + expdata + "]\n" + "[" + d1 + expdata1 + d1 + "]\n" + "[" + d2 + expdata2 + d2 + "]\n" + "[" + d3 + expdata3 + d3 + "]\n" + "[" + d4 + expdata4 + d4 + "]\n" + "[" + d5 + expdata5 + d5 + "]\n" + "[" + d6 + expdata6 + d6 + "]\n")
                    f3.close()
                    print("已清除学习进度")
                    ProgramStart()
                elif gettrue == "2":
                    ProgramStart()
                else:
                    gettruere()
            elif qcnd=="2":
                gettrue=str(input("该操作将清楚所有用户数据！！是否继续？\n1.我明白我在做什么 2.取消: "))
                if gettrue=="1":
                    rvwdorg = []
                    rvwdmn = []
                    fswdorg = []
                    fswdmn = []
                    f1 = open("lnwdorg.txt", "r", encoding="utf-8-sig")
                    f2 = open("lnwdmn.txt", "r", encoding="utf-8-sig")
                    lnwdorg = f1.readlines()
                    lnwdorg = [i.rstrip() for i in lnwdorg]
                    lnwdmn = f2.readlines()
                    lnwdmn = [j.rstrip() for j in lnwdmn]
                    f1.close()
                    f2.close()
                    lnmode = "ln"
                    tmtgs = 0
                    gettmttime = 25
                    getrsttime = 5
                    gettmttime2 = gettmttime
                    getrsttime2 = getrsttime
                    tnum = 0
                    lnwdlen = len(lnwdorg)
                    f3 = open("data.txt", "w", encoding="utf-8-sig")
                    data[0] = tmtgs
                    expdata = ','.join([str(word) for word in data])
                    expdata1 = "','".join([str(word1) for word1 in lnwdorg])
                    expdata2 = "','".join([str(word2) for word2 in lnwdmn])
                    expdata3 = "','".join([str(word3) for word3 in rvwdorg])
                    expdata4 = "','".join([str(word4) for word4 in rvwdmn])
                    expdata5 = "','".join([str(word5) for word5 in fswdorg])
                    expdata6 = "','".join([str(word6) for word6 in fswdmn])
                    if not lnwdorg:
                        d1 = ""
                    else:
                        d1 = "'"
                    if not lnwdmn:
                        d2 = ""
                    else:
                        d2 = "'"
                    if not rvwdorg:
                        d3 = ""
                    else:
                        d3 = "'"
                    if not rvwdmn:
                        d4 = ""
                    else:
                        d4 = "'"
                    if not fswdorg:
                        d5 = ""
                    else:
                        d5 = "'"
                    if not fswdmn:
                        d6 = ""
                    else:
                        d6 = "'"
                    f3.write(
                        "[" + expdata + "]\n" + "[" + d1 + expdata1 + d1 + "]\n" + "[" + d2 + expdata2 + d2 + "]\n" + "[" + d3 + expdata3 + d3 + "]\n" + "[" + d4 + expdata4 + d4 + "]\n" + "[" + d5 + expdata5 + d5 + "]\n" + "[" + d6 + expdata6 + d6 + "]\n")
                    f3.close()
                    print("已清除所有数据")
                    ProgramStart()
                elif gettrue=="2":
                    ProgramStart()
                else:
                    gettruere()
            elif qcnd == "3":
                ProgramStart()
            else:
                gettruere()
        gettruere()
    elif getstartmode == "5":
        print('''命令帮助：
        你可以在学习或复习模式中使用一下命令

        /time -- 获取当前时间
        /tmt -- 番茄钟剩余时间
        /quit -- 退出学习/复习，返回主页

        更多使用提示请查看说明文档！
        ''')
        ProgramStart()
    elif getstartmode == "6":
        startsave()
        print("*已完成，退出成功")
        exit()
    else:
        ProgramStart()

ProgramStart() #主程序主控的入口
