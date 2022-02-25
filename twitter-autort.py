import tweepy

# ツイートするときのAPI
API_KEY = "自分のAPI"
API_SECRET = "自分のAPI"
ACCESS_TOKEN = "自分のAPI"
ACCESS_TOKEN_SECRET = "自分のAPI"
Bearer_token = '自分のAPI'

# Twitter API v2対応
client = tweepy.Client(consumer_key=API_KEY, consumer_secret=API_SECRET, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET, bearer_token=Bearer_token)

# 検索結果をリツイートしたい場合
# 検索したいキーワード入力
q = 'キーワード入力'

# 取得したい件数
counts = 10

# search_result = client.search_recent_tweets(query=q, max_results=counts)

# リスト取得 非公開リストは取得NG 公開設定にする
search_result = client.get_list_tweets(id="リストIDをここに入力", max_results=counts)
tweetids = search_result.data

for tweetid in tweetids:
    tid = tweetid.id
    try:
        client.retweet(tid) # 取り出したTweet idをRT
    except Exception as e:
        print(e)

print(search_result)