  from pyrogram import Client, filters


API_ID = "27936813"
API_HASH = "1a2c6cd63ebf1360b316a1179ae5d561"
BOT_TOKEN = "MIIBCgKCAQEAyMEdY1aR+sCR3ZSJrtztKTKqigvO/vBfqACJLZtS7QMgCGXJ6XIR"

TechMagazine = Client(
    name="samplebot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


@TechMagazine.on_message(filter.command("start"))
async def start_cmd(client, message):
    print("START Command")


@TechMagazine.on_message(filter.command("help"))
async def help_cmd(client, message):
    print("HELP Command")

print("Bot was started")

TechMagazine.run()
