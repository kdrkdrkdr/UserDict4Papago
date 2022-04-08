import MeCab
from lib.util import ReplaceText
from lib.convert_dict import ConvertDictionary

class PreFilter:
    def __init__(self, text: str, dictList: dict):
        self.mecab = MeCab.Tagger()
        self.text = text
        self.dictList = dictList
        self.c = ConvertDictionary()

    def pre_process(self):
        sep_nl = '∮'
        self.text = ReplaceText(
            self.text, {
                '\r':'',
                '\n':sep_nl,
                '　':'',
                '｢':' "',
                '｣':'" '
            }
        )
        
        a = self.mecab.parse(self.text).split()[:-1]
        surface = a[0::2]
        pos = a[1::2]
        b = [(surface[i], i) for i, p in enumerate(pos) if ('固有名詞' in p) and (surface[i] in self.dictList)]

        for sur, idx in b:
            surface[idx] = f'^{self.c._ko2kata(self.dictList[sur])}'

        pre = ''.join(surface).replace(sep_nl, '\n')
        return (pre, b)
        