import re
from lib.util import ReplaceText, sep


class PostFilter:
    

    def __init__(self, text: str, dict_list:dict, repl_list:list):
        self.text = text
        self.dict_list = dict_list
        self.repl_list = repl_list

    def post_process(self):
        post = ReplaceText(
            self.text, {
                '｣':'"',
                '｢':'"',
                '^':'',
            }
        )
        return post