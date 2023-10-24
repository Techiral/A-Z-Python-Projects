
from instabot import Bot

bot = Bot()
bot.login(username="your_username", password="your_password")

follow_opt = input("Follow single or multiple users(y/n):")
if follow_opt == 'y' or follow_opt == 'Y':
    to_follow = ["user_1","user_1","user_1","user_1"]
    bot.follow(user_id=to_follow)

unfollow_opt = input("Unfollow single or multiple users(y/n):")
if unfollow_opt == 'y' or unfollow_opt == 'Y':
    to_unfollow = ["user_1","user_1","user_1","user_1"]
    bot.unfollow(user_id=to_unfollow)

unfollow_non_opt = input("Unfollow those who don't follow you(y/n): ")
if unfollow_non_opt == 'y' or unfollow_non_opt == 'Y':
    bot.unfollow_non_followers()

message_opt = input("Message single or multiple users (y/n): ")
if message_opt == 'y' or message_opt == 'Y':
    message = "hello!"
    message_to = ["user_1","user_1","user_1","user_1"]
    bot.send_message(text=message, user_ids=message_to)

media_opt = input("Send media to single or multiple users (y/n): ")
if media_opt == 'y' or media_opt == 'Y':
    capt = "This is an image"
    media_path = "image.jpg"
    media_to = ["user_1","user_1","user_1","user_1"]
    bot.send_media(media_id=media_path, user_ids=media_to, text=capt)

hash_like_opt = input("Like posts having a hashtag (y/n): ")
if hash_like_opt == 'y' or hash_like_opt == 'Y':
    hashtag = ["hacktoberfest","coding"]
    amount = 10
    bot.like_hashtag(hashtag=hashtag, amount=amount)

block_opt = input("Block single or multiple users (y/n):")
if block_opt == 'y' or block_opt == 'Y':
    to_block = ["user_1","user_1","user_1","user_1"]
    bot.block_users(user_ids=to_block)

approve_pend_opt = input("Approve all pending follow requests (y/n):")
if approve_pend_opt == 'y' or approve_pend_opt == 'Y':
    bot.approve_pending_follow_requests()

hashtag_comment = input("Comment on all posts containing a specific hashtag (y/n):")
if hashtag_comment == 'y' or hashtag_comment == 'Y':
    hashtag_ = ["hacktoberfest","coding"]
    comment_ = ["wow", "nice", "cool"]
    num_comments = 10
    bot.comment_hashtag(hashtag_, amount=num_comments, comments=comment_)

user_hashtag_opt = input("Get the username of all the users who have participated in a hashtag (y/n):")
if user_hashtag_opt == 'y' or user_hashtag_opt == 'Y':
    hashtag = "hacktoberfest"
    bot.get_hashtag_users(hashtag=hashtag)

bot.logout()