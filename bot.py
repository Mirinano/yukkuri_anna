import discord
import datetime
import random

client = discord.Client()

master_server = ""
log_ch = ""

joined_content = """
時刻: {0}
参加メンバー名: {1}
メンション: <@{2}>
現在のメンバー数: {3}
"""
left_content = """
時刻: {0}
退出メンバー名: {1}
メンション: <@{2}>
現在のメンバー数: {3}
"""
count_content1 = """
えっと…、今のギルドのメンバーの数は…{}人、です…。
すごい、ね…♪
"""
count_content2 = """
今のギルドのメンバーの人数は、{}人だよ！
こんなにもたくさんの仲間ができて、杏奈とっても嬉しいな！
"""
count_content = (count_content1, count_content2)

@client.event
async def on_ready():
    print("Complete!")

@client.event
async def on_member_join(member):
    if member.server.id == master_server:
        now_time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        count_member = member.server.member_count
        send_content = joined_content.format(now_time, member.name, member.id, count_member)
        await client.send_message(client.get_channel(log_ch), send_content)

@client.event
async def on_member_remove(member):
    if member.server.id == master_server:
        now_time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        count_member = member.server.member_count
        send_content = left_content.format(now_time, member.name, member.id, count_member)
        await client.send_message(client.get_channel(log_ch), send_content)

@client.event
async def on_message(message):
    if message.author != client.user:
        if (("杏奈" in message.content) and ("メンバー数" in message.content) and ("教えて" in message.content)):
            count_member = message.server.member_count
            send_content = random.choice(count_content)
            await client.send_message(message.channel, send_content.format(count_member))

client.run("Token")
