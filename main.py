import re
import json
import discord
import asyncio, time
from discord.ext import commands
import json
import datetime
import inspect
from prettytable import PrettyTable

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

getestates_thumb = {
    1:'https://media.discordapp.net/attachments/837564505952747520/837681898700537866/1.png',
    2:'https://media.discordapp.net/attachments/837564505952747520/837682702450032660/2.png',
    3:'https://media.discordapp.net/attachments/837564505952747520/837697702326042674/3.png',
    4:'https://cdn.discordapp.com/attachments/837564505952747520/837565525143453716/unknown.png',
    5:'https://cdn.discordapp.com/attachments/837564505952747520/837566247439695882/unknown.png',
    6:'https://cdn.discordapp.com/attachments/837564505952747520/837566247439695882/unknown.png',
    7:'https://cdn.discordapp.com/attachments/837564505952747520/837566473920577556/unknown.png',
    8:'https://cdn.discordapp.com/attachments/837564505952747520/837567047754973234/unknown.png',
    9:'https://cdn.discordapp.com/attachments/837564505952747520/837567047754973234/unknown.png',
    10:'https://cdn.discordapp.com/attachments/837564505952747520/837567877103484938/unknown.png',
    11:'https://cdn.discordapp.com/attachments/837564505952747520/837567877103484938/unknown.png',
    12:'https://cdn.discordapp.com/attachments/837564505952747520/837568882892996628/unknown.png',
    13:'https://cdn.discordapp.com/attachments/837564505952747520/837568882892996628/unknown.png',
    14:'https://cdn.discordapp.com/attachments/837564505952747520/837569387220434974/unknown.png',
    15:'https://cdn.discordapp.com/attachments/837564505952747520/837570918993100820/unknown.png',
    16:'https://cdn.discordapp.com/attachments/837564505952747520/837570918993100820/unknown.png',
    17:'https://cdn.discordapp.com/attachments/837564505952747520/837572907713691688/unknown.png',
    18:'https://cdn.discordapp.com/attachments/837564505952747520/837574437389729802/unknown.png',
    19:'https://cdn.discordapp.com/attachments/837564505952747520/837576416039403530/unknown.png',
    20:'https://cdn.discordapp.com/attachments/837564505952747520/837577291898945546/unknown.png',
    21:'https://cdn.discordapp.com/attachments/837564505952747520/837577291898945546/unknown.png',
    22:'https://cdn.discordapp.com/attachments/837564505952747520/837577637349687306/unknown.png',
    23:'https://cdn.discordapp.com/attachments/837564505952747520/837578058500276244/unknown.png',
    24:'https://cdn.discordapp.com/attachments/837564505952747520/837578847456722995/unknown.png',
    25:'https://cdn.discordapp.com/attachments/837564505952747520/837579030374776832/unknown.png',
    26:'https://cdn.discordapp.com/attachments/837564505952747520/837579385330466827/unknown.png',
    27:'https://cdn.discordapp.com/attachments/837564505952747520/837579988949008404/unknown.png',
    28:'https://cdn.discordapp.com/attachments/837564505952747520/837580290977300530/unknown.png',
    29:'https://cdn.discordapp.com/attachments/837564505952747520/837580694505914398/unknown.png',
    30:'https://cdn.discordapp.com/attachments/837564505952747520/837581436407644190/unknown.png'
}

estates_tasks = {
    1:'Add a room',
    2:'Improve Restaurant',
    3:'Add a room',
    4:'Build a store',
    5:'Add more items in store',
    6:'Add a room',
    7:'Add a Helper Desk',
    8:'Improve Helper Desk',
    9:'Add a Presidential Suite',
    10:'Upgrade Rooms and Suite',
    11:'Add Laundary Service',
    12:'Expand Laundary',
    13:'Add Elevator',
    14:'Improve Rooms',
    15:'Improve Meals Variety and Quality',
    16:'Expand Kitchen',
    17:'Add two Master Chef',
    18:'Build second floor and add Cafè',
    19:'Build a Gym',
    20:'Improve Service Speed and Cleanliness',
    21:'Build a Casino',
    22:'Build a Swimming Pool',
    23:'Build a Night Bar',
    24:'Add Valet Parking',
    25:'Add a Movie Theatre',
    26:'Add a Voilenist to entertain Guests',
    27:'Add a Pianoist to Welcome VIPs',
    28:'Add a Pet Store',
    29:'Add Decorations like Paintings and Plants',
}

e_wallet = '<:wallet:836814969290358845>'
e_bank = '🏦'

async def update_logs(stuff: str):
    with open('logs.txt', 'a') as logs:
        logs.write(f'\n{stuff}')

