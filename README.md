# cmd_tomato
## 前言
如你所见，这是早些年写的shi山（里面有很多莫名其妙的东西）。
本人不会再作任何修改与解释，一些所涉及到安全部分的代码段（api这些）已删除。
以下是早些时候为此写的readme。

# 番茄背单词说明文档
- [简介](#简介)
- [使用方法](#使用方法)
- [提示和注意事项](#提示和注意事项)

## 简介
首先番茄工作法是一种**时间管理方法**——使用番茄工作法，选择一个待完成的任务，将番茄时间设为25分钟，专注工作，中途不允许做任何与该任务无关的事，直到番茄时钟响起，然后进行短暂休息一下（5分钟就行），然后再开始下一个番茄。每4个番茄时段多休息一会儿。

本人所制的程序将令多数学生头疼的**背单词**与**番茄工作法**结合在一起，以提高**用户学习单词的效率**。
## 使用方法
### 1. 导入词书
刚开始程序已预置473单词供学习，可以**直接运行使用**。

如需导入自己的词书，**请将英语单词与中文释义按照“lnwdorg.txt”和“lnwdmn.txt”的格式分别导入“lnwdorg.txt”和“lnwdmn.txt”两个文本文件中。**
### 2. 开始学习
打开“**主程序.py**”后，如是第一次使用，**建议在主界面返回“3”以清除数据**（该操作提示会重新载入“lnwdorg.txt”和“lnwdmn.txt”的词数数据）。

以下是主程序运行时主界面第一次运行时的样式：
                                                  
    ,--------.                          ,--.          
    '--.  .--',---. ,--,--,--. ,--,--.,-'  '-. ,---.  
       |  |  | .-. ||        |' ,-.  |'-.  .-'| .-. | 
       |  |  ' '-' '|  |  |  |\ '-'  |  |  |  ' '-' ' 
       `--'   `---' `--`--`--' `--`--'  `--'   `---'  
    主页

    *欢迎使用番茄背单词，如是第一次使用，建议先查阅"README.md"说明文档
    *你也可以访问 https://tmt.batecube.cyou/ 阅读我们的在线文档
    选择模式：
    1.开始学习
    2.查看状态
    3.智能翻译
    4.清除数据
    5.在线文档
    6.安全退出
                                                    
以上完成后，在主界面返回“1”即可开始学习，返回“1”后，会提示“**请设置番茄的个数（必须为偶数：第一个番茄为学习时间，第二个番茄为复习时间，其中番茄专注时间为25min，休息时间为5min）**”这意味着你的番茄个数必须设置为**双数**（不包括0）。其中第一个番茄是一个学习番茄，另外一个番茄是一个复习番茄。

以下是学习阶段的界面：

    [进度1/473][剩余时间：1500(sec)]beginning
    请输入:1.认识 2.不认识： 
这需要你返回"1"/"2"来告诉程序你是否认识这个单词

如果返回"1"，这个单词就被程序归纳为以学习单词，**在该阶段不会再提示该单词了**，但在接下来的复习阶段将重新对此单词进行过目。如果返回"2"，代表这个单词你不认识，仍需重新学习。

学习阶段结束后，会进入五分钟的休息阶段 。***[注意]在该阶段请不要操作键盘，可能会导致意料之外的结果！！***

休息阶段结束后，你会**获得一个番茄**，便会进入复习阶段，以下是复习阶段的界面：

    [进度0/5][剩余时间：1493(sec)]commercial
    *返回回车或任意值查看释义，即表示已过目
你只需进行回车，代表你已经复习了该单词，如果你提前复习完本次所需要复习的单词，程序将会让你复习曾经已经复习过的单词，直到番茄钟结束。

复习阶段结束后，会进入五分钟的休息阶段 。***[注意]在该阶段请不要操作键盘，可能会导致意料之外的结果！！***

休息时间结束后，你会获得一个番茄，最终回到主界面。

### 3. 查看状态
当你在主界面返回“2”时，程序将会返回列如以下内容：

    你的状态：
    所有单词：5
    已学习单词：5
    未复习单词：4
    已完成单词：1
    你现在拥有的番茄：2

### 4. 智能翻译
**[注意]请检查你是否安装了requests库，否则你无法体验到该功能！！**
你只需要输入翻译的内容回车即可：

    请输入要翻译的内容：
    What's your name?
    结果:你叫什么名字？

### 5. 关于命令
在学习和复习模式中，可以使用以下命令：

/time -- 获取当前时间

    [进度5/473][剩余时间：1497(sec)]allergic
    请输入:1.认识 2.不认识： /time
    *现在时间：13:47.34

/tmt -- 番茄钟剩余时间

    请输入:1.认识 2.不认识： /tmt
    *剩余时间：1451(sec)

/quit -- 退出学习/复习，返回主页

    请输入:1.认识 2.不认识： /quit
    *尝试强制退出，本次学习你不会得到番茄
    *保存中...
    保存成功
### 6. 退出程序
**非常不建议在程序运行之时直接暂停或关闭程序**，通过在主界面返回“6”，如过出现以下输出结果，便代表程序已正常退出：

    *保存中...
    保存成功
    *已完成，退出成功

**在其他方面只需根据命令行提示去做即可。**

## 提示和注意事项
1. 当程序程序出现该提示时：

        *保存中...
    请不要在此时停止程序，可能会导致数据的丢失，直到出现：
    
        保存成功

    你才可以关闭程序（**尽管不建议这么做**）

2. 当你学习所有单词或完成所有单词，不支持设置番茄个数，一但开始学习将**直接进入复习阶段**。
3. 考虑 25min+5min+25min+5min 的学习测试时间过久，如要测试程序，**建议将以下有备注的代码段的 sleep() 值减小以加快学习进程**：

        def starttmt():
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



感谢你使用该程序！！