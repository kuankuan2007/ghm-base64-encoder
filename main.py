import tkinter
from tkinter import ttk,messagebox,filedialog,simpledialog 
import base64
import os
import sys
import threading
import pyperclip
import windnd
threadingNumber=10
def keyControl(event):
    if(12==event.state and (event.keysym in ["c","a"])):
        return
    else:
        return "break"
def resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        #base_path = os.path.abspath(".")
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

def resetEntry(entry,text="",readonly=False):
    entry.config(state="normal")
    entry.delete(0,tkinter.END)
    entry.insert(0,text)
    if readonly:
        entry.config(state="readonly")
def aboutShower():
    auboutScreen=tkinter.Tk()
    auboutScreen.iconbitmap(resource_path(os.path.join("logo.ico")))
    auboutScreen.title("关于")

    messageBox=tkinter.Frame(auboutScreen)
    messageBox.grid(row=0,column=0)

    createrTitle=tkinter.Label(messageBox,text="作者:")
    createrTitle.grid(row=0,column=0,sticky="W",pady=2)
    creater=tkinter.Entry(messageBox)
    creater.insert(0,"宽宽")
    creater.config(state="readonly")
    creater.grid(row=0,column=1,sticky="W")

    openSourceTitle=tkinter.Label(messageBox,text="开源地址")
    openSourceTitle.grid(row=1,column=0,sticky="W",pady=2)
    openSource=tkinter.Entry(messageBox,fg="blue",cursor="hand2")
    def startOpenSorce(event):
        os.system("start https://gitee.com/kuankuan2007/ghm-base64-encoder/")
    openSource.bind("<Button-1>", startOpenSorce)
    openSource.insert(0,"gitee")
    openSource.config(state="readonly")
    openSource.grid(row=1,column=1,sticky="W")

    helpTitle=tkinter.Label(messageBox,text="帮助")
    helpTitle.grid(row=2,column=0,sticky="W",pady=2)
    help=tkinter.Entry(messageBox,fg="blue",cursor="hand2")
    help.insert(0,"帮助文档")
    def startHelp(event):
        os.system("start https://kuankuan2007.gitee.io/docs/ghm-base64-encoder/")
    help.bind("<Button-1>", startHelp)
    help.config(state="readonly")
    help.grid(row=2,column=1,sticky="W")

    createrQQTitle=tkinter.Label(messageBox,text="作者QQ:")
    createrQQTitle.grid(row=3,column=0,sticky="W",pady=2)
    createrQQ=tkinter.Entry(messageBox)
    createrQQ.insert(0,"2163826131")
    createrQQ.config(state="readonly")
    createrQQ.grid(row=3,column=1,sticky="W")
    
    createrUrlTitle=tkinter.Label(messageBox,text="作者主页:")
    createrUrlTitle.grid(row=4,column=0,sticky="W",pady=2)
    createrUrl=tkinter.Entry(messageBox,fg="blue",cursor="hand2")
    createrUrl.insert(0,"宽宽2007的小天地")
    def startURL(event):
        os.system("start https://kuankuan2007.gitee.io")
    createrUrl.bind("<Button-1>", startURL)
    createrUrl.config(state="readonly")
    createrUrl.grid(row=4,column=1,sticky="W")

    createrGiteeTitle=tkinter.Label(messageBox,text="作者Gitee:")
    createrGiteeTitle.grid(row=5,column=0,sticky="W",pady=2)
    createrGitee=tkinter.Entry(messageBox,fg="blue",cursor="hand2")
    createrGitee.insert(0,"宽宽2007")
    def startGitee(event):
        os.system("start https://gitee.com/kuankuan2007")
    createrGitee.bind("<Button-1>", startGitee)
    createrGitee.config(state="readonly")
    createrGitee.grid(row=5,column=1,sticky="W")

    createrWeiXinPayTitle=tkinter.Label(messageBox,text="赞助作者")
    createrWeiXinPayTitle.grid(row=6,column=0,sticky="W",pady=2)
    createrWeiXinPay=tkinter.Entry(messageBox,fg="blue",cursor="hand2")
    createrWeiXinPay.insert(0,"微信支付")
    def startWeiXinPayTitle(event):
        os.system("start https://kuankuan2007.gitee.io/WeiXinPay.png")
    createrWeiXinPay.bind("<Button-1>", startWeiXinPayTitle)
    createrWeiXinPay.config(state="readonly")
    createrWeiXinPay.grid(row=6,column=1,sticky="W")

    auboutScreen.mainloop()

