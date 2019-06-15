# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 23:05:12 2019

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


def confirmation(nowType = ""):
    message = TemplateSendMessage(
        alt_text = 'Confirm template',
        template = ConfirmTemplate(
            text = '請問您還要繼續查詢其他基金的相關資訊嗎?',
            actions=[
                PostbackTemplateAction(
                    label = '是',
                    text = None,
                    data = nowType
                ),
                PostbackTemplateAction(
                    label = '否',
                    text = None,
                    data = 'exit'
                )
            ]
        )
    )
    return message

