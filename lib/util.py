import codecs


def WriteFile(text: str, filename: str):
    f = codecs.open(filename, mode='w', encoding='utf-8')
    f.write(u'{}'.format(text))
    f.close()


def ReadFile(filename: str):
    f = codecs.open(filename, mode='r', encoding='utf-8')
    return f.read()


def ListChunk(lst, n):
    return tuple([tuple(lst[i:i+n]) for i in range(0, len(lst), n)])