async def get_avg():
    with open('average.json', 'r') as avg:
        return json.loads(avg.read())

async def get_estates():
    with open('estates.json', 'r') as f:
        return json.loads(f.read())

async def update_avg(avg):
    with open('average.json', 'w') as avgbal:
        avgbal.write(json.dumps(avg))

async def update_est(data):
    with open('estates.json', 'w') as f:
        f.write(json.dumps(data))

async def update_alerts(data):
    with open('alerts.json', 'w') as f:
        f.write(json.dumps(data))

async def get_alert_info():
    with open('alerts.json', 'r') as a:
        aler = json.loads(a.read())
    return aler

async def est_update():
    est = await get_estates()
    keys = [x for x in est.keys()]

    for i in keys:
        person = est[i]
        lm = person['lm']
        pending = person['p']

        cur = time.time()
        diff = cur - lm

        if diff >= 172800:
            aler = await get_alert_info()
            persona = aler[i]

            state, last = persona['state'], persona['last']
            dm_diff = cur - last

            person['p'] = diff - 172800
            est[str(i)] = person
            await update_est(est)

            if state == 'on' and dm_diff > 21600:
                embed = discord.Embed(title='Maintainance Reminder',
                                      description='Your Hotel Maintainance is due. Use `e.maintain` to pay for it.\n'
                                                  'Note: You will get less revenue if maintainance isn\'t done!',
                                      colour=embedcolor)
                fetched = bot.get_user(int(i))
                embed.timestamp = datetime.datetime.utcnow()
                embed.set_author(name=f'{fetched.name}', icon_url=fetched.avatar_url)
                embed.set_footer(text='Economy Bot', icon_url=bot_pfp)

                persona['last'] = cur
                aler[str(i)] = persona
                await update_alerts(aler)

                await fetched.send(embed=embed)

async def loops():
    while True:
        await avg_update()
        await est_update()
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
    asyncio.create_task(loops())
    print('Ready!')

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

async def open_estates(ctx):
    data = await get_estates()
    if data.get(str(ctx.author.id)) is None:
        data[f'{ctx.author.id}'] = {'level':1, 'name':f'{ctx.author.name}', 'lm':time.time(), 'lr':time.time(), 'p':0, 'c':0}

    await update_est(data)

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

async def get_revenue(level:int):
    return int((level*200 - 50)*0.97)

async def get_maint(level:int):
    return int((level*200 - 50)*0.9)

async def get_cost(level:int):
    return int((300*level)**(1.75))

async def alerts_state(userid, state:str):
    with open('alerts.json', 'r') as a:
        aler = json.loads(a.read())
    userid = str(userid)
    person = aler.get(userid)
    if person is None:
        person = {'state':0, 'last':0}

    person['state'] = state
    aler[userid] = person

    with open('alerts.json', 'w') as aa:
        aa.write(json.dumps(aler))

async def commait(val):
    val = str(val)
    val = [x for x in val]
    val.reverse()

    count = 0
    string = ''
    for i in val:
        if count == 3:
            string += ','
            count = 0
        string += i
        count += 1

    return string[::-1]

@bot.event
async def on_message(message):
    await bot.process_commands(message)

@bot.command() #DEV ONLY
async def logs(ctx):
    if ctx.author.id not in devs:
        return
    with open('logs.txt', 'r') as log:
        logs_data = log.readlines()
    await ctx.send(f'Logs:\n```{"".join(logs_data)}```') #

@bot.command(aliases=['eval'])  # DEV ONLY
async def evaluate(ctx, *, expression):
    if ctx.author.id not in devs:
        return
    try:
        if inspect.isawaitable(expression):
            await ctx.reply(await eval(expression))
        else:
            await ctx.reply(eval(expression))
    except Exception as e:
        await ctx.reply(f'```\n{e}```')

@bot.command(aliases=['exec']) #DEV ONLY
async def execute(ctx, *, expression):
    if ctx.author.id not in devs:
        return
    try:
        await eval(expression)
    except Exception as e:
        await ctx.reply(f'```\n{e}```')

@bot.command() #DEV ONLY
async def add(ctx, person:discord.Member, bal:int, *args):
    if ctx.author.id not in devs:
        return
    if '-i' in args:
        logsignore = 1
    else:
        logsignore = None

    data = await get_data()
    toadd = data.get(f'{person.id}')

    if '-b' in args:
        new_bal = toadd['bank'] + bal
        toadd['bank'] = new_bal
    else:
        new_bal = toadd['wallet'] + bal
        toadd['wallet'] = new_bal
    data[f'{person.id}'] = toadd
    await update_data(data)

    if logsignore is None:
        await update_logs(f'{ctx.author} used "add" command [{person.id}, {await commait(bal)}]')
        await ctx.send(f'{ctx.author.mention} added `{await commait(bal)}` coins to {person.mention}.')
    else:
        await ctx.send(f'{ctx.author.mention} added `{await commait(bal)}` coins to {person.mention}.\n**This actions isnt added in logs!**')

