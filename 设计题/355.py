from collections import defaultdict
from typing import List


class Tweet:
    def __init__(self, user_id, time, tweet_id):
        # 当前推特属于哪个用户
        self.user_id = user_id
        # 生成时间
        self.time = time
        # 当前推特的id
        self.tweet_id = tweet_id


class User:
    def __init__(self, user_id):
        # 当前用户id
        self.user_id = user_id
        # 发送的推特
        self.tweets = []
        # 推特记录
        self.tweets_record = {self.user_id: self.tweets}


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 记录当前的用户
        self.record = defaultdict(User)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        # 创建一条推文
        self.time += 1
        # 生成推文

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        # 获取最近的推文，按逆序排列

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        # 关注一个用户
        # 将用户的推文放到推文列表中

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        # 取关一个用户
        # 将取关用户的推文删除


twitter = Twitter()

twitter.postTweet(1, 1)

twitter.getNewsFeed(1)

twitter.follow(2, 1)

twitter.getNewsFeed(2)

twitter.unfollow(2, 1)

twitter.getNewsFeed(2)
