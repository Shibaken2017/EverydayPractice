#!/usr/bin/env python
# -*- coding: utf-8 -*-



def _rot13(c):
    if 'A' <= c and c <= 'Z':
        # 13 文字分ずらす
        return chr((ord(c) - ord('A') + 13) % 26 + ord('A'))

    if 'a' <= c and c <= 'z':
        # 13 文字分ずらす
        return chr((ord(c) - ord('a') + 13) % 26 + ord('a'))

    # その他の文字は対象外
    return c


def rot13(s):
    # ジェネレータ内包表記で文字列に ROT13 を適用する
    g = (_rot13(c) for c in s)
    # 文字列に直す
    return ''.join(g)





print rot13("abcdetgt8adfkajdflakjdl!!!!!!")