@bot.command(aliases=['bal'])
async def balance(ctx, member:discord.Member = None):
    await open_account(ctx)
    data = await get_data()
    if member is None:
        userid = ctx.author.id
    else:
        userid = member.id
    person = data.get(str(userid))
    bank_type = person['bank_type']
    wallet = person['wallet']
    bank = person['bank']

    embed = discord.Embed(title=f'__{bank_names[bank_type]}__', colour=embedcolor,
                          description=f'**{e_wallet} Wallet:** {await commait(wallet)}\n**{e_bank} Bank:** {await commait(bank)}')

    fetched = bot.get_user(userid)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text='Economy Bot', icon_url=bot_pfp)
    embed.set_author(name=fetched.name, icon_url=fetched.avatar_url)

    await ctx.send(embed=embed)

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
    await ctx.send(f'{ctx.author.mention} Successfully deposited `{await commait(amount)}` coins.')

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
    await ctx.send(f'{ctx.author.mention} Successfully withdrew `{await commait(amount)}` coins.')

@bot.command()
async def bank(ctx, member:discord.Member = None):
    await avg_update()
    data = await get_data()
    avgbal = await get_avg()
    if member is None:
        userid = ctx.author.id
    else:
        userid = member.id
    person = data.get(f'{userid}')
    person2 = avgbal.get(f'{userid}')
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

    fetched = bot.get_user(userid)
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
                return await ctx.reply(f'You have to wait for `{str(final).split(" ")[1]}` (HH:MM:SS) time more before you can claim daily interest.')
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

    await ctx.send(f'Daily interest payout of `{await commait(int(avgbal * multiplier))}` coins credited successfully!')

@bot.command()
async def give(ctx, member:discord.Member, amount:int):
    if amount == 0:
        return await ctx.send(f'{ctx.author.mention} Sending 0 coins... Hmm nice idea but we dont do that here.')
    if amount < 0:
        return await ctx.send(f'{ctx.author.mention} Dont try to be oversmart kiddo.')
    if member == ctx.author:
        return await ctx.send(f'{ctx.author.mention} Did you just try to send **yourself** some coins?')
    amount = int(amount)

    data = await get_data()
    author = data.get(f'{ctx.author.id}')
    person = data.get(f'{member.id}')

    a_wallet = author['wallet']
    a_bank = author['bank']

    if amount > a_wallet:
        return await ctx.send(f'{ctx.author.mention} You dont have enough coins. Go beg or withdraw.')

    author['wallet'] = new_a_wallet
    author['bank'] = new_a_bank
    data[f'{ctx.author.id}'] = author

    p_wallet = person['wallet']
    person['wallet'] = p_wallet + amount
    data[f'{member.id}'] = person

    await update_data(data)

    embed = discord.Embed(title='Act of Generosity', color=embedcolor,
                          description=f'{ctx.author.mention} gave `{await commait(amount)}` coins to {member.mention}')
    fetched = bot.get_user(ctx.author.id)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text='Economy Bot', icon_url=bot_pfp)
    embed.set_author(name=fetched.name, icon_url=fetched.avatar_url)

    await ctx.send(embed=embed)

@bot.command(aliases=['property'])
async def estates(ctx):
    await open_estates(ctx)
    est = await get_estates()
    person = est[f'{ctx.author.id}']
    level = person['level']
    name = person['name']
    revenue = await get_revenue(level)
    maint = await get_maint(level)

    embed = discord.Embed(description='\u200b', colour=embedcolor)
    embed.add_field(name='Current Level', value=f'{level}')
    embed.add_field(name='Revenue Earned', value=f'`{revenue}` coins')
    embed.add_field(name='Maintainance Cost', value=f'`{maint}` coins')
    embed.add_field(name='Next Task', value=f'```css\n[{estates_tasks[level]}]\nUse e.upgrade to Upgrade!\n```', inline=False)
    embed.add_field(inline=False, name='Note:', value='```diff\nThe revenue is earned in per hour\n+ Use e.revenue to claim revenue\n- Use e.maintain to do maintainance\n```')

    fetched = bot.get_user(ctx.author.id)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text='Economy Bot', icon_url=bot_pfp)
    embed.set_author(name=f'{fetched.name} | {name} Hotel', icon_url=fetched.avatar_url)
    embed.set_image(url=getestates_thumb[level])

    await ctx.send(embed=embed)

