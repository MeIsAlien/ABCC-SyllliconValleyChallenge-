import Speech_Module
import Compiler_Module
import pyautogui as pygui

sr = Speech_Module.speech()
cmpl = Compiler_Module.translator_py()

final_res = str()
lineCount = 0

newLine_flag = False
compliled_flag = False

def_dict = {}

while True:
    try:
        raw_text = sr.mic_input().lower()
        print(raw_text)
        raw_text = raw_text.replace("star", "*").replace("\in", "\n").replace("unicode exclamation mark", "!").replace("unicode a", "@").replace("unicode hashtag", "#").replace("unicode dollar", "$").replace("unicode percent sign", "%").replace("caret", "^").replace("ampersand", "&")
        print(raw_text)
        if 'print' in raw_text.split()[0]:
            cmpl.t_print(raw_text)
            compliled_flag = True

        if 'variable' in raw_text.split(" ")[0]:
            cmpl.t_var(raw_text)
            compliled_flag = True

        if 'if' in raw_text.split(" ")[0]:
            cmpl.t_IF(raw_text)
            compliled_flag = True

        if 'else' in raw_text.split(" ")[0] and 'if' in raw_text.split(" ")[1]:
            cmpl.t_ELIF(raw_text)
            raw_text=raw_text.replace("else if ", "elif")
            compliled_flag = True
        
        if 'else' in raw_text.split(
            " ")[0]:
            cmpl.t_ELSE(raw_text)
            compliled_flag = True
        
        if 'for' in raw_text.split(" ")[0]:
            cmpl.t_FOR(raw_text)
            compliled_flag = True

        if 'run' in raw_text.split(" ")[0] and 'the' in raw_text.split(" ")[1] and 'code' in raw_text.split(" ")[2]:
            pygui.hotkey("ctrl", "f5")
            raw_text = raw_text.replace("run the code", "")
            newLine_flag = False
            compliled_flag = True

        if "define" in raw_text.split(" ")[0] and 'method' in raw_text.split(" ")[1]:
            Mname = cmpl.t_def(raw_text)[1].replace(" ", "")
            def_dict[Mname] = lineCount+1
            compliled_flag = True

        if "add" in raw_text.split(" ")[0] and 'parameters' in raw_text.split(" ")[1] or "add" in raw_text.split(" ")[0] and "parameter" in raw_text.split(" ")[1]:
            method = raw_text.split(" ")[-1]
            print(def_dict)

            print(method)
            cmpl.t_param(raw_text, def_dict.get(method), method)
            newLine_flag = True
            compliled_flag = True

        if 'return' in raw_text.split(" ")[0]:
            cmpl.t_return(raw_text)
            compliled_flag = True

        if 'indent' in raw_text.split(" ")[0]:
            cmpl.t_indent(raw_text)
            compliled_flag = True
        
        if 'delete' in raw_text.split(" ")[0] and 'line' in raw_text.split(" ")[1]:
            pygui.press('home')
            pygui.hotkey('shift', 'down')
            pygui.press('delete')
            raw_text.replace("delete line", "")
            newLine_flag = True
            compliled_flag = True
        

        # #if 'input' in stg12_res:
        # #    stg13_res = cmpl.t_input(stg12_res)
        # #    val = cmpl.t_input(stg12_res)[1]
        # #    sr.t2s("what do you want to input for " + val)
        # #    input = sr.mic_input()
        # #    pygui.write(input)
        # #else:
        # #    stg13_res = stg12_res

        if 'go' in raw_text.split(" ")[0] and 'to' in raw_text.split(" ")[1]:
            cmpl.tN_goto(raw_text)
            newLine_flag = True
            compliled_flag = True
        
        if 'back' in raw_text.split(" ")[0]:
            raw_text.replace("back", '')
            pygui.press("backspace")
            newLine_flag = True
            compliled_flag = True

        if newLine_flag == False and compliled_flag == True:
            pygui.press("enter")
            lineCount = lineCount+1
        # final_res = stg15_res

        # if final_res != "" and newLine_flag == False:
        #     lineCount = lineCount + 1
        #     pygui.write(final_res+"\n")
        # elif final_res != "" and newLine_flag == True:
        #     lineCount = lineCount + 1
        #     pygui.write(final_res.replace("", '').replace("divided by", ''))
        #     newLine_flag = False
    except Exception as e:
        raw_text= ""
        print(e)
    