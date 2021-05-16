import os
import random
#import ujson as json
import json
import requests, operator
import discord
import asyncio, time
from discord.ext import commands
import datetime
import csv
from prettytable import PrettyTable
import matplotlib.pyplot as plt
from PIL import Image, ImageTk, ImageDraw, ImageFont
from io import BytesIO

intents = discord.Intents.default()
intents.members = True
intents.presences = True
bot = commands.Bot(command_prefix=["e.", "E."], intents=intents, case_insensitive=True)
bot.dev = 1
bot.remove_command('help')
devs = [771601176155783198, 713056818972066140, 619377929951903754, 669816890163724288]
disregarded = []
embedcolor = 3407822
links_channel = 832083121486037013

support_server = 'https://discord.gg/aMqWWTunrJ'
patreon_page = 'https://www.patreon.com/ThunderGameBot'
invite_url = 'https://i0.wp.com/incipia.co/wp-content/uploads/2016/08/incipia-coming-soon.png'
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
    30:'Maxed Out'
}
xp_levels = {
100:1,
250:2,
500:3,
800:4,
1200:5,
1700:6,
2200:7,
3000:8,
3800:9,
4700:10,
5800:11,
8000:12,
9300:13,
10500:14,
12000:15,
13700:16,
16300:17,
18000:18,
19800:19,
22000:20,
24500:21,
26700:22,
29000:23,
31500:24,
34000:25,
37200:26,
40500:27,
43800:28,
46800:29,
50000:30,
54500:31,
60000:32,
66000:33,
73000:34,
83000:35,
95000:36,
110000:37,
130000:38,
165000:39,
200000:40,
230000:41,
270000:42,
325000:43,
395000:44,
470000:45,
560000:46,
650000:47,
740000:48,
850000:49,
1000000:50
}
help_json = {
    "Estates":{
        "category":"Estates",
      "e.estates": {"aliases":["None"], "usage":"e.estates", "desc":"Estates are a way to earn some coins for free. You have being provided with a hotel which will earn you revenue.\nDont forget, money never comes entirely for free, so you have to maintain your hotel too."},
      "e.revenue": {"aliases":["None"], "usage":"e.revenue", "desc": "Use this command to earn revenue. The revenue will be added in your bank"},
      "e.maintain": {"aliases": ["None"], "usage": "e.maintain", "desc": "Use this to maintain your hotel to look shining new! Not maintaining for a long time will lead to lesser revenue."},
      "e.upgrade": {"aliases": ["None"], "usage": "e.upgrade", "desc": "Upgrading your hotel will lead to more revenue and less maintenance relatively. It also increases your net-worth"}
    }, "Stocks": {
    "category":"Stocks",
      "e.stocks": {"aliases": ["None"], "usage": "e.stocks", "desc": "Invest in stock market which refreshes every 20-30 secs. New stock starts every day. Probably the best and fastest way to earn money?"},
      "e.buy": {"aliases": ["None"], "usage": "e.buy <quantity>", "desc": "Buy stocks on current price"},
      "e.sell": {"aliases": ["None"], "usage": "e.sell <quantity>", "desc": "Sell stocks on current price"}
    }, "Bank": {
        "category":"Bank",
        "e.balance": {"aliases": ["bal"], "usage": "e.balance [user]", "desc": "View you balance: Bank, Wallet and Stocks"},
        "e.mybank": {"aliases": ["None"], "usage": "e.mybank", "desc": "View interest rate, average balance, bank tier etc."},
        "e.statement": {"aliases": ["transactions"], "usage":"e.statement [-a <amount>] [-t <c | d>] [-r <reason>]", "desc":"View your bank statement and filter records based on Type, Amount and/or Reason"},
        "e.deposit": {"aliases": ["dep"], "usage":"e.deposit <amount>", "desc":"Deposit coins to bank"},
        "e.withdraw": {"aliases": ["with"], "usage":"e.withdraw <amount>", "desc":"Withdraw coins from bank"}
    }, "Admin":{
        "category":"Admin",
        "e.set_chl":{"aliases":["None"], "usage":"e.set_chl #channel", "desc":"Allows the bot to respond in that channel"},
        "e.del_chl":{"aliases":["None"], "usage":"e.del_chl #channel", "desc":"Disallows the bot to respond in that channel"},
        "e.list_chl":{"aliases":["None"], "usage":"e.list_chl", "desc":"Lists all the channels where the bot is allowed to respond"},
        "e.reset_chl":{"aliases":["None"], "usage":"e.reset_chl", "desc":"Clears all the configuration and makes the bot to respond again in **all** the channels"}
    }, "Misc":{
        "category":"Misc",
        "e.level": {"aliases":["pf"], "usage":"e.level [user]", "desc":"Shows you level, perks and other stats"},
        "e.give": {"aliases": ["None"], "usage":"e.give <user> <amount>", "desc":"Send coins to a person from your wallet"},
        "e.transfer": {"aliases": ["None"], "usage":"e.transfer <user> <amount> [Reason]", "desc":"Transfer coins from your bank to others\' bank. It costs interest if bank isn't same.\nThis action is recorded in bank statements"},
        "e.alerts": {"aliases":["None"], "usage":"e.alerts <on | off>", "desc":"Receive DMs from bot upon stock ending, pending maintenance etc."},
        "e.daily": {"aliases":["None"], "usage":"e.daily", "desc":"Gives you your daily interest. It is the product of interest rate and average bank balance"}
    }
}
usercmds = {}
stock_names = ['Ava', 'Neil', 'Ryan', 'Anthony', 'Bernadette', 'Lauren', 'Justin', 'Matt', 'Wanda', 'James', 'Emily', 'Vanessa', 'Carl', 'Fiona', 'Stephanie', 'Pippa', 'Phil', 'Carol', 'Liam', 'Michael', 'Ella', 'Amanda', 'Caroline', 'Nicola', 'Sean', 'Oliver', 'Kylie', 'Rachel', 'Leonard', 'Julian', 'Richard', 'Peter', 'Irene', 'Dominic', 'Connor', 'Dorothy', 'Gavin', 'Isaac', 'Karen', 'Kimberly', 'Abigail', 'Yvonne', 'Steven', 'Felicity', 'Evan', 'Bella', 'Alison', 'Diane', 'Joan', 'Jan', 'Wendy', 'Nathan', 'Molly', 'Charles', 'Victor', 'Sally', 'Rose', 'Robert', 'Claire', 'Theresa', 'Grace', 'Keith', 'Stewart', 'Andrea', 'Alexander', 'Chloe', 'Nicholas', 'Edward', 'Deirdre', 'Anne', 'Joseph', 'Alan', 'Rebecca', 'Jane', 'Natalie', 'Cameron', 'Owen', 'Eric', 'Gabrielle', 'Sonia', 'Tim', 'Sarah', 'Madeleine', 'Megan', 'Lucas', 'Joe', 'Brandon', 'Brian', 'Jennifer', 'Alexandra', 'Adrian', 'John', 'Mary', 'Tracey', 'Jasmine', 'Penelope', 'Hannah', 'Thomas', 'Angela', 'Warren', 'Blake', 'Simon', 'Audrey', 'Frank', 'Samantha', 'Dan', 'Victoria', 'Paul', 'Jacob', 'Heather', 'Una', 'Lily', 'Carolyn', 'Jonathan', 'Ian', 'Piers', 'William', 'Gordon', 'Dylan', 'Olivia', 'Jake', 'Leah', 'Jessica', 'David', 'Katherine', 'Amelia', 'Benjamin', 'Boris', 'Sebastian', 'Lisa', 'Diana', 'Michelle', 'Emma', 'Sam', 'Stephen', 'Faith', 'Kevin', 'Austin', 'Jack', 'Ruth', 'Colin', 'Trevor', 'Joanne', 'Virginia', 'Anna', 'Max', 'Adam', 'Maria', 'Sophie', 'Sue', 'Andrew', 'Harry', 'Amy', 'Christopher', 'Donna', 'Melanie', 'Elizabeth', 'Lillian', 'Julia', 'Christian', 'Luke', 'Zoe', 'Joshua', 'Jason']
xp_timeout = []
warn1 = []
warn2 = []
error_embed = 16290332
success_embed = 2293571

