#微信机器人的设计
#2018.3.14
#Tony Stark
#wxpy mark1
#########################

#导入wxpy模块
from wxpy import *
#登陆微信
bot=Bot(cache_path=True,console_qr=True)
# 机器人账号自身
myself = bot.self
#向文件助手发送消息
bot.file_helper.send("Hello from wxpy!")

"""
bot.self.add()
bot.self.accept()
bot.self.send('Hello!')

Girlfriend=bot.friends().search(u'LEEANyuu')[0]
Girlfriend.send('Hello')

DingNing=bot.friends().search(u'ding')[0]
DingNing.send('Hello')

ZhuangQianhui=bot.friends().search(u'晓月、寒')[0]
ZhuangQianhui.send('Hello')

WuJiaxing=bot.friends().search(u'黑MAMBA曼爷')[0]
WuJiaxing.send('Hello')
"""
