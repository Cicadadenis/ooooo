import sqlite3
import requests, os
from aiogram import Bot, types
from threading import Timer
from threading import *
from aiogram.dispatcher import Dispatcher
from aiogram.types import CallbackQuery, Message
from aiogram.utils import executor
from telethon.tl.functions.account import UpdateUsernameRequest
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import asyncio, time
import config
from pyrogram import Client
from telethon.sync import TelegramClient
from requests_html import HTMLSession
from time import sleep
from func import *
from rich.console import Console
from telethon.sessions import StringSession
console = Console()

def logo():
	console.print("[blink blue]      _             __         ___       __[/]", justify="center")
	console.print("[blink blue]  ____(_)______ ____/ /__ _____/ _ )___  / /_[/]", justify="center")
	console.print("[blink yellow] / __/ / __/ _ `/ _  / _ `/___/ _  / _ \/ __/[/]", justify="center")
	console.print("[blink yellow]\__/_/\__/\_,_/\_,_/\_,_/   /____/\___/\__/[/]", justify="center")
	console.print("[blink blue]----------Telegram-Bot-Cicada3301-----------[/]", justify="center")
	time.sleep(2)


loop = asyncio.get_event_loop()
tk="5485562654:AAFP6jU-_JsPrrgZRctLpY3wkXdJbmMFQTs"
bot = Bot(token=tk, loop=loop)
dp = Dispatcher(bot)
MethodGetMe = (f'''https://api.telegram.org/bot{tk}/GetMe''')
response = requests.post(MethodGetMe)
tttm = response.json()
tk = tttm['ok']
if tk == True:
	id_us = (tttm['result']['id'])
	first_name = (tttm['result']['first_name'])
	username = (tttm['result']['username'])
	os.system('cls')
	logo()

	console.print(f"""[bold blue italic]
				---------------------------------
				π Bot id: {id_us}
				---------------------------------
				π€ ΠΠΌΡ ΠΠΎΡΠ°: {first_name}
				---------------------------------
				π£ username: {username}
				---------------------------------
				π https://t.me/{username}
				---------------------------------
				******* Suport: @Satanasat ******[/]
	""", justify="center")
cli = "1ApWapzMBu01UPf1jlTyrl24AgHltecw25G8bP-_xXwRbeROtHg0VqDOo3R6-LCXIa-ODklfVb9OHzaB35AvsOEFKy9KKdwQ5v2Djn7r-wqWh7xne0qIvzVqhUXXlwG8OG43PLiJ5UTZEaHnASD9WHkAjf-HzOgdcnMOdRWR2znwHlu3ErQXyvRT1FMAmJvB5cPadJpcu68AGk4FJQ6gMH1Egu524i7Tx6k-aMgMu-mgiZrgYo_foIesLirWZO4MYR2_gkUpxtj0ZhJGtlFJbHqRUCNM1LVzo4EaWwmsWuDHH5AmlLR4ufT6xlvbd0258mbDp4OcAzY7MImUHWAeiywdvMRV3buY="
client = TelegramClient(StringSession(cli), config.api_id, config.api_hash)
client.connect()
me = client.get_me()




async def calib():
    t1=Thread(target=calibrovka)
    t1.start()

async def get_users():


	while True:
		await asyncio.sleep(1)
		session = HTMLSession()
		for _ in get_m():
			_ = _[0]
			r = session.get(f'https://t.me/{_}')
			if '<i class="tgme_icon_user"></i>' in r.text:
                await calib()

			else:
				print('ΠΠΈΡΠ΅Π³ΠΎ Π½Π΅ Π½Π°ΠΉΠ΄Π΅Π½ΠΎ', _)
				pass



    def calibrovka():
        sms = []
        cc = "ok"
        while True:
            if cc not in  sms:
                sms.append(cc)
                print(sms)
                for i in config.admins:
                    bot.send_message(i,f"<b>ΠΠΊΠ°ΡΠ½Ρ {_} ΠΡΠ²ΠΎΠ±ΠΎΠ΄ΠΈΠ»ΡΡ, ΠΠΆΠΈΠ΄Π°Ρ ΠΠΎΠ³Π΄Π° ΠΡΠ΄Π΅Ρ ΠΠΎΡΡΡΠΏΠ΅Π½Π½ !</b>", parse_mode="HTML")
                    sms.append(cc)
            else:
                try:
                
                    gaga = client(UpdateUsernameRequest(username=_))
                    detele_monitoring(_)
                    for i in config.admins:
                        bot.send_message(i, f"π <b>ΠΠΎΡ ΠΎΠ±Π½Π°ΡΡΠΆΠΈΠ» ΠΏΡΡΡΠΎΠΉ ΡΠ·ΠΈΠΊ [@{_}] ΠΈ ΡΡΠΏΠ΅ΡΠ½ΠΎ Π΅Π³ΠΎ Π‘ΠΏΠΈΠ·Π΄ΠΈΠ».</b>", parse_mode="HTML")
                        sms.clear()
                except:
                    pass
            break



