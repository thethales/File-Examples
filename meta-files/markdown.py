class Markdown:
    char_space = ' '
    line_break = '\n'

    #def addDelimiter(delimiter:str):


    @staticmethod
    def header(level:int,content:str):
        return "".join('#'*level) + Markdown.char_space + content + Markdown.line_break
    
    @staticmethod
    def lineBreak():
        return Markdown.line_break

    @staticmethod
    def table(arr_json):
        theaders = "|"
        tlines = "|"
        tseparator = "|"
        for item in arr_json:
            for line in item:
                theaders += line + '|'
                tseparator += "----" + '|'
                tlines += line + '|'

        return theaders + '\n' + tseparator + '\n' + tlines + '\n'

    @staticmethod
    def tableHeader(arr_json:dict):
        theaders = "|"
        tseparator = "|"
        for item in arr_json:
            for line in item:
                theaders += line + '|'
                tseparator += "----" + '|'
            break

        return theaders + '\n' + tseparator + '\n'

    @staticmethod
    def tableLines(arr_json:dict):
        tlines = "|"
        tseparator = "|"
        for item in arr_json:
            for line in item:
                tlines += item[line] + '|'
            tlines += '\n'

        return tlines