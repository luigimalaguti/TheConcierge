from telethon import events


@events.register(events.NewMessage(pattern="[Hh]i|[Hh]ello"))
async def welcome(event):
    await event.reply("Welcome!")
    raise events.StopPropagation

@events.register(events.NewMessage)
async def echo(event):
    bot = event.client
    await bot.send_message(event.chat.id, event.text)