def is_dev(ctx):
    return ctx.author.id in devs

async def spam_protect(userid):
    last = usercmds.get(userid, 0)
    current = time.time()
    usercmds[userid] = current
    if current - last < 2:
        if userid not in warn1:
            asyncio.create_task(handle_1(userid))
            return 'warn'
        elif userid not in warn2:
            asyncio.create_task(handle_2(userid))
            return 'warn'
        else:
            asyncio.create_task(handle_disregard(userid))
            return 'disregard'
    else:
        return 'ok'

async def handle_1(userid):
    warn1.append(userid)
    await asyncio.sleep(2)
    warn1.remove(userid)

async def handle_2(userid):
    warn2.append(userid)
    await asyncio.sleep(2)
    warn2.remove(userid)

async def handle_disregard(userid):
    disregarded.append(userid)
    await asyncio.sleep(10*60)
    disregarded.remove(userid)

async def get_avg():
    with open('average.json', 'r') as avg:
        return json.load(avg)

async def get_admin():
    with open('admin.json', 'r') as f:
        return json.load(f)

async def close_admin(a):
    with open('admin.json', 'w') as f:
        f.write(json.dumps(a))

async def get_estates():
    with open('estates.json', 'r') as f:
        return json.load(f)

async def get_alert_info():
    with open('alerts.json', 'r') as a:
        aler = json.load(a)
    return aler

async def get_data():
    with open('accounts.json', 'r') as f:
        data = f
        if data == '{}':
            return {1:1}
        else:
            return json.load(data)

async def get_revenue(level:int):
    return int((level*200 - 50)*0.97)

async def get_maint(level:int):
    return int((level*200 - 50)*0.9)

async def get_cost(level:int):
    return int((300*level)**(1.75))

async def get_fees(user, amt):
    btype = user['bank_type']
    fees = {1:1, 2:1.2, 3:1.5}

    if 20000 >= amt > 5000:
        a = 250
    elif 30000 >= amt > 20000:
        a = 500
    elif 50000 >= amt > 30000:
        a = 1000
    elif 75000 >= amt > 50000:
        a = 2000
    elif amt > 75000:
        a = 5000
    else:
        a = 0

    return int(a*fees[btype])

async def get_xp():
    with open('xp.json', 'r') as xp:
        return json.load(xp)

async def get_todays_stock():
    a = os.listdir('stocks')
    b = [f'{x}_today.csv' for x in range(1, 1001)]
    today = [x for x in a if x in b]

    if len(today) == 0:
        pass
    else:
        return today[0]

    b = [f'{x}_done.csv' for x in range(1, 1001)]
    newlist = [x for x in a if x not in b]

    choose = random.choice(newlist)
    os.rename(f'stocks/{choose}', f'stocks/{str(choose)[:-4]}_today.csv')
    return f'{str(choose)[:-4]}_today.csv'

async def get_statements():
    with open('statements.json', 'r') as s:
        return json.load(s)

async def get_stocks():
    with open('stocks.json', 'r') as s:
        return json.load(s)

async def get_badges():
    with open('badges.json', 'r') as b:
        return json.load(b)

async def get_data_stock(file):
    with open(f'stocks/{file}', 'r') as f:
        return list(csv.reader(f))

async def get_url(url):
    a = requests.get(url)
    return a.content

async def update_stock_data(data):
    with open('stocks.json', 'w') as avgbal:
        avgbal.write(json.dumps(data))

async def update_badges(data):
    with open('badges.json', 'w') as b:
        b.write(json.dumps(data))

async def update_avg(avg):
    with open('average.json', 'w') as avgbal:
        avgbal.write(json.dumps(avg))

async def update_est(data):
    with open('estates.json', 'w') as f:
        f.write(json.dumps(data))

async def update_alerts(data):
    with open('alerts.json', 'w') as f:
        f.write(json.dumps(data))

async def update_logs(stuff: str):
    with open('logs.txt', 'a') as logs:
        logs.write(f'\n{stuff}')

async def update_data(data):
    with open('accounts.json', 'w') as f:
        f.write(str(json.dumps(data)))

async def update_statements(stat):
    with open('statements.json', 'w') as w:
        w.write(json.dumps(stat))

async def update_xp(data):
    with open('xp.json', 'w') as w:
        w.write(json.dumps(data))

async def clear_dues():
    data = await get_data()
    stock_data = await get_stocks()

    for i in stock_data:
        person = data[str(i)]
        value = stock_data[str(i)]
        if value == 0:
            continue
        current_price = int(current_stock[-1][5])

        bulk = int(current_price*value)
        person['bank'] += bulk
        data[str(i)] = person
        stock_data[str(i)] = 0
        user = await bot.fetch_user(i)
        if user is None:
            continue
        embed = discord.Embed(title='Stock Ended', description=f'The current stock ended and `{await commait(bulk)}` coins have been added to your bank.')
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_author(name=f'{user.name}', icon_url=user.avatar_url)
        embed.set_footer(text='Economy Bot', icon_url=bot_pfp)
        #await user.send(embed=embed)
        await create_statement(user, bot.user, bulk, f"Sold {value} Stocks", "Credit")

    await update_data(data)
    await update_stock_data(stock_data)
    with open('stock_config.json', 'w') as r:
        r.write('{}')
    with open('stocks.json', 'w') as r:
        r.write('{}')

