

from telethon import TelegramClient, events
from telethon.sync import TelegramClient

APP_ID = 12345
APP_HASH = "1234:sdfgh"
BOT_TOKEN = "12314:fsdfsdfghj"
MSG = "edited message"

try:
    bot = TelegramClient('editcaption', APP_ID,
                         APP_HASH).start(bot_token=BOT_TOKEN)
finally:
    print("Bot çalışıyor.")


@bot.on(events.NewMessage(func=lambda e: e.photo or e.media))
async def photo(event):
    if event.message.message == '':
        return
    mesaj_id = event.message.id
    await event.client.edit_message(event.chat_id, mesaj_id, MSG)


bot.start()
bot.run_until_disconnected()
