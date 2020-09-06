secret = 'AzeXYjJ5JiRATg_1NU5V31u4WS8'
ID = 'HblZI_4KTr2kKA'
import praw
# a reddit instance
reddit = praw.Reddit(client_id='**',
                     client_secret='**',
                     user_agent='**',
                     username='**',
                     password='**',)
# phrase to trigger the bot
trigger_phrase = "!beejbot "
# check every comment in the subreddit
for comment in reddit.subreddit('ritbeej').stream.comments():
    # check the trigger_phrase in each comment
    if trigger_phrase in comment.body:
        # extract the word from the comment
        number = comment.body.replace(trigger_phrase, "")
        try:
            number = int(number)
        except:
            number = 10
        if number > 500:
            number = 500
        beej = ''
        for i in range(number):
            beej += 'rit beej '
        comment.reply(beej + ' https://imgur.com/a/ltIaifR')