import re

class PostFilter:
    

    def __init__(self, text: str, dict_list:dict, repl_list:list):
        self.text = text
        self.dict_list = dict_list
        self.repl_list = repl_list

    def post_process(self):
        sep = '▒'

        post = self.text.replace(f'{sep} ', f'{sep}').replace(f'{sep}{sep}', f'{sep} {sep}')

        for i, j in zip(re.findall(f'{sep}.*?{sep}', post), self.repl_list):
            print(i, ' -> ', self.dict_list[j[0]])
            post = post.replace(i, f' {self.dict_list[j[0]]}').replace('  ', ' ')

        return post