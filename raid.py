import random
import time

from config import *
from rich.console import Console
from multiprocessing import Process
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

console = Console()

class Raid:
    def __init__(self, tokens):
        self.tokens = tokens
        self.bot = Bot(token = self.tokens)
        self.dp = Dispatcher(self.bot)
        self.message = messages
        self.ids = adm_id
        self.delay = delay

    def start(self):
        @self.dp.message_handler(commands = ['raid','start'])
        async def start_raid(msg: types.Message):
            if msg.from_user.id == self.ids:
                while True:
                    await msg.answer(random.choice(self.message))
                    time.sleep(self.delay)

        executor.start_polling(self.dp, skip_updates=True)


if __name__ == '__main__':
    if adm_id == 1:
        console.print('[red]Error[/]')
        exit()

    for tokens in token:
        bot = Raid(tokens)
        Process(target = bot.start).start()



