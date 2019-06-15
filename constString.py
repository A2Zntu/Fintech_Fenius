import pandas as pd
import random
import time

CAT = "pmzekB9tmEgsQdpAMMUI90jnUCpGUEVlzWpw+XuHDU+GrBvV1aNFacIkHrBOp1iszYCTBM90BJWoMINmkImKpBtbwmeiGtIv4deoK/CtGbgjRiniW9j8YDd5A0nKY3z9yAwySjjj3kZYYDQsfGVQpQdB04t89/1O/w1cDnyilFU="
CS = "04c8f8542383ce366112a122977ae64d"

newcoming_text = "歡迎加入Fenius, 我會盡力為大家服務的～"

back2Menu = "返回基金目錄"

thank2leave = "謝謝您的使用，歡迎您查詢基金其他功能，我將竭盡為您服務 \U0001f603"

helloWords = ["您好", "Hello","hi", "Hi", "哈囉", "安安你好", "早安", "嗨", "你好", "妳好"]

helloReply = random.choice(helloWords)

JoanChen = ["陳往昀", "往昀"]

thankChen = "謝謝往昀 (板橋桂綸鎂) 幫我設計這麼完美的大頭貼與圖文選單，非常感謝您"

noSupport = "尚未支援該功能，正在開發中，敬請稍後 \U0001f602"

exampleText = "請輸入基金代碼，如A01, 即可幫您查詢 「元大台灣卓越50基金」，以此類推 \U0001f600"

waitingMsg = "正在計算資料，這個步驟花費大概會花費10秒，請您耐心稍等"

passReturnMsg = "請選擇下一個所欲查詢的內容"

indicatorMsg = "改我"

selectMenu = "您好，請選擇Fenius的清單，我將竭盡為您服務"

def best6risk(category):
    if category == "tech":
        line = "科技型基金最佳: 安聯台灣科技基金" + "\n"+ "其風險Q值為 4.1408 * 10^-8"
    elif category == "china":
        line = "中概型基金最佳: 聯邦中國龍基金" + "\n"+ "其風險Q值為 2.8838 * 10^-4"
    elif category == "common":
        line = "一般型基金最佳: 兆豐豐台灣基金" + "\n"+ "其風險Q值為 1.5216 * 10^-11"
    elif category == "etf":
        line = "指數型基金最佳: 富邦台灣金融基金" + "\n"+ "其風險Q值為 1.7027 * 10^-12"
    elif category == "value":
        line = "價值型基金最佳: 野村台灣高股息基金" + "\n"+ "其風險Q值為 7.7762 * 10^-10"
    elif category == "otc":
        line = "價值型基金最佳: 群益店頭市場基金" + "\n"+ "其風險Q值為 5.1085 * 10^-3"
    
    return line


port_suggestion_intro = "試算方式：配合您想要組合的基金數量(2~5隻)，以等權重試算各種可能的組合，最後為您選出最佳搭配！"

def randomTemplate(script):
    random.seed(time.time())
    if script == "song":
        scriptName =  "song" + str(random.choice([0])) + ".txt"
        
    elif script == "joke":
        scriptName = "joke" + str(random.choice([0, 1, 2, 3, 4])) + ".txt"
    
    scriptContent = "".join(word + "\n" for word in pd.read_csv("subfunction/reply_text/" + scriptName, encoding = "cp950")["Begin"])
    return scriptContent

def webList():
    df_webList = pd.read_csv("subfunction/data/website_list.csv", encoding = "cp950")
    
    lines = []
    for i in range(len(df_webList)):
        string = u'\u2022' + " " + df_webList["WebName"][i] + " : " + df_webList["URL"][i] + "\n"
        lines.append(string)
        lines.append("\n")
    
    content = "".join(line for line in lines)
    return content

webInfo = webList()

joke = randomTemplate(script = "joke")

song = randomTemplate(script = "song")