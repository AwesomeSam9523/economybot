import re
import json
import discord
import asyncio, time
from discord.ext import commands
import json
import datetime

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="e.", intents=intents)
devs = [771601176155783198, 713056818972066140]
embedcolor = 3407822
links_channel = 832083121486037013

bank_names = {
    1: 'Common Finance Bank Ltd.',
    2: 'National Bank Pvt. Ltd.',
    3: 'International Bank of Finance Ltd.'
}

rates = {
    1: 3,
    2: 5,
    3: 7
}

bank_tier = {
    1:'III',
    2:'II',
    3:'I'
}

e_wallet = '<:wallet:836814969290358845>'
e_bank = '🏦'

async def update_logs(stuff: str):
    with open('logs.txt', 'a') as logs:
        logs.write(f'\n{stuff}')

async def get_avg():
    with open('average.json', 'r') as avg:
        return json.loads(avg.read())

async def update_avg(avg):
    with open('average.json', 'w') as avgbal:
        avgbal.write(json.dumps(avg))

async def average_bal():
    while True:
        await avg_update()
        await asyncio.sleep(300)

async def avg_update():
    avgbal = await get_avg()
    data = await get_data()
    data_keys = data.keys()
    avg_keys = avgbal.keys()

    for key in data_keys:
        if key not in avg_keys:
            person = data[key]
            person_bal = person['bank']
            avgbal[key] = {'sum': 0, 'avg': 0, 'i': 1, 'claimed':0}

    for x in avgbal:
        person_data = data[x]
        person_avg = avgbal[x]

        newbal = person_data['bank']
        sum = person_avg['sum']

        newsum = sum + newbal
        person_avg['sum'] = newsum
        i = int(person_avg['i'])

        person_avg['avg'] = int(newsum / i)
        person_avg['i'] = i + 1
        avgbal[x] = person_avg

    with open('average.json', 'w') as avg:
        avg.write(str(json.dumps(avgbal)))

async def create_stuff():
    global bot_pfp
    mybot = bot.get_user(832083717417074689)
    bot_pfp = mybot.avatar_url

async def get_data():
    with open('accounts.json', 'r') as f:
        data = f.read()
        if data == '{}':
            return {1:1}
        else:
            return json.loads(data)

async def update_data(data):
    with open('accounts.json', 'w') as f:
        f.write(str(json.dumps(data)))

async def open_account(ctx):
    data = await get_data()
    if data.get(str(ctx.author.id)) is None:
        data[ctx.author.id] = {'bank_type':1, 'wallet':0, 'bank':1000}
        await update_data(data)

async def checktimeout(userid, event):
    with open('timeouts.json', 'r') as t:
        timeouts = json.loads(t.read())
    userid = f'{userid}'
    if userid not in timeouts:
        return None
    person = timeouts[userid]
    event_t = person.get(event)

    if event_t is None:
        return None

    current = time.time()
    difference = current - event_t
    return difference

async def add_timeout(userid, event):
    with open('timeouts.json', 'r') as f:
        data = json.loads(f.read())

    person = data.get(f'{userid}')
    if person is None:
        person = {}
    person[event] = time.time()

    data[userid] = person
    with open('timeouts.json', 'w') as f:
        f.write(json.dumps(data))

@bot.event
async def on_message(message):
    await bot.process_commands(message)

@bot.command()
async def logs(ctx):
    if ctx.author.id not in devs:
        return
    with open('logs.txt', 'r') as log:
        logs_data = log.readlines()
    await ctx.send(f'Logs:\n```{"".join(logs_data)}```')

@bot.command(aliases=['bal'])
async def balance(ctx):
    await open_account(ctx)
    data = await get_data()
    person = data.get(str(ctx.author.id))
    bank_type = person['bank_type']
    wallet = person['wallet']
    bank = person['bank']

    embed = discord.Embed(title=f'__{bank_names[bank_type]}__', colour=embedcolor,
                          description=f'**{e_wallet} Wallet:** {wallet}\n**{e_bank} Bank:** {bank}')

    fetched = bot.get_user(ctx.author.id)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text='Economy Bot', icon_url=bot_pfp)
    embed.set_author(name=fetched.name, icon_url=fetched.avatar_url)

    await ctx.send(embed=embed)

@bot.command()
async def add(ctx, person:discord.Member, bal:int, logsignore=None):
    if ctx.author.id not in devs:
        return
    data = await get_data()
    toadd = data.get(f'{person.id}')
    new_bal = toadd['wallet'] + bal
    toadd['wallet'] = new_bal
    data[f'{person.id}'] = toadd
    await update_data(data)
    if logsignore is None:
        await update_logs(f'{ctx.author} used "add" command [{person.id}, {bal}]')
        await ctx.send(f'{ctx.author.mention} added `{bal}` coins to {person.mention}.')
    else:
        await ctx.send(f'{ctx.author.mention} added `{bal}` coins to {person.mention}.\n**This actions isnt added in logs!**')

