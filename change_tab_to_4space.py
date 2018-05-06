#!/usr/bin/python3
# -*- coding:utf8 -*-
import codecs
import os, re, sys

FILE_PATH = '..\\AwesomeRenderer\\AwesomeRenderer\\src'

def analize_code(codefile):
    tab_num = 0
    file = None

    try:
        with open(codefile, 'r+',encoding="utf8") as f:
            file = f.read()
            for word in file:
                if word == '\t':
                    tab_num += 1
            # if '\t' in file:
                # print("存在tab, 将tab转换成4空格。")
            file_new = file.replace('\t', '    ')
            f.close()

        tab_num = 0
        for word in file_new:
            if word == '\t':
                tab_num += 1

        with open(codefile, 'w+',encoding="utf8") as f:
            f.write(file_new)
            f.close()
    except:
        print ("在%s中：" % codefile)
        print("error ")
    finally:
        pass

def run(FILE_PATH):
    total_lines = 0
    total_comment_lines = 0
    total_blank_lines = 0
    if not os.path.isdir(FILE_PATH):
        if os.path.splitext(FILE_PATH)[1] == '.h' or os.path.splitext(FILE_PATH)[1] == '.cpp' or os.path.splitext(FILE_PATH)[1] == '.hpp':
            analize_code(FILE_PATH)
    else:
        for i in os.listdir(FILE_PATH):
            if i[0] == '.':
                print(os.path.join(FILE_PATH, i))
                print("continue")
                continue
            run(os.path.join(FILE_PATH, i))

if __name__ == '__main__':
    run(FILE_PATH)