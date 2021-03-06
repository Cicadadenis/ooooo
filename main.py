import sqlite3
import requests, os
from aiogram import Bot, types
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
from telethon.tl.functions.users import GetFullUserRequest

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


async def get_users():
	while True:
		await asyncio.sleep(1)
		session = HTMLSession()
		for x in get_m():
			x = x[0]
			r = session.get(f'https://t.me/{x}')
			if '<i class="tgme_icon_user"></i>' in r.text:
				for s in os.listdir("sessions"):
					print(s)
					with open(f"sessions/{s}", "r") as f:
						ses = f.read()
					
						client = TelegramClient(StringSession(ses), config.api_id, config.api_hash)
						await client.connect()
						p = await client.get_me()
						print(p.username)
					try:
						sleep(60*10)
						dd = await client(UpdateUsernameRequest(username=f"{x}"))
						await detele_monitoring(x)
						for i in config.admins:
							await bot.send_message(i, f"<b>Username {ydal} ΠΠΎΠ»ΡΡΠ΅Π½</b>", parse_mode="HTML")
						break
					except:
						pass
			else:
				print('ΠΠΈΡΠ΅Π³ΠΎ Π½Π΅ Π½Π°ΠΉΠ΄Π΅Π½ΠΎ', x)
				pass

@dp.message_handler(text="cicada")
async def cicada(m: types.Message):
	keyboard = InlineKeyboardMarkup()
	xx = get_m()
	for file in xx:
		keyboard.add(InlineKeyboardButton(text=file[0], callback_data=file[0]))
	await m.answer("<b>CΠ»Π΅ΠΆΠΊΠ° ΠΠ° ΠΠΈΠΌΠΈ</b>", parse_mode="HTML",  reply_markup=keyboard)
@dp.callback_query_handler(lambda c: c.data)
async def poc_callback_but(c:CallbackQuery):
	ydal = c.data
	detele_monitoring(ydal)
	for i in config.admins:
		await bot.send_message(i, f"<b>Username {ydal} Π£Π΄Π°Π»Π΅Π½ Π‘ΠΎ Π‘Π»Π΅ΠΆΠΊΠΈ</b>", parse_mode="HTML")


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
					await bot.send_message(m.chat.id, f'β <b>Username "{_}" Π±ΡΠ» ΡΡΠΏΠ΅ΡΠ½ΠΎ ΠΠΎΠ±Π°Π²Π»Π΅Π½ ΠΠ»Ρ Π‘Π»Π΅ΠΆΠΊΠΈ.</b>', parse_mode="HTML")
				else:
					pass
				

if __name__ == '__main__':
	loop.create_task(get_users())
	#dp.loop.create_task(get_channels())
	executor.start_polling(dp)
