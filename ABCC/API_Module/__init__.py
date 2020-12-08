import requests
import Compiler_Module

class APIs:
    def __init__(self):
        pass

    def POST(self, program, LanguageChoice):
        code = {"Program": program, "LanguageChoice": LanguageChoice}

        req1 = requests.post('https://rextester.com/rundotnet/api', data=code)
        result = req1.json()

        return result

#Coming in the future for docs referrence
#   def GET(self, context):
