import MeCab

class PreFilter:
    def __init__(self, text: str, dictList: dict):
        self.mecab = MeCab.Tagger()
        self.text = text
        self.dictList = dictList

    def pre_process(self):
        sep = '▒'
        sep_nl = '∮'
        self.text = self.text.replace('\r', '').replace('\n', sep_nl).replace('　', '')
        
        a = self.mecab.parse(self.text).split()[:-1]
        surface = a[0::2]
        pos = a[1::2]
        b = [(surface[i], i) for i, p in enumerate(pos) if ('固有名詞' in p) and (surface[i] in self.dictList)]

        for sur, idx in b:
            surface[idx] = f'{sep}{sur}{sep}'

        pre = ''.join(surface).replace(f'{sep}{sep}', f'{sep} {sep}').replace(sep_nl, '\n')
        return (pre, b)
        


