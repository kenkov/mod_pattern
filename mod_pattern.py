#! /usr/bin/env python
# coding:utf-8


from mod import Mod
import random
import os
import re
from typing import List, Tuple


class ModPattern(Mod):
    def __init__(
            self,
            filename: str=None,
            logger=None
    ):
        Mod.__init__(self, logger)
        self.dict_path = filename or os.path.join(
            os.path.abspath(os.path.dirname(__file__)),
            "pattern_dict.txt"
        )
        self.re_text_lst = self.load_dict()

    def load_dict(self) -> List[Tuple["ReObj", str]]:
        re_text_lst = []
        with open(self.dict_path) as f:
            for line in f:
                regex, text = line.strip().split("\t")
                re_text_lst.append(
                    (re.compile(regex), text)
                )
        return re_text_lst

    def can_utter(self, message, master):
        return True

    def utter(self, message, master):
        replies = []
        for regex, text in self.re_text_lst:
            if regex.search(message["text"]):
                replies.append((regex, text))
        return [
            (random.uniform(0, 0.2),
             text, "random", dict())
            for _, text in replies
        ]