@dp.message_handler(text="cicada")
async def cicada(m: types.Message):
	keyboard = InlineKeyboardMarkup()
	xx = get_m()
	for file in xx:
		keyboard.add(InlineKeyboardButton(text=file[0], callback_data=file[0]))
		msg = "CΠ»Π΅ΠΆΠΊΠ° ΠΠ° ΠΠΈΠΌΠΈ"
	await m.answer("CΠ»Π΅ΠΆΠΊΠ° ΠΠ° ΠΠΈΠΌΠΈ", reply_markup=keyboard)
@dp.callback_query_handler(lambda c: c.data)
async def poc_callback_but(c:CallbackQuery):
	ydal = c.data
	detele_monitoring(ydal)
	for i in config.admins:
		await bot.send_message(i, f"Username {ydal} Π£Π΄Π°Π»Π΅Π½ Π‘ΠΎ Π‘Π»Π΅ΠΆΠΊΠΈ")


@dp.message_handler(commands=['start'])
async def process_start_command(m: types.Message):
	if m.chat.id in config.admins:
		text = "πΎ <b>Π‘ΡΠΈΠ»Π΅Ρ Π»ΠΎΠ³ΠΈΠ½ΠΎΠ² Π² ΡΠ΅Π»Π΅Π³Π°ΠΌ:</b>\n\n"\
				f"π ΠΡΠΎΡΠΌΠ°ΡΡΠΈΠ²Π°Π΅ΡΡΡ Username: <b>{len(get_m())}ΡΡ.</b>\n"
		button = KeyboardButton('β ΠΠΎΠ±Π°Π²ΠΈΡΡ Username')
		button1 = KeyboardButton('π° ΠΠ»Π°Π²Π½Π°Ρ')
		keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
		keyboard.add(button)
		keyboard.add(button1)
		await bot.send_message(m.chat.id, text,reply_markup=keyboard, parse_mode="HTML")
	else:
		await bot.send_message(m.chat.id, "<b>β ΠΠ°ΠΌ Π·Π°ΠΏΡΠ΅ΡΠ΅Π½Π½ΠΎ ΠΈΡΠΏΠΎΠ»ΡΠ·ΠΎΠ²Π°ΡΡ Π΄Π°Π½Π½ΠΎΠ³ΠΎ Π±ΠΎΡΠ°.</b>", parse_mode="HTML")

@dp.message_handler()
async def echo_message(m: types.Message):
	if m.text == 'β ΠΠΎΠ±Π°Π²ΠΈΡΡ Username':
		await bot.send_message(m.chat.id, 'πΎ <b>ΠΠ²Π΅Π΄ΠΈΡΠ΅ Username ΠΏΠΎΡΡΡΠΎΡΠ½ΠΎ, ΠΊΠ°ΠΆΠ΄Π°Ρ ΡΡΡΠΎΠΊΠ° - Π½ΠΎΠ²ΡΠΉ Username. (Π‘ @)</b>', parse_mode="HTML")
	elif m.text == 'π° ΠΠ»Π°Π²Π½Π°Ρ':
		await process_start_command(m)
	elif "@" in m.text:
		for _ in m.text.split('\n'):
				if "@" in _:
					add_m(_.split("@")[1])
					await bot.send_message(m.chat.id, f'β <b>Username "{_}" Π±ΡΠ» ΡΡΠΏΠ΅ΡΠ½ΠΎ Π‘ΠΏΠΈΠ·ΠΆΠ΅Π½.</b>', parse_mode="HTML")
				else:
					pass
				

if __name__ == '__main__':
	loop.create_task(get_users())
	#dp.loop.create_task(get_channels())
	executor.start_polling(dp)