def showTextRetsult(content):
    def copyContent():
        pyperclip.copy(content)
        messagebox.showinfo("内容已复制","本文本到系统剪切板,使用Ctrl+v粘贴",parent=showRetsult)
    showRetsult=tkinter.Toplevel(mainScreen)
    showRetsult.resizable(width=False,height=False)
    showRetsult.iconbitmap(resource_path(os.path.join("logo.ico")))
    showRetsult.title("结果")
    showRetsult.grab_set()
    retsultFrame=tkinter.Frame(showRetsult)
    retsultFrame.grid(row=0,column=0)

    retsultBoxScrollbar=ttk.Scrollbar(retsultFrame)
    retsultBoxScrollbar.grid(column=1, row=0,sticky="NSW")
    retsultBox=tkinter.Text(retsultFrame,yscrollcommand=retsultBoxScrollbar.set)
    retsultBoxScrollbar.config(command=retsultBox.yview)
    retsultBox.insert(0.0,content)
    retsultBox.bind("<Key>", keyControl)
    retsultBox.grid(row=0,column=0,sticky="W")

    buttonFrame=tkinter.Frame(showRetsult)
    buttonFrame.grid(row=1,column=0,sticky="E")
    
    copyButton=ttk.Button(buttonFrame,text="复制",command=copyContent)
    copyButton.grid(row=0,column=0,sticky="E")

    closeButton=ttk.Button(buttonFrame,text="关闭",command=showRetsult.destroy)
    closeButton.grid(row=0,column=1,sticky="E")
def encodingFiles(files):
    filename=filedialog.asksaveasfilename(title="请选择保存位置",filetypes=[("GHM-BASE64", ".GHMBASE64")],defaultextension=".ghm-base64")
    if not filename:
        return
    showProgress=tkinter.Toplevel(mainScreen)
    showProgress.resizable(width=False,height=False)
    showProgress.iconbitmap(resource_path(os.path.join("logo.ico")))
    showProgress.title("编码进度")
    showProgress.grab_set()
    
    title1=tkinter.Label(showProgress,text="进度:打开文件")
    title1.grid(row=0,column=0,sticky="W",pady=2,padx=2)

    title2=tkinter.Label(showProgress,text="正在处理:",width="40",anchor="w")
    title2.grid(row=1,column=0,sticky="W",pady=2,padx=2)

    progressbar=ttk.Progressbar(showProgress,mode="indeterminate",length="300")
    progressbar.grid(row=2,column=0,sticky="W",pady=2,padx=2)
    def encodeingFile():
        try:
            content=[]
            for i in files:
                title2.config(text="正在处理:"+i)
                f=open(i,"rb")
                content.append((f,i))
            
            with open(filename,"w") as f:
                progressbar.config(mode="determinate")
                progressbar.config(value=0.0)
                title1.config(text="进度:正在编码")
                title2.config(text="正在处理:")
                f.write("#SAVING WITH GHM-BASE64")
                for i in range(len(content)):
                    progressbar.config(value=(i+1)*100/(len(content)))
                    title1.config(text="进度:正在编码(%d/%d)"%(i+1,len(content)))
                    i=content[i]
                    title2.config(text=f"正在处理:{i[1]}")
                    f.write("\n#FILE|%s\n"%(os.path.split(i[1])[1]))
                    f.write(base64.b64encode(i[0].read()).decode("ansi"))
                    i[0].close()
                    f.flush()
                f.write("\n#END OF DOCUMENT")
            showProgress.destroy()
            messagebox.showinfo("编码完成","已成功对所有文件编码")
        except BaseException as e:
            if len(content)<len(files):
                messagebox.showerror("编码失败","请确认文件%s是否存在"%(files[len(content)]))
            else:
                messagebox.showerror("编码失败","意外错误\n%s:%s"%(e.__class__.__name__,str(e)))
            for i in content:
                i[0].close()
            showProgress.destroy()
    threading.Thread(target=encodeingFile,daemon=True).start()
    showProgress.mainloop()
