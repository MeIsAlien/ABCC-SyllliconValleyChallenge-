import Speech_Module
import Compiler_Module
import pyautogui as pygui

sr = Speech_Module.speech()
cmpl = Compiler_Module.translator_py()

code_result = str()
stg1_res = str()
stg2_res = str()
stg3_res = str()
stg4_res = str()
stg5_res = str()
stg6_res = str()
stg7_res = str()
stg8_res = str()
stg9_res = str()
stg10_res = str()
stg11_res = str()
stg12_res = str()
stg13_res = str()
stg14_res = str()
stg15_res = str()
stg16_res = str()
stg17_res = str()

final_res = str()
lineCount = 0
newLine_flag = False

def_dict = {}
class_dict = {}

while True:
    raw_text = sr.mic_input()
    if 'print' in raw_text:
        stg1_res = cmpl.t_print(raw_text)
    else:
        stg1_res = raw_text

    if 'variable' in stg1_res:
        stg2_res = cmpl.t_var(stg1_res)
    else:
        stg2_res = stg1_res

    if 'if' in stg2_res:
        stg3_res = cmpl.t_IF(stg2_res)
    else:
        stg3_res = stg2_res

    if 'else if' in stg3_res:
        stg4_res = cmpl.t_ELIF(stg3_res)
    else:
        stg4_res =stg3_res

    if 'else' in stg4_res:
        stg5_res = cmpl.t_ELSE(stg4_res)
    else:
        stg5_res = stg4_res

    if 'for' in stg5_res:
        stg6_res = cmpl.t_FOR(stg5_res)
    else:
        stg6_res = stg5_res

    if 'run the code' in stg6_res:
        pygui.hotkey("shift", "f10")
        stg7_res = stg6_res.replace("run the code", "")
    else:
        stg7_res = stg6_res

    if "define method" in stg7_res:
        stg8_res = cmpl.t_def(stg7_res)[0]
        Mname = cmpl.t_def(stg7_res)[1].replace(" ", "")
        def_dict[Mname] = lineCount+1
        print(def_dict.get(Mname))
    else:
        stg8_res = stg7_res

    if "add parameters" in stg8_res or "add parameter" in stg8_res:
        method = stg8_res.split(" ")[-1]
        print(def_dict)

        print(method)
        stg9_res = cmpl.t_param(stg8_res, def_dict.get(method), method)
        newLine_flag = True
    else:
        stg9_res = stg8_res

    if 'return' in stg9_res:
        stg10_res = cmpl.t_return(stg9_res)
    else:
        stg10_res = stg9_res

    if 'indent' in stg10_res:
        stg11_res = cmpl.t_indent(stg10_res)
    else:
        stg11_res = stg10_res

    if 'delete line' in stg11_res:
        pygui.press('home')
        pygui.hotkey('shift', 'down')
        pygui.press('delete')
        stg12_res = stg11_res.replace("delete line", "")
        newLine_flag = True
    else:
        stg12_res = stg11_res

    stg13_res = stg12_res

    #if 'input' in stg12_res:
    #    stg13_res = cmpl.t_input(stg12_res)
    #    val = cmpl.t_input(stg12_res)[1]
    #    sr.t2s("what do you want to input for " + val)
    #    input = sr.mic_input()
    #    pygui.write(input)
    #else:
    #    stg13_res = stg12_res

    if 'go to' in stg13_res:
        stg14_res = cmpl.tN_goto(stg13_res)
        newLine_flag = True
    else:
        stg14_res = stg13_res

    if 'stop' in stg14_res:
        stg15_res = stg14_res.replace("stop", '')
        pygui.press("backspace")
        newLine_flag = True
    else:
        stg15_res = stg14_res

    if 'class' in stg15_res:
        stg16_res = cmpl.t_class(stg15_res)[0]
        Cname = cmpl.t_class(stg15_res)[1].replace(" ", "")
        class_dict[Cname] = lineCount + 1
        print(class_dict)
    else:
        stg16_res = stg15_res

    if 'add class' in stg16_res:
        Class = stg16_res.split(" ")[-1].replace("():", "")
        print(Class)
        print(class_dict.get(Class))
        stg17_res = cmpl.t_extends(stg16_res, class_dict.get(Class), Class)
        newLine_flag = True
    else:
        stg17_res = stg16_res

    final_res = stg17_res

    if final_res != "" and newLine_flag == False:
        lineCount = lineCount + 1
        pygui.write(final_res+"\n")
    elif final_res != "" and newLine_flag == True:
        lineCount = lineCount + 1
        pygui.write(final_res.replace("", '').replace("divided by", ''))
        newLine_flag = False