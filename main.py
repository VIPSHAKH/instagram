# -*- coding: utf-8 -*-
# DONT_REMOVE_THIS
#  TheDarkW3b (c)

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import ParseMode, Update
import logging
import requests
import json

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',

                    level=logging.INFO)

#Logger Setup
logger = logging.getLogger(__name__)

TOKEN = "6099343372:AAEeZlUfpYLFCdyipCBBA4G3UflG12CJuAA"

def download(update: Update, context: CallbackContext):
    message = update.effective_message
    instagram_post = message.text
    if instagram_post=="/start":
        context.bot.send_chat_action(chat_id=update.message.chat_id, action="typing")
        update.message.reply_text("❤️ Thanks For Using Me Just Send Me The Link In Below Format  \n🔥 Format :- https://www.instagram.com/p/B4zvXCIlNTw/ \nVideos Must Be Less Then 20MB, For Now It Cannot Support Long IGTV Videos \n\n<b>Support Group :-</b> @Technology_Arena \n<b>🌀 Source</b> \nhttps://github.com/TheDarkW3b/instagram", parse_mode=ParseMode.HTML, disable_web_page_preview=True)
    else:
        pass
    if "instagram.com" in instagram_post:
        changing_url = instagram_post.split("/")
        url_code = changing_url[4]
        url = f"https://instagram.com/p/{url_code}?__a=1"
        try:
            global checking_video
            visit = requests.get(url).json()
            checking_video = visit['graphql']['shortcode_media']['is_video']
        except:
            context.bot.sendMessage(chat_id=update.message.chat_id, text="Send Me Only Public Instagram Posts ⚡️")
        
        if checking_video==True:
            try:
                video_url = visit['graphql']['shortcode_media']['video_url']
                context.bot.send_chat_action(chat_id=update.message.chat_id, action="upload_video")
                context.bot.sendVideo(chat_id=update.message.chat_id, video=video_url)
            except:
                pass

        elif checking_video==False:
            try:
                post_url = visit['graphql']['shortcode_media']['display_url']
                context.bot.send_chat_action(chat_id=update.message.chat_id, action="upload_photo")
                context.bot.sendPhoto(chat_id=update.message.chat_id, photo=post_url)
            except:
                pass
        else:
            context.bot.send_chat_action(chat_id=update.message.chat_id, action="typing")
            context.bot.sendMessage(chat_id=update.message.chat_id, text="I Cant Send You Private Posts :-( ")
    else:
        context.bot.sendMessage(chat_id=update.message.chat_id, text="Kindly Send Me Public Instagram Video/Photo Url")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    logger.info("Setting Up MessageHandler")
    dp.add_handler(MessageHandler(Filters.text, download))
    updater.start_polling()
    logging.info("Starting Long Polling!")
    updater.idle()

if __name__ == "__main__":
    main()
