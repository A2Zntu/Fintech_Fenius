# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 16:46:32 2019

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
from subfunction.fund_info import *
import random
import time

def carousel():

    random.seed(time.time())
    message = TemplateSendMessage(
        alt_text = 'Carousel template',
        template = CarouselTemplate(
            columns = [
                # Index 
                CarouselColumn(
                    thumbnail_image_url = 'https://i.imgur.com/xW7A61K.jpg',
                    title = '指數型基金',
                    text = '共14檔有效基金',
                    actions=[
                        PostbackTemplateAction(
                            label = '\U0001f4CC 指數型基金列表',
                            text = None,
                            data = 'IndexFundList'
                        ),
                        MessageTemplateAction(
                            label = '\U0001f500 隨機一檔基金',
                            text = "".join(random.choice(allFund(category = "Index"))[:3])
                        )
                    ]
                ), 
                # Technology    
                CarouselColumn(
                    thumbnail_image_url = 'https://i.imgur.com/dfedd6c.jpg',
                    title = '科技型基金',
                    text = '共25檔有效基金',
                    actions = [
                        PostbackTemplateAction(
                            label = '\U0001f4CC 科技型基金列表',
                            text = None,
                            data = 'TechFundList'
                        ),
                        MessageTemplateAction(
                            label='\U0001f500 隨機一檔基金',
                            text = "".join(random.choice(allFund(category = "Tech"))[:3])
                        )
                    ]
                ),
                # Common
                CarouselColumn(
                    thumbnail_image_url = 'https://i.imgur.com/5waJyuI.jpg',
                    title = '一般股票型基金',
                    text = '共73檔有效基金',
                    actions = [
                        PostbackTemplateAction(
                            label = '\U0001f4CC 一般股票型基金列表',
                            text = None,
                            data = 'CommonFundList'
                        ),
                        MessageTemplateAction(
                            label = '\U0001f500 隨機一檔基金',
                            text = "".join(random.choice(allFund(category = "Common"))[:3])
                        )
                    ]
                ),
                # China
                CarouselColumn(
                    thumbnail_image_url = 'https://i.imgur.com/oX9VLFY.jpg',
                    title = '中概型基金',
                    text = '共6檔有效基金',
                    actions = [
                        PostbackTemplateAction(
                            label = '\U0001f4CC 中概型基金列表',
                            text = None,
                            data = 'ChinaFundList'
                        ),
                        MessageTemplateAction(
                            label = '\U0001f500 隨機一檔基金',
                            text = "".join(random.choice(allFund(category = "China"))[:3])
                        )
                    ]
                ), 
                # Value
                CarouselColumn(
                    thumbnail_image_url = 'https://i.imgur.com/kIVlWiQ.jpg',
                    title = '價值型基金',
                    text = '共5檔有效基金',
                    actions = [
                        PostbackTemplateAction(
                            label = '\U0001f4CC 價值型基金列表',
                            text = None,
                            data = 'ValueFundList'
                        ),
                        MessageTemplateAction(
                            label = '\U0001f500 隨機一檔基金',
                            text = "".join(random.choice(allFund(category = "Value"))[:3])
                        )
                    ]
                ), 
                # OTC
                CarouselColumn(
                    thumbnail_image_url = 'https://i.imgur.com/dFEG8ow.jpg',
                    title = '店頭型基金',
                    text = '共5檔有效基金',
                    actions = [
                        PostbackTemplateAction(
                            label = '\U0001f4CC 店頭型基金列表',
                            text = None,
                            data = 'OTCFundList'
                        ),
                        MessageTemplateAction(
                             label = '\U0001f500 隨機一檔基金',
                             text = "".join(random.choice(allFund(category = "OTC"))[:3])
                        )
                    ]
                )
            ]
        )
    )
    
    return message

