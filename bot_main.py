import discord
import os

client = discord.Client()


@client.event
async def on_ready():

    print(client.user.name)
    print("start")
    game = discord.Game('$도움말 또는 $help')
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content == "$help":
        await message.channel.send("Team Studio's first public work is still being made, so please look forward to it!  마딩 MineCoding#1778")
    if message.content == "$도움말":
        await message.channel.send("팀 스튜디오의 첫 공개작품 아직은 만들어 지는중이니 기대해 주세요!  마딩 MineCoding#1778")

    if message.content == "$명령어":
        await message.channel.sand("아직은 추가중 입니다!")

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
