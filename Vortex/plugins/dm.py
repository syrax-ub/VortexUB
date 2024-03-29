#copy right by @VortexUb
from . import *

@Vortex.on(admin_cmd(pattern="dm ?(.*)"))
@Vortex.on(sudo_cmd(pattern="dm ?(.*)", allow_sudo=True))
async def dm(e):
    if len(e.text) > 3:
        if not e.text[3] == " ":  # weird fix
            return
    d = e.pattern_match.group(1)
    c = d.split(" ")
    try:
        chat_id = await get_user_id(c[0])
    except Exception as ex:
        return await eod(e, "`" + str(ex) + "`", time=5)
    msg = ""
    masg = await e.get_reply_message()
    if e.reply_to_msg_id:
        await ultroid_bot.send_message(chat_id, masg)
        await eod(e, "Message Delivered!", time=4)
    for i in c[1:]:
        msg += i + " "
    if msg == "":
        return
    try:
        await ultroid_bot.send_message(chat_id, msg)
        await eod(e, "Message Delivered!", time=4)
    except BaseException:
        await eod(
            e,
            "`{i}help dm`",
            time=4,
        )
