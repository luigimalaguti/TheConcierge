from sympy import sympify

from telethon import events


@events.register(events.NewMessage(pattern="[^a-zA-Z]"))
async def resolver(event):
    result = str(float(sympify(event.text)))
    await event.respond(result)
    raise events.StopPropagation