def decodingUnknownContent(content):
    try:
        content=base64.b64decode(content)
    except:
        messagebox.showerror("错误","这段内容不是Base64编码")
    try:
        content=content.decode("ansi")
        showTextRetsult(content)
    except:
        saveFile=filedialog.asksaveasfilename(title="选择保存位置")
        if not saveFile:
            return
        with open(saveFile,"wb") as f:
            f.write(content)
        messagebox.showinfo("完成",f"文件已保存至{saveFile}")

class AboutShowerT(threading.Thread):
    def __init__(self):
        global threadingNumber
        threading.Thread.__init__(self)
        self.threadID = threadingNumber
        self.name = "关于"
        self.counter = threadingNumber
        threadingNumber+=1
    def run(self):
        aboutShower()

def aboutBooter():
    aboutShowerT=AboutShowerT()
    aboutShowerT.daemon=True
    aboutShowerT.start()
def doFiles(files):
    if len(files)>1:
        if messagebox.askokcancel("进行编码?","对%d个文件进行编码?"%len(files)):
            encodingFiles(files)
        return
    with open(files[0],"rb") as f:
        content=f.read()
    try:
        content=content.decode("ansi")
    except:
        if messagebox.askokcancel("进行编码?",f"对{files[0]}文件进行编码?"):
            encodingFiles(files)
        return
    if len(content)>23 and content[:23] =="#SAVING WITH GHM-BASE64":
        if messagebox.askokcancel("进行解码?",f"按照GHM-BASE64格式,对{files[0]}文件进行解码?"):
            decodingGHMBASE64(files[0])
        return
    try:
        base64.b64decode(content)
    except:
        if messagebox.askokcancel("进行编码?",f"对{files[0]}文件进行编码?"):
            encodingFiles(files)
        return
    if messagebox.askokcancel("进行解码?",f"按照BASE64格式,对{files[0]}文件进行解码?"):
        decodingUnknownContent(content)
def draggedFiles(files):
    for i in range(len(files)):
        files[i] = files[i].decode("ansi")
    doFiles(files)
def doArgv():
    argv=sys.argv
    if len(argv)==1:
        return
    argv =argv[1:]
    for i in range(len(argv)):
        if argv[i] in ["-h","help","/h","/?","/help"]:
            os.system("start https://kuankuan2007.gitee.io/docs/ghm-base64-encoder/")
            return
        else:
            files=[]
            for i in argv:
                try:
                    with open(i,"rb") as f:
                        f.read()
                except:
                    messagebox.showerror("错误",i+"不是一个可以打开的文件")
                else:
                    files.append(i)
    if len(files)>=1:
        doFiles(files)

mainScreen=tkinter.Tk()
mainScreen.iconbitmap(resource_path(os.path.join("logo.ico")))
mainScreen.title("Base64转换器")

notebook = ttk.Notebook(mainScreen)
encodeFrame=tkinter.Frame(notebook)
decodeFrame=tkinter.Frame(notebook)


notebook.add(encodeFrame, text='编码')
notebook.add(decodeFrame, text='解码')
notebook.grid(column=0, row=0,sticky="W")

def encodOpenFiles():
    retsult=filedialog.askopenfilenames(title="请选择要编码的文件")
    retsult="|".join(retsult)
    resetEntry(encodeFileBox,retsult)
def encodClearFiles():
    resetEntry(encodeFileBox)
def encodeFileTextTrack(value):
    if value.get()=="":
        if encodeContentBox.get(0.0,tkinter.END)=="\n":
            startEncodeButton.config(state="disable")
        encodeContentBox.config(state="normal")
    else:
        startEncodeButton.config(state="normal")
        encodeContentBox.config(state="disable")
def contentTextTrack(event):
    if encodeContentBox.get(0.0,tkinter.END)=="\n":
        if encodeFileText.get()=="":
            startEncodeButton.config(state="disable")
        encodeFileBox.config(state="normal")
    else:
        startEncodeButton.config(state="normal")
        encodeFileBox.config(state="disable")