@bot.command(aliases=['dep'])
async def deposit(ctx, amount:str = None):
    if amount is None:
        await ctx.reply('`e.dep <amount>`, idiot.')
    data = await get_data()
    person = data.get(f'{ctx.author.id}')
    wallet = person['wallet']
    bank = person['bank']
    if amount == 'all':
        amount = wallet
    elif amount == 'half':
        amount = int(wallet/2)
    else:
        amount = int(amount)

    newbal_w = wallet - amount
    newbal_b = bank + amount

    person['wallet'] = newbal_w
    person['bank'] = newbal_b
    data[f'{ctx.author.id}'] = person

    await update_data(data)
    await ctx.send(f'{ctx.author.mention} Successfully deposited `{amount}` coins.')

@bot.command(aliases=['with'])
async def withdraw(ctx, amount: str = None):
    if amount is None:
        await ctx.reply('`e.with <amount>`, idiot.')
    data = await get_data()
    person = data.get(f'{ctx.author.id}')
    wallet = person['wallet']
    bank = person['bank']
    if amount == 'all':
        amount = bank
    elif amount == 'half':
        amount = int(bank / 2)
    else:
        amount = int(amount)

    newbal_w = wallet + amount
    newbal_b = bank - amount

    person['wallet'] = newbal_w
    person['bank'] = newbal_b
    data[f'{ctx.author.id}'] = person

    await update_data(data)
    await ctx.send(f'{ctx.author.mention} Successfully withdrew `{amount}` coins.')

@bot.command()
async def bank(ctx):
    await avg_update()
    data = await get_data()
    avgbal = await get_avg()
    person = data.get(f'{ctx.author.id}')
    person2 = avgbal.get(f'{ctx.author.id}')
    btype = person['bank_type']

    embed = discord.Embed(description='Here are your bank details:\n\u200b', color=embedcolor)
    embed.add_field(name='Bank Name', value=f'{bank_names[btype]}')
    embed.add_field(name='Bank Tier', value=f'{bank_tier[btype]}')
    embed.add_field(name='\u200b', value='\u200b')
    embed.add_field(name='Weekly Interest', value=f'{rates[btype]}%')
    embed.add_field(name='Current Balance', value=f'{person["bank"]}')
    embed.add_field(name='Average Balance', value=f'{person2["avg"]}')
    embed.add_field(name='Note:', value='To claim interest, use `e.daily`.\n'
                                        'Your average balance in last 24 hours will be taken in account for that.')

    fetched = bot.get_user(ctx.author.id)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text='Economy Bot', icon_url=bot_pfp)
    embed.set_author(name=f'{fetched.name} | {e_bank} Know Your Bank!', icon_url=fetched.avatar_url)

    await ctx.send(embed=embed)

@bot.command()
async def daily(ctx):
    await avg_update()

    avg = await get_avg()
    data = await get_data()

    avg_p = avg.get(f'{ctx.author.id}')
    data_p = data.get(f'{ctx.author.id}')
    claimed = avg_p['claimed']
    if avg_p is not None:
        i = avg_p['i']
    else:
        i = 0
    if data_p is None:
        return await ctx.send(f'{ctx.author.mention} Looks like you dont have a bank account. Use `e.bal` to open one.' )

    if claimed != 0:
        check = await checktimeout(ctx.author.id, 'weekly')
        if check is not None:
            if i < 288:
                left = datetime.timedelta(seconds=(86400 - check))
                final = datetime.datetime.strptime(str(left), '%H:%M:%S.%f').replace(microsecond=0)
                return await ctx.reply(f'You have to wait for `{str(final).split(" ")[1]}` (HH:MM:SS) time more before you can claim weekly interest.')
    elif i < 288:
        return await ctx.send(f'{ctx.author.mention} Looks like you dont own a bank account over 24 hours! Try Later.')

    btype = data_p['bank_type']
    avgbal = avg_p['avg']
    bank_d = data_p['bank']
    multiplier = (rates[btype])/100

    newbal = bank_d + int(avgbal * multiplier)
    data_p['bank'] = newbal
    data[f'{ctx.author.id}'] = data_p
    avg_p['claimed'] = 1
    avg_p['sum'] = int(avgbal)
    avg_p['i'] = 1

    print(avg_p)
    print(avg)

    avg[f'{ctx.author.id}'] = avg_p

    await update_avg(avg)
    await update_data(data)
    await add_timeout(ctx.author.id, 'weekly')

    await ctx.send(f'Weekly interest payout of `{int(avgbal * multiplier)}` coins credited successfully!')

@bot.command(aliases=['eval'])
async def evaluate(ctx, *, expression):
    if ctx.author.id not in devs:
        return
    try:
        result = eval(expression)
        await ctx.reply(result)
    except Exception as e:
        await ctx.reply(f'```\n{e}```')

@bot.command(aliases=['exec'])
async def execute(ctx, *, expression):
    if ctx.author.id not in devs:
        return
    try:
        eval(expression)
    except Exception as e:
        await ctx.reply(f'```\n{e}```')

@bot.event
async def on_ready():
    await create_stuff()
    chl = bot.get_channel(836849401904234521)
    asyncio.create_task(average_bal())
    embed = discord.Embed(description='<a:checkmark:836850860180373514> I am updated and ready to use!')
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text='Economy Bot', icon_url=bot_pfp)

    await chl.send(embed=embed)

print("Running...")

bot.run("ODMyMDgzNzE3NDE3MDc0Njg5.YHeoWQ._O5uoMS_I7abKdI_YzVb9BuEHzs")