async def update_stocks():
    global current_stock, total_lines
    stock = await get_todays_stock()
    with open(f'stocks/{stock}', 'r') as st:
        data = list(csv.reader(st))
    total_lines = len(data)

    with open('stock_config.json', 'r') as c:
        config = json.load(c)
    line = config.setdefault("line", 1)
    name = config.setdefault("name", random.choice(stock_names))
    if line == total_lines:
        os.rename(f'stocks/{stock}', f'stocks/{str(stock).replace("_today", "_done")}')
        config['line'] = line + 1
        with open('stock_config.json', 'w') as c:
            c.write(json.dumps(config))
        await clear_dues()
        await update_stocks()
    else:
        config['line'] = line + 1
        with open('stock_config.json', 'w') as c:
            c.write(json.dumps(config))

        current_stock = list(data[line])
        current_stock.pop(0)
        current_stock.pop(0)

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
            persona = aler.get(i)
            if persona is None:
                continue

            state, last = persona['state'], persona['last']
            dm_diff = cur - last

            person['p'] = diff - 172800
            est[str(i)] = person
            await update_est(est)

            if state == 'on' and dm_diff > 21600:
                embed = discord.Embed(title='Maintenance Reminder',
                                      description='Your Hotel Maintenance is due. Use `e.maintain` to pay for it.\n'
                                                  'Note: You will get less revenue if maintenance isn\'t done!',
                                      colour=embedcolor)
                fetched = bot.get_user(int(i))
                if fetched is None:
                    continue
                embed.timestamp = datetime.datetime.utcnow()
                embed.set_author(name=f'{fetched.name}', icon_url=fetched.avatar_url)
                embed.set_footer(text='Economy Bot', icon_url=bot_pfp)

                persona['last'] = cur
                aler[str(i)] = persona
                #await update_alerts(aler)

                #await fetched.send(embed=embed)

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

async def stock_update():
    while True:
        await update_stocks()
        await perform_stuff(current_stock)
        await asyncio.sleep(86400/total_lines)

async def loops():
    while True:
        await avg_update()
        await est_update()
        await asyncio.sleep(300)

async def open_account(userid):
    data = await get_data()
    if data.get(str(userid)) is None:
        data[userid] = {'bank_type':1, 'wallet':0, 'bank':1000}
        await update_data(data)

async def open_estates(userid):
    data = await get_estates()
    if data.get(str(userid)) is None:
        user = await bot.fetch_user(userid)
        data[f'{userid}'] = {'level':1, 'name':f'{user.name}', 'lm':time.time(), 'lr':time.time(), 'p':0, 'c':0}

    await update_est(data)

async def checktimeout(userid, event):
    with open('timeouts.json', 'r') as t:
        timeouts = json.load(t)
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
        data = json.load(f)

    person = data.get(f'{userid}')
    if person is None:
        person = {}
    person[event] = time.time()

    data[userid] = person
    with open('timeouts.json', 'w') as f:
        f.write(json.dumps(data))

async def alerts_state(userid, state:str):
    with open('alerts.json', 'r') as a:
        aler = json.load(a)
    userid = str(userid)
    person = aler.get(userid)
    if person is None:
        person = {'state':0, 'last':0}

    person['state'] = state
    aler[userid] = person

    with open('alerts.json', 'w') as aa:
        aa.write(json.dumps(aler))

async def commait(val):
    return "{:,}".format(val)

async def current_time():
    return datetime.datetime.today().replace(microsecond=0)

async def create_statement(user, person, amount, reason, type):
    states = await get_statements()
    user_s = states.get(f'{user.id}')
    if reason is None:
        reason = 'N.A.'
    if person != bot.user:
        entry = {'person':f'{person.name}#{person.discriminator}', 'type':type, 'amount':amount, 'time':f'{await current_time()}', 'reason':reason}
    else:
        entry = {'person':f'System', 'type':type, 'amount':amount, 'time':f'{await current_time()}', 'reason':reason}
    if user_s is None:
        user_s = [entry]
    else:
        user_s.append(entry)

    states[str(user.id)] = user_s
    await update_statements(states)

async def create_stuff():
    global bot_pfp
    mybot = bot.get_user(832083717417074689)
    bot_pfp = mybot.avatar_url
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Thunder qt"))
    #await bot.change_presence(status=discord.Status.invisible)
    asyncio.create_task(loops())
    asyncio.create_task(stock_update())
    print('Ready!')

async def calculate_level(xp:int):
    level_found = -1
    for i in xp_levels.keys():
        if xp <= i:
            for key, value in xp_levels.items():
                if i == key:
                    level_found = value
                    break
            if level_found != -1:
                break
    return level_found

async def add_xp_tm(userid):
    xp_timeout.append(userid)
    await asyncio.sleep(50)
    xp_timeout.remove(userid)

async def perform_stuff(data):
    with open('stock_config.json', 'r') as r:
        stock_data = json.load(r)
    #columns = ['Name', 'Highest', 'Lowest', 'Current', 'Volume']
    highest = float(stock_data.setdefault('highest', data[1]))
    lowest = float(stock_data.setdefault('lowest', data[2]))
    current = float(data[3])
    if highest < current:
        highest = current
    if lowest > current:
        lowest = current

    users = await get_stocks()
    volume = 0
    for i in users.values():
        volume += i
    stock_data['volume'] = volume
    stock_data['lowest'] = lowest
    stock_data['highest'] = highest
    with open('stock_config.json', 'w') as r:
        r.write(json.dumps(stock_data))

    return stock_data

async def get_avatar(user):
    return Image.open(BytesIO(await user.avatar_url_as(format="png").read())).resize((140, 140))

