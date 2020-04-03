from PIL import Image, ImageDraw, ImageFont
import tkinter as tk
from tkinter import filedialog
from time import sleep
import numpy as np
from time import strptime
import datetime

like_picture = Image.open('bgimgs/like.png')
like_picture = like_picture.resize((17, 17))
comment_picture = Image.open('bgimgs/comment.png')
comment_picture = comment_picture.resize((17, 17))
retweet_picture = Image.open('bgimgs/retweet.png')
retweet_picture = retweet_picture.resize((17, 17))


bg_value = ['w', 'd', 'b']
bg_color = input(
    'Do you want background color to be white, dark or black?\nChoose w for white, d for dark or b for black\n')

if bg_color not in bg_value:
    print('Choose w, d or b')
    quit()

if bg_color == 'w':
    bg_path = 'bgimgs/light.png'
elif bg_color == 'd':
    bg_path = 'bgimgs/dark.png'
elif bg_color == 'b':
    bg_path = 'bgimgs/black.png'

bg_img = Image.open(bg_path)
bg_img = bg_img.resize((600, 420))


print('Select profile picture for the account\r')
sleep(1.5)


root = tk.Tk()
root.withdraw()
image_file = filedialog.askopenfilename()

profile_pic = Image.open(image_file, mode='r')

profile_pic = profile_pic.resize((55, 55))

mask = Image.new('L', profile_pic.size, 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0) + profile_pic.size, fill=255)
mask = mask.resize(profile_pic.size, Image.ANTIALIAS)
profile_pic.putalpha(mask)

bg_img.paste(profile_pic, (25, 40))

name = input('Enter name on the profile (not username)\n')
username = input('Enter username of profile\n')

img_draw = ImageDraw.Draw(bg_img)
font = ImageFont.truetype('bgimgs/helvetica-bold.ttf', 20)
if bg_color == 'w':
    img_draw.text((85, 45), name, (0, 0, 0), font=font)
elif bg_color == 'd':
    img_draw.text((85, 45), name, (255, 255, 255), font=font)
elif bg_color == 'b':
    img_draw.text((85, 45), name, (255, 255, 255), font=font)
font = ImageFont.truetype('bgimgs/helvetica-light.ttf', 17)
img_draw.text((85, 63), '@'+username,
              font=font, fill=(80, 80, 80))

if ' ' in username:
    print('Username cannot have space')
    quit()

tweet = input('Enter tweet')

font = ImageFont.truetype('bgimgs/helvetica.ttf', 23)
if bg_color == 'w':
    img_draw.text((25, 120), tweet, (0, 0, 0), font=font)
elif bg_color == 'd':
    img_draw.text((25, 120), tweet, (255, 255, 255), font=font)
elif bg_color == 'b':
    img_draw.text((25, 120), tweet, (255, 255, 255), font=font)

likes = int(input('Enter number of likes you want to see on this post\n'))
num_comments = int(
    input('Enter number of comments you want to see on the post\n'))
if num_comments > 3:
    print('Only less than 3 comments are supported at the moment')
    quit()
if num_comments >= 1:
    tweet_time = int(input(('Enter time in hhmm format')))

    if tweet_time > 2359:
        print("lol, that time doesn't exists")
        quit()

    tweet_time = str(tweet_time)
    tweet_time = strptime(tweet_time, '%H%M')

    tweet_date = input('Enter date in YYYY/MM/DD format')
    year, month, day = map(int, tweet_date.split('/'))

    try:
        tweet_date = datetime.date(year, month, day)
    except ValueError as dateerror:
        print('Enter proper date')
        quit()

    # print(f'{tweet_time.tm_hour}: {tweet_time.tm_min}')
retweets = int(input('Enter number of retweets you want to see on the post\n'))

if num_comments > 1:
    for yo in range(num_comments):
        comment = input('Enter %d comment' % yo)
elif num_comments == 1:
    comment = input('Enter comment')


if num_comments >= 1:

bg_img.paste(comment_picture, (27, 145))
font = ImageFont.truetype('bgimgs/helvetica.ttf', 17)
if bg_color == 'w':
    img_draw.text((57, 145), str(num_comments), (0, 0, 0), font=font)
elif bg_color == 'd':
    img_draw.text((57, 145), str(num_comments),
                  (255, 255, 255), font=font)
elif bg_color == 'b':
    img_draw.text((57, 145), str(num_comments),
                  (255, 255, 255), font=font)


bg_img.paste(retweet_picture, (150, 145))
font = ImageFont.truetype('bgimgs/helvetica.ttf', 17)
if bg_color == 'w':
    img_draw.text((180, 145), str(retweets), (0, 0, 0), font=font)
elif bg_color == 'd':
    img_draw.text((180, 145), str(retweets),
                  (255, 255, 255), font=font)
elif bg_color == 'b':
    img_draw.text((180, 145), str(retweets),
                  (255, 255, 255), font=font)


bg_img.paste(like_picture, (250, 145))
font = ImageFont.truetype('bgimgs/helvetica.ttf', 17)
if bg_color == 'w':
    img_draw.text((280, 145), str(likes), (0, 0, 0), font=font)
elif bg_color == 'd':
    img_draw.text((280, 145), str(likes), (255, 255, 255), font=font)
elif bg_color == 'b':
    img_draw.text((280, 145), str(likes), (255, 255, 255), font=font)

bg_img.show()
