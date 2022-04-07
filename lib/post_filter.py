import re
from lib.util import ReplaceText


class PostFilter:
    

    def __init__(self, text: str, dict_list:dict):
        self.text = text
        self.dict_list = dict_list

    def post_process(self):
        # 옛날 발음 나는 애들 어떻게 처리할까...
        post = ReplaceText(
            self.text, {
                '｣':'"',
                '｢':'"',
                '^':'',
            }
        )
        return post