from pprint import pprint
import re
from lib.util import ReplaceText
import lib.ko_pron
import itertools


class PostFilter:
    

    def __init__(self, text: str, dict_list:dict, repl_list:list):
        self.text = text
        self.dict_list = dict_list
        self.repl_list = list(set([self.dict_list[r[0]] for r in repl_list]))

        self.b = {
            'ㅋ' : 'ㄱㄲ',
            'ㅊ' : 'ㅉ',
            'ㅌ' : 'ㄷㄸ',
        }



    def post_process(self):
        post = ReplaceText(
            self.text, {
                '｣':'"',
                '｢':'"',
                '^':'',
            }
        )
        # for i in self.repl_list:
        #     for j in self.get_takeum_possibility_word_list(i):
        #         # 다만 이거 치환할 때 한국어 형태소 분석을 먼저 하는게 좋을 것 같음.
        #         if not j in self.dict_list:
        #             post = post.replace(j, i)

        return post



    # def to_takeum(self, s):
    #     a = []
    #     t = lib.ko_pron.split_syllable_char(s)
    #     for i in self.b[t[0]]:

    #         if t[2] == None:
    #             a.append(lib.ko_pron.join_jamos(i+t[1]))
    #         else:
    #             a.append(lib.ko_pron.join_jamos(i+t[1]+t[2]))

    #     return a[0] if len(a)==1 else a


    


    # def get_takeum_possibility_word_list(self, n):
    #     tak_ = [idx for idx, i in enumerate(n) if lib.ko_pron.split_syllable_char(i)[0] in self.b]
    #     k = []

    #     for i in range(len(tak_)):
    #         for t in list(itertools.combinations(tak_, i+1)): # 진부분집합: 만들어지는 조합은 2^p -1 개, p는 탁음 가능성의 개수
    #             c = list(n)
    #             for j in t:
    #                 c[j] = self.to_takeum(c[j])
    #             k.append(c)

    #     v = [''.join(j) for i in k for j in list(itertools.product(*i))] # 카테시안 곱: 리스트로 만들 수 있는 모든 조합 가능성의 개수
    #     return v