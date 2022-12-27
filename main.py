from aiogram.utils import executor
from commands import dp

async def started(_):
    print('Bot online')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=started)

