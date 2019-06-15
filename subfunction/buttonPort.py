# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 10:23:30 2019

@author: Evan
"""

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

from constString import *

def buttonsForPort():
    
    message = TemplateSendMessage(
        alt_text = 'Buttons for Portfolio Template',
        template = ButtonsTemplate(
            thumbnail_image_url = 'https://i.imgur.com/3sajEuA.jpg',
            title = '基金投資組合建議',
            text = port_suggestion_intro,
            actions = [
                PostbackTemplateAction(
                    label = '六選二',
                    data = 'c62'
                ),
                PostbackTemplateAction(
                    label = '六選三',
                    data = 'c63'
                ), 
                PostbackTemplateAction(
                    label = '六選四',
                    data = 'c64'
                ),
                PostbackTemplateAction(
                    label = '六選五',
                    data = 'c65'
                )
            ]
        )
    )
    return message  