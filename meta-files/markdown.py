class Markdown:
    char_space = ' '
    line_break = '\n'

    @staticmethod
    def f_reorderDict(dic):
        ordered_dic={}
        key_ls=sorted(dic.keys())
        for key in key_ls:
            ordered_dic[key]=dic[key]
        return ordered_dic

    @staticmethod
    def header(level:int,content:str):
        return "".join('#'*level) + Markdown.char_space + content + Markdown.line_break
    
    @staticmethod
    def lineBreak():
        return Markdown.line_break

    @staticmethod
    def tableHeader(arr_json:dict):
        theaders = "|"
        tseparator = "|"
        for item in arr_json:
            item = Markdown.f_reorderDict(item)
            for line in item:
                theaders += line.title() + '|'
                tseparator += "----" + '|'
            break
        return theaders + '\n' + tseparator + '\n'

    @staticmethod
    def tableLines(arr_json:dict):
        tlines = ''
        for item in arr_json:
            item = Markdown.f_reorderDict(item)
            for line in item:
                if line == 'link':
                    tlines += '|' + Markdown.link(item['name'],item['link'])
                else:
                    tlines += '|' + item[line]
            tlines += '|\n'
        return tlines

    @staticmethod
    def link(placeholder:str,link:str):
        link = "[" + placeholder + "]"+"(" + link + ")"
        return link

