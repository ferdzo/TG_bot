#!/usr/bin/python3
from telegram.ext import Updater, CommandHandler
import logging
import random
import sys
import os
from ratelimit import limits
import ratelimit
from time import sleep

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

tibam_arr = ["zenite", "chupinjata sho ni ebaja mater", "Θ"]
pesna_arr = ["https://youtu.be/zJCKU54NozA", "https://youtu.be/VlOe4tuVklg",
             "https://youtu.be/f46LkPDypSY", "https://youtu.be/MmAAcmV1D5U", "https://youtu.be/Aa_Ht2EAsso"]
#rand_int = random.randint(0, len(tibam_arr))


def tibam_update(sho):
    with open('tibam_conf.txt', 'a') as f:
        f.write("%s\n" % sho)


def pesna_update(sho):
    with open('pesna_conf.txt', 'a') as f:
        f.write("%s\n" % sho)


#@limits(calls=2, period=30)
def tibam(bot, update):
    try:
        rand_int = random.randint(0, len(tibam_arr)-1)
        update.message.reply_text('/tibam {}!'.format(tibam_arr[rand_int].rstrip()))
    except:
        bot.delete_message(chat_id=-1001328727045,
                           message_id=update.message.message_id)


@limits(calls=2, period=30)
def tibam_add(bot, update, args="asidofjsoifjdsoifj"):
    if(args == "asidofjsoifjdsoifj"):
        update.message.reply_text('Tibam glupio!')
    else:
        try:
            # print(args)
            ebenoto = " "
            ebenoto = ebenoto.join(args)
            # print(ebenoto)
            tibam_arr.append(ebenoto)
            tibam_update(ebenoto)
            update.message.reply_text(
                '\"{}\" ke bide ebeno otsega!'.format(ebenoto))
        except:
            bot.delete_message(chat_id=-1001328727045,
                               message_id=update.message.message_id)


@limits(calls=2, period=30)
def pesna_add(bot, update, args="asidofjsoifjdsoifj"):
    if(args == "asidofjsoifjdsoifj"):
        update.message.reply_text('Tibam glupio!')
    else:
        try:
            # print(args)
            if("youtube.com" in args[0] or "youtu.be" in args[0] and args[0] not in pesna_arr):
                pesnata = args[0]
            else:
                update.message.reply_text('Ne si zdrav ti')
            pesna_arr.append(pesnata)
            pesna_update(pesnata)
            update.message.reply_text(
                '\"{}\" ke bide svirena otsega!'.format(pesnata))
        except RateLimitException:
            bot.delete_message(chat_id=-1001328727045, message_id=update.message.message_id)


@limits(calls=2, period=30)
def pesna(bot, update):
    try:
        rand_int = random.randint(0, len(pesna_arr)-1)
        update.message.reply_text(pesna_arr[rand_int])
    except ratelimit.RateLimitException:
        bot.delete_message(chat_id=-1001328727045,
                           message_id=update.message.message_id)
    #bot.sendPhoto(chat_id=-1001328727045, photo="https://i.ytimg.com/vi/-dTBmozP1k0/hqdefault.jpg", caption="siptar")


@limits(calls=1, period=120)
def gaysearch(bot, update):
    try:
        id = bot.send_message(chat_id=-1001328727045,
                              text="Trazenje pedera")["message_id"]
        for j in range(1, 3):
            for i in range(1, 4):
                bot.edit_message_text(
                    chat_id=-1001328727045, message_id=id, text="Trazenje pedera" + "."*i)
                sleep(2)
        peder_arr = ["@Laminati", "@Yanderrated", "@dimitarbez", "@ferdzo"]
        peder = peder_arr[random.randint(0, len(peder_arr)-1)]
        bot.send_message(chat_id=-1001328727045,
                         text="PEDER PRONADJEN!!!!!! " + str(peder))
    except:
        bot.delete_message(chat_id=-1001328727045,
                           message_id=update.message.message_id)
# def slika(bot, update):

def delete(bot, update):
    bot.delete_message(chat_id=-1001328727045,
                           message_id=update.message.message_id)

updater = Updater('932777104:AAEdosIzLAgPzXA24v01-L6BGsFK282L4Jo')
with open('tibam_conf.txt', 'r') as f:
    for x in f:
        tibam_arr.append(x)
with open('pesna_conf.txt', 'r') as f:
    for x in f:
        pesna_arr.append(x)

updater.dispatcher.add_handler(CommandHandler('tibam', tibam))
updater.dispatcher.add_handler(CommandHandler(
    'tibam_add', tibam_add, pass_args=True))
updater.dispatcher.add_handler(CommandHandler('pesna', pesna))
updater.dispatcher.add_handler(CommandHandler(
    'pesna_add', pesna_add, pass_args=True))
updater.dispatcher.add_handler(CommandHandler('peder', gaysearch))
updater.dispatcher.add_handler(CommandHandler('izbrishime', delete))
#updater.dispatcher.add_handler(CommandHandler('gibnigo_tunaso', alarm))

updater.start_polling()
updater.idle()
