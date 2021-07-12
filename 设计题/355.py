from collections import defaultdict
from typing import List


class Tweet:
    def __init__(self, tweet_id, time):
        # 生成时间
        self.time = time
        # 当前推特的id
        self.tweet_id = tweet_id


class User:
    def __init__(self, user_id):
        # 发送的推特
        self.tweets = []
        # 推特记录
        self.tweets_record = {user_id: self.tweets}


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 记录当前的用户
        self.record = defaultdict(User)
        self.time = 0

    def valid_user(self, user_id: int):
        # 验证是用户是否存在，如果不存在，则注册一个用户
        if user_id not in self.record:
            # 注册一个用户
            self.record[user_id] = User(user_id)
        return self.record[user_id]

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        # 创建一条推文
        self.time += 1
        # 生成推文
        user = self.valid_user(userId)
        tweet = Tweet(tweetId, self.time)
        user.tweets.append(tweet)

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        # 获取最近的十条推文，按逆序排列
        user = self.valid_user(userId)
        # 获取全部推文
        all_tweets = []
        for tweet_items in user.tweets_record.values():
            all_tweets.extend(tweet_items)
        # 按时间排序
        all_tweets.sort(key=lambda x: -x.time)
        # 获取全部推文
        tweet_result = []
        for item in all_tweets:
            tweet_result.append(item.tweet_id)

        return tweet_result[:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        # 关注一个用户
        # 将用户的推文放到推文列表中
        follow_user = self.valid_user(followerId)
        followee_user = self.valid_user(followeeId)
        follow_user.tweets_record[followeeId] = followee_user.tweets

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        # 取关一个用户
        # 将取关用户的推文删除
        follow_user = self.valid_user(followerId)
        if followeeId in follow_user.tweets_record:
            follow_user.tweets_record.pop(followeeId)


twitter = Twitter()

# twitter.postTweet(1, 1)
#
# print(twitter.getNewsFeed(1))
#
# twitter.follow(2, 1)
#
# print(twitter.getNewsFeed(2))
#
# twitter.unfollow(2, 1)
#
# print(twitter.getNewsFeed(2))

twitter.postTweet(1, 4)
twitter.postTweet(2, 5)
twitter.unfollow(1, 2)
print(twitter.getNewsFeed(1))