@bot.command()
async def revenue(ctx):
    await open_estates(ctx)
    await est_update()
    est = await get_estates()
    person = est[f'{ctx.author.id}']

    level = person['level']
    name = person['name']
    last_m = person['lm']
    last_r = person['lr']
    pending = person['p']
    alr_claimed = person['c']
    current = time.time()

    m_diff = current - last_m
    r_diff = current - last_r

    revenue_rate = await get_revenue(level)
    if alr_claimed == 1 and m_diff >= 172800:
        fixed_rev = 0
        low_rev = int((r_diff/3600)*revenue_rate*0.4)
    else:
        fixed_rev = int((r_diff / 3600) * revenue_rate)
        low_rev = int((pending/3600)*revenue_rate*0.4)
    if pending > 172800:
        fine = -5000
    else:
        fine = 0
    totalpay = int(fixed_rev+low_rev+fine)

    x = PrettyTable()
    x.field_names = ["    Name", "       ", "      ", "Amount  "]
    x.align["    Name"] = "l"
    x.align["Amount  "] = "r"
    x.add_row(["Fixed Revenue", "", "", f'{await commait((fixed_rev))}.00/-'])
    x.add_row(["Late Revenue", "", "", f'{await commait(low_rev)}.00/-'])
    x.add_row(["Late Fine", "", "", f'{await commait(fine)}.00/-'])
    x.add_row(["", "", "", f''])
    x.add_row(["[Grand Total]", "", "", f'{await commait(totalpay)}.00/-'])

    embed = discord.Embed(title='Hotel Revenue',
                          description=f'`{totalpay}.00` coins added to bank successfully!\n\nHere is the revenue split:\n```css\n{x}```',
                          colour=embedcolor)
    fetched = bot.get_user(ctx.author.id)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text='Economy Bot', icon_url=bot_pfp)
    embed.set_author(name=f'{fetched.name} | {name} Hotel', icon_url=fetched.avatar_url)

    data = await get_data()
    persona = data[f'{ctx.author.id}']
    bank_ = persona['bank']
    persona['bank'] = bank_ + totalpay
    data[f'{ctx.author.id}'] = persona
    person['lr'] = time.time()
    person['pending'] = 0
    person['c'] = 1
    est[f'{ctx.author.id}'] = person

    await update_est(est)
    await update_data(data)
    await ctx.send(embed=embed)

@bot.command()
async def maintain(ctx):
    data = await get_data()
    est = await get_estates()
    userid = str(ctx.author.id)

    persona = data[userid]
    person = est[userid]

    bank_bal = persona['bank']
    wal_bal = persona['wallet']

    lm = person['lm']
    level = person['level']
    name = person['name']
    cur = time.time()

    maint = await get_maint(level)
    cost = int(((cur-lm) / 3600)*maint)
    cost_d = int(cost*0.1)+int(cost*0.4)+int(cost*0.3)+int(cost*0.2)

    x = PrettyTable()
    x.field_names = ["    Name", "       ", "      ", "Amount  "]
    x.align["    Name"] = "l"
    x.align["Amount  "] = "r"
    x.add_row(["Cleaning", "", "", f'{await commait(int(cost*0.1))}.00/-'])
    x.add_row(["Staff Salary", "", "", f'{await commait(int(cost*0.4))}.00/-'])
    x.add_row(["Meals", "", "", f'{await commait(int(cost*0.3))}.00/-'])
    x.add_row(["Repair Work", "", "", f'{await commait(int(cost*0.2))}.00/-'])
    x.add_row(["", "", "", f''])
    x.add_row(["[Grand Total]", "", "", f'{await commait(cost_d)}.00/-'])

    if bank_bal+wal_bal < cost_d:
        embed = discord.Embed(title='Oops..',
                              description=f'You dont have enough coins to find the maintainance.\n```css\n{x}```', color=embedcolor)
    else:
        if bank_bal < cost_d:
            new_bbal = 0
            new_wbal = wal_bal - cost_d + bank_bal
        else:
            new_bbal = bank_bal - cost_d
            new_wbal = wal_bal

        persona['bank'] = new_bbal
        persona['wallet'] = new_wbal
        data[userid] = persona

        person['lm'] = cur
        person['p'] = 0
        est[userid] = person

        await update_data(data)
        await update_est(est)

        embed = discord.Embed(title='Success!',
                              description=f'`{cost_d}.00` coins have been deducted and your hotel looks shining new!\n```css\n{x}```',
                              color=embedcolor)

    fetched = bot.get_user(ctx.author.id)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text='Economy Bot', icon_url=bot_pfp)
    embed.set_author(name=f'{fetched.name} | {name} Hotel', icon_url=fetched.avatar_url)

    await ctx.send(embed=embed)

