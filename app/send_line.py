from linebot import LineBotApi
from linebot.models import TextSendMessage

# 初始化 LineBotApi
line_bot_api = LineBotApi('你的 Channel Access Token')

# 發送訊息
def send_message(user_id, message):
    try:
        line_bot_api.push_message(user_id, TextSendMessage(text=message))
        print("訊息已成功發送！")
    except Exception as e:
        print(f"發送失敗：{e}")

# 測試發送
if __name__ == "__main__":
    user_id = "用戶的 LINE ID"
    message = "教會志工管理系統測試通知：本週服侍安排已更新！"
    send_message(user_id, message)
