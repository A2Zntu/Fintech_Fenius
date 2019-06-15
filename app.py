from flask import Flask, request, abort, render_template, url_for

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)

from constString import *
from linebot.models import *
from subfunction.fund_info import *
from subfunction.fund_best import *
from subfunction.carousel import *
from subfunction.confirmation import *
from subfunction.buttonPort import *
from subfunction.carouselbest6 import *
import pandas as pd 


app = Flask(__name__)



menuOptions = ["basicInfo","indicator","best6","history","portfolio","web"]

fundType2List = ["TechFundList","IndexFundList", "CommonFundList", "ChinaFundList","ValueFundList","OTCFundList"]

users = {}

rich_menu_id = ""

best5Data = ""

# Channel Access Token
line_bot_api = LineBotApi(CAT)
# Channel Secret
handler = WebhookHandler(CS)



# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


@handler.add(JoinEvent)
def handle_join(event):
    
    line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text = newcoming_text)
        )
    
    print("JoinEvent =", JoinEvent)

# here we handle 6 type of requests
@handler.add(PostbackEvent)
def handle_postback(event):
    eventType = event.postback.data
    uid = event.source.user_id
    print(eventType)

    if uid not in users or users[uid] == -1:
        # User choose the main menu
        if eventType == 'exit':
            users[uid] = -1
            reply_text = back2Menu
            message = TextSendMessage(text = reply_text) 
            reply_text2 = thank2leave 
            message2 = TextSendMessage(text = reply_text2) 
            replyMessage = [message, message2]
            line_bot_api.reply_message(event.reply_token, replyMessage)


        elif eventType not in menuOptions:
            print("Invalid post back data")

        elif eventType == "basicInfo":
            users[uid] = 0

            message = carousel()
            line_bot_api.reply_message(event.reply_token, message)
            
        elif eventType == "indicator":
            # TODO 
            image_message = ImageSendMessage(
                original_content_url='https://hello-ym-world.herokuapp.com/static/indicator.jpg',
                preview_image_url='https://hello-ym-world.herokuapp.com/static/indicator.jpg'
            )
            line_bot_api.reply_message(event.reply_token, image_message)
            
        elif eventType == "best6":
            users[uid] = 2

            message = carouselforbest6()
            line_bot_api.reply_message(event.reply_token, message)
 
        elif eventType == "history":
            users[uid] = 3
            message = carousel()
            line_bot_api.reply_message(event.reply_token, message)

        elif eventType == "portfolio":
            users[uid] = 4
            message = buttonsForPort()
            line_bot_api.reply_message(event.reply_token, message)
            
        elif eventType == "web":
            users[uid] = 5
            message = TextSendMessage(text = webInfo)
            line_bot_api.reply_message(event.reply_token, message)
            users[uid] = -1

        else:
            # the program shouldn't run here !!
            message = TextSendMessage(text = noSupport)
            line_bot_api.reply_message(event.reply_token, message)

    elif users[uid] in [0,1,2,3,4,5]:

        
        if eventType in fundType2List:
            # get list fund post back command
            if users[uid] == 0 or users[uid] == 3:
                fundType = eventType.split("FundList")[0]
                FundList = allFund(category = fundType)
                message = "\n".join(s for s in FundList)
                message = TextSendMessage(text = message)
                message2 = TextSendMessage(text = exampleText)
                replyMessage = [message, message2]
                line_bot_api.reply_message(event.reply_token, replyMessage)
            
            elif users[uid] == 2:
                fundType = eventType.split("FundList")[0]
                image_message = ImageSendMessage(
                original_content_url='https://hello-ym-world.herokuapp.com/static/{}.jpg'.format(fundType),
                preview_image_url='https://hello-ym-world.herokuapp.com/static/{}.jpg'.format(fundType)
                )
                
                confirmMessage = confirmation(menuOptions[users[uid]])
                reply_message = [image_message, confirmMessage]
                line_bot_api.reply_message(event.reply_token, reply_message)       
                
                users[uid] = -1  
            
            
            else:
                 # TODO
                message = TextSendMessage(text = noSupport)
                line_bot_api.reply_message(event.reply_token, message)

        elif users[uid] == 4:
            num = eventType[-1]
            f = open("subfunction/data/Port_info/port_{}.txt".format(num),"r")
            msg = f.read()
            
            message = TextSendMessage(text = msg)
            confirmMessage = confirmation(menuOptions[users[uid]])

            reply_message = [message, confirmMessage]

            line_bot_api.reply_message(event.reply_token, reply_message)

            users[uid] = -1

    else:
        message = TextSendMessage(text = noSupport) 
        line_bot_api.reply_message(event.reply_token, message)



# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):    
    text = event.message.text
    uid = event.source.user_id

    print("recieved message:{}".format(text))
    if not (uid in users) or users[uid] == -1:
        if text == "講笑話" or text == "笑話":
            reply_text = joke
        elif text == "唱首歌" or text == "唱歌":
            reply_text = song
        elif text in helloWords:
            reply_text = helloReply
        elif text in JoanChen:
            reply_text = thankChen
        else:
            reply_text = selectMenu
        message = TextSendMessage(text = reply_text) 
        line_bot_api.reply_message(event.reply_token, message)
            
    else:
        if text.lower() == "exit":
            users[uid] = -1
            reply_text = back2Menu
            message = TextSendMessage(text = reply_text) 
            reply_text2 = thank2leave 
            message2 = TextSendMessage(text = reply_text2) 
            replyMessage = [message, message2]
            line_bot_api.reply_message(event.reply_token, replyMessage)

        elif users[uid] == 0: 
            # user want to check a specific fund state
            # need to change category into codename
            reply = info_generate(codeName = text)
            reply_text = "".join(s for s in reply)
            message = TextSendMessage(text = reply_text) 
            confirmMessage = confirmation(menuOptions[users[uid]])
            # conbine two messages
            replyMessage = [message, confirmMessage]
            line_bot_api.reply_message(event.reply_token, replyMessage)

            users[uid] = -1


        elif users[uid] == 3:

            image_message = ImageSendMessage(
                original_content_url='https://hello-ym-world.herokuapp.com/static/{}.jpg'.format(text),
                preview_image_url='https://hello-ym-world.herokuapp.com/static/{}.jpg'.format(text)
            )
            reply = ret_generate(codeName = text)
            reply_text = "".join(s for s in reply)
            message = TextSendMessage(text = reply_text)
            
            confirmMessage = confirmation(menuOptions[users[uid]])
            reply_message = [image_message, message, confirmMessage]
            line_bot_api.reply_message(event.reply_token, reply_message)       
            
            users[uid] = -1    
        
        elif users[uid] == 2:
            if text == "指數型最佳基金":
                reply = best6risk(category = "etf")
 
            elif text == "科技型最佳基金":
                reply = best6risk(category = "tech")
                
            elif text == "一般股票型最佳基金":
                reply = best6risk(category = "common")
                
            elif text == "價值型最佳基金":
                reply = best6risk(category = "value")
                
            elif text == "店頭市場型最佳基金":
                reply = best6risk(category = "otc")
                
            elif text == "中概型最佳基金":
                reply = best6risk(category = "china")
                
            else:
                # should not be here
                reply = "Something wrong"
                
            reply_message = TextSendMessage(text = reply)
            line_bot_api.reply_message(event.reply_token, reply_message) 
            
            users[uid] = -1              
        
        
        else:
            reply_text = event.message.text
            message = TextSendMessage(text = reply_text) 
            line_bot_api.reply_message(event.reply_token, message)



        

import os
if __name__ == "__main__":


    try:
        f = open("static/best6.txt","r")
    except:
        best5Data = best5Caller() # only need to change this !
        f = open("static/best6.txt","w")
        f.write("\n\n".join(s for s in best5Data))
        f.close()


    rich_menu_list = line_bot_api.get_rich_menu_list()
    rich_menu_id = rich_menu_list[0].rich_menu_id

    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
