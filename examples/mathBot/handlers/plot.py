import sympy
import sys
import os

from telethon import events


@events.register(events.NewMessage(pattern="(?:[0-9-+*/^()x]|abs|e\^x|ln|log|a?(?:sin|cos|tan)h?)+"))
async def plotting(event):
    bot = event.client
    path = os.path.abspath(sys.argv[0]).replace(os.path.basename(sys.argv[0]), "")
    path += "files/plot.png"
    plot = sympy.plotting.plot(event.text, show=False)
    plot.save(path)
    await bot.send_file(event.chat.id, path)