async def make_lvl_img(member, level, xp, total_xp, guildid):
    def AddShadow(text, x, y):
        font = ImageFont.truetype("badges/font2.ttf", 30)
        sc1 = '#313131'
        sc2 = '#313131'
        draw.text((x - 2, y), text, font=font, fill=sc2)
        draw.text((x + 2, y), text, font=font, fill=sc2)
        draw.text((x, y - 2), text, font=font, fill=sc2)
        draw.text((x, y + 2), text, font=font, fill=sc2)

        draw.text((x - 2, y - 2), text, font=font, fill=sc1)
        draw.text((x + 2, y - 2), text, font=font, fill=sc1)
        draw.text((x - 2, y + 2), text, font=font, fill=sc1)
        draw.text((x + 2, y + 2), text, font=font, fill=sc1)

        draw.text((x, y), text, font=font)

    img = Image.open("./badges/3.png")
    member_colour = member.color.to_rgb()
    avatar = await get_avatar(member)
    ava_mask = Image.open("badges/AVAmask.png").convert('L')
    ava_mask2 = Image.open("badges/AVAmas2k.png").convert('L')
    img.paste(Image.new("RGBA", (148, 148), member_colour), (11, 11), ava_mask2)
    img.paste(avatar, (15, 15), ava_mask)
    member_status = member.status
    status = Image.open(f'badges/{member_status}.png')
    img.paste(status.resize((30, 30)), (124, 113), status.resize((30, 30)))

    xpbar = Image.open("./badges/xpbar.png")
    xpbar = xpbar.resize((579, 27))
    pixdata = xpbar.load()
    for y in range(xpbar.size[1]):
        for x in range(xpbar.size[0]):
            pixdata[x, y] = tuple(list(member_colour) + [pixdata[x, y][-1]])

    xpbar = xpbar.crop((0, 0, xpbar.width * (int(xp) / int(total_xp)), xpbar.height))
    img.paste(xpbar, (180, 105), xpbar)

    badges = await get_badges()
    if str(member.id) in badges['staff']: staff = True
    else: staff = False
    if str(member.id) in badges['patron']: patron = True
    else: patron = False
    location = 710
    if staff:
        staff_icon = Image.open('badges/staff.png')
        pixdata = staff_icon.load()
        for y in range(staff_icon.size[1]):
            for x in range(staff_icon.size[0]):
                pixdata[x, y] = tuple(list(member_colour) + [pixdata[x, y][-1]])
        staff_icon = staff_icon.resize((37, 37))
        img.paste(staff_icon, (location, 55), staff_icon)
        location -= 45
    if patron:
        patron_icon = Image.open('badges/patron.png')
        patron_icon = patron_icon.resize((37, 37))
        img.paste(patron_icon, (location, 55), patron_icon)
        location -= 45
    server_r, global_r = await xp_ranks(member.id, guildid)
    if global_r > 1000:
        global_r = 'Unknown'
    else:
        global_r = f'#{global_r}'
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("badges/font2.ttf", 19)
    font_rank = ImageFont.truetype("badges/font2.ttf", 24)
    fontm = ImageFont.truetype("badges/font2.ttf", 13)
    fonts = ImageFont.truetype("badges/font2.ttf", 10)
    #fontu = ImageFont.truetype("badges/unicode.ttf", 25)
    draw.text((180, 34), f'{member.name}#{member.discriminator}', (255, 255, 255), font=font)
    draw.text((180, 70), f"Level {level}", (255, 255, 255), font=fontm)
    draw.text((120, 210), f'Server Rank', font=font)
    draw.text((530, 210), f'Global Rank', font=font)
    draw.text((120, 250), f'#{server_r}',(255, 243, 0), font=font_rank)
    draw.text((530, 250), f'{global_r}', (255, 243, 0), font=font_rank)
    AddShadow('Some Stuff Soon...', 220, 450)
    twidth, theight = draw.textsize(f"{await commait(xp)}/{await commait(total_xp)}", fonts)
    draw.text((468 - (twidth / 2), 121 - (theight / 2)), f"{await commait(xp)}/{await commait(total_xp)}", (255, 255, 255), font=fonts,
              stroke_width=1, stroke_fill=(0, 0, 0))
    image_bytes = BytesIO()
    img.save(image_bytes, 'PNG')
    image_bytes.seek(0)
    return discord.File(fp=image_bytes, filename='level.png')

async def xp_ranks(member, guild):
    userid = str(member)
    xp = await get_xp()
    xp_sorted_desc = sorted(xp.items(), key=operator.itemgetter(1), reverse=True)
    guild = bot.get_guild(guild)
    guildmembers = guild.members
    member_list = [x.id for x in guildmembers]
    global_rank = 1
    guild_rank = 1
    for i in xp_sorted_desc:
        if i[0] == userid:
            break
        global_rank += 1
        if int(i[0]) in member_list:
            guild_rank += 1
    return guild_rank, global_rank

async def check_channel(chlid, guildid):
    a = await get_admin()
    server = a.get(str(guildid))
    if server is None: return True
    if len(server) == 0: return True
    if chlid in server: return True
    else: return False

devmode = True

@bot.check
async def is_dm(ctx):
    return ctx.guild != None

@bot.check
async def if_allowed(ctx):
    return await check_channel(ctx.channel.id, ctx.guild.id)

@bot.event
async def on_command_error(ctx, error):
    print(error)

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    await open_account(message.author.id)
    if message.content.startswith('e.') or message.content.startswith('E.'):
        if bot.dev == 1 and message.author.id not in devs: return
        if message.author.id in disregarded:
            if message.author.id not in devs: return
        state = await spam_protect(message.author.id)
        if state == 'warn':
            embed = discord.Embed(title='Using commands too fast!', color=error_embed)
            return await message.channel.send(embed=embed)
        elif state == 'disregard':
            embed = discord.Embed(title='Warning!', description=f'{message.author.mention} has been disregarded for 10 mins!\n**Reason: Spamming Commands**',color=error_embed)
            return await message.channel.send(embed=embed)
        if message.author.id not in xp_timeout:
            userid = message.author.id
            xps = await get_xp()
            xp = xps.setdefault(f'{userid}', 0)
            togive = random.randint(10, 25)
            xps[str(userid)] = xp + togive
            asyncio.create_task(update_xp(xps))
            asyncio.create_task(add_xp_tm(userid))
    try:
        await bot.process_commands(message)
    except Exception as e:
        if message.author.id in devs:
            await message.channel.send(f'```\n{e}```')

@bot.command()
@commands.check(is_dev)
async def dvm(ctx):
    if bot.dev == 1:
        await ctx.reply('Changed Dev Mode state to: **`Off`**')
        bot.dev = 0
    else:
        await ctx.reply('Changed Dev Mode state to: **`On`**')
        bot.dev = 1

@bot.command() #DEV ONLY
@commands.check(is_dev)
async def logs(ctx, *, search:str=None):
    with open('logs.txt', 'r') as log:
        logs_data = log.readlines()
    logs_data.reverse()
    x = PrettyTable()
    x.field_names = ['Used By', 'Command', 'Parameters', "Time"]
    count = 1
    for i in logs_data:
        if i == '' or i == '\n':
            continue
        if count > 15:
            break
        i = i.replace('\n', '')
        splitted = i.split('-!-')
        splitted[3] = splitted[3].replace(':','˸')
        if search is not None:
            if splitted[1] != search:
                continue
        x.add_row(splitted)
        count += 1
    await ctx.send(f'**Requested by:** `{ctx.author.name}`\n```css\n{x.get_string()[:1900]}```')

@bot.command(aliases=['eval'])  # DEV ONLY
@commands.check(is_dev)
async def evaluate(ctx, *, expression):
    try:
        await ctx.reply(eval(expression))
    except Exception as e:
        await ctx.reply(f'```\n{e}```')

@bot.command(aliases=['exec']) #DEV ONLY
@commands.check(is_dev)
async def execute(ctx, *, expression):
    try:
        exec(expression.replace('```', ''))
    except Exception as e:
        await ctx.reply(f'Command:```py\n{expression}```\nOutput:```\n{e}```')

@bot.command() #DEV ONLY
@commands.check(is_dev)
async def add(ctx, person:discord.Member, bal:int, *args):
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

    await update_logs(f'{ctx.author}-!-add-!-[{person.id}, {await commait(bal)}]-!-{datetime.datetime.today().replace(microsecond=0)}')
    await ctx.send(f'{ctx.author.mention} added `{await commait(bal)}` coins to {person.mention}.')

