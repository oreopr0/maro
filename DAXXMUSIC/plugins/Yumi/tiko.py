import requests
import telebot



@bot.message_handler(regexp='https://vm.tiktok.com')
def Url(message):
    global msgg
    try:
        msgg = bot.send_message(message.chat.id, "*دادەبەزێت کەمێك چاوەڕێبە . . . ❗️*", parse_mode="markdown")
        msg = message.text
        url = requests.get(f'https://tikwm.com/api/?url={msg}').json()
        music = url['data']['music']
        region = url['data']['region']
        tit = url['data']['title']
        vid = url['data']['play']
        ava = url['data']['author']['avatar']
        ##
        name = url['data']['music_info']['author']
        time = url['data']['duration']
        sh = url['data']['share_count']
        com = url['data']['comment_count']
        wat = url['data']['play_count']
        bot.delete_message(chat_id=message.chat.id, message_id=msgg.message_id)
        bot.send_photo(message.chat.id, ava,
                       caption=f'*✧ ¦ ناو : {name}*\n*✧ ¦ وڵات : {region}*\n\n*✧ ¦ ژمارەی بینەر : {wat}*\n*✧ ¦ ژمارەی کۆمێنت : {com}*\n*✧ ¦ ژمارەی شەیرەکان : {sh}*\n*✧ ¦ درێژی ڤیدیۆ : {time}*',
                       parse_mode="markdown")
        bot.send_video(message.chat.id, vid, caption=f"{tit}")
    except:
        pass
        bot.delete_message(chat_id=message.chat.id, message_id=msgg.message_id)
        bot.reply_to(message, '*هەڵەیە *', parse_mode="markdown")