def startEncode():
    if encodeContentBox.get(0.0,tkinter.END)!="\n":
        content=encodeContentBox.get(0.0,tkinter.END).encode("ansi")
        content=base64.b64encode(content).decode("ansi")
        if messagebox.askquestion('显示方式', '是否保存为文件')=="yes":
            filename=filedialog.asksaveasfilename(title="请选择保存位置",filetypes=[("GHM-BASE64", ".GHMBASE64")],defaultextension=".ghm-base64")
            if not filename:
                return
            with open(filename,"w",encoding="ansi") as f:
                f.write("#SAVING WITH GHM-BASE64\n#TEXT\n")
                f.write(content)
                f.write("\n#END OF DOCUMENT")
            messagebox.showinfo("保存成功",f"内容已经保存进{filename}\n注意,我们进行了特殊的格式,以保证在反编码时不会混淆原格式")
        else:
            showTextRetsult(content)
    else:
        encodingFiles(encodeFileBox.get().split("|"))
encodeFileFrame=tkinter.Frame(encodeFrame)
encodeFileFrame.grid(column=0, row=0,pady=2,sticky="W")

encodeFileBoxTitle = tkinter.Label(encodeFileFrame,text="文件:")
encodeFileBoxTitle.grid(row=0,column=0,sticky="W")

encodeFileText=tkinter.StringVar(encodeFileFrame)
encodeFileText.trace("w", lambda name, index, mode, encodeFileText=encodeFileText: encodeFileTextTrack(encodeFileText))

encodeFileBox=ttk.Entry(encodeFileFrame,width=30,textvariable=encodeFileText)
encodeFileBox.grid(row=0,column=1,sticky="W")

encodeFileChoices = ttk.Button(encodeFileFrame,text="打开",command=encodOpenFiles)
encodeFileChoices.grid(row=0,column=2,sticky="W")

encodeFileClear = ttk.Button(encodeFileFrame,text="清空",command=encodClearFiles)
encodeFileClear.grid(row=0,column=3,sticky="W")

encodeContentFrame = tkinter.Frame(encodeFrame)
encodeContentFrame.grid(row=1,column=0,sticky="W",pady=2)

encodeContentTitle= ttk.Label(encodeContentFrame,text="文字:")
encodeContentTitle.grid(row=0,column=0,sticky="W")

encodeContentBoxScrollbar=ttk.Scrollbar(encodeContentFrame)
encodeContentBoxScrollbar.grid(column=1, row=1,sticky="NSW")
encodeContentBox=tkinter.Text(encodeContentFrame,width=60,height=10,yscrollcommand=encodeContentBoxScrollbar.set)
encodeContentBoxScrollbar.config(command=encodeContentBox.yview)
encodeContentBox.bind("<KeyRelease>",contentTextTrack)
encodeContentBox.grid(row=1,column=0,sticky="W")

encodeButtonFrame=tkinter.Frame(encodeFrame)
encodeButtonFrame.grid(row=3,column=0,sticky="E",pady=2)

startEncodeButton=ttk.Button(encodeButtonFrame,text="编码",state="disable",command=startEncode)
startEncodeButton.grid(row=0,column=1,sticky="E")

aboutButton=ttk.Button(encodeButtonFrame,text="关于",command=aboutBooter)
aboutButton.grid(row=0,column=0,sticky="E")



def encodOpenFiles():
    retsult=filedialog.askopenfilename(title="请选择要解码的文件")
    resetEntry(decodeFileBox,retsult)
def encodClearFiles():
    resetEntry(decodeFileBox)
def decodeFileTextTrack(value):
    if value.get()=="":
        if decodeContentBox.get(0.0,tkinter.END)=="\n":
            startDecodeButton.config(state="disable")
        decodeContentBox.config(state="normal")
    else:
        startDecodeButton.config(state="normal")
        decodeContentBox.config(state="disable")
def contentTextTrack(event):
    if decodeContentBox.get(0.0,tkinter.END)=="\n":
        if decodeFileText.get()=="":
            startDecodeButton.config(state="disable")
        decodeFileBox.config(state="normal")
    else:
        startDecodeButton.config(state="normal")
        decodeFileBox.config(state="disable")
def startdecode(file=None):
    if decodeContentBox.get(0.0,tkinter.END)!="\n":
        content=decodeContentBox.get(0.0,tkinter.END)[:-1]
        decodingUnknownContent(content)
    else:
        try:
            with open(decodeFileBox.get(),"r") as f:
                firstline=f.readline()
                if firstline=="#SAVING WITH GHM-BASE64\n":
                    decodingGHMBASE64(decodeFileBox.get())
                else:
                    decodingUnknownContent(firstline)
        except BaseException as e:
            messagebox.showerror("错误","无法打开并解码文件"+decodeFileBox.get()+"\n%s:%s"%(e.__class__.__name__,str(e)))
            return
