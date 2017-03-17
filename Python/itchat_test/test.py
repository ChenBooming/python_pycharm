#coding=utf8
import itchat
# tuling plugin can be get here:
# https://github.com/littlecodersh/EasierLife/tree/master/Plugins/Tuling

from tuling import get_response

@itchat.msg_register('Text')
def text_reply(msg):
    if u'作者' in msg['Text'] or u'主人' in msg['Text']:
        return u'找陈蒙 421235586@qq.com'
    elif u'同盟会群' in msg['Text'] or u'同盟会' in msg['Text']:
        itchat.send('@img@/Users/koudai232/PycharmProjects/python_pycharm/Python/itchat_test/img/tongmenghui_group.png', msg['FromUserName'])
        return u'长按扫码进群，有问题请@陈蒙或者群主'
    elif u'白领活动' in msg['Text']:
        itchat.send('@img@/Users/koudai232/PycharmProjects/python_pycharm/Python/itchat_test/img/funbailing.jpg', msg['FromUserName']) # there should be a picture
        return u'长按扫码关注，有问题联系@陈蒙'
    elif u'亲子活动' in msg['Text']:
        itchat.send('@img@/Users/koudai232/PycharmProjects/python_pycharm/Python/itchat_test/img/funmili.jpg', msg['FromUserName'])  # there should be a picture
        return u'长按扫码关注，有问题联系@陈蒙'
    else:
        return get_response(msg['Text'])

@itchat.msg_register(['Picture', 'Recording', 'Attachment', 'Video'])
def atta_reply(msg):
    return (u'很好，'+{ 'Picture': u'图片', 'Recording': u'录音',
        'Attachment': u'附件', 'Video': u'视频', }.get(msg['Type']) +
        u'已转发给王珂') # download function is: msg['Text'](msg['FileName'])

@itchat.msg_register(['Map', 'Card', 'Note', 'Sharing'])
def mm_reply(msg):
    if msg['Type'] == 'Map':
        return u'收到位置分享'
    elif msg['Type'] == 'Sharing':
        return u'收到分享' + msg['Text']
    elif msg['Type'] == 'Note':
        return u'收到：' + msg['Text']
    elif msg['Type'] == 'Card':
        return u'收到好友信息：' + msg['Text']['Alias']

@itchat.msg_register('Text', isGroupChat = True)
def group_reply(msg):
    if msg['isAt']:
        return u'@%s\u2005%s' % (msg['ActualNickName'],
            get_response(msg['Text']) or u'收到：' + msg['Text'])

@itchat.msg_register('Friends')
def add_friend(msg):
    itchat.add_friend(**msg['Text'])
    itchat.send_msg(u'可设置自定义回复消息、图片甚至文件，比如：\n'
        + u'同盟会入群：回复 同盟会群\n' + u'亲子活动：回复 亲子活动\n' + u'白领活动：回复 白领活动\n'
        + u'有问题反馈：回复 有问题 然后发送到邮箱即可', msg['RecommendInfo']['UserName'])

itchat.auto_login(True, enableCmdQR=False)
itchat.run()

