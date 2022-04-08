from lib.post_filter import PostFilter
from lib.pre_filter import PreFilter
from lib.translator import PapagoTranslator
from lib.convert_dict import ConvertDictionary
from lib.util import ReadFile, WriteFile

text = ReadFile("./example_text/test.txt")


def main():

    dict_list = ConvertDictionary().convert()
    pre = PreFilter(text, dict_list).pre_process()
    trans = PapagoTranslator(pre[0], 10).translate()
    post = PostFilter(trans, dict_list, pre[1]).post_process()

    WriteFile(pre[0], './result/t-pre.txt') # 전처리
    WriteFile(trans, './result/t-trans.txt') # 파파고 번역
    WriteFile(post, './result/t-post.txt') # 후처리


import cProfile
main()
# cProfile.run("main()")