@bot.command() #DEV Only
@commands.check(is_dev)
async def clear(ctx, member:discord.Member):
    data = await get_data()
    userid = str(member.id)

    person = data[userid]
    person['bank'] = 0
    person['wallet'] = 0

    data[userid] = person
    await update_data(data)
    await update_logs(f'{ctx.author}-!-clear-!-[{member.id}]-!-{datetime.datetime.today().replace(microsecond=0)}')
    await ctx.send(f'{ctx.author.mention} Cleared data of `{member.name}#{member.discriminator}` successfully!')

@bot.command()
@commands.check(is_dev)
async def format(ctx, member:discord.Member):
    data = await get_data()
    estate = await get_estates()
    xp = await get_xp()
    st = await get_stocks()
    state = await get_statements()
    userid = str(member.id)

    person = data[userid]
    person['bank'] = 0
    person['wallet'] = 0

    data[userid] = person
    await update_data(data)
    await update_logs(f'{ctx.author}-!-clear-!-[{member.id}]-!-{datetime.datetime.today().replace(microsecond=0)}')
    await ctx.send(f'{ctx.author.mention} Cleared data of `{member.name}#{member.discriminator}` successfully!')

@bot.command() #DEV Only
@commands.check(is_dev)
async def release(ctx, title:str, link:str):
    with open('updates.json', 'r') as upd:
        updates = json.load(upd)

    update = updates[title]
    desc = ''
    for i in update:
        desc += f'{i}\n'
    embed = discord.Embed(title=f'Updated to v{title}', color=embedcolor, description=desc)
    embed.url = link
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_author(name=f'Bot Updated!', icon_url=bot_pfp)

    chl = bot.get_channel(838963496476606485)
    await chl.send('<@&839370096248881204> New Update Out!',embed = embed)

@bot.command()
@commands.check(is_dev)
async def stockinfo(ctx):
    with open(f'stocks/{await get_todays_stock()}', 'r') as f:
        stock = list(csv.reader(f))
    with open(f'stock_config.json', 'r') as c:
        config = json.load(c)

    embed = discord.Embed(title='Stock Info', color=embedcolor)
    embed.add_field(name='Total Rows', value=f'{len(stock)}')
    embed.add_field(name='Current Row', value=f'{config["line"]}')
    embed.add_field(name='Approx Refresh Time', value=f'{round(86400/len(stock), 4)} secs')
    left = datetime.timedelta(seconds=((len(stock)-config["line"])*round(86400/len(stock), 4)))
    final = datetime.datetime.strptime(str(left), '%H:%M:%S.%f').replace(microsecond=0)
    embed.add_field(name='Ending Time', value=f'`{str(final).split(" ")[1]}` (HH:MM:SS)')

    await ctx.send(embed=embed)

@bot.command()
@commands.check(is_dev)
async def badge(ctx, member:discord.Member, badge:str):
    badges = await get_badges()
    userid = str(member.id)

    badge_type = badges.get(badge)
    if badge_type is None:
        list_of_all = list(badges.keys())
        await ctx.message.add_reaction('‼️')
        return await ctx.send(f'{ctx.author.mention} Badge `{badge_type}` not found!\n'
                        f'Please Choose from: `{" ,".join(list_of_all)}`')
    if userid in badge_type:
        return await ctx.message.add_reaction('✅')
    badge_type.append(userid)
    badges[badge] = badge_type
    await update_badges(badges)
    await ctx.message.add_reaction('✅')

@bot.command(aliases=['bal'])
async def balance(ctx, member:discord.Member = None):
    if member is None:
        userid = ctx.author.id
    else:
        userid = member.id
    await open_account(userid)
    data = await get_data()
    person = data.get(str(userid))
    bank_type = person['bank_type']
    wallet = person['wallet']
    bank = person['bank']
    s = await get_stocks()
    stocks_num = s.get(str(userid), 0)
    embed = discord.Embed(title=f'__{bank_names[bank_type]}__', colour=embedcolor)
    embed.add_field(name=f'**<:wallet:836814969290358845> Wallet**', value=f'> `{await commait(wallet)}`', inline=False)
    embed.add_field(name=f'**🏦 Bank**', value=f'> `{await commait(bank)}`', inline=False)
    embed.add_field(name=f'**<:stocks:839162083324198942> Stocks**', value=f'> `{await commait(stocks_num)}`', inline=False)
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
    print(amount, wallet)
    if amount < 0:
        return await ctx.send(f'{ctx.author.mention} No over-smartness with me.')
    if amount == 0:
        return await ctx.send(f'{ctx.author.mention} `0` coins? Are you drunk or something?')
    if wallet < amount:
        return await ctx.send(f'{ctx.author.mention} Want to deposit more you have? Nah not here.')

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

    if amount < 0:
        return await ctx.send(f'{ctx.author.mention} No over-smartness with me.')
    if amount == 0:
        return await ctx.send(f'{ctx.author.mention} `0` coins? Are you drunk or something?')
    if bank < amount:
        return await ctx.send(f'{ctx.author.mention} Now dont\'t try to withdraw more than you have.')

    newbal_w = wallet + amount
    newbal_b = bank - amount

    person['wallet'] = newbal_w
    person['bank'] = newbal_b
    data[f'{ctx.author.id}'] = person

    await update_data(data)
    await ctx.send(f'{ctx.author.mention} Successfully withdrew `{await commait(amount)}` coins.')

@bot.command()
async def mybank(ctx, member:discord.Member = None):
    if member is None:
        userid = ctx.author.id
    else:
        userid = member.id
    await open_account(userid)
    await avg_update()
    data = await get_data()
    avgbal = await get_avg()

    person = data.get(f'{userid}')
    person2 = avgbal.get(f'{userid}')
    btype = person['bank_type']

    embed = discord.Embed(description='Here are your bank details:\n\u200b', color=embedcolor)
    embed.add_field(name='Bank Name', value=f'{bank_names[btype]}')
    embed.add_field(name='Bank Tier', value=f'{bank_tier[btype]}')
    embed.add_field(name='\u200b', value='\u200b')
    embed.add_field(name='Daily Interest', value=f'{rates[btype]}%')
    embed.add_field(name='Current Balance', value=f'{person["bank"]}')
    embed.add_field(name='Average Balance', value=f'{person2["avg"]}')
    embed.add_field(name='Note:', value='To claim interest, use `e.daily`.\n'
                                        'Your average balance in last 24 hours will be taken in account for that.')
    fetched = bot.get_user(userid)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text='Economy Bot', icon_url=bot_pfp)
    embed.set_author(name=f'{fetched.name} | 🏦 Know Your Bank!', icon_url=fetched.avatar_url)

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
        check = await checktimeout(ctx.author.id, 'daily')
        if check is not None:
            if i < 288:
                time_gap = 86400 - check
                if time_gap < 0:
                    time_gap = check - 86400
                left = datetime.timedelta(seconds=(time_gap))
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

    avg[f'{ctx.author.id}'] = avg_p

    await update_avg(avg)
    await update_data(data)
    await add_timeout(ctx.author.id, 'weekly')

    await ctx.send(f'Daily interest payout of `{await commait(int(avgbal * multiplier))}` coins credited successfully!')

