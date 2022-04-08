import itertools
from pprint import pprint
import sys, os
sys.path.append(os.path.abspath(r"C:\Users\power\Desktop\Project\Dev\UserDict4Papago"))
import lib.ko_pron


 
n = '토츠카'

b = {
    'ㅋ' : 'ㄱㄲ',
    'ㅊ' : 'ㅉ',
    'ㅌ' : 'ㄷㄸ',
}


def repl(s):
    a = []
    t = lib.ko_pron.split_syllable_char(s)
    for i in b[t[0]]:

        if t[2] == None:
            a.append(lib.ko_pron.join_jamos(i+t[1]))
        else:
            a.append(lib.ko_pron.join_jamos(i+t[1]+t[2]))

    return a[0] if len(a)==1 else a




tak_ = [idx for idx, i in enumerate(n) if lib.ko_pron.split_syllable_char(i)[0] in b]
k = []

for i in range(len(tak_)):
    for t in list(itertools.combinations(tak_, i+1)): # 진부분집합: 만들어지는 조합은 2^p -1 개, p는 탁음 가능성의 개수
        c = list(n)
        for j in t:
            c[j] = repl(c[j])
        k.append(c)

v = [''.join(j) for i in k for j in list(itertools.product(*i))] # 카테시안 곱: 리스트로 만들 수 있는 모든 조합 가능성의 개수
print(v)