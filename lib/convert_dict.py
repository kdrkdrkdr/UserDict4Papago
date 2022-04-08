import os
import codecs
from lib import ko_pron
from jaconv import alphabet2kata
from lib.util import WriteFile
from pprint import pprint








class ConvertDictionary:
    
    def __init__(self, prj_root=os.getcwd(), mecab_dir=r'C:\Program Files\MeCab'):
        self.prj_root = prj_root
        self.mecab_dir = mecab_dir

    def convert(self):
        t2c = self.txt2csv()
        self.csv2dic()
        return t2c


    def txt2csv(self):
        nl = ""
        nd = {}

        f = codecs.open(self.prj_root+r'\userdic\UserDict.txt', 'r', encoding='utf-8')
        dict_string = f.read()
        r = dict_string.split('\n')
        for i in r:
            if not i.replace(' ', '').startswith('//'):
                try:
                    b = i.replace(' ', '').replace('\r', '').split(',')

                    jp_pron = self._ko2kata(b[1])
                    nl += f'{b[0]},,,1000,名詞,固有名詞,人名,一般,*,*,*,{jp_pron},{jp_pron}\n'
                    # nd[b[0]] = jp_pron
                    nd[b[0]] = b[1]
                    
                except IndexError as e:
                    pass

        WriteFile(nl, self.prj_root+'\\userdic\\userdic.csv')
        return nd



    # mecabrc 파일 userdic 옵션 수정해야함.
    # userdic = self.prj_root + '\\userdic.dic'
    def csv2dic(self):
        c2d = os.popen(rf'"{self.mecab_dir}\bin\mecab-dict-index.exe" -d "{self.mecab_dir}\dic\ipadic" -u "{self.prj_root}\userdic\userdic.dic" -f utf-i -t utf8 "{self.prj_root}\userdic\userdic.csv"').read()
        



    def _ko2kata(self, string):
        r = ko_pron.romanise(string, 'rr')
        r = self._replacetext(r, {
            'si':'shi',
            'cheu':'tsu',
            'seu':'su',
            'ja':'za',
            'jeu':'zu',
            'je':'ze',
            'jo':'zo',
            'nxtsu':'n',
            '-':'',
        }) # 영어 표기에 잘못된 표기 커버 침.
        a = alphabet2kata(r)
        # print(f"{string}->{r}->{a}")
        return a


    def _replacetext(self, text, repl_dict):
        for key, value in repl_dict.items():
            text = str(text).replace(key, value)
        return text