@bot.command()
async def give(ctx, member:discord.Member, amount:int):
    data = await get_data()
    await open_account(member.id)
    author = data.get(f'{ctx.author.id}')
    person = data.get(f'{member.id}')

    a_wallet = author['wallet']
    a_bank = author['bank']

    if amount == 'all':
        amount = a_bank
    elif amount == 'half':
        amount = a_bank/2
    else:
        amount = int(amount)

    if amount == 0:
        return await ctx.send(f'{ctx.author.mention} Sending 0 coins... Hmm nice idea but we dont do that here.')
    if amount < 0:
        return await ctx.send(f'{ctx.author.mention} Dont try to be oversmart kiddo.')
    if amount > 5000:
        return await ctx.send(f'{ctx.author.mention} You cannot give more than `5,000` coins through `e.give`.\nUse `e.transfer` instead.')
    if member == ctx.author:
        return await ctx.send(f'{ctx.author.mention} Did you just try to send **yourself** some coins?')

    if amount > a_wallet:
        return await ctx.send(f'{ctx.author.mention} You dont have enough coins. Go beg or withdraw.')

    new_a_wallet = a_wallet - amount

    author['wallet'] = new_a_wallet
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
async def estates(ctx, member:discord.Member=None):
    if member is None:
        userid = ctx.author.id
    else:
        userid = member.id

    await open_estates(userid)
    est = await get_estates()
    person = est[f'{userid}']
    level = person['level']
    name = person['name']
    revenue = await get_revenue(level)
    maint = await get_maint(level)
    if level == 30:
        extra = ' `(Maxed Out!)`'
    else:
        extra = ''
    embed = discord.Embed(description='\u200b', colour=embedcolor)
    embed.add_field(name='Current Level', value=f'{level}{extra}')
    embed.add_field(name='Revenue Earned', value=f'`{await commait(revenue)}` coins')
    embed.add_field(name='Maintainance Cost', value=f'`{await commait(maint)}` coins')
    if level < 30:
        embed.add_field(name='Next Task', value=f'```css\n[{estates_tasks[level]}]\nUse e.upgrade to Upgrade!\n```', inline=False)
    embed.add_field(inline=False, name='Note:', value='```diff\nThe revenue is earned in per hour\n+ Use e.revenue to claim revenue\n- Use e.maintain to do maintainance\n```')

    fetched = bot.get_user(userid)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text='Economy Bot', icon_url=bot_pfp)
    embed.set_author(name=f'{fetched.name} | {name} Hotel', icon_url=fetched.avatar_url)
    a = Image.open(BytesIO(await get_url(getestates_thumb[level])))
    h, w = a.size
    a.resize((int(h*0.6), int(w*0.6)))
    image_bytes = BytesIO()
    a.save(image_bytes, 'PNG')
    image_bytes.seek(0)
    uri = (await bot.get_guild(826824650713595964).get_channel(837564505952747520).send(f'{level}', file=discord.File(image_bytes, filename="estate.png"))).attachments[0].url
    embed.set_image(url=uri)

    await ctx.send(embed=embed)

@bot.command()
async def revenue(ctx):
    userid = ctx.author.id
    await open_estates(userid)
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
    x.add_row(["Late Maintenance", "", "", f'{await commait(low_rev)}.00/-'])
    x.add_row(["Late Fine", "", "", f'{await commait(fine)}.00/-'])
    x.add_row(["", "", "", f''])
    x.add_row(["[Grand Total]", "", "", f'{await commait(totalpay)}.00/-'])

    embed = discord.Embed(title='Hotel Revenue',
                          description=f'`{totalpay}.00` coins added to bank successfully!\n\nHere is the revenue split:\n```css\n{x}```',
                          colour=success_embed)
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
    userid = ctx.author.id
    await open_estates(userid)
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

    if bank_bal < cost_d:
        embed = discord.Embed(title='Oops..',
                              description=f'You dont have enough coins in bank to do the maintainance.\n```css\n{x}```', color=error_embed)
    else:
        new_bbal = bank_bal - cost_d
        persona['bank'] = new_bbal
        data[userid] = persona

        person['lm'] = time.time()
        person['p'] = 0
        est[userid] = person

        await update_data(data)
        await update_est(est)

        embed = discord.Embed(title='Success!',
                              description=f'`{cost_d}.00` coins have been deducted and your hotel looks shining new!\n```css\n{x}```',
                              color=success_embed)

    fetched = bot.get_user(ctx.author.id)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text='Economy Bot', icon_url=bot_pfp)
    embed.set_author(name=f'{fetched.name} | {name} Hotel', icon_url=fetched.avatar_url)

    await ctx.send(embed=embed)

@bot.command()
async def upgrade(ctx):
    userid = ctx.author.id
    await open_estates(userid)
    est = await get_estates()
    eperson = est[f'{ctx.author.id}']
    level = eperson['level']
    name = eperson['name']
    if level == 30:
        embed = discord.Embed(title='Maxed Out!',
                              description='You are already at the maximum level, Chill down mate!',
                              color=embedcolor)
        fetched = bot.get_user(ctx.author.id)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text='Economy Bot', icon_url=bot_pfp)
        embed.set_author(name=f'{fetched.name} | {name} Hotel', icon_url=fetched.avatar_url)

        return await ctx.send(embed=embed)

    rev_now = await get_revenue(level)
    rev_after = await get_revenue(level+1)
    main_now = await get_maint(level)
    main_after = await get_maint(level+1)

    cost = await get_cost(level)

    embed = discord.Embed(title='Upgrade Hotel', colour=embedcolor)
    if level < 30:
        embed.add_field(name='Level Change', value=f'`{level} => {level+1}`')
    else:
        embed.add_field(name='Level Change', value=f'``{level} => Maxed Out!`')
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
            aler = json.load(a)
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

@bot.command()
async def transfer(ctx, togive:discord.Member = None, amount = None, *, reason = None):
    if togive is None or amount is None:
        return await ctx.send(f'{ctx.author.mention} The format for the command is: `e.transfer @user <amount> [reason]`')
    data = await get_data()
    current = data[f'{ctx.author.id}']
    person = data[f'{togive.id}']

    c_bank = current['bank']
    p_bank = person['bank']

    if amount == 'all':
        amount = c_bank
    elif amount == 'half':
        amount = c_bank/2
    else:
        amount = int(amount)

    if togive == ctx.author:
        return await ctx.send(f'{ctx.author.mention} Did you just try to send **yourself** some coins?')
    if amount == 0:
        return await ctx.send(f'{ctx.author.mention} Sending 0 coins... Hmm nice idea but we dont do that here.')
    if amount < 0:
        return await ctx.send(f'{ctx.author.mention} Dont try to be oversmart kiddo.')

    if current['bank_type'] != person['bank_type']:
        fees = await get_fees(person, amount)
    else:
        fees = 0

    if amount > c_bank:
        return await ctx.send(f'{ctx.author.mention} Well, you don\'t have enough coins. RIP.')
    if amount + fees > c_bank:
        return await ctx.send(f'{ctx.author.mention} You don\'t have enough coins to pay for transaction fees.')

    current['bank'] = c_bank - amount - fees
    person['bank'] = p_bank + amount

    data[f'{togive.id}'] = person
    data[f'{ctx.author.id}'] = current

    await update_data(data)
    await create_statement(ctx.author, togive, amount, reason, 'Debit')
    await create_statement(togive, ctx.author, amount, reason, 'Credit')

    embed = discord.Embed(title='Transfer Successful!',
                          description=f'You transfered `{amount}` coins to {togive.mention}.',
                          color=success_embed)
    embed.add_field(name='Tax on transaction', value=f'`{fees}` coins')
    embed.add_field(name='Your Balance', value=f'`{c_bank - amount}` coins')
    fetched = bot.get_user(ctx.author.id)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text='Economy Bot', icon_url=bot_pfp)
    embed.set_author(name=f'{fetched.name}', icon_url=fetched.avatar_url)

    await ctx.send(embed=embed)

