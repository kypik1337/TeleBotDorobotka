from botconfig import dp, bot
from aiogram.types import Message
from random import randint
from aiogram.dispatcher.filters import Text
from keyBoards.client import button_client, button_client2
import text
import game
import wikipedia, re


@dp.message_handler(commands='start')
async def startBot(message: Message):
    await bot.send_animation(message.chat.id,r'https://t.me/gifcollection/10774')
    await message.answer(text=f'{message.from_user.first_name}'
                              f'{text.one_greetings}',reply_markup = button_client2)
       
@dp.message_handler(commands='game')
async def start_new_game(message: Message):
    await bot.send_animation(message.chat.id,r'https://t.me/gifcollection/10848')
    game.new_game()
    if game.check_game():
        toss = randint(0, 1)
        if toss:
            await player_turn(message)
        else:
            await bot_turn(message)



@dp.message_handler(commands='set_total')
async def set_max_total(message: Message):
    if not game.check_game ():
        max_total = message.text.split()
        if len(max_total) > 1 and max_total [1].isdigit():
            game.set_max_total(int(max_total[1]))
            await bot.send_animation(message.chat.id,r'https://t.me/gifcollection/10838')
            await message.reply(text=f'максимальное значение candis измененено на {max_total[1]} нажимай кнопочку /game',reply_markup = button_client2)
        else:
            await message.reply(text='Этой командой можем настроить максимальное количество candis введите /set_total')
    else:
        await bot.send_animation(message.chat.id,r'https://t.me/gifcollection/10830')
        await message.reply(text='Данную настройку можно изменить только в после завершения игры')



async def player_turn(message: Message):
    await message.answer(f'{message.from_user.first_name},{text.hod_player}')

@dp.message_handler()
async def take(message: Message):
    name = message.from_user.first_name
    if game.check_game():
        if message.text.isdigit():
            take = int(message.text)
            if (0 < take < 29) and take <= game.get_total():
                game.take_candis(take)
                if await check_win(message, take, 'player'):
                    return 
                await message.answer(f'{name} взял {take} {text.stor}'
                f'{game.get_total()}. Ходит бот...')
                await bot_turn(message)
            else:
                await bot.send_animation(message.chat.id,r'https://t.me/gifcollection/10846')
                await message.answer(text.max_candis)
        else:
            pass

async def bot_turn(message):
    total = game.get_total()
    if total <= 28:
        take = total
    else:
        take = randint(1, 28)
    game.take_candis(take)
    await message.answer(f'Бот взял {take} {text.stor} {game.get_total()}')
    if await check_win(message, take, 'Бот'):
        return
    await player_turn(message)

async def check_win(message, take: int, player: str):
    if game.get_total() <=0:
        if player == 'player':
            await bot.send_animation(message.chat.id,r'https://t.me/gifcollection/10796')
            await message.answer(f'{message.from_user.first_name} взял {take} и одержал победу над Ботом')
        else:
            await message.answer(f'{message.from_user.first_name}'
            f'Бот взял {take} конфет и одержал победу Бро,'
            f' {text.traning}')
        game.new_game()
        return True
    else:
        return False

        