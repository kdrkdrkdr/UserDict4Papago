from lib.papagopy.papagopy import Papagopy
from lib.util import ListChunk
import asyncio

class PapagoTranslator:
    def __init__(self, text: str, chunk=5):
        self.chunk = chunk
        self.text = text
        self.p = Papagopy()
        self.t_list = []

    def translate(self):
        loop = asyncio.get_event_loop()
        text_list = self.text_chunk(self.text)
        self.t_list = list(range(len(text_list)))
        tasks = [asyncio.ensure_future(self.t_j2k(t, i)) for i, t in enumerate(text_list)]
        loop.run_until_complete(asyncio.wait(tasks))
        return ''.join(self.t_list)


    def text_chunk(self, text: str):
        a = text.splitlines()
        b = ListChunk(a, 1+int(len(a)//self.chunk))
        return ['\n'.join(i) for i in b]


    async def t_j2k(self, text, idx):
        t = self.p.translate(text, 'ko', 'ja')
        self.t_list[idx] = t

        


    