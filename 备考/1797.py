#!/usr/bin/python3
# -*- coding:utf-8 -*-
from collections import defaultdict


class Token:
    def __init__(self, token_id: str, time: int):
        # 当前验证的id
        self.token_id = token_id
        # 验证码生成时间，如果被更新，则延长
        self.time = time
        # 验证码过期时间
        self.die_time = 0


class AuthenticationManager:

    def __init__(self, timeToLive: int):
        # 验证码有效时间
        self.live_time = timeToLive
        # 记录当前系统的验证码
        self.record = defaultdict(Token)

    def generate(self, tokenId: str, currentTime: int) -> None:
        # 生成验证码
        if tokenId not in self.record:
            # 生成验证码
            token = Token(tokenId, currentTime)
            # 更新验证码过期时间
            token.die_time = currentTime + self.live_time
            # 存储到系统
            self.record[tokenId] = token

    def renew(self, tokenId: str, currentTime: int) -> None:
        # 更新验证码
        if tokenId not in self.record:
            return
        # 验证当前时间和过期时间，如果未过期，则更新
        if self.record[tokenId].die_time < currentTime:
            # 更新过期 时间
            self.record[tokenId].die_time = currentTime + self.live_time

    def countUnexpiredTokens(self, currentTime: int) -> int:
        cnt = 0
        # 返回没有过期的验证个数
        for token_id, token in self.record.items():
            if token.die_time > currentTime:
                cnt += 1
        return cnt


authenticationManager = AuthenticationManager(5)  # 构造 AuthenticationManager ，设置 timeToLive = 5 秒。
authenticationManager.renew("aaa", 1)  # 时刻 1 时，没有验证码的 tokenId 为 "aaa" ，没有验证码被更新。
authenticationManager.generate("aaa", 2)  # 时刻 2 时，生成一个 tokenId 为 "aaa" 的新验证码。
authenticationManager.countUnexpiredTokens(6)  # 时刻 6 时，只有 tokenId 为 "aaa" 的验证码未过期，所以返回 1 。
authenticationManager.generate("bbb", 7)  # 时刻 7 时，生成一个 tokenId 为 "bbb" 的新验证码。
authenticationManager.renew("aaa", 8)  # tokenId 为 "aaa" 的验证码在时刻 7 过期，且 8 >= 7 ，所以时刻 8 的renew 操作被忽略，没有验证码被更新。
authenticationManager.renew("bbb", 10)  # tokenId 为 "bbb" 的验证码在时刻 10 没有过期，所以 renew 操作会执行，该 token 将在时刻 15 过期。
authenticationManager.countUnexpiredTokens(
    15)  # tokenId 为 "bbb" 的验证码在时刻 15 过期，tokenId 为 "aaa" 的验证码在时刻 7 过期，所有验证码均已过期，所以返回 0 。
print(authenticationManager.record)
