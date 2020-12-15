import logging
import pyautogui as pygui

pygui.FAILSAFE = False

class translator_py:
    def __init__(self):
        pass

    #TODO:- have to write inside method instead of returning
    def t_print(self, text):
        x = text.lower().replace('\in', " \n")
        x = x.replace('print ', '').replace("nun", "none").replace("print", "")

        z=str()
        y=str()
        endNone = False
        try:
            y=text.lower().split()[-1].replace("nun", "none")
            z=text.lower().split()[-2].replace("nun", "none")
        except Exception as e:
            print(e)

        if z == "last":
            x = x.replace(f" last {y}", "")
            endNone = True

        if y=="none" or y=="null":
            y = y.replace(y, '""')
        else:
            y = y.replace(y, f'"{y}"')

        if 'format' in x:
            variableName = []
            xArray = x.split()

            for i in range(len(xArray)-1):
                print(i)
                if xArray[i] == "format":
                    variableName.append(xArray[i+1])
                    xArray[i] = "{}"
                    xArray.pop(i+1)
            
            if endNone == True:
                result = '"' +' '.join(map(str, xArray)) + '"' +".format("+','.join(map(str, variableName))+")"+f", end={y}"
            else:
                result = '"' +' '.join(map(str, xArray)) + '"' +".format("+','.join(map(str, variableName))+")"

            result = "print(" + result + ')'

        elif 'placeholder' in x.split()[0]:
            if endNone == False:
                result = "print(" + x.replace("placeholder ", "") + ')'
            else:
                result = "print(" + x.replace("placeholder", "") + f', end={y})'
        else:
            if endNone == True:
                result = "print" + '("' + x + f'", end={y}' +")"
            else:
                result = "print" + '("' + x +'")'

        pygui.write(result)

    def t_var(self, text):
        x = text.lower()
        x = x.replace('is equal to', '=').replace('equal to', '=').replace('variable ', '')

        value = x.split('=', 1)[1]
        x = x.replace(value, '')
        result = str()
        value = value.replace(" ", "", 1)
        try:
            float(value)
            result = x + value.replace("variable", "")
        except Exception as e:
            print(value.split()[0])
            if value.isnumeric() or value.split()[0] == 'variable' or value.split()[0] == 'input':
                if value.split()[0] == 'input':
                    result = x + 'input("' + value.replace("input", "") + '")'
                else:
                    result = x + value.replace("variable", "")
            elif value=="true" or value=="false":
                result = x+value.replace("true", "True").replace("false", "False")
            else:
                result = x + '"' + value + '"'
        #TODO:-  Currently need to add variable reassignment for later iteration

        pygui.write(result)
    def t_IF(self, text):
        x = text.lower()
        x = x.replace('is equal to', '==').replace('is not equal to', '!=').replace('is greater than', '>').replace('is lesser than', '<').replace('is greater than or equal to', '>=').replace('is lesser than or equal to', '<=')

        if "if" not in x.split('=')[-1]:
            value = x.split('=')[-1]
        elif "if" not in x.split('>')[-1]:
            value = x.split('>')[-1]
        elif "if" not in x.split('<')[-1]:
            value2 = x.split('<')[-1]
            
        x = x.replace(value, '')
        result = str()

        if value.replace(" ", "").isnumeric():
            result = x + value
        elif value=="true" or value=="false":
            result = x+value.replace("true", "True").replace("false", "False")
        else:
            result = x + '"' + value + '"'

        pygui.write(result+":")

    def t_ELIF(self, text):
        x = text.lower()
        x = x.replace('else if', 'elif').replace('is equal to', '==').replace('is not equal to', '!=').replace('is greater than', '>').replace('is lesser than', '<').replace('is greater than or equal to', '>=').replace('is lesser than or equal to', '<=')

        value = x.split('=')[-1]
        x = x.replace(value, '')
        result = x

        if value.replace(" ", "").isnumeric():
            result = x + value
        elif value=="true" or value=="false":
            result = x+value.replace("true", "True").replace("false", "False")
        else:
            result = x + '"' + value + '"'

        pygui.press("home")
        print(result)
        pygui.write(result+":")
        pygui.press("end")

    def t_ELSE(self, text):
        x = text.lower()
        result = x

        pygui.press("home")
        pygui.write(result+":")

    def t_FOR(self, text):
        x = text.lower()

        value = x.split(' ')[-1]
        x = x.replace(value, '')
        result = str()

        if value.isnumeric():
            result = x + "(" + value + ")"
        else:
            result = x + "(" + value + ")"

        pygui.write(result + ":")
        print(result)

    def t_input(self, text):
        x = text.lower()
        result = x.split('input', 1)[1]

        pygui.write(result)

    def t_def(self, text):
        x = text.lower()
        x = x.replace("define method", "def")
        mName = text.replace("define method","")

        pygui.write(x+"():")
        return mName

    def t_param(self, text, line, mName):
        pygui.hotkey('ctrl', 'home')
        print(line)
        for i in range(int(line) - 1):
            pygui.press("down")
        pygui.press("end")
        pygui.press("left")
        pygui.press("left")

        pygui.write(text.replace("add parameters", "").replace("add parameter", "").replace("and", ",").split("in method", 1)[0])

    def t_return(self, text):
        x = text.lower()
        x = x.replace('true', 'True').replace('false', 'False')

        value = x.split('=', 1)[1]
        actualVal = x.split(" ")[-1]
        x = x.replace(value, '')
        result = str()

        if actualVal.isnumeric():
            result = x + value
        else:
            result = x + '"' + value + '"'

        pygui.write(result)

    def t_indent(self, text):
        result = "    "+text.lower().replace('indent', '')
        pygui.write(result)

    #Navigator
    def tN_goto(self, text):
        number = text.split(" ")[-1]

        pygui.hotkey('ctrl', 'home')
        if number == "next":
            pygui.press("end")
            pygui.press("enter")
        elif number.isnumeric():
            for i in range(int(number)-1):
                pygui.press("down")

        replaceVal = "go to line " + number
        pygui.write(text.replace(replaceVal, ""))
