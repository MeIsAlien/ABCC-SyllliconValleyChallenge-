import pyautogui as pygui
import os
import Speech_Module
import Compiler_Module
import logging

flag_listen = False

class mainOne():

    def __init__(self):
        global flag_listen
        self.sr = Speech_Module.speech()
        self.cmpl = Compiler_Module.translator_py()
        logging.basicConfig(filename="LOG.txt", filemode="a", level=logging.INFO, format="%(asctime)s %(message)s")
        self.final_res = str()
        self.lineCount = 0
        self.compliled_flag = False
        self.def_dict = {}

    def stopListening(self):
        global flag_listen
        flag_listen = False
        print("Stopped Listening")

    def resumeListening(self):
        global flag_listen
        flag_listen = True
        print("Started Listening")

    def startListening(self):
        while True:
            global flag_listen
            if flag_listen:
                try:
                    raw_text = self.sr.mic_input().lower()
                    logging.info(f"User Said: {raw_text}")
                    raw_text = raw_text.replace("one", "1").replace("two", "2").replace("three", "3").replace("four", "4").replace("five", "5").replace("six", "6").replace("seven", "7").replace("eight", "8").replace("nine", "9").replace('"ad', "add").replace("divided by", "/").replace("minus", "-").replace("elss", "else").replace("unicode star", "*").replace("\in", "\n").replace("unicode exclamation mark", "!").replace("unicode a", "@").replace("unicode hashtag", "#").replace("unicode dollar", "$").replace("unicode percent sign", "%").replace("unicode caret", "^").replace("unicode ampersand", "&")
                    if 'print' in raw_text.split()[0]:
                        self.cmpl.t_print(raw_text)
                        self.lineCount = self.lineCount+1
                    if 'variable' in raw_text.split()[0]:
                        self.cmpl.t_var(raw_text)
                        self.lineCount = self.lineCount+1
                    if 'if' in raw_text.split()[0]:
                        self.cmpl.t_IF(raw_text)
                        self.lineCount = self.lineCount+1
                    try:
                        if 'else' in raw_text.split()[0] and 'if' in raw_text.split()[1]:
                            self.cmpl.t_ELIF(raw_text)
                            raw_text = raw_text.replace("else if ", "elif")
                            self.lineCount = self.lineCount+1
                    except:
                        if 'else' in raw_text.split()[0]:
                            self.cmpl.t_ELSE(raw_text)
                            self.lineCount = self.lineCount+1
                        pass
                    if 'for' in raw_text.split()[0]:
                        self.cmpl.t_FOR(raw_text)
                        self.lineCount = self.lineCount+1
                    if 'run' in raw_text.split()[0] and 'the' in raw_text.split()[1] and 'code' in raw_text.split()[2]:
                        pygui.hotkey("ctrl", "shift", "f10")
                        pygui.press("enter")
                        raw_text = raw_text.replace("run the code", "")
                    if "define" in raw_text.split()[0] and 'method' in raw_text.split()[1]:
                        Mname = self.cmpl.t_def(raw_text).replace(" ", "", 1)
                        self.def_dict[Mname] = self.lineCount+1
                        self.lineCount = self.lineCount+1
                    if "add" in raw_text.split()[0] and 'parameters' in raw_text.split()[1] or "add" in raw_text.split()[0] and "parameter" in raw_text.split()[1]:
                        method = raw_text.split()[-1]
                        self.cmpl.t_param(raw_text, self.def_dict.get(method), method)
                    if 'return' in raw_text.split()[0]:
                        self.cmpl.t_return(raw_text)
                        self.lineCount = self.lineCount+1
                    if 'indent' in raw_text.split()[0]:
                        self.cmpl.t_indent(raw_text)
                    if 'delete' in raw_text.split()[0] and 'line' in raw_text.split()[1]:
                        pygui.press('end')
                        pygui.hotkey('shift', 'up')
                        pygui.press('backspace')
                        raw_text = raw_text.replace("delete line", "")
                        self.lineCount = self.lineCount-1
                    if 'go' in raw_text.split()[0] and 'to' in raw_text.split()[1]:
                        self.cmpl.tN_goto(raw_text)
                    if 'back' in raw_text.split()[0]:
                        raw_text.replace("back", '')
                        pygui.press("backspace")
                    if "call" == raw_text.split()[0] and "method" == raw_text.split()[1]:
                        self.cmpl.t_callMethod(raw_text)
                        self.lineCount = self.lineCount+1
                    if "open" in raw_text.split()[0] and "terminal" in raw_text.split()[0]:
                        pygui.hotkey("alt" + "f12")
                    if raw_text == "triangle":
                        pygui.press("enter")
                        self.lineCount = self.lineCount+1
                    if raw_text.split()[0] == "write":
                        pygui.write(raw_text.replace("write ", ""))
                    if raw_text.split()[0] == "read" and raw_text.split()[1] == "logs":
                        os.system("notepad.exe LOG.txt")
                    logging.info("No Errors")
                except Exception as e:
                    raw_text= ""
                    logging.error(e)