@bot.command(aliases=['transactions'])
async def statement(ctx, *args):
    if '-u' not in args:
        member = ctx.author
    else:
        if ctx.author.id not in devs:
            member = ctx.author
        else:
            index = 1
            for i in args:
                if i == '-u': break
                index += 1
            member = await bot.fetch_user(int(args[index]))

    stats = await get_statements()
    all_s = stats.get(str(member.id))
    if all_s is None:
        desc = 'No Statements Yet..'
    else:
        all_s.reverse()
        x = PrettyTable()
        x.field_names = ['S.No.', 'From/To', 'Date and Time', 'Amount', 'Type', 'Reason']
        x.align['Reason'] = 'l'

        count = 1
        for s in all_s:
            date = s['time'].split(" ")[0]
            time_ = s['time'].split(" ")[1].replace(":", "˸")
            if '-t' in args:
                index = 1
                for i in args:
                    if i == '-t': break
                    index += 1
                cd_type = args[index]
                if cd_type.lower() == 'c' and s['type'] != 'Credit': continue
                elif cd_type.lower() == 'd' and s['type'] != 'Debit': continue
            if '-a' in args:
                index = 1
                for i in args:
                    if i == '-a': break
                    index += 1
                amount = args[index]
                if int(amount) != int(s['amount']): continue
            if '-r' in args:
                index = 1
                for i in args:
                    if i == '-r': break
                    index += 1
                reason = list(args[index:])
                mainr_split = [x.lower() for x in s["reason"][:25].split(' ')]
                if not (all(x in mainr_split for x in reason)): continue
            x.add_row([count, f'{s["person"]}', f"{date} {time_}",  s['amount'], s['type'], f'[{s["reason"][:25]}]'])
            count += 1
            if count == 13:
                break
        desc = x

    await ctx.send(f'**Bank Statement of `{member.name}`:**\n```css\n{desc}```')

@bot.command(aliases=['pf'])
async def level(ctx, member:discord.Member = None):
    if member is None:
        member = ctx.author

    xpdata = await get_xp()
    xp = xpdata.setdefault(f'{member.id}', 0)
    lev = await calculate_level(xp)

    max_xp = 0
    for key, value in xp_levels.items():
        if lev == value:
            max_xp = key
            break
    file = await make_lvl_img(member, lev, xp, max_xp, ctx.guild.id)
    await ctx.send(file=file)

@bot.command()
async def stocks(ctx):
    columns = ['Name', 'Highest   ', 'Lowest', 'Current', 'Volume']
    details = list(current_stock)
    mydata = await perform_stuff(details)
    with open('stock_config.json', 'r') as c:
        config = json.load(c)
    x = PrettyTable()
    x.add_column('   Name', columns)
    x.align['   Name'] = 'l'
    x.add_column('          ', ['          ','          ','          ','          ','          '])
    x.add_column('   Value  ', [config['name'], mydata['highest'], mydata['lowest'], details[3], mydata['volume']])
    x.align['   Value  '] = 'r'
    line = config['line']
    file = await get_todays_stock()
    stock_data = await get_data_stock(file)
    gap = int(line/19)
    if gap == 0:
        gap = 1
    y_axis = []

    for i in range(1, line, gap):
        y_axis.append(float(stock_data[i][5]))
        if len(y_axis) == 20:
            break
    y_axis.pop(-1)
    y_axis.append(float(stock_data[line][5]))
    x_axis = []
    for i in range(1, (len(y_axis))):
        x_axis.append(i)
    x_axis.append('20')

    COLOR = '#52FF51'

    plt.rcParams['text.color'] = COLOR
    plt.rcParams['axes.labelcolor'] = COLOR
    plt.rcParams['xtick.color'] = COLOR
    plt.rcParams['ytick.color'] = COLOR
    plt.rcParams['grid.color'] = '#8A8175'
    fig = plt.figure()
    host = fig.add_subplot(111)
    host.grid()
    plt.plot(x_axis, y_axis, color='#03FFA9', marker='o', ls='-.')
    plt.title('Stock Price vs Time')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.rc('grid', linestyle="-", color='white')
    plt.savefig('graph.png', transparent=True)
    plt.close()

    left = datetime.timedelta(seconds=((len(stock_data) - config["line"]) * round(86400 / len(stock_data), 4)))
    final = datetime.datetime.strptime(str(left), '%H:%M:%S.%f').replace(microsecond=0)
    colon_format = str(final).split(" ")[1].split(':')
    p_data = await get_stocks()
    holdings = p_data.get(str(ctx.author.id), 0)
    myfile = discord.File('graph.png','stock_graph.png')
    embed = discord.Embed(title='Today\'s Stock', description=f'```\n{x}```', color=embedcolor)
    embed.add_field(name='Your Holdings', value=f'`{await commait(holdings)}` stocks')
    embed.add_field(name='Current Value', value=f'`{await commait(int(holdings*float(details[3])))}` coins')
    embed.add_field(name='Time Left', value=f'`{colon_format[0]}h {colon_format[1]}m {colon_format[2]}s`')

    embed.set_image(url="attachment://graph.png")
    await ctx.send(embed=embed, file=discord.File("graph.png"))

