import os
import sys
sys.path.append(os.path.abspath(r"C:\Users\power\Desktop\Project\Dev\UserDict4Papago"))
import re
from pprint import pprint
import cProfile
import MeCab
from lib.util import *
from lib.convert_dict import ConvertDictionary
from lib.papagopy.papagopy import Papagopy


def main():

    # 파파고에서 안 사라지는 문자 찾아야함.. -> seperator.txt
    sep = '▒▒▒'
    sep_nl = '∮' # 분석기에서 사라질 \n 보완

    p = Papagopy()
    c = ConvertDictionary()
    dictList = c.convert()

    t = MeCab.Tagger()

    rf = ReadFile('./example_text/t.txt')
    s = rf.replace('\r', '').replace('\n', sep_nl).replace('　', '')


    a = t.parse(s).split()[:-1]

    surface = a[0::2]
    pos = a[1::2]

    b = [(surface[i], i) for i, p in enumerate(pos) if ('固有名詞' in p) and (surface[i] in dictList)]

    for sur, idx in b:
        surface[idx] = f'{sep}{sur}{sep}'

    pre = ''.join(surface).replace(f'{sep}{sep}', f'{sep} {sep}').replace(sep_nl, '\n KDR ')
    trans = p.translate(pre, 'ko', 'ja')
    
    post = trans.replace(f'{sep} ', f'{sep}').replace(f'{sep}{sep}', f'{sep} {sep}')

    c = 0
    for i, j in zip(re.findall(f'{sep}.*?{sep}', post), b):
        print(f'{c} :::', i, ' -> ', dictList[j[0]])
        post = post.replace(i, f'{dictList[j[0]]}')
        c+=1


    WriteFile(pre, 't-pre.txt') # 전처리
    WriteFile(trans, 't-trans.txt') # 파파고 번역
    WriteFile(post, 't-post.txt') # 후처리


if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run(fr"main()")