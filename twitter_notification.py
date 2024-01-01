# twitter_notification.py

import tweepy
from plyer import notification

# Twitter API credentials
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Retrieve direct messages
direct_messages = api.get_direct_messages()

# Filter message requests
message_requests = [msg for msg in direct_messages if 'message_create' in msg]

# Display notifications for message requests
for request in message_requests:
    sender = request['message_create']['sender_id']
    notification.notify(
        title="Twitter Notification",
        message=f"New Message Request from {sender}",
    )