def decodingGHMBASE64(filename):
    f=open(filename,"r")
    f.readline()
    try:
        saveDirname=None
        while True:
            line1=f.readline()
            if line1=="#END OF DOCUMENT":
                if saveDirname:
                    messagebox.showinfo("解码完成","所有文件已保存至%s"%(saveDirname))
                break
            if line1[0]!="#":
                messagebox.showerror("错误","文件标记为GHM-BASE64编码,但是其格式不满足编码规范")
            line2=f.readline()
            if line1=="#TEXT\n":
                try:
                    content=base64.b64decode(line2)
                except:
                    messagebox.showerror("文本内容不是Base64编码")
                    return
                try:
                    content=content.decode("ansi")
                except:
                    messagebox.showerror("这条内容被标记为文本,但他不是ansi编码")
                    return
                showTextRetsult(content)
            elif line1[:5]=="#FILE":
                while not saveDirname:
                    saveDirname=filedialog.askdirectory(title="选择文件的保存目录")
                line1=line1[:-1].split("|")
                saveName=""
                if len(line1) !=2:
                    while not saveName:
                        saveName=simpledialog.askstring("指定文件名","文件名未找到，请手动指定")
                else:
                    saveName=line1[1]
                content=base64.b64decode(line2)
                with open(os.path.join(saveDirname,saveName),"wb") as saveFile:
                    saveFile.write(content)
    except BaseException as e:
        f.close()
        raise e

decodeFileFrame=tkinter.Frame(decodeFrame)
decodeFileFrame.grid(column=0, row=0,pady=2,sticky="W")

decodeFileBoxTitle = tkinter.Label(decodeFileFrame,text="文件:")
decodeFileBoxTitle.grid(row=0,column=0,sticky="W")

decodeFileText=tkinter.StringVar(decodeFileFrame)
decodeFileText.trace("w", lambda name, index, mode, decodeFileText=decodeFileText: decodeFileTextTrack(decodeFileText))

decodeFileBox=ttk.Entry(decodeFileFrame,width=30,textvariable=decodeFileText)
decodeFileBox.grid(row=0,column=1,sticky="W")

decodeFileChoices = ttk.Button(decodeFileFrame,text="打开",command=encodOpenFiles)
decodeFileChoices.grid(row=0,column=2,sticky="W")

decodeFileClear = ttk.Button(decodeFileFrame,text="清空",command=encodClearFiles)
decodeFileClear.grid(row=0,column=3,sticky="W")

decodeContentFrame = tkinter.Frame(decodeFrame)
decodeContentFrame.grid(row=1,column=0,sticky="W",pady=2)

decodeContentTitle= ttk.Label(decodeContentFrame,text="文字:")
decodeContentTitle.grid(row=0,column=0,sticky="W")

decodeContentBoxScrollbar=ttk.Scrollbar(decodeContentFrame)
decodeContentBoxScrollbar.grid(column=1, row=1,sticky="NSW")
decodeContentBox=tkinter.Text(decodeContentFrame,width=60,height=10,yscrollcommand=decodeContentBoxScrollbar.set)
decodeContentBoxScrollbar.config(command=decodeContentBox.yview)
decodeContentBox.bind("<KeyRelease>",contentTextTrack)
decodeContentBox.grid(row=1,column=0,sticky="W")

decodeButtonFrame=tkinter.Frame(decodeFrame)
decodeButtonFrame.grid(row=3,column=0,sticky="E",pady=2)

startDecodeButton=ttk.Button(decodeButtonFrame,text="解码",state="disable",command=startdecode)
startDecodeButton.grid(row=0,column=1,sticky="E")

aboutButton=ttk.Button(decodeButtonFrame,text="关于",command=aboutBooter)
aboutButton.grid(row=0,column=0,sticky="E")

windnd.hook_dropfiles(mainScreen, func=draggedFiles)
threading.Thread(target=doArgv,daemon=True).start()
mainScreen.mainloop()