@bot.command()
async def upgrade(ctx):
    await open_estates(ctx)
    est = await get_estates()
    eperson = est[f'{ctx.author.id}']
    level = eperson['level']
    name = eperson['name']
    rev_now = await get_revenue(level)
    rev_after = await get_revenue(level+1)
    main_now = await get_maint(level)
    main_after = await get_maint(level+1)

    cost = await get_cost(level)

    embed = discord.Embed(title='Upgrade Hotel', colour=embedcolor)
    embed.add_field(name='Level Change', value=f'`{level} => {level+1}`')
    embed.add_field(name='Revenue Boost', value=f'`{await commait(rev_now)} + {await commait(rev_after-rev_now)}` coins')
    embed.add_field(name='Maintainance Increase', value=f'`{await commait(main_now)} + {await commait(main_after-main_now)}` coins')
    embed.add_field(name='Upgrade Cost', value=f'`{await commait(cost)}` coins')
    embed.add_field(name='Confirm?', value='Click ✅ to confirm or ❌ to cancel', inline=False)
    embed.add_field(name='\u200b', value='Here is the look after upgrade:', inline=False)
    embed.set_image(url=getestates_thumb[level+1])
    fetched = bot.get_user(ctx.author.id)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text='Economy Bot', icon_url=bot_pfp)
    embed.set_author(name=f'{fetched.name} | {name} Hotel', icon_url=fetched.avatar_url)

    msg = await ctx.send(embed=embed)
    await msg.add_reaction('✅')
    await msg.add_reaction('❌')

    def check(reaction, user):
        if user == ctx.author and str(reaction.emoji) in ['✅', '❌']:
            return True
    try:
        reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)
        await msg.clear_reaction('✅')
        await msg.clear_reaction('❌')
        if str(reaction) == '✅':
            data = await get_data()
            person = data[f'{ctx.author.id}']
            wallet = person['wallet']
            bank = person['bank']

            if cost > wallet:
                left = cost-wallet
                new_wallet = 0
                if left > bank:
                    return await ctx.send(f'{ctx.author.mention} Oopsie! Looks like there aren\'t enough coins in your pockets.')
                new_bank = bank - left
            else:
                new_wallet = wallet - cost
                new_bank = bank

            person['wallet'] = new_wallet
            person['bank'] = new_bank
            eperson['level'] = level + 1

            est[f'{ctx.author.id}'] = eperson
            data[f'{ctx.author.id}'] = person

            await update_data(data)
            await update_est(est)
            await ctx.send(f'{ctx.author.mention} Wohoo! Your upgrade was successful! Use `e.estates` to see newly upgraded property!')
        else:
            await ctx.send(f'{ctx.author.mention} Cancelled!')
    except asyncio.TimeoutError:
        pass

@bot.command()
async def alerts(ctx, state:str = None):
    if state is None:
        embed = discord.Embed(title='Alerts System',
                              description='Get Alerts on pending loans, hotel maintainance, robberies etc straight to your DMs\n'
                                          '```diff\n+ To turn on: e.alerts on\n- To turn off: e.alerts off\n```',
                              color=embedcolor)
        with open('alerts.json', 'r') as a:
            aler = json.loads(a.read())
        if f'{ctx.author.id}' in aler:
            current = 'On'
        else:
            current = 'Off'

        embed.add_field(name='Current State', value=current)
        fetched = bot.get_user(ctx.author.id)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_author(name=f'{fetched.name}', icon_url=fetched.avatar_url)
        embed.set_footer(text='Economy Bot', icon_url=bot_pfp)
        return await ctx.send(embed=embed)

    if state == 'on':
        await ctx.send(f'{ctx.author.mention} Alerts are switched **On**. Make sure you have your DMs open :)')
        await alerts_state(ctx.author.id, 'on')
    elif state == 'off':
        await ctx.send(f'{ctx.author.mention} Alerts are switched **Off**. "Yay no more bot DMs", huh?')
        await alerts_state(ctx.author.id, 'off')
    else:
        await ctx.send(f'{ctx.author.mention} Incorrect Option. Use `e.alerts` to see help.')

@bot.event
async def on_ready():
    await create_stuff()

print("Running...")
bot.run("ODMyMDgzNzE3NDE3MDc0Njg5.YHeoWQ._O5uoMS_I7abKdI_YzVb9BuEHzs")