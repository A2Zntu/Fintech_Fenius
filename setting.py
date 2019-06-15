from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import requests as re


CAT = "pmzekB9tmEgsQdpAMMUI90jnUCpGUEVlzWpw+XuHDU+GrBvV1aNFacIkHrBOp1iszYCTBM90BJWoMINmkImKpBtbwmeiGtIv4deoK/CtGbgjRiniW9j8YDd5A0nKY3z9yAwySjjj3kZYYDQsfGVQpQdB04t89/1O/w1cDnyilFU="
CS = "04c8f8542383ce366112a122977ae64d"


w = 2500
h = 1686
# Channel Access Token
line_bot_api = LineBotApi(CAT)
# Channel Secret
handler = WebhookHandler(CS)


rich_menu_list = line_bot_api.get_rich_menu_list()

for rich_menu in rich_menu_list:
	line_bot_api.delete_rich_menu(rich_menu.rich_menu_id)


rich_menu_to_create = RichMenu(
    size=RichMenuSize(width=w, height=h),
    selected=False,
    name="Nice richmenu",
    chat_bar_text="Start here",
    areas=[
    RichMenuArea(
        bounds=RichMenuBounds(x=0, y=0, width=w/3, height=h/2),
        action=PostbackAction(
                label='basicInfo',
                data='basicInfo')
        ),
    RichMenuArea(
        bounds=RichMenuBounds(x=0, y=h/2, width=w/3, height=h/2),
        action=PostbackAction(
                label='history',
                data='history')
        ),
    RichMenuArea(
        bounds=RichMenuBounds(x=w/3, y=0, width=w/3, height=h/2),
        action=PostbackAction(
                label='indicator',
                data='indicator')
        ),
    RichMenuArea(
        bounds=RichMenuBounds(x=w/3, y=h/2, width=w/3, height=h/2),
        action=PostbackAction(
                label='portfolio',
                data='portfolio')
        ),
    RichMenuArea(
        bounds=RichMenuBounds(x=w*2/3, y=0, width=w/3, height=h/2),
        action=PostbackAction(
                label='best6',
                data='best6')
        ),
    RichMenuArea(
        bounds=RichMenuBounds(x=w*2/3, y=h/2, width=w/3, height=h/2),
        action=PostbackAction(
                label='web',
                data='web')
        )]
)
rich_menu_id = line_bot_api.create_rich_menu(rich_menu=rich_menu_to_create)
print(rich_menu_id)

with open("subfunction/pictures/RGB_1.jpg","rb") as f:
	line_bot_api.set_rich_menu_image(rich_menu_id, "image/jpeg", f)

headers = {"Authorization":"Bearer {}".format(CAT)}

re.post("https://api.line.me/v2/bot/user/all/richmenu/{}".format(rich_menu_id),headers=headers)