@bot.command()
async def buy(ctx, amount):
    data = await get_data()
    stock_data = await get_stocks()
    userid = str(ctx.author.id)
    dperson = data[userid]
    sperson = stock_data.setdefault(userid, 0)
    if dperson['bank'] == 0:
        return await ctx.send(f'{ctx.author.mention} You have an empty bank bro..')
    stock_price = float(current_stock[3])
    if amount == 'all':
        amount = dperson['bank']
        amount = int(amount/stock_price)
    elif amount == 'half':
        amount = int(dperson['bank']/2)
        amount = int(amount / stock_price)
    else:
        amount = int(amount)

    if amount <= 0:
        return await ctx.send(f'{ctx.author.mention} No Fam.')

    bulk = int(amount * stock_price)
    if bulk > dperson['bank']:
        embed = discord.Embed(title='Oops..',
                              description=f'You don\'t have enough bank balance to buy `{await commait(amount)}` stocks.',
                              color=error_embed)
        embed.set_footer(
            text=f'Your Balance: {await commait(dperson["bank"])} coins\nStock Price: {await commait(bulk)} coins\nDifference: {await commait(bulk - dperson["bank"])} coins')
        return await ctx.send(embed=embed)

    dperson['bank'] = dperson['bank'] - bulk
    data[userid] = dperson
    stock_data[userid] = sperson + amount

    await update_data(data)
    await update_stock_data(stock_data)
    await create_statement(ctx.author, bot.user, bulk, f"Bought {amount} stock(s)", "Debit")

    embed = discord.Embed(title='Success!',
                          description=f'You bought `{await commait(amount)}` stocks at price of `{stock_price}`.\n'
                                      f'\nCoins Spent: `{await commait(bulk)}` coins', color=success_embed)
    fetched = bot.get_user(ctx.author.id)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text='Economy Bot', icon_url=bot_pfp)
    embed.set_author(name=f'{fetched.name}', icon_url=fetched.avatar_url)

    await ctx.send(embed=embed)

@bot.command()
async def sell(ctx, amount):
    data = await get_data()
    stock_data = await get_stocks()
    userid = str(ctx.author.id)
    dperson = data[userid]
    sperson = stock_data.setdefault(userid, 0)

    stock_price = float(current_stock[3])
    if amount == 'all':
        amount = sperson
    elif amount == 'half':
        amount = int(sperson/2)
    else:
        amount = int(amount)

    if amount <= 0:
        return await ctx.send(f'{ctx.author.mention} No Fam.')
    bulk = int(amount * stock_price)

    if amount > sperson:
        return await ctx.send(f'{ctx.author.mention} You don\'t own `{amount}` stocks.')

    dperson['bank'] = dperson['bank'] + bulk
    data[userid] = dperson
    stock_data[userid] = sperson - amount

    await update_data(data)
    await update_stock_data(stock_data)
    await create_statement(ctx.author, bot.user, bulk, f"Sold {amount} stock(s)", "Credit")

    embed = discord.Embed(title='Success!',
                          description=f'You sold `{await commait(amount)}` stock(s) at price of `{stock_price}`.\n'
                                      f'\nCoins Earned: `{await commait(bulk)}` coins', color=success_embed)
    fetched = bot.get_user(ctx.author.id)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text='Economy Bot', icon_url=bot_pfp)
    embed.set_author(name=f'{fetched.name}', icon_url=fetched.avatar_url)

    await ctx.send(embed=embed)

@bot.command()
async def help(ctx, specify=None):
    embed = discord.Embed(color=embedcolor,
                          description=f'[Support Server]({support_server}) | [Invite Url]({invite_url}) | [Patreon Page]({patreon_page})\nTo get help on a command, use `e.help <command name>`')
    embed.set_author(name='Help', icon_url=bot_pfp)
    embed.set_footer(text='Syntax: <> = required, [] = optional')
    if specify is None:
        for j in help_json:
            mylist = []
            max_l = 0
            for i in help_json[j].keys():
                if i == "category": continue
                info = help_json[j][i]['usage']
                cmdl = len(info.split(' ')[0])
                if cmdl > max_l:
                    max_l = cmdl
                mylist.append(info)
            finallist = []
            for cmds in mylist:
                splitted = cmds.split(' ')
                first = splitted[0]
                first = first + ' '*(max_l-len(first))
                splitted.pop(0)
                splitted.insert(0, first)
                finallist.append(' '.join(splitted))
            content = '\n'.join(finallist)
            embed.add_field(name=f'**● __{j}__**', value=f'```less\n{content}```', inline=False)
        try:
            await ctx.author.send(embed=embed)
            embed = discord.Embed(title='📧 You received a mail!', color=success_embed)
            await ctx.reply(embed=embed)
        except:
            await ctx.send(embed=embed)
        return
    x = help_json.values()
    notfound = True
    for i in x:
        for j in i.keys():
            if j == 'category':
                continue
            available = []
            available.append(j[2:])
            info = i[j]
            #print(info)
            for k in info['aliases']:
                available.append(k)
            print(available)
            if specify.lower() in available:
                embed = discord.Embed(color=embedcolor, title=f'Command: {j[2:]}', description=info['desc']+f'\n\n**Usage:** `{info["usage"]}`\n**Category:** `{i["category"]}`')
                embed.add_field(name='Aliases', value='```less\n'+'\n'.join([f'e.{q}' for q in info['aliases']])+'```', inline=False)
                embed.set_footer(text='Syntax: <> = required, [] = optional')
                notfound = False
                await ctx.send(embed=embed)
                break
    if notfound:
        embed = discord.Embed(description='No help found or command doesn\'t exist!', embedcolor=error_embed)
        await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_channels=True)
async def set_chl(ctx, channel:discord.TextChannel):
    a = await get_admin()
    server = a.get(str(ctx.guild.id), [])
    if channel.id in server:
        embed = discord.Embed(description=f'{channel.mention} is already in list of registered channels!', color=error_embed)
        return await ctx.send(embed=embed)
    server.append(channel.id)
    a[str(ctx.guild.id)] = server
    await close_admin(a)
    embed = discord.Embed(description=f'{channel.mention} added to list of registered channels successfully!', color=success_embed)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_channels=True)
async def del_chl(ctx, channel:discord.TextChannel):
    a = await get_admin()
    server = a.get(str(ctx.guild.id), [])
    if channel.id not in server:
        embed = discord.Embed(description=f'{channel.mention} not in list of registered channels!', color=error_embed)
        return await ctx.send(embed=embed)
    server.remove(channel.id)
    a[str(ctx.guild.id)] = server
    await close_admin(a)
    embed = discord.Embed(description=f'{channel.mention} removed from list of registered channels successfully!', color=success_embed)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_channels=True)
async def list_chl(ctx):
    a = await get_admin()
    server = a.get(str(ctx.guild.id), [])
    if len(server) == 0: channels = ['> No channels set']
    else: channels = [f'> <#{x}>' for x in server]
    embed = discord.Embed(title='Allowed Channels for the bot:', description='\n'.join(channels), color=embedcolor)
    embed.set_footer(text='Add a channel using e.set_chl <name>\nRemove a channel using e.del_chl <name>')
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_channels=True)
async def reset_chl(ctx):
    a = await get_admin()
    a[str(ctx.guild.id)] = []
    embed = discord.Embed(title='Done', description='Cleared Successfully!', color=embedcolor)
    await close_admin(a)
    embed.set_footer(text='Add a channel using e.set_chl <name>\nRemove a channel using e.del_chl <name>')
    await ctx.send(embed=embed)

@bot.event
async def on_ready():
    await create_stuff()

print("Running...")
bot.run("ODMyMDgzNzE3NDE3MDc0Njg5.YHeoWQ._O5uoMS_I7abKdI_YzVb9BuEHzs")