import logging
import pyautogui as pygui

pygui.FAILSAFE = False

class translator_py:
    def __init__(self):
        pass

    def t_print(self, text):
        x = text.lower()
        x = x.replace('print ', '')
        if "placeholder" in x:
            result = "print" + '(' + x + ')'
            result = result.replace("placeholder", "").replace("x", '*')
        else:
            result = "print" + '("' + x + '")'
        return result

    def t_var(self, text):
        x = text.lower()
        x = x.replace('is equal to', '=').replace('equal to', '=').replace('variable ', '', 1)
        print(x)
        value = x.split('=', 1)[1]
        x = x.replace(value, '')
        result = str()
        if value.isnumeric():
            result = x + value
        else:
            if 'variable' in value:
                result = x + value.replace("variable ", "")
            else:
                result = x + '"' + value + '"'

        #TODO:-  Currently need to add variable reassignment for later iteration

        return result

    def t_IF(self, text):
        x = text.lower()
        x = x.replace('is equal to', '==').replace('is not equal to', '!=').replace('is greater than', '>').replace('is lesser than', '<').replace('is greater than or equal to', '>=').replace('is lesser than or equal to', '<=')

        value = x.split(' ')[-1]
        x = x.replace(value, '')
        result = str()

        if value.isnumeric():
            result = x + value
        else:
            result = x + '"' + value + '"'

        return result+":"

    def t_ELIF(self, text):
        x = text.lower()
        x = x.replace('else if', 'elif').replace('is equal to', '==').replace('is not equal to', '!=').replace('is reater than', '>').replace('is lesser than', '<').replace('is greater than or equal to', '>=').replace('is lesser than or equal to', '<=')

        value = x.split(' ')[-1]
        x = x.replace(value, '')
        result = str()

        if value.isnumeric():
            result = x + value
        else:
            result = x + '"' + value + '"'

        return result+":"

    def t_ELSE(self, text):
        x = text.lower()
        result = x

        return result+":"

    def t_FOR(self, text):
        x = text.lower()

        value = x.split(' ')[-1]
        x = x.replace(value, '')
        result = str()

        if value.isnumeric():
            result = x + "(" + value + ")"

        return result + ":"

    def t_input(self, text):
        x = text.lower()
        result = x.split('input', 1)[1]

        return result

    def t_def(self, text):
        x = text.lower()
        x = x.replace("define method", "def")
        mName = text.replace("define method","")

        return x+"():", mName

    def t_param(self, text, line, mName):
        pygui.hotkey('ctrl', 'home')
        print(line)
        for i in range(int(line) - 1):
            pygui.press("down")
        pygui.press("end")
        pygui.press("left")
        pygui.press("left")

        return text.replace("add parameters", "").replace("add parameter", "").replace("and", ",").split("in method", 1)[0]

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

    def t_class(self, text):
        x = text.lower()
        x = x.replace("create ", "")
        cName = text.replace("create class ","")

        return x+"():", cName

    def t_extends(self, text, line, cName):
        pygui.hotkey('ctrl', 'home')
        for i in range(int(line) - 1):
            pygui.press("down")
        pygui.press("end")
        pygui.press("left")
        pygui.press("left")
#command to trigger this function "add classes x to class y"
        return text.replace("add parent class", "").replace("add parent classes", "").replace("and", ",").split("to class", 1)[0]

    def t_indent(self, text):
        result = "    "+text.lower().replace('indent', '')
        return result

    def t_array(self, text):
        x = text.lower().replace("new list ", "").replace(" and ", ",").replace('is equal to', '=').replace('equal to', '=')
        values = x.split("= ")[1]
        arrayOfValues = values.split(",")
        resultArray = []

        for i in arrayOfValues:
            if i.isnumeric():
                resultArray.append(int(i))
            else:
                resultArray.append(i)

        return x.replace(values, "") + str(resultArray)

    #TODO:- have to create a way for arrays and dictionary, input
    #Navigator
    def tN_goto(self, text):
        number = text.split(" ")[-1]

        pygui.hotkey('ctrl', 'home')
        if number == "next":
            pygui.press("end")
            pygui.press("enter")
        elif int(number):
            for i in range(int(number)-1):
                pygui.press("down")

        replaceVal = "go to line " + number
        return text.replace(replaceVal, "")

obj = translator_py()
print(obj.t_array("array x = 1 and hello world and hello world and 19191 and justin is a noob 1"))