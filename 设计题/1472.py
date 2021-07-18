#!/usr/bin/python3
# -*- coding:utf-8 -*-
class BrowserHistory:

    def __init__(self, homepage: str):
        # 当前浏览页面
        self.homepage = homepage
        # 初始化历史记录
        self.history = [self.homepage]
        # 当前在历史记录中的节点
        self.current_index = 0

    def visit(self, url: str) -> None:
        # 删除前进的浏览记录,当前节点后面的值，都会删除掉
        # 浏览节点更新
        self.current_index += 1
        # 删除当前节点后的访问记录
        self.history = self.history[:self.current_index]
        self.history.append(url)
        # 更新当前主页
        self.homepage = url

    def back(self, steps: int) -> str:
        # 返回后退到的网页
        index = self.current_index - steps
        if index < 0:
            index = 0
        self.current_index = index
        self.homepage = self.history[self.current_index]
        return self.homepage

    def forward(self, steps: int) -> str:
        # 返回前进的网页
        index = self.current_index + steps
        if index >= len(self.history):
            index = len(self.history) - 1
        self.current_index = index
        self.homepage = self.history[self.current_index]
        return self.homepage


browserHistory = BrowserHistory("leetcode.com")
browserHistory.visit("google.com")  # 你原本在浏览 "leetcode.com" 。访问 "google.com"
browserHistory.visit("facebook.com")  # 你原本在浏览 "google.com" 。访问 "facebook.com"
browserHistory.visit("youtube.com")  # 你原本在浏览 "facebook.com" 。访问 "youtube.com"

print(browserHistory.back(1))  # 你原本在浏览 "youtube.com" ，后退到 "facebook.com" 并返回 "facebook.com"
print(browserHistory.back(1))  # 你原本在浏览 "facebook.com" ，后退到 "google.com" 并返回 "google.com"
print(browserHistory.forward(1))  # 你原本在浏览 "google.com" ，前进到 "facebook.com" 并返回 "facebook.com"
print(browserHistory.visit("linkedin.com"))  # 你原本在浏览 "facebook.com" 。 访问 "linkedin.com"
print(browserHistory.forward(2))  # 你原本在浏览 "linkedin.com" ，你无法前进任何步数。

print(browserHistory.back(2))  # 你原本在浏览 "linkedin.com" ，后退两步依次先到 "facebook.com" ，然后到 "google.com" ，并返回 "google.com"
print(browserHistory.back(7))  # 你原本在浏览 "google.com"， 你只能后退一步到 "leetcode.com" ，并返回 "leetcode.com"
