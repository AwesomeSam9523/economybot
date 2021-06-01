import time
t1 = time.time()
import datetime, csv, threading, functools, asyncio, discord, requests, operator, json, random, os
from discord.ext import commands
from discord.ext.commands import *
from prettytable import PrettyTable
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter
from io import BytesIO
from concurrent.futures import ThreadPoolExecutor
from discord_components import Button, ButtonStyle, InteractionType, DiscordComponents, Select, Context, Option
from asteval import Interpreter
import traceback
aeval = Interpreter()
print(f"Imports Complete in {float('{:.2f}'.format(time.time()-t1))} secs")
tnew = time.time()
intents = discord.Intents.default()
intents.members = True
intents.presences = True
bot = commands.Bot(command_prefix=["e.", "E."], intents=intents, case_insensitive=True)
ddb = DiscordComponents(bot)
bot.launch_time = datetime.datetime.utcnow()
bot.dev = 1
bot.remove_command('help')
bot.loop.set_debug(True)
bot.loop.slow_callback_duration = 0.3
print(f'Bot Initialized in {float("{:.2f}".format(time.time()-tnew))} secs')
tnew = time.time()
devs = [669816890163724288, 771601176155783198]
staff = [669816890163724288, 771601176155783198, 619377929951903754, 713056818972066140, 517402093066256404, 459350068877852683]
disregarded = []
embedcolor = 3407822

support_server = 'https://discord.gg/aMqWWTunrJ'
patreon_page = 'https://www.patreon.com/ThunderGameBot'
invite_url = 'https://discord.com/api/oauth2/authorize?client_id=832083717417074689&permissions=392256&scope=bot'
bank_details = {
    1: {"name":'Common Finance Bank Ltd.', "rate":3, "tier":"III"},
    2: {"name":'National Bank Pvt. Ltd.', "rate":5, "tier":"II"},
    3: {"name":'International Bank of Finance Ltd.', "rate":7, "tier":"I"}
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
bot.help_json = {}
bot.phrases = {}
bot.current_stock = []
bot.total_lines = 0
bot.pfp = ''
bot.shopc = {}
bot.items = {}
bot.emotes = {}
bot.unboxbgs = {}
bot.allitems = {}
bot.cachedinv = {}
bot.used = {}
bot.ms = {}
bot.activems = {"users":[]}
bot.waitings = {}
bot.status = []
bot.random_status = True

usercmds = {}
stock_names = ['Ava', 'Neil', 'Ryan', 'Anthony', 'Bernadette', 'Lauren', 'Justin', 'Matt', 'Wanda', 'James', 'Emily', 'Vanessa', 'Carl', 'Fiona', 'Stephanie', 'Pippa', 'Phil', 'Carol', 'Liam', 'Michael', 'Ella', 'Amanda', 'Caroline', 'Nicola', 'Sean', 'Oliver', 'Kylie', 'Rachel', 'Leonard', 'Julian', 'Richard', 'Peter', 'Irene', 'Dominic', 'Connor', 'Dorothy', 'Gavin', 'Isaac', 'Karen', 'Kimberly', 'Abigail', 'Yvonne', 'Steven', 'Felicity', 'Evan', 'Bella', 'Alison', 'Diane', 'Joan', 'Jan', 'Wendy', 'Nathan', 'Molly', 'Charles', 'Victor', 'Sally', 'Rose', 'Robert', 'Claire', 'Theresa', 'Grace', 'Keith', 'Stewart', 'Andrea', 'Alexander', 'Chloe', 'Nicholas', 'Edward', 'Deirdre', 'Anne', 'Joseph', 'Alan', 'Rebecca', 'Jane', 'Natalie', 'Cameron', 'Owen', 'Eric', 'Gabrielle', 'Sonia', 'Tim', 'Sarah', 'Madeleine', 'Megan', 'Lucas', 'Joe', 'Brandon', 'Brian', 'Jennifer', 'Alexandra', 'Adrian', 'John', 'Mary', 'Tracey', 'Jasmine', 'Penelope', 'Hannah', 'Thomas', 'Angela', 'Warren', 'Blake', 'Simon', 'Audrey', 'Frank', 'Samantha', 'Dan', 'Victoria', 'Paul', 'Jacob', 'Heather', 'Una', 'Lily', 'Carolyn', 'Jonathan', 'Ian', 'Piers', 'William', 'Gordon', 'Dylan', 'Olivia', 'Jake', 'Leah', 'Jessica', 'David', 'Katherine', 'Amelia', 'Benjamin', 'Boris', 'Sebastian', 'Lisa', 'Diana', 'Michelle', 'Emma', 'Sam', 'Stephen', 'Faith', 'Kevin', 'Austin', 'Jack', 'Ruth', 'Colin', 'Trevor', 'Joanne', 'Virginia', 'Anna', 'Max', 'Adam', 'Maria', 'Sophie', 'Sue', 'Andrew', 'Harry', 'Amy', 'Christopher', 'Donna', 'Melanie', 'Elizabeth', 'Lillian', 'Julia', 'Christian', 'Luke', 'Zoe', 'Joshua', 'Jason']
xp_timeout = []
warn1 = []
warn2 = []
storeitems = []
error_embed = 16290332
success_embed = 2293571
economysuccess = '<a:EconomySuccess:843499891522797568>'
economyerror = '<a:EconomyError:843499981695746098>'


def is_dev(ctx):
    return ctx.author.id in devs

def is_staff(ctx):
    return ctx.author.id in staff

def cache_allitems():
    t = time.time()
    bot.allitems = {}
    for i in bot.items.keys():
        mychest = i
        for j in bot.items[i]["items"]:
            item_name = j["name"]
            item = Image.open(f'items/{item_name}.png').resize((225, 225))
            y = 60
            degree = 5
            bgdegree = 0
            frames = {}
            font = ImageFont.truetype('badges/font2.ttf', 35)

            def addframe(i, y, bgdegree):
                bg = bot.unboxbgs[mychest][i]
                frame = Image.new('RGBA', (850, 450))
                frame.paste(bg, (0, 0), bg.convert('RGBA'))
                frame.paste(item, (300, int(y)), item.convert('RGBA'))
                draw = ImageDraw.Draw(frame)
                draw.text((425 - (font.getsize(item_name)[0] / 2), 300), item_name, font=font, stroke_width=5,
                          stroke_fill=(0, 0, 0))
                obj = BytesIO()
                frame.save(obj, 'PNG')
                frame = Image.open(obj)
                frames[i] = frame

            for i in range(20):
                first = threading.Thread(target=addframe, args=(i, y, bgdegree,))
                first.start()
                y -= 1.5
                bgdegree -= 2.3077

            for i in range(20, 40):
                second = threading.Thread(target=addframe, args=(i, y, bgdegree,))
                second.start()
                y += 1.5
                bgdegree -= 2.3077
                second.join()

            allframes = []
            for i in range(40):
                allframes.append(frames[i])
            unbox_gif = BytesIO()
            allframes[0].save(unbox_gif,
                              format='GIF',
                              save_all=True,
                              append_images=allframes[1:],
                              duration=75,
                              loop=0)
            unbox_gif.seek(0)
            file = discord.File(fp=unbox_gif, filename='unboxing.gif')
            bot.allitems[item_name] = unbox_gif
            print(f'{item_name} cached successfully!')
    print(f'All {len(bot.allitems.keys())} items cached successfully in {time.time() - t} secs')

async def spam_protect(userid):
    if userid in disregarded:
        if userid not in devs: return 'return'
        else: return 'ok'
    last = usercmds.get(userid, 0)
    current = time.time()
    usercmds[userid] = current
    if current - last < 2:
        if userid in warn2:
            asyncio.create_task(handle_disregard(userid))
            return 'disregard'
        elif userid in warn1:
            asyncio.create_task(handle_2(userid))
            return 'warn'
        else:
            asyncio.create_task(handle_1(userid))
            return 'warn'
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
    with open('files/average.json', 'r') as avg:
        return json.load(avg)

async def get_admin():
    with open('files/admin.json', 'r') as f:
        return json.load(f)

async def close_admin(a):
    with open('files/admin.json', 'w') as f:
        f.write(json.dumps(a, indent=2))

async def get_estates():
    with open('files/estates.json', 'r') as f:
        return json.load(f)

async def get_alert_info():
    with open('files/alerts.json', 'r') as a:
        return json.load(a)

async def get_data():
    with open('files/accounts.json', 'r') as f:
        data = f
        if data == '{}':
            return {1:1}
        else:
            return json.load(data)

async def get_stockconfigs():
    with open('files/stock_config.json', 'r') as stc:
        return json.load(stc)

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
    with open('files/xp.json', 'r') as xp:
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
    with open('files/statements.json', 'r') as s:
        return json.load(s)

async def get_stocks():
    with open('files/stocks.json', 'r') as s:
        return json.load(s)

async def get_badges():
    with open('files/badges.json', 'r') as b:
        return json.load(b)

async def get_data_stock(file):
    with open(f'stocks/{file}', 'r') as f:
        return list(csv.reader(f))

async def get_url(url):
    a = requests.get(url)
    return a.content

async def get_inv():
    with open('files/inventory.json', 'r') as e:
        return json.load(e)

async def update_inv(a):
    with open('files/inventory.json', 'w') as e:
        e.write(json.dumps(a, indent=2))

async def update_stockinfo(data):
    with open('files/stock_config.json', 'w') as stc:
        stc.write(json.dumps(data, indent=2))

async def update_stock_data(data):
    with open('files/stocks.json', 'w') as avgbal:
        avgbal.write(json.dumps(data, indent=2))

async def update_badges(data):
    with open('files/badges.json', 'w') as b:
        b.write(json.dumps(data, indent=2))

async def update_avg(avg):
    with open('files/average.json', 'w') as avgbal:
        avgbal.write(json.dumps(avg, indent=2))

async def update_est(data):
    with open('files/estates.json', 'w') as f:
        f.write(json.dumps(data, indent=2))

async def update_alerts(data):
    with open('files/alerts.json', 'w') as f:
        f.write(json.dumps(data, indent=2))

async def update_logs(stuff: str):
    with open('files/logs.txt', 'a') as logs:
        logs.write(f'\n{stuff}')

async def update_data(data):
    with open('files/accounts.json', 'w') as f:
        f.write(str(json.dumps(data, indent=2)))

async def update_statements(stat):
    with open('files/statements.json', 'w') as w:
        w.write(json.dumps(stat, indent=2))

async def update_xp(data):
    with open('files/xp.json', 'w') as w:
        w.write(json.dumps(data, indent=2))

async def update_sorted_inv(userid):
    inv = await get_inv()
    userinv = inv.get(userid)
    if userinv is None:
        bot.cachedinv[userid] = ()
        return "userinv"
    itemsinv = userinv.get("items")
    embed = discord.Embed(color=embedcolor)
    if itemsinv is None:
        bot.cachedinv[userid] = ()
        return "itemsinv"

    done = []
    for items in userinv["items"]:
        done.append(items)
    invdict = {}
    for i in set(done):
        invdict[i] = done.count(i)
    bot.cachedinv[userid] = sorted(invdict.items(), key=lambda x: x[1], reverse=True)
    return bot.cachedinv[userid]

async def clear_dues():
    data = await get_data()
    stock_data = await get_stocks()

    for i in stock_data:
        person = data[str(i)]
        value = stock_data[str(i)]
        if value == 0:
            continue
        current_price = int(bot.current_stock[-1][5])

        bulk = int(current_price*value)
        person['bank'] += bulk
        data[str(i)] = person
        stock_data[str(i)] = 0
        user = bot.get_user(i)
        if user is None:
            continue
        embed = discord.Embed(title='Stock Ended', description=f'The current stock ended and `{await commait(bulk)}` coins have been added to your bank.')
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_author(name=f'{user.name}', icon_url=user.avatar_url)
        embed.set_footer(text='Economy Bot', icon_url=bot.pfp)
        await user.send(embed=embed)
        await create_statement(user, bot.user, bulk, f"Sold {value} Stocks", "Credit")

    await update_data(data)
    await update_stock_data(stock_data)
    with open('files/stock_config.json', 'w') as stc:
        stc.write('{}')
    with open('files/stocks.json', 'w') as stc:
        stc.write('{}')

async def update_stocks():
    stock = await get_todays_stock()
    with open(f'stocks/{stock}', 'r') as st:
        data = list(csv.reader(st))
    bot.total_lines = len(data)

    config = await get_stockconfigs()
    line = config.setdefault("line", 1)
    name = config.setdefault("name", random.choice(stock_names))
    if line == bot.total_lines:
        os.rename(f'stocks/{stock}', f'stocks/{str(stock).replace("_today", "_done")}')
        config['line'] = line + 1
        await update_stockinfo(config)
        await clear_dues()
        await update_stocks()
    else:
        config['line'] = line + 1
        await update_stockinfo(config)

        bot.current_stock = list(data[line])
        bot.current_stock.pop(0)
        bot.current_stock.pop(0)

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
                embed.set_footer(text='Economy Bot', icon_url=bot.pfp)

                persona['last'] = cur
                aler[str(i)] = persona
                await update_alerts(aler)
                await fetched.send(embed=embed)

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

    await update_avg(avgbal)

async def stock_update():
    while True:
        await update_stocks()
        await perform_stuff(bot.current_stock)
        await asyncio.sleep(86400/bot.total_lines)

async def check_storetime():
    with open('files/bot_data.json', 'r') as c:
        config = json.load(c)
    return config["shop"]["updated"]

async def shop_update():
    with open('files/bot_data.json', 'r') as c:
        alldata = json.load(c)
    config = alldata["shop"]
    ct = time.time()
    if ct - config["updated"] < 86400: return
    for i in range(len(storeitems)):
        storeitems.pop(0)
    await load_shop()
    for i in storeitems:
        i["special"] = False
    storetime = config["updated"]
    newitem = random.choice(storeitems)
    storeitems.remove(newitem)
    newitem["special"] = True
    disc = int(newitem["price"].replace(",", ""))
    percent = random.randint(10, 50)
    newitem["disc"] = await commait(int(disc*(100-percent)/100))
    newitem["percent"] = percent
    storeitems.append(newitem)
    config['updated'] = ct
    config['value'] = storeitems
    alldata["shop"] = config
    with open('files/bot_data.json', 'w') as c:
        c.write(json.dumps(alldata, indent=2))

async def loops():
    while True:
        await avg_update()
        await est_update()
        await shop_update()
        await asyncio.sleep(300)

async def open_account(userid):
    data = await get_data()
    if data.get(str(userid)) is None:
        data[userid] = {'bank_type':1, 'wallet':0, 'bank':1000}
        await update_data(data)

async def open_estates(userid):
    data = await get_estates()
    if data.get(str(userid)) is None:
        user = bot.get_user(userid)
        data[f'{userid}'] = {'level':1, 'name':f'{user.name}', 'lm':time.time(), 'lr':time.time(), 'p':0, 'c':0}

    await update_est(data)

async def checktimeout(userid, event):
    with open('files/timeouts.json', 'r') as t:
        timeouts = json.load(t)
    userid = f'{userid}'
    if userid not in timeouts:
        return 0
    person = timeouts[userid]
    event_t = person.get(event)

    current = time.time()
    return current - event_t

async def add_timeout(userid, event):
    with open('files/timeouts.json', 'r') as f:
        data = json.load(f)

    person = data.get(f'{userid}', {})
    person[event] = time.time()

    data[str(userid)] = person
    with open('files/timeouts.json', 'w') as f:
        f.write(json.dumps(data, indent=2))

async def alerts_state(userid, state:str):
    aler = await get_alert_info()
    userid = str(userid)
    person = aler.get(userid)
    if person is None:
        person = {'state':0, 'last':0}

    person['state'] = state
    aler[userid] = person

    await update_alerts(aler)

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

async def load_shop():
    with open('files/bot_data.json', 'r') as s:
        config = json.load(s)
    for i in config["shop"]["value"]:
        storeitems.append(i)

async def bot_status():
    raw_status = ""
    while True:
        if not bot.random_status: break
        current_status = random.choice(bot.status)
        if current_status["status"] == raw_status: continue
        guilds = len(bot.guilds)
        users = 0
        for i in bot.guilds: users += len(i.members)

        s_type = current_status["type"]
        raw_status = current_status["status"]
        s_status = raw_status.format(users=await commait(users), guilds=await commait(guilds))
        if s_type == "p":
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=s_status))
        elif s_type == "w":
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=s_status))
        elif s_type == "l":
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=s_status))

        await asyncio.sleep(720)

async def create_stuff():
    tnew = time.time()
    mybot = bot.get_user(832083717417074689)
    bot.pfp = mybot.avatar_url
    tnew = time.time()
    #await bot.change_presence(status=discord.Status.invisible)
    await load_shop()
    await refresh()
    await bot_status()
    print(f'Data Loaded and Activity set in {float("{:.2f}".format(time.time() - tnew))} secs')
    asyncio.create_task(loops())
    asyncio.create_task(stock_update())
    print(f'Loops created! Boot Time: {float("{:.2f}".format(time.time()-t1))} secs')

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
    stock_data = await get_stockconfigs()
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
    await update_stockinfo(stock_data)

    return stock_data

async def get_avatar(user):
    return Image.open(BytesIO(await user.avatar_url_as(format="png").read())).resize((140, 140))

async def make_lvl_img(member, level, xp, total_xp, guildid):
    font = ImageFont.truetype("badges/font2.ttf", 19)
    font_rank = ImageFont.truetype("badges/font2.ttf", 24)
    fontm = ImageFont.truetype("badges/font2.ttf", 13)
    fonts = ImageFont.truetype("badges/font2.ttf", 10)

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
        staff_icon.close()
        location -= 45
    if patron:
        patron_icon = Image.open('badges/patron.png')
        patron_icon = patron_icon.resize((37, 37))
        img.paste(patron_icon, (location, 55), patron_icon)
        patron_icon.close()
        location -= 45
    server_r, global_r = await xp_ranks(member.id, guildid)
    if global_r > 1000:
        global_r = 'Unknown'
    else:
        global_r = f'#{global_r}'
    draw = ImageDraw.Draw(img)
    newimg = Image.new('RGBA', img.size, (0,0,0,0))
    newdraw = ImageDraw.Draw(newimg)

    newdraw.text((180, 34), f'{member.name}#{member.discriminator}', font=font, fill='#000000')
    newdraw.text((180, 70), f"Level {level}", font=fontm, fill='#000000')
    newdraw.text((120, 210), f'Server Rank', font=font, fill='#000000')
    newdraw.text((530, 210), f'Global Rank', font=font, fill='#000000')
    newdraw.text((120, 250), f'#{server_r}', font=font_rank, fill='#000000')
    newdraw.text((530, 250), f'{global_r}', font=font_rank, fill='#000000')

    newimg = newimg.filter(ImageFilter.GaussianBlur(radius=2))
    newimg = newimg.filter(ImageFilter.GaussianBlur(radius=4))
    img.paste(newimg, (0, 0), newimg)

    draw.text((180, 34), f'{member.name}#{member.discriminator}', (255, 255, 255), font=font)
    draw.text((180, 70), f"Level {level}", (255, 255, 255), font=fontm)
    draw.text((120, 210), f'Server Rank', font=font)
    draw.text((530, 210), f'Global Rank', font=font)
    draw.text((120, 250), f'#{server_r}', (255, 243, 0), font=font_rank)
    draw.text((530, 250), f'{global_r}', (255, 243, 0), font=font_rank)

    twidth, theight = draw.textsize(f"{await commait(xp)}/{await commait(total_xp)}", fonts)
    draw.text((468 - (twidth / 2), 121 - (theight / 2)), f"{await commait(xp)}/{await commait(total_xp)}", (255, 255, 255), font=fonts, stroke_width=1, stroke_fill=(0, 0, 0))

    invdata = await get_inv()
    userinv = invdata.get(str(member.id), [])
    if len(userinv) != 0:
        eq_lock = userinv.get('eq_lock')
        eq_boost = userinv.get('eq_boost')
        paste_loc = 302
        if eq_lock is not None:
            for i in storeitems:
                if eq_lock == i["name"]:
                    lock = Image.open(f'store/{i["icon"]}').resize((30, 30))
                    img.paste(lock, (paste_loc, 140), lock.convert('RGBA'))
                    lock.close()
        if eq_boost is not None:
            for i in storeitems:
                if eq_lock == i["name"]:
                    lock = Image.open(i["icon"]).resize((40, 40))
                    img.paste(lock, (260, 135), lock.convert('RGBA'))
                    lock.close()
        if eq_lock is None and eq_boost is None:
            draw.text((306, 150), 'None', font=ImageFont.truetype("badges/font2.ttf", 16))
    else:
        draw.text((306, 150), 'None', font=ImageFont.truetype("badges/font2.ttf", 16))
    enhancer = ImageEnhance.Sharpness(img)
    img = enhancer.enhance(2)
    image_bytes = BytesIO()
    img.save(image_bytes, 'PNG')
    img.close()
    ava_mask.close()
    ava_mask2.close()
    status.close()
    xpbar.close()
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

async def get_errorfile():
    with open('files/errors.json', 'r') as f:
        return json.load(f)

async def inv_components(userid, user_page_orignal, rarity):
    user_page = (user_page_orignal - 1) * 6
    components = []
    sorted_inv = await update_sorted_inv(userid)
    item_count = 0
    while True:
        try:
            current_item = sorted_inv[user_page][0]
        except:
            break
        for i in bot.items.keys():
            if rarity is not None:
                i = rarity
            for j in bot.items[i]["items"]:
                if j["name"] == current_item:
                    if item_count == 5: break
                    itemname = j['name']
                    if i == "common":
                        rarity_emoji = 847687974414319626
                    elif i == "rare":
                        rarity_emoji = 847687973202165841
                    else:
                        rarity_emoji = 847687925596160002
                    emoji = j["emoji"].split(':')[-1].replace('>', '')
                    qty_userhas = sorted_inv[user_page][1]
                    name = Button(style=ButtonStyle.green, label=itemname,
                                  emoji=bot.get_emoji(int(emoji)), id="info")
                    rarity_qty = Button(style=ButtonStyle.grey, label=str(qty_userhas) + "x",
                                        emoji=bot.get_emoji(rarity_emoji))
                    components.append([rarity_qty, name])
                    item_count += 1
                    user_page += 1
            if rarity is not None:
                user_page+=1
                break
            if item_count == 5: break
        if item_count == 5: break
    return components

async def update_errorfile(a):
    with open('files/errors.json', 'w') as f:
        f.write(json.dumps(a, indent=2))

async def debugcode(code, error):
    a = await get_errorfile()
    if code in a:
        return False
    a[code] = error
    await update_errorfile(a)
    return True

async def createstore(start, page):
    storetime = await check_storetime()
    storetime = 86400 - time.time() + storetime
    frame = Image.open('store/frame.png')
    title = ImageFont.truetype("badges/font2.ttf", 22)
    special = ImageFont.truetype("badges/font2.ttf", 25)
    description = ImageFont.truetype("badges/font2.ttf", 17)
    newimg = Image.new('RGBA', frame.size, (0, 0, 0, 0))
    newdraw = ImageDraw.Draw(newimg, mode="RGBA")
    newdraw.fontmode = "1"
    special_item = {}
    left = datetime.timedelta(seconds=storetime)
    final = datetime.datetime.strptime(str(left), '%H:%M:%S.%f').replace(microsecond=0)
    colon_format = str(final).split(" ")[1].split(':')
    for i in storeitems:
        if i["special"]:
            special_item = i
    price_sp = special_item["price"]
    text_loc = 267
    icon_loc = 258
    desc_loc = 270
    allpages=0
    leng = len(storeitems)
    while True:
        allpages += 1
        leng -= 8
        if leng < 0: break
    for i in range(start, page):
        if i > len(storeitems) - 1: break
        item = storeitems[i]
        if item["special"]: continue
        newdraw.text((135, text_loc), text=item['name'], fill=(0, 0, 0), font=title)
        newdraw.text((145 + title.getsize(item["name"])[0], desc_loc), text=item['desc'], fill=(0, 0, 0),
                  font=description)
        newdraw.text((800, text_loc), text=item['price'], fill=(0, 0, 0), font=title)

        text_loc += 62
        desc_loc += 62
        icon_loc += 61
    newdraw.text((210, 90), f'{special_item["name"]}', font=special, fill=(0,0,0))
    newdraw.text((210, 130), f'{special_item["desc"]}', font=description, fill=(0,0,0))
    newdraw.text((73, 694), f'Refreshes in: {colon_format[0]}h {colon_format[1]}m {colon_format[2]}s', fill=(0, 0, 0),
              font=ImageFont.truetype("badges/font2.ttf", 20))
    newdraw.text((800, 694), f'Page #{int(page/8)}/{allpages}', font=ImageFont.truetype("badges/font2.ttf", 20), fill=(0, 0, 0))
    newdraw.text((700, 90), price_sp, font=title, fill=(0,0,0))
    newdraw.text((715+title.getsize(price_sp)[0], 90),
              special_item["disc"], font=ImageFont.truetype("badges/font2.ttf", 30), fill=(0,0,0))
    newdraw.text((700, 139), f'{special_item["percent"]}% DISCOUNT!', font=ImageFont.truetype("badges/font2.ttf", 20),
              fill=(0,0,0))

    newimg = newimg.filter(ImageFilter.GaussianBlur(radius=2))
    newimg = newimg.filter(ImageFilter.GaussianBlur(radius=4))
    #frame.paste(newimg, (0, 0), newimg)
    frame = Image.alpha_composite(frame, newimg)
    draw = ImageDraw.Draw(frame, mode="RGBA")
    draw.fontmode = "1"
    draw.text((210, 90), f'{special_item["name"]}', font=special)
    draw.text((210, 130), f'{special_item["desc"]}', font=description, fill=(189, 189, 189))
    draw.text((700, 90), price_sp, font=title, fill=(189, 189, 189))
    draw.line((698, 100, 699+title.getsize(price_sp)[0], 100), width=6, fill=(255, 91, 91))
    draw.text((715+title.getsize(price_sp)[0], 90), special_item["disc"], font=ImageFont.truetype("badges/font2.ttf", 30))
    draw.text((700, 139), f'{special_item["percent"]}% DISCOUNT!', font=ImageFont.truetype("badges/font2.ttf", 20), fill=(255,100,69))
    icon = Image.open(f'store/{special_item["icon"]}').resize((50, 50))
    frame.paste(icon, (140, 100), icon.convert('RGBA'))
    icon.close()
    text_loc=267
    icon_loc=258
    desc_loc=270
    for i in range(start, page):
        if i > len(storeitems)-1: break
        item = storeitems[i]
        if item["special"]: continue
        icon = Image.open(f'store/{item["icon"]}').resize((40, 40))
        frame.paste(icon, (71, icon_loc), icon.convert('RGBA'))
        draw.text((135, text_loc), text=item['name'], fill=(255, 255, 255), font=title)
        draw.text((145+title.getsize(item["name"])[0], desc_loc), text=item['desc'], fill=(189, 189, 189), font=description)
        draw.text((800, text_loc), text=item['price'], fill=(255, 255, 255), font=title)
        icon.close()
        text_loc += 62
        desc_loc += 62
        icon_loc += 61
    draw.text((73, 694), f'Refreshes in: {colon_format[0]}h {colon_format[1]}m {colon_format[2]}s', fill=(61, 255, 48), font=ImageFont.truetype("badges/font2.ttf", 20))
    draw.text((800, 694), f'Page #{int(page/8)}/{allpages}', font=ImageFont.truetype("badges/font2.ttf", 20), fill=(61, 255, 48))
    enhancer = ImageEnhance.Sharpness(frame)
    frame = enhancer.enhance(2)
    image_bytes = BytesIO()
    frame.save(image_bytes, 'PNG')
    image_bytes.seek(0)
    frame.close()
    return discord.File(fp=image_bytes, filename='store.png')

async def inventory_image(userid):
    userid = str(userid)
    invdata = await get_inv()
    userinv = invdata.get(userid, {"inv":[]})
    userinv = userinv["inv"]
    heading = ImageFont.truetype("badges/font2.ttf", 32)
    inv_font = ImageFont.truetype("badges/font2.ttf", 18)
    bg = Image.open('store/bg.png')
    newimg = Image.new('RGBA', bg.size)
    newdraw = ImageDraw.Draw(newimg)
    inv = {}
    empty = False
    if len(userinv) == 0:
        empty = True
    else:
        for i in userinv:
            qty = inv.setdefault(i, 0)
            inv[i] = qty + 1

    if empty:
        newdraw.text((270, 146), '-- Empty Inventory --', font=inv_font, fill=(0,0,0))
        newimg = newimg.crop((0, 0, newimg.width, 200))
        newimg = newimg.filter(ImageFilter.GaussianBlur(radius=2))
        newimg = newimg.filter(ImageFilter.GaussianBlur(radius=4))
        bg = bg.crop((0, 0, bg.width, 200))
        bg = Image.alpha_composite(bg.convert('RGBA'), newimg)

        draw = ImageDraw.Draw(bg)
        draw.line((47, 133, 47, 183), (149, 149, 149), width=5)
        draw.line((752, 133, 752, 183), (149, 149, 149), width=5)
        draw.line((46, 181, 753, 181), (149, 149, 149), width=5)
        draw.text((270, 146), '-- Empty Inventory --', font=inv_font)
    else:
        item_loc = 146
        for i in inv:
            newdraw.text((120, item_loc), i, font=inv_font, fill=(0, 0, 0))
            newdraw.text((558+(int(194-inv_font.getsize(f'{inv[i]}')[0])/2), item_loc), f'{inv[i]}', font=inv_font, fill=(0, 0, 0))
            item_loc += 43
        newimg = newimg.crop((0, 0, newimg.width, item_loc+10))
        newimg = newimg.filter(ImageFilter.GaussianBlur(radius=2))
        newimg = newimg.filter(ImageFilter.GaussianBlur(radius=4))
        bg = bg.crop((0, 0, bg.width, item_loc+10))
        bg = Image.alpha_composite(bg.convert('RGBA'), newimg)

        draw = ImageDraw.Draw(bg)
        line_loc = 133
        item_loc = 146
        for i in inv:
            icon_name = 'undefined.png'
            for j in storeitems:
                if j["name"] == i: icon_name = j["icon"]
            icon = Image.open(f'store/{icon_name}').resize((35, 35))
            bg.paste(icon, (55, item_loc-5), icon.convert('RGBA'))

            draw.line((47, line_loc, 47, line_loc+50), (149, 149, 149), width=5)
            draw.line((752, line_loc, 752, line_loc+50), (149, 149, 149), width=5)
            draw.line((98, line_loc, 98, line_loc + 50), (149, 149, 149), width=5)
            draw.line((558, line_loc, 558, line_loc + 50), (149, 149, 149), width=5)

            draw.text((120, item_loc), i, font=inv_font)
            draw.text((558+(int(194-inv_font.getsize(f'{inv[i]}')[0])/2), item_loc), f'{inv[i]}', font=inv_font)
            icon.close()
            item_loc += 43
            line_loc += 43
        draw.line((46, line_loc+5, 753, line_loc+5), (149, 149, 149), width=5)

    enhancer = ImageEnhance.Sharpness(bg)
    bg = enhancer.enhance(2)
    image_bytes = BytesIO()
    bg.save(image_bytes, 'PNG')
    image_bytes.seek(0)
    bg.close()
    return discord.File(fp=image_bytes, filename='inventory.png')

@bot.command(aliases=["ms", "mine"], pass_context=True, invoke_without_command=True)
async def minesweeper(ctx):
    bomb_count = random.randint(5, 10)
    mainlist = ["empty" for i in range(25)]

    for i in range(bomb_count):
        while True:
            getrand = random.randint(0, 24)
            check = mainlist[getrand]
            if check == "empty":
                break
            if "bomb" not in mainlist:
                break
        mainlist.insert(getrand, "bomb")
        mainlist.pop(getrand + 1)

    rows = []
    minesweeper = []
    count = 0

    for i in range(len(mainlist)):
        rows.append(mainlist[i])
        count += 1
        if count == 5:
            minesweeper.append(rows)
            rows = []
            count = 0

    count_row = []
    count_sweeper = []
    final_count = 0
    for i in range(len(minesweeper)):
        row = minesweeper[i]
        if i != 0:
            behind = minesweeper[i - 1]
        else:
            behind = ["empty" for i in range(5)]
        if i != 4:
            after = minesweeper[i + 1]
        else:
            after = ["empty" for i in range(5)]

        for item in range(len(row)):
            if item == 0:
                a1 = "empty"
                b1 = "empty"
                c1 = "empty"
            else:
                a1 = behind[item - 1]
                b1 = row[item - 1]
                c1 = after[item - 1]

            if item == 4:
                a3 = "empty"
                b3 = "empty"
                c3 = "empty"
            else:
                a3 = behind[item + 1]
                b3 = row[item + 1]
                c3 = after[item + 1]

            a2 = behind[item]
            b2 = row[item]
            c2 = after[item]

            count_list = [x for x in [a1, a2, a3, b1, b2, b3, c1, c2, c3] if x == "bomb"]
            itemtype = len(count_list)
            count_row.append(itemtype)
            final_count += 1
            if final_count == 5:
                count_sweeper.append(count_row)
                count_row = []
                final_count = 0
    bot.ms[ctx.author.id] = {"main":minesweeper, "count":count_sweeper}
    await start_ms(ctx)

async def start_ms(ctx):
    ifactive = ctx.author.id in bot.activems["users"]
    if ifactive:
        a = await ctx.send(f"You have already started a game earlier, please finish it.\n"
                       f"If you want to discard that for `5,000` coins and start again, react with {economysuccess}")
        await a.add_reaction(economysuccess)
        def check(reaction, user):
            if user == ctx.author and str(reaction.emoji) in [economysuccess]:
                return True

        try:
            reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)
            net = -5000
            bot.activems["users"].remove(ctx.author.id)
        except:
            return
    else:
        net = 0
    components = []
    back_rows = []
    count=0
    for i in bot.ms[ctx.author.id]["main"]:
        for j in i:
            btn = Button(style=ButtonStyle.grey, label="\u200b", id=f'{j}_{count}')
            back_rows.append(btn)
            count += 1
        components.append(back_rows)
        back_rows = []
    minemsg = await ctx.send("**Welcome to Minesweeper!**\n"
                   "Rules:\n"
                   "> For each correct move, you get `1,000` coins\n"
                   "> For each incorrect move, `2,000` coins are taken away!\n"
                   "> Your aim is to click on blocks avoiding any bombs. All the best!\n"
                   f"`Note:` To end the game, react with {economyerror}\n\n"
                   "Total Moves: `0`    Correct: `0`    Incorrect: `0`\n"
                   f"Net Profit: `{net}`\n"
                   "Here is your board:", components=components)
    await minemsg.add_reaction(economyerror)
    bot.activems["users"].append(ctx.author.id)
    moves = 0
    correct = 0
    wrong = 0

    bot.activems[minemsg.id] = (minemsg, ctx, net)
    while True:
        res = await bot.wait_for("button_click")
        if res.user.id != ctx.author.id or res.message.id != minemsg.id:
            continue

        btnid = str(res.component.id).split('_')
        pos = int(btnid[1])
        typ = btnid[0]
        moves += 1

        getbtn = 0
        getrow = []
        prec = res.message.components
        change = prec[pos]
        emojisetter = {
            0: "0\N{variation selector-16}\N{combining enclosing keycap}",
            1: "1\N{variation selector-16}\N{combining enclosing keycap}",
            2: "2\N{variation selector-16}\N{combining enclosing keycap}",
            3: "3\N{variation selector-16}\N{combining enclosing keycap}",
            4: "4\N{variation selector-16}\N{combining enclosing keycap}",
            5: "5\N{variation selector-16}\N{combining enclosing keycap}",
            6: "6\N{variation selector-16}\N{combining enclosing keycap}",
            7: "7\N{variation selector-16}\N{combining enclosing keycap}",
            8: "8\N{variation selector-16}\N{combining enclosing keycap}"
        }
        if typ == "bomb":
            wrong += 1
            net -= 2000
            change.emoji = "💣"
            change.style = ButtonStyle.red
        else:
            correct += 1
            net += 1000
            cc = 0
            done = False
            for i in bot.ms[ctx.author.id]["count"]:
                if done: break
                for nxt in i:
                    if pos == cc:
                        change.emoji = emojisetter[nxt]
                        change.style = ButtonStyle.green
                        done = True
                    else: cc += 1
                    if done: break

        change.disabled = True
        prec.pop(pos)
        prec.insert(pos, change)

        fcom = []
        for i in prec:
            getrow.append(i)
            getbtn += 1

            if getbtn == 5:
                fcom.append(getrow)
                getrow = []
                getbtn = 0
        cntn = f"Total Moves: `{moves}`    Correct: `{correct}`    Incorrect: `{wrong}`\n" \
               f"Net Profit: `{net}`\n"
        bot.activems[minemsg.id] = (minemsg, ctx,  net)
        if moves == 25:
            await stop_ms(minemsg, ctx, net)
            break
        else:
            await res.respond(type=InteractionType.UpdateMessage, content=cntn, components=fcom)

async def stop_ms(minemsg, ctx, net):
    data = await get_data()
    user = data[str(ctx.author.id)]
    user["wallet"] += net
    data[str(ctx.author.id)] = user
    await update_data(data)
    bot.activems["users"].remove(ctx.author.id)
    await minemsg.edit(content=f"**The game ended**\nNet Profit: `{await commait(net)}`", components=[])
    await minemsg.clear_reactions()

async def general_checks_loop(ctx):
    state = await spam_protect(ctx.author.id)
    toreturn = True
    if state == 'warn':
        embed = discord.Embed(title=f'{economyerror} Using commands too fast!', color=error_embed)
        await ctx.send(embed=embed)
        toreturn = False
    elif state == 'disregard':
        embed = discord.Embed(title=f'{economyerror} Warning!',
                              description=f'{ctx.author.mention} has been disregarded for 10 mins!\n**Reason: Spamming Commands**',
                              color=error_embed)
        await ctx.send(embed=embed)
        toreturn= False
    elif state == 'return':
        toreturn= False
    if ctx.author.id not in xp_timeout:
        userid = ctx.author.id
        xps = await get_xp()
        xp = xps.setdefault(f'{userid}', 0)
        togive = random.randint(10, 25)
        xps[str(userid)] = xp + togive
        asyncio.create_task(update_xp(xps))
        asyncio.create_task(add_xp_tm(userid))
    return toreturn

@bot.command(aliases=["ttt"])
async def tictactoe(ctx, user:discord.Member, bet:int=100):
    if user == ctx.author:
        return await ctx.send("Bruh you cant start a game with yourself")
    if bet not in [100, 200, 500, 1000, 2500, 5000, 10000]:
        return await ctx.send(f"The betting amount should be {', '.join(str(x) for x in [100, 250, 200, 500, 1000, 2000, 2500, 5000, 10000])} "
                              f"or 20000")
    bot.waitings[ctx.author.id] = [ctx.author, user]

    cont = f"{ctx.author.mention} vs {user.mention}\n" \
           f"Bet Amount: `{await commait(bet)}`\n" \
           f"Click 'Accept' to start. Waiting on: {' '.join([x.mention for x in bot.waitings[ctx.author.id]])}"
    pre = await ctx.send(cont, components=[Button(label='Accept', style=ButtonStyle.green)])
    data = await get_data()
    started = False
    while True:
        res = await bot.wait_for("button_click")
        if res.user not in [ctx.author, user]: continue
        if res.user in bot.waitings[ctx.author.id]:
            per = data[str(user.id)]
            p = per["wallet"]
            if p < bet:
                cont = f"{user.mention} doesn't have enough coins!"
                compo = []
            else:
                per["wallet"] -= bet
                data[str(user.id)] = per
                await update_data(data)

                bot.waitings[ctx.author.id].remove(res.user)
                cont = f"{ctx.author.mention} vs {user.mention}\n" \
                       f"Bet Amount: `{await commait(bet)}`\n" \
                       f"Click 'Accept' to start. Waiting on: {' '.join([x.mention for x in bot.waitings[ctx.author.id]])}"
                compo = [Button(label='Accept', style=ButtonStyle.green)]
            await res.respond(type=7, content=cont, components=compo)
        else:
            await res.respond(type=InteractionType.DeferredUpdateMessage)

        if len(bot.waitings[ctx.author.id]) == 0:
            await pre.delete()
            started = True
            break

    if started:
        board = {1: "", 2: "", 3: "",
                 4: "", 5: "", 6: "",
                 7: "", 8: "", 9: ""}
        row = []
        cont = []
        c = 0
        for i in range(1, 10):
            row.append(Button(style=2, label="\u200b", id=i))
            c += 1
            if c == 3:
                cont.append(row)
                row = []
                c = 0
        turn = random.choice([ctx.author, user])
        msg = await ctx.send(f"{turn.mention} to move first:", components=cont)
        emoji = "❌"
        moves = 0
        for i in range(10):
            while True:
                res = await bot.wait_for("button_click")
                if res.user.id != turn.id: continue
                else: break
            cc = msg.components
            resid = res.component.id
            board[int(resid)] = emoji
            count = 1
            done = False
            for j in cc:
                for k in j:
                    if count == int(resid):
                        k.emoji = emoji
                        k.disabled = True
                        done = True
                    if done: break
                    count += 1
                if done: break
            moves += 1
            tie = False
            gameover = False
            if moves >= 5:
                if board[7] == board[8] == board[9] != '':  # across the top
                    gameover = True

                elif board[4] == board[5] == board[6] != '':  # across the middle
                    gameover = True

                elif board[1] == board[2] == board[3] != '':  # across the bottom
                    gameover = True

                elif board[1] == board[4] == board[7] != '':  # down the left side
                    gameover = True

                elif board[2] == board[5] == board[8] != '':  # down the middle
                    gameover = True

                elif board[3] == board[6] == board[9] != '':  # down the right side
                    gameover = True

                elif board[7] == board[5] == board[3] != '':  # diagonal
                    gameover = True

                elif board[1] == board[5] == board[9] != '':  # diagonal
                    gameover = True
            if moves >= 9:
                tie = True

            if gameover:
                await res.respond(type=7, content=f"**Game Over!**\nWinner: 🏆 {turn.mention} 🏆", components=[])
                if turn == ctx.author: id2 = user
                else: id2 = ctx.author
                await ttt_end(turn, id2, bet)
                break
            elif tie:
                await res.respond(type=7, content=f"**Game Tied!**\nWell Played!", components=[])
                if turn == ctx.author: id2 = user
                else: id2 = ctx.author
                await ttt_tie(turn.id, id2.id, bet)
                break
            else:
                if turn == ctx.author: turn = user
                else: turn = ctx.author
                if emoji == "❌": emoji = "⭕"
                else: emoji = "❌"

                await res.respond(type=7, content=f"{turn.mention} Your chance:", components=cc)

async def ttt_end(id1, id2, bet):
    data = await get_data()
    winner = data[str(id1.id)]
    winner["wallet"] += 1.5*bet
    data[str(id1)] = winner

    await create_statement(id1, bot.user, 0.5*bet, "Won Tic-Tac-Toe", 'Credit')
    await create_statement(id2, bot.user, bet, "Lost Tic-Tac-Toe", 'Debit')
    await update_data(data)

async def ttt_tie(id1, id2, bet):
    data = await get_data()
    winner1 = data[str(id1)]
    winner1["wallet"] += bet
    data[str(id1)] = winner1

    winner2 = data[str(id2)]
    winner2["wallet"] += bet
    data[str(id2)] = winner2

    await update_data(data)

@bot.check
async def is_dm(ctx):
    return ctx.guild != None

@bot.check
async def if_allowed(ctx):
    return await check_channel(ctx.channel.id, ctx.guild.id)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        embed = discord.Embed(description=f'{economyerror} The command you are trying to use doesn\'t exist.', color=error_embed)
        return await ctx.send(embed=embed)
    if isinstance(error, CheckFailure):
        embed = discord.Embed(description=f'{economyerror} You are not qualified to use this command!', color=error_embed)
        return await ctx.send(embed=embed)
    if isinstance(error, MissingRequiredArgument):
        embed = discord.Embed(description=f'{economyerror} Missing an argument! Use `e.help {ctx.command}` for syntax.', color=error_embed)
        return await ctx.send(embed=embed)
    if isinstance(error, BadArgument):
        embed = discord.Embed(description=f'{economyerror} Bad/Incorrect argument(s)! Use `e.help {ctx.command}` for syntax.', color=error_embed)
        return await ctx.send(embed=embed)
    if isinstance(error, UnboundLocalError): return
    code = hex(random.randint(1000, 9999))

    a = await debugcode(code, f'{ctx.author} ({ctx.author.id}) =>\n**Command:** `{ctx.command}`\n**Message:** `{ctx.message.content}`\n**Error:** `{error}`')
    if not a:
        while True:
            code = hex(random.randint(1000, 9999))
            a = await debugcode(code, f'{ctx.author} ({ctx.author.id}) =>\n\n**Command:** `{ctx.command}`\n**Message:** `{ctx.message.content}`\n**Error:** `{error}`')
            if a:
                break
    embed = discord.Embed(title=f'{economyerror} Oops! You just ran into an error',
                          description=f'Kindly report this error using `e.report {code}` for further investigation.\n'
                                      f'For a unique and error that is never been reported before, you get `1,000` coins!\n',
                          color=error_embed)
    embed.set_footer(text='Sorry for the inconvinience')
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)

@bot.event
async def on_raw_reaction_add(payload):
    if payload.message_id in bot.activems.keys():
        if payload.user_id != bot.activems[payload.message_id][1].author.id: return
        await stop_ms(bot.activems[payload.message_id][0], bot.activems[payload.message_id][1],bot.activems[payload.message_id][2])
    if payload.channel_id != 844184710678577193: return
    if payload.user_id not in devs: return
    a = await get_errorfile()
    if str(payload.emoji) == economysuccess:
        chl = bot.get_channel(payload.channel_id)
        msg = await chl.fetch_message(payload.message_id)
        cont = str(msg.content)
        errorcode = cont.split(' ')[3].replace('`', '')
        a.pop(errorcode)
        await update_errorfile(a)

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if bot.dev == 1 and message.author.id not in (devs+staff): return
    if message.author.id in disregarded:
        if message.author.id not in devs: return
    if message.content == 'e.' or message.content == f'{bot.user.mention}':
        await message.channel.send('Do you need my help?\nGet started using `e.help`')
    await open_account(message.author.id)
    await bot.process_commands(message)

@bot.command()
@commands.check(general_checks_loop)
async def report(ctx, code):
    a = await get_errorfile()
    if code not in a:
        return await ctx.reply('Invalid Code or Error may be already fixed!')
    already = a['reported']
    if code in already:
        return await ctx.reply('Error already reported')

    already.append(code)
    a['reported'] = already
    await update_errorfile(a)
    errors_chl = bot.get_channel(844184710678577193)
    e = await errors_chl.send(f'New error reported: `{code}` by {ctx.author} ({ctx.author.id})')
    await e.add_reaction(economysuccess)
    await ctx.message.add_reaction(economysuccess)

@bot.command()
@commands.check(is_dev)
async def debug(ctx, code):
    a = await get_errorfile()
    if code not in a:
        return await ctx.send('No matching code found!')

    embed=discord.Embed(title=f'Error {code}',
                        description=a[code],
                        color=success_embed)
    await ctx.send(embed=embed)

@bot.command()
@commands.check(is_dev)
async def dvm(ctx):
    if bot.dev == 1:
        await ctx.reply('Changed Dev Mode state to: **`Off`**')
        bot.dev = 0
    else:
        await ctx.reply('Changed Dev Mode state to: **`On`**')
        bot.dev = 1

@bot.command(aliases=["exit"])
@commands.check(is_dev)
async def _exit(ctx):
    await bot.wait_until_ready()
    await bot.close()

@bot.command()
@commands.check(is_dev)
async def logs(ctx, *, search:str=None):
    with open('files/logs.txt', 'r') as log:
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
async def evaluate(ctx, *, expression):
    if ctx.author.id == 669816890163724288:
        try:
            await ctx.reply(eval(expression))
        except Exception as e:
            await ctx.reply(f'```\n{e}```')
    elif ctx.author.id == 771601176155783198:
        try:
            calculated = aeval(expression)
            msg = await ctx.send('Calculating!')
            if len(aeval.error) > 0:
                calculated = ""
                for err in aeval.error:
                    for er2 in err.get_error(): calculated += str(er2) + '\n'
            await msg.edit(content=f'Input:\n```py\n{expression}```\nOutput:\n```py\n{calculated}```')
        except Exception as ex:
            await ctx.send(
                f"```py\n{''.join(traceback.format_exception(etype=type(ex), value=ex, tb=ex.__traceback__))}\n```")

@bot.command(aliases=['exec']) #DEV ONLY
async def execute(ctx, *, expression):
    if ctx.author.id != 669816890163724288: return
    try:
        exec(expression.replace('```', ''))
    except Exception as e:
        await ctx.reply(f'Command:```py\n{expression}```\nOutput:```\n{e}```')

@bot.command()
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

    await update_logs(f'{ctx.author}-!-add-!-[{person.id}; {await commait(bal)}]-!-{await current_time()}')
    await ctx.send(f'{ctx.author.mention} added `{await commait(bal)}` coins to {person.name}.')

@bot.command()
@commands.check(is_staff)
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

@bot.command()
@commands.is_owner()
async def release(ctx, title:str, fake:int=0):
    if ctx.author.id != 771601176155783198: return
    with open('files/updates.json', 'r') as upd:
        updates = json.load(upd)

    update = updates[title]
    embed = discord.Embed(title=f'Whats New:', color=embedcolor)
    i = 0
    while True:
        try: name = update[i]
        except: break

        try: value = update[i + 1]
        except: value = '\u200b'

        embed.add_field(name=name, value=value, inline=False)
        i += 2
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_author(name=f'Version {title}', icon_url=bot.pfp)

    with open('files/updates.json', 'w') as n:
        n.write(json.dumps(updates, indent=2))

    if fake == 1:
        chl = bot.get_channel(838963496476606485)
        await chl.send('<@&839370096248881204>', embed = embed)
    else:
        await ctx.send(embed=embed)

@bot.command()
@commands.check(is_staff)
async def stockinfo(ctx):
    with open(f'stocks/{await get_todays_stock()}', 'r') as f:
        stock = list(csv.reader(f))
    config = await get_stockconfigs()

    embed = discord.Embed(title='Stock Info', color=embedcolor)
    embed.add_field(name='Total Rows', value=f'{len(stock)}')
    embed.add_field(name='Current Row', value=f'{config["line"]}')
    embed.add_field(name='Approx Refresh Time', value=f'{round(86400/len(stock), 4)} secs')
    left = datetime.timedelta(seconds=((len(stock)-config["line"])*round(86400/len(stock), 4)))
    final = datetime.datetime.strptime(str(left), '%H:%M:%S.%f').replace(microsecond=0)
    embed.add_field(name='Ending Time', value=f'`{str(final).split(" ")[1]}` (HH:MM:SS)')

    await ctx.send(embed=embed)

@bot.command()
@commands.check(general_checks_loop)
async def uptime(ctx):
    delta_uptime = datetime.datetime.utcnow() - bot.launch_time
    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    await ctx.send(f"I have been working for `{days}d, {hours}h, {minutes}m, {seconds}s`")

@bot.command(pass_context=True)
@commands.check(is_staff)
async def refresh(ctx=None):
    with open('files/bot_data.json', 'r') as c:
        data = json.load(c)
    bot.phrases = data["phrases"]
    bot.help_json = data["help"]
    bot.shopc = data["shop"]["category"]
    bot.items = data["items"]
    bot.status = data["status"]
    if ctx is not None:
        msg = await ctx.send(f'{ctx.author.mention} ⚠️Warning! Do you want to rebuild the cache for items? This can take a long time')
        await msg.add_reaction(economyerror)
        await msg.add_reaction(economysuccess)

        def check(reaction, user):
            if user == ctx.author and str(reaction.emoji) in [economyerror, economysuccess]:
                return True
        try:
            reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)
            if str(reaction) == economyerror:
                await msg.delete()
                await ctx.message.add_reaction(economysuccess)
                return
        except:
            pass
    common_bgs = []
    rare_bgs = []
    legendary_bgs = []
    for i in range(40):
        img = Image.open(f'items/bgs/common_bg{i}.png')
        common_bgs.append(img)
    for i in range(40):
        img = Image.open(f'items/bgs/rare_bg{i}.png')
        rare_bgs.append(img)
    for i in range(40):
        img = Image.open(f'items/bgs/legendary_bg{i}.png')
        legendary_bgs.append(img)
    bot.unboxbgs["common"] = common_bgs
    bot.unboxbgs["rare"] = rare_bgs
    bot.unboxbgs["legendary"] = legendary_bgs
    print('Caching Items')
    with ThreadPoolExecutor(max_workers=1) as executor:
        await bot.loop.run_in_executor(executor, functools.partial(cache_allitems))

    if ctx is not None: await ctx.message.add_reaction(economysuccess)

@bot.command()
@commands.check(is_staff)
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
    await update_logs(f'{ctx.author}-!-badges-!-[{member.id}; {badge}]-!-{await current_time()}')
    await ctx.message.add_reaction('✅')

@bot.command(aliases=['bal'])
@commands.check(general_checks_loop)
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
    embed = discord.Embed(title=f'__{bank_details[bank_type]["name"]}__', colour=embedcolor)
    embed.add_field(name=f'**<:wallet:836814969290358845> Wallet**', value=f'> `{await commait(wallet)}`', inline=False)
    embed.add_field(name=f'**🏦 Bank**', value=f'> `{await commait(bank)}`', inline=False)
    embed.add_field(name=f'**<:stocks:839162083324198942> Stocks**', value=f'> `{await commait(stocks_num)}`', inline=False)
    fetched = bot.get_user(userid)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text='Economy Bot', icon_url=bot.pfp)
    embed.set_author(name=fetched.name, icon_url=fetched.avatar_url)

    await ctx.send(embed=embed)

@bot.command(aliases=['dep'])
@commands.check(general_checks_loop)
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
@commands.check(general_checks_loop)
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
@commands.check(general_checks_loop)
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
    embed.add_field(name='Bank Name', value=f'{bank_details[btype]["name"]}')
    embed.add_field(name='Bank Tier', value=f'{bank_details[btype]["tier"]}')
    embed.add_field(name='\u200b', value='\u200b')
    embed.add_field(name='Daily Interest', value=f'{bank_details[btype]["rate"]}%')
    embed.add_field(name='Current Balance', value=f'{person["bank"]}')
    embed.add_field(name='Average Balance', value=f'{person2["avg"]}')
    embed.add_field(name='Note:', value='To claim interest, use `e.daily`.\n'
                                        'Your average balance in last 24 hours will be taken in account for that.')
    fetched = bot.get_user(userid)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text='Economy Bot', icon_url=bot.pfp)
    embed.set_author(name=f'{fetched.name} | 🏦 Know Your Bank!', icon_url=fetched.avatar_url)

    await ctx.send(embed=embed)

@bot.command()
@commands.check(general_checks_loop)
async def daily(ctx):
    await avg_update()

    avg = await get_avg()
    data = await get_data()

    avg_p = avg.get(f'{ctx.author.id}')
    data_p = data.get(f'{ctx.author.id}')
    if avg_p is not None:
        i = avg_p['i']
    else:
        i = 0
    check = await checktimeout(ctx.author.id, 'daily')
    time_gap = 86400 - check
    if time_gap > 0 and check != 0:
        left = datetime.timedelta(seconds=time_gap)
        final = datetime.datetime.strptime(str(left).split(" ")[-1], '%H:%M:%S.%f').replace(microsecond=0)
        return await ctx.reply(f'You have to wait for `{str(final).split(" ")[-1]}` (HH:MM:SS) time more before you can claim daily interest.')
    btype = data_p['bank_type']
    avgbal = avg_p['avg']
    bank_d = data_p['bank']
    multiplier = (bank_details[btype]["rate"])/100

    newbal = bank_d + int(avgbal * multiplier)
    data_p['bank'] = newbal
    data[f'{ctx.author.id}'] = data_p
    avg_p['claimed'] = 1
    avg_p['sum'] = int(avgbal)
    avg_p['i'] = 1

    avg[f'{ctx.author.id}'] = avg_p

    await update_avg(avg)
    await update_data(data)
    await add_timeout(ctx.author.id, 'daily')
    embed = discord.Embed(title=f'{economysuccess} Claimed Successfully!', description=f'Daily interest payout of `{await commait(int(avgbal * multiplier))}` coins credited successfully!', color=success_embed)
    await ctx.send(embed=embed)

@bot.command()
@commands.check(general_checks_loop)
async def give(ctx, member:discord.Member, amount:int):
    data = await get_data()
    await open_account(member.id)
    await open_account(ctx.author.id)
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

    embed = discord.Embed(title=f'{economysuccess} Success!', color=embedcolor,
                          description=f'You gave `{await commait(amount)}` coin(s) to {member.mention}. What an act of generosity!')
    fetched = bot.get_user(ctx.author.id)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text='Economy Bot', icon_url=bot.pfp)

    await ctx.send(embed=embed)

@bot.command(aliases=['property'])
@commands.check(general_checks_loop)
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
    embed.set_footer(text='Economy Bot', icon_url=bot.pfp)
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
@commands.check(is_dev)
async def disregard(ctx, member:discord.Member):
    if member.id in disregarded: disregarded.remove(member.id)
    else: disregarded.append(member.id)
    await ctx.message.add_reaction(economysuccess)

@bot.command()
@commands.check(general_checks_loop)
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

    embed = discord.Embed(title=f'{economysuccess} Revenue Claimed!',
                          description=f'`{totalpay}.00` coins added to bank successfully!\n\nHere is the revenue split:\n```css\n{x}```',
                          colour=success_embed)
    fetched = bot.get_user(ctx.author.id)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text='Economy Bot', icon_url=bot.pfp)
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
@commands.check(general_checks_loop)
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
        embed = discord.Embed(title=f'{economyerror} Oops..',
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

        embed = discord.Embed(title=f'{economysuccess} Success!',
                              description=f'`{cost_d}.00` coins have been deducted and your hotel looks shining new!\n```css\n{x}```',
                              color=success_embed)

    fetched = bot.get_user(ctx.author.id)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text='Economy Bot', icon_url=bot.pfp)
    embed.set_author(name=f'{fetched.name} | {name} Hotel', icon_url=fetched.avatar_url)

    await ctx.send(embed=embed)

@bot.command()
@commands.check(general_checks_loop)
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
        embed.set_footer(text='Economy Bot', icon_url=bot.pfp)
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
    embed.add_field(name='Confirm?', value=f'Click {economysuccess} to confirm or {economyerror} to cancel', inline=False)
    embed.add_field(name='\u200b', value='Here is the look after upgrade:', inline=False)
    embed.set_image(url=getestates_thumb[level+1])
    fetched = bot.get_user(ctx.author.id)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text='Economy Bot', icon_url=bot.pfp)
    embed.set_author(name=f'{fetched.name} | {name} Hotel', icon_url=fetched.avatar_url)

    msg = await ctx.send(embed=embed)
    await msg.add_reaction(economysuccess)
    await msg.add_reaction(economyerror)

    def check(reaction, user):
        if user == ctx.author and str(reaction.emoji) in [economyerror, economysuccess]:
            return True
    try:
        reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)
        await msg.clear_reactions()
        if str(reaction) == economysuccess:
            data = await get_data()
            person = data[f'{ctx.author.id}']
            wallet = person['wallet']
            bank = person['bank']

            if cost > wallet:
                left = cost-wallet
                new_wallet = 0
                if left > bank:
                    embed = discord.Embed(title=f'{economyerror} Oopsie!',
                                          description='Looks like there aren\'t enough coins in your bank. Please deposit or earn more.',
                                          color=error_embed)
                    return await ctx.send(embed=embed)
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
            embed = discord.Embed(title=f'{economysuccess} Success!', description='Wohoo! Your upgrade was successful! Use `e.estates` to see newly upgraded property!', color=success_embed)
            await msg.edit(embed=embed)
        else:
            embed=discord.Embed(title=f'{economyerror} Cancelled!', color=error_embed)
            await msg.edit(embed=embed)
    except asyncio.TimeoutError:
        await msg.clear_reactions()
        await msg.edit(embed=discord.Embed(description=f'{economyerror} Timed Out!', color=error_embed))

@bot.command()
@commands.check(general_checks_loop)
async def alerts(ctx, state:str = None):
    if state is None:
        embed = discord.Embed(title='Alerts System',
                              description='Get Alerts on pending loans, hotel maintainance, robberies etc straight to your DMs\n'
                                          '```diff\n+ To turn on: e.alerts on\n- To turn off: e.alerts off\n```',
                              color=embedcolor)
        aler = await get_alert_info()
        if f'{ctx.author.id}' in aler:
            current = 'On'
        else:
            current = 'Off'

        embed.add_field(name='Current State', value=current)
        fetched = bot.get_user(ctx.author.id)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_author(name=f'{fetched.name}', icon_url=fetched.avatar_url)
        embed.set_footer(text='Economy Bot', icon_url=bot.pfp)
        return await ctx.send(embed=embed)

    if state == 'on':
        embed = discord.Embed(title=f'{economysuccess} Success!', description='Alerts are switched **On**. Make sure you have your DMs open', colour=success_embed)
        await ctx.send(embed=embed)
        await alerts_state(ctx.author.id, 'on')
    elif state == 'off':
        embed = discord.Embed(title=f'{economysuccess} Success!',
                              description='Alerts are switched **Off**. "Yay no more DMs" huh?',
                              colour=success_embed)
        await ctx.send(embed=embed)
        await alerts_state(ctx.author.id, 'off')
    else:
        await ctx.send(f'{ctx.author.mention} Incorrect Option. Use `e.alerts` to see help.')

@bot.command()
@commands.check(general_checks_loop)
async def transfer(ctx, togive:discord.Member = None, amount = None, *, reason = None):
    await open_account(togive.id)
    await open_account(ctx.author.id)
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

    embed = discord.Embed(title=f'{economysuccess} Transfer Successful!',
                          description=f'You transfered `{amount}` coins to {togive.mention}.',
                          color=success_embed)
    embed.add_field(name='Tax on transaction', value=f'`{fees}` coins')
    embed.add_field(name='Your Balance', value=f'`{c_bank - amount}` coins')
    fetched = bot.get_user(ctx.author.id)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text='Economy Bot', icon_url=bot.pfp)
    embed.set_author(name=f'{fetched.name}', icon_url=fetched.avatar_url)

    await ctx.send(embed=embed)

@bot.command(aliases=['transactions'])
@commands.check(general_checks_loop)
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
            member = bot.get_user(int(args[index]))

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
@commands.check(general_checks_loop)
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
@commands.check(general_checks_loop)
async def stocks(ctx):
    columns = ['Name', 'Highest   ', 'Lowest', 'Current', 'Volume']
    details = list(bot.current_stock)
    mydata = await perform_stuff(details)
    config = await get_stockconfigs()
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
@commands.check(general_checks_loop)
async def buystocks(ctx, amount):
    data = await get_data()
    stock_data = await get_stocks()
    userid = str(ctx.author.id)
    dperson = data[userid]
    sperson = stock_data.setdefault(userid, 0)
    if dperson['bank'] == 0:
        return await ctx.send(f'{ctx.author.mention} You have an empty bank bro..')
    stock_price = float(bot.current_stock[3])
    if amount == 'all':
        amount = dperson['bank']
        amount = int(amount/stock_price)
    elif amount == 'half':
        amount = int(dperson['bank']/2)
        amount = int(amount / stock_price)
    else:
        try: amount = int(amount)
        except: return await ctx.send(f'{ctx.author.mention} Dude, the stocks can be bought and sold in integral values only. Provide a valid number.')

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

    embed = discord.Embed(title=f'{economysuccess} Success!',
                          description=f'You bought `{await commait(amount)}` stocks at price of `{stock_price}`.\n'
                                      f'\nCoins Spent: `{await commait(bulk)}` coins', color=success_embed)
    fetched = bot.get_user(ctx.author.id)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text='Economy Bot', icon_url=bot.pfp)
    embed.set_author(name=f'{fetched.name}', icon_url=fetched.avatar_url)

    await ctx.send(embed=embed)

@bot.command()
@commands.check(general_checks_loop)
async def sellstocks(ctx, amount):
    data = await get_data()
    stock_data = await get_stocks()
    userid = str(ctx.author.id)
    dperson = data[userid]
    sperson = stock_data.setdefault(userid, 0)

    stock_price = float(bot.current_stock[3])
    if amount == 'all':
        amount = sperson
    elif amount == 'half':
        amount = int(sperson/2)
    else:
        try: amount = int(amount)
        except: return await ctx.send(
                f'{ctx.author.mention} Dude, the stocks can be bought and sold in integral values only. Provide a valid number.')

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

    embed = discord.Embed(title=f'{economysuccess} Success!',
                          description=f'You sold `{await commait(amount)}` stock(s) at price of `{stock_price}`.\n'
                                      f'\nCoins Earned: `{await commait(bulk)}` coins', color=success_embed)
    fetched = bot.get_user(ctx.author.id)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text='Economy Bot', icon_url=bot.pfp)
    embed.set_author(name=f'{fetched.name}', icon_url=fetched.avatar_url)

    await ctx.send(embed=embed)

@bot.command()
@commands.check(general_checks_loop)
async def help(ctx, specify=None):
    embed = discord.Embed(color=embedcolor,
                          description=f'[Support Server]({support_server}) | [Invite Url]({invite_url}) | [Patreon Page]({patreon_page})\nTo get help on a command, use `e.help <command name>`')
    embed.set_author(name='Help', icon_url=bot.pfp)
    embed.set_footer(text='Bot developed by: AwesomeSam#7985 and BlackThunder#4007')
    if specify is None:
        for j in bot.help_json:
            mylist = []
            max_l = 0
            for i in bot.help_json[j].keys():
                if i == "category": continue
                info = bot.help_json[j][i]['usage']
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
        embed.add_field(name='\u200b', value=f'For more support, visit our Support Server (click button) or use `e.server`\n'
                                             f'`<>` and `[]` are **not** required while using commands\n\n'
                                             f'Syntax: `<>` = Required `[]` = Optional')
        components = [[Button(style=ButtonStyle.URL, label="Support Server", url=support_server),
                      Button(style=ButtonStyle.URL, label="Invite URL", url=invite_url),
                      Button(style=ButtonStyle.URL, label="Patron Page", url=patreon_page)]]
        try:
            await ctx.author.send(embed=embed, components=components)
            embed = discord.Embed(title=f'{economysuccess} You received a mail!', color=success_embed)
            await ctx.reply(embed=embed)
        except:
            await ctx.send(embed=embed, components=components)
        return
    x = bot.help_json.values()
    notfound = True
    for i in x:
        for j in i.keys():
            if j == 'category':
                continue
            available = []
            available.append(j[2:])
            info = i[j]

            for k in info['aliases']:
                available.append(k)
            if specify.lower() in available:
                alias_list = [f'{q}' for q in info['aliases']]

                for aliases in alias_list:
                    if aliases[0:2] != 'e.':
                        if aliases == 'None': continue
                        alias_list.remove(aliases)
                        aliases = 'e.' + aliases
                        alias_list.insert(0, aliases)
                embed = discord.Embed(color=embedcolor, title=f'Command: {j[2:]}', description=info['desc']+f'\n\n**Usage:** `{info["usage"]}`\n**Category:** `{i["category"]}`')
                embed.add_field(name='Aliases', value='```less\n'+'\n'.join(alias_list)+'```', inline=False)
                embed.set_footer(text='Syntax: <> = required, [] = optional')
                notfound = False
                await ctx.send(embed=embed)
                break
    if notfound:
        embed = discord.Embed(description=f'{economyerror} No help found or command doesn\'t exist!', color=error_embed)
        await ctx.send(embed=embed)

@bot.command(aliases=['add_chl'])
@commands.check(general_checks_loop)
@commands.has_permissions(manage_channels=True)
async def set_chl(ctx, channel:discord.TextChannel):
    a = await get_admin()
    server = a.get(str(ctx.guild.id), [])
    if channel.id in server:
        embed = discord.Embed(description=f'{economyerror} {channel.mention} is already in list of registered channels!', color=error_embed)
        return await ctx.send(embed=embed)
    server.append(channel.id)
    if ctx.channel.id not in server:
        server.append(ctx.channel.id)
    a[str(ctx.guild.id)] = server
    await close_admin(a)
    embed = discord.Embed(description=f'{economysuccess} {channel.mention} added to list of registered channels successfully!', color=success_embed)
    await ctx.send(embed=embed)

@bot.command(aliases=['rem_chl', 'remove_chl', 'delete_chl'])
@commands.check(general_checks_loop)
@commands.has_permissions(manage_channels=True)
async def del_chl(ctx, channel:discord.TextChannel):
    a = await get_admin()
    server = a.get(str(ctx.guild.id), [])
    if channel.id not in server:
        embed = discord.Embed(description=f'{economyerror} {channel.mention} not in list of registered channels!', color=error_embed)
        return await ctx.send(embed=embed)
    server.remove(channel.id)
    a[str(ctx.guild.id)] = server
    await close_admin(a)
    embed = discord.Embed(description=f'{economysuccess} {channel.mention} removed from list of registered channels successfully!', color=success_embed)
    await ctx.send(embed=embed)

@bot.command(aliases=['show_chl'])
@commands.check(general_checks_loop)
@commands.has_permissions(manage_channels=True)
async def list_chl(ctx):
    a = await get_admin()
    server = a.get(str(ctx.guild.id), [])
    if len(server) == 0: channels = ['> No channels set']
    else: channels = [f'> <#{x}>' for x in server]
    embed = discord.Embed(title=f'{economysuccess} Allowed Channels for the bot:', description='\n'.join(channels), color=embedcolor)
    embed.set_footer(text='Add a channel using e.set_chl <name>\nRemove a channel using e.del_chl <name>')
    await ctx.send(embed=embed)

@bot.command()
@commands.check(general_checks_loop)
@commands.has_permissions(manage_channels=True)
async def reset_chl(ctx):
    a = await get_admin()
    a[str(ctx.guild.id)] = []
    embed = discord.Embed(title=f'{economysuccess} Done', description='Cleared Successfully!', color=embedcolor)
    await close_admin(a)
    embed.set_footer(text='Add a channel using e.set_chl <name>\nRemove a channel using e.del_chl <name>')
    await ctx.send(embed=embed)

@bot.command()
@commands.check(general_checks_loop)
async def rob(ctx, member:discord.Member):
    await open_account(member.id)
    await open_account(ctx.author.id)
    if member == bot.user:
        pass
    success = random.randint(0, 100)
    a = await get_data()

    lock = 0
    inv = await get_inv()
    userinv = inv.get(str(member.id), {"inv":[]})
    user = userinv["inv"]
    eq = userinv['eq_lock']
    if len(user) == 0: pass
    else:
        if eq == 'Bronze Lock': lock = 10
        if eq == 'Silver Lock': lock = 25
        if eq == 'Gold Lock': lock = 40
    wallet = a[str(ctx.author.id)]['wallet']
    if wallet < 100:
        return await ctx.send(f'{ctx.author.mention} You need `100` coins to start a robbery!')
    if success > 50+lock:
        if member == ctx.author:
            walleta = a[str(ctx.author.id)]['wallet']
            prize = random.randint(int(walleta / 5), int(walleta / 2))
            desc = random.choice(bot.phrases['selfrob_success']).format(prize=f'`{await commait(prize)}`')
        else:
            walletm = a[str(member.id)]['wallet']
            if walletm == 0:
                return await ctx.send(f'{ctx.author.mention} Robbing a person with empty wallet.\n**Logic: 100**')
            prize = random.randint(int(walletm / 5), int(walletm / 2))
            walletm -= prize
            walleta = a[str(ctx.author.id)]['wallet']
            walleta += prize
            a[str(member.id)]['wallet'] = walletm
            a[str(ctx.author.id)]['wallet'] = walleta
            await update_data(a)
            desc = random.choice(bot.phrases['rob_success']).format(prize=f'`{await commait(prize)}`', whom=member.mention)
            alert = await get_alert_info()
            if str(member.id) in alert:
                if alert[str(member.id)]['state'] == 'on':
                    embed = discord.Embed(title=f'{economyerror} You were robbed!',
                                          description=f'You were robbed of `{await commait(prize)}` coins by `{ctx.author.name}#????` in `{ctx.guild.name}`!', color=error_embed)
                    await member.send(embed=embed)
            if lock != 0:
                if lock == 25: user.remove('Silver Lock')
                elif lock == 10: user.remove('Bronze Lock')
                elif lock == 40: user.remove('Gold Lock')
            userinv["inv"] = user
            userinv["eq_lock"] = ''
            inv[str(member.id)] = userinv
            await update_inv(inv)
        embed = discord.Embed(title=f'{economysuccess} Robbery Successful!', description=desc, color=success_embed)
    else:
        if member == ctx.author:
            walleta = a[str(ctx.author.id)]['wallet']
            prize = random.randint(int(walleta / 5), int(walleta / 2))
            desc = random.choice(bot.phrases['selfrob_failed']).format(prize=f'`{await commait(prize)}`')
            walleta -= prize
            a[str(ctx.author.id)]['wallet'] = walleta
            await update_data(a)
        else:
            walletm = a[str(ctx.author.id)]['wallet']
            prize = random.randint(int(walletm / 5), int(walletm / 2))
            walleta = a[str(ctx.author.id)]['wallet']
            walleta -= prize
            a[str(ctx.author.id)]['wallet'] = walleta
            await update_data(a)
            desc = random.choice(bot.phrases['rob_failed']).format(prize=f'`{await commait(prize)}`', whom=member.mention)
        embed = discord.Embed(title=f'{economyerror} Robbery Failed!', description=desc, color=error_embed)
    await ctx.send(embed=embed)

@bot.command()
@commands.check(general_checks_loop)
async def find(ctx):
    chance = random.randint(1, 100)
    a = await get_data()
    wallet = a[str(ctx.author.id)]['wallet']
    if wallet < 50:
        chance = 1
    if 45 > chance > 0:
        c = random.randint(50, 400)
        embed = discord.Embed(description=economysuccess+ ' ' +random.choice(bot.phrases['find_success']).format(c=c), color=success_embed)
        a[str(ctx.author.id)]['wallet'] = wallet + c
    elif 90 > chance >= 45:
        c = random.randint(int(wallet/5), int(wallet/2))
        embed = discord.Embed(description=economyerror+ ' ' +random.choice(bot.phrases['find_failed']).format(c=c), color=error_embed)
        a[str(ctx.author.id)]['wallet'] = wallet - c
    else:
        embed = discord.Embed(description=economyerror+ ' ' +random.choice(bot.phrases['find_neutral']), color=error_embed)
    await update_data(a)
    await ctx.send(embed=embed)

@bot.command(aliases=['store'])
@commands.check(general_checks_loop)
async def shop(ctx, page:int=1):
    if page <= 0: page = 1
    while True:
        if page*8 > len(storeitems):
            page -= 1
        else:
            break
    storeimg = await createstore((page)*8,(page+1)*8)
    await ctx.send(file=storeimg)

@bot.command(aliases=['inv'])
@commands.check(general_checks_loop)
async def inventory(ctx):
    inv = await inventory_image(ctx.author.id)
    await ctx.send(file=inv)

@bot.command(aliases=['purchase'])
@commands.check(general_checks_loop)
async def buy(ctx, *, item):
    a = str(item).split(' ')
    qty = 1
    try:
        fqty = a[-1]
        item_name = a[0]
        if fqty != item_name:
            qty = int(fqty)
            a.pop(-1)
            item = ' '.join(a)
    except: pass
    if qty < 0:
        return await ctx.send(f'{ctx.author.mention} Yeah! Lets buy items in negative!')
    elif qty == 0:
        return await ctx.send(f'{ctx.author.mention} Why bother typing when you want to buy nothing?')
    found = False
    store_item = ''
    for i in storeitems:
        if item.lower() == i["name"].lower():
            found = True
            store_item = i
            break

    if not found:
        embed = discord.Embed(title=f'{economyerror} Item Not Found!',
                              description=f'The item `{item}` wasn\'t found. {random.choice(bot.phrases["shop_noitem"])}',
                              color=error_embed)
        return await ctx.send(embed=embed)

    data = await get_data()
    if store_item["special"]: price = store_item["disc"]
    else: price = store_item["price"]

    user = data[str(ctx.author.id)]
    wallet = user["wallet"]
    qty = int(qty)
    price = int(price.replace(',', ''))
    if price*qty > wallet:
        embed = discord.Embed(title=f'{economyerror} Insufficient Funds',
                              description=f'{random.choice(bot.phrases["less_bal"])}',
                              color=error_embed)
        return await ctx.send(embed=embed)
    inv = await get_inv()
    member_inv = inv.get(str(ctx.author.id), {"inv":[]})
    memberinv = member_inv["inv"]
    appends = 0
    while appends < qty:
        memberinv.append(store_item["name"])
        appends += 1
    member_inv["inv"] = memberinv
    inv[str(ctx.author.id)] = member_inv
    user["wallet"] = wallet - (price*qty)
    data[str(ctx.author.id)] = user
    embed = discord.Embed(description=f'{economysuccess} Done! `{qty}` quantity of `{store_item["name"]}` purchased successfully!',
                          color=success_embed)
    await update_data(data)
    await update_inv(inv)
    await ctx.send(embed=embed)

@bot.command()
@commands.check(general_checks_loop)
async def server(ctx):
    embed = discord.Embed(description=f'**Discord Support Server:** [Join Here]({support_server})\n'
                                      f'Server Members: `idk lol`', color=embedcolor)
    embed.set_author(icon_url=bot.pfp, name=f'{bot.user.name}')
    await ctx.send(embed=embed)

@bot.command()
@commands.check(general_checks_loop)
async def invite(ctx):
    guilds = bot.guilds
    members = 0
    for i in guilds:
        members += len(i.members)
    embed = discord.Embed(description=f'Invite the bot: [Invite URL]({invite_url})\n\n'
                                      f'Support Server: [Join]({support_server})\n'
                                      f'Support us on Patreon: [Support]({patreon_page})\n\n'
                                      f'Servers: `{len(guilds)}`\n'
                                      f'Users: `{members}`\n'
                                      f'Shards: `{bot.shard_count}`',
                          color=embedcolor)
    embed.set_author(icon_url=bot.pfp, name=f'{bot.user.name}')
    await ctx.send(embed=embed)

@bot.command()
async def use(ctx, *, item:str):
    async def lock(shopitem):
        eq = userinv.setdefault('eq_lock', '')
        if eq != shopitem:
            eq = shopitem
            embed = discord.Embed(description=f'{economysuccess} `{shopitem}` equiped successfully!', color=success_embed)
        else:
            eq = ''
            embed = discord.Embed(description=f'{economysuccess} `{shopitem}` **unequiped** successfully!', color=success_embed)
        userinv['eq_lock'] = eq
        await ctx.send(embed=embed)

    async def chest(chest):
        mychest = chest.split(" ")[0].lower()
        chances = {'common':{'c':[0, 70], 'r':[70, 95], 'e':[95, 100]},
                   'rare':{'c':[0, 50], 'r':[50, 90], 'e':[90, 100]},
                   'legendary':{'c':[0, 30], 'r':[30, 80], 'e':[80, 100]}}
        rng = random.randint(1, 100)
        mychance = chances[mychest]
        if mychance['c'][0] < rng < mychance['c'][1]: rarity = 'common'
        elif mychance['r'][0] <= rng < mychance['r'][1]: rarity = 'rare'
        elif mychance['e'][0] <= rng < mychance['e'][1]: rarity = 'legendary'
        else: rarity = 'common'
        item_name = random.choice(bot.items[rarity]["items"])["name"]
        if len(bot.allitems.keys()) != 50:
            embed = discord.Embed(description=f'{economyerror} Please Wait! The bot is caching all the items', color=error_embed)
            embed.set_footer(text=f'Approx Time Left: {(50-len(bot.allitems.keys()))*8} secs')
            userinv.append(chest)
            return await ctx.send(embed=embed)
        file = discord.File(fp=bot.allitems[item_name], filename='unboxing.gif')
        if mychest == 'common': chestcol = 183398
        elif mychest == 'rare': chestcol = 5164244
        elif mychest == 'legendary': chestcol = 16475796
        else: chestcol = 0
        embed = discord.Embed(color=chestcol)
        fetched = bot.get_user(ctx.author.id)
        embed.set_footer(text='Type e.sell <item-name> to sell an item for coins\nType e.iteminfo <item-name> for info!', icon_url=bot.pfp)
        embed.set_author(name=f'{fetched.name} Unboxed: {item_name}', icon_url=fetched.avatar_url)
        embed.set_image(url="attachment://unboxing.gif")
        await ctx.send(embed=embed, file=file)

        useritems = userinv.setdefault("items", [])
        useritems.append(item_name)
        userinv["items"] = useritems

    def boost():
        pass

    inv = await get_inv()
    userinv = inv.get(str(ctx.author.id), {"inv":[]})
    allinv = userinv["inv"]
    user = [x.lower() for x in allinv]
    if item.lower() not in user:
        embed = discord.Embed(description=f'{economyerror} The item `{item}` isn\'t found. {random.choice(bot.phrases["inv_noitem"])}', color=error_embed)
        return await ctx.send(embed=embed)
    for i in bot.shopc.keys():
        for k in [j for j in bot.shopc[i]]:
            if item.lower() == k.lower():
                if i == "lock": await lock(k)
                elif i == "chest": await chest(k)
                allinv.remove(k)
                userinv["inv"] = allinv
    inv[str(ctx.author.id)] = userinv
    await update_inv(inv)

@bot.command()
async def ping(ctx):
    msg = await ctx.send('Pong!')
    ping = "{:.2f}".format(bot.latency*1000)
    await msg.edit(content=f'Pong! `{ping} ms`')

@bot.command()
@commands.check(general_checks_loop)
async def bank(ctx, tier:int=None):
    if tier is None:
        await open_account(ctx.author.id)
        x = PrettyTable()
        x.field_names = ["Bank Name", "Tier", "Interest"]
        for i in bank_details.values():
            x.add_row([i["name"], i["tier"], f'{i["rate"]}%'])
        embed = discord.Embed(title='List of Banks',
                              description=f'Choose your bank to get higher interest rate, loans and more benefits!\n```\n{x}```\n'
                                          f'To change your bank: `e.bank <tier>`',
                              color=embedcolor)
        fetched = bot.get_user(ctx.author.id)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text='Economy Bot', icon_url=bot.pfp)
        embed.set_author(name=fetched.name, icon_url=fetched.avatar_url)
        return await ctx.send(embed=embed)
    data = await get_data()
    user = data[str(ctx.author.id)]

    if tier <= 0 or tier > 3:
        return await ctx.send(f'{ctx.author.mention} Invalid Tier')
    if user['bank_type'] == tier:
        return await ctx.send(f'{ctx.author.mention} You already own a account in this bank')
    elif user['bank_type'] > tier:
        return await ctx.send(f'{ctx.author.mention} You cannot downgrade your bank tier')

    bal = user['wallet'] + user['bank']
    price = 5000 if tier == 2 else 10000
    total = int(bal*0.01 + price)

    x = PrettyTable()
    x.field_names = ['Name', '      ', 'Cost']
    x.align["Cost"] = "l"
    x.add_row(['Account Opening', '      ', price])
    x.add_row(['Transfering', '      ', bal*0.01])
    x.add_row(['      ', '      ', '      '])
    x.add_row(['Grand Total', '      ', total])

    embed = discord.Embed(title='Upgrade your bank',
                          description=f'Here is the cost for upgrading your bank: \n```\n{x}```\n'
                                      f'Confirm: {economysuccess}\n'
                                      f'Decline: {economyerror}\n'
                                      f'**React below, you have 60 secs until timeout**',
                          color=embedcolor)
    msg = await ctx.send(embed=embed)
    await msg.add_reaction(economysuccess)
    await msg.add_reaction(economyerror)

    def check(reaction, member):
        if member == ctx.author and str(reaction.emoji) in [economyerror, economysuccess]:
            return True
    try:
        reaction, member = await bot.wait_for('reaction_add', timeout=60.0, check=check)
        await msg.clear_reactions()
        if str(reaction) == economysuccess:
            if total > user["bank"]:
                embed = discord.Embed(title=f'{economyerror} Insufficient Funds in bank!',
                                      description=f'You do not have enough balance to upgrade tier. {bot.phrases["less_bal"]}',
                                      color=error_embed)
            else:
                user["bank"] = user["bank"] - total
                user["bank_type"] = tier
                data[str(ctx.author.id)] = user
                await update_data(data)
                embed = discord.Embed(title=f'{economysuccess} Success!', description=f'Bank upgraded to `Tier {tier}` successfully!', color=success_embed)
            await msg.edit(embed=embed)
        else:
            embed=discord.Embed(title=f'{economyerror} Cancelled!', color=error_embed)
            await msg.edit(embed=embed)
    except asyncio.TimeoutError:
        await msg.clear_reactions()
        await msg.edit(embed=discord.Embed(description=f'{economyerror} Timed Out!', color=error_embed))

@bot.command(aliases=["item"], pass_context=True)
@commands.check(general_checks_loop)
async def iteminfo(ctx, *, name:str, via:bool=False):
    found = False
    for i in bot.items.keys():
        for j in bot.items[i]["items"]:
            if name.lower() == j["name"].lower():
                found = True
                item = j
                mychest = i
                break
    if not found:
        embed = discord.Embed(description=f'{economyerror} The item `{name}` doesn\'t exist.', color=error_embed)
        return await ctx.send(embed=embed)
    if mychest == 'common':
        chestcol = 183398
    elif mychest == 'rare':
        chestcol = 5164244
    elif mychest == 'legendary':
        chestcol = 16475796
    embed = discord.Embed(title="Item Info", color=chestcol)
    embed.add_field(name="Name", value=f'{item["name"]}', inline=False)
    embed.add_field(name="Description", value=item["desc"], inline=False)
    embed.add_field(name="Rarity", value=mychest.capitalize())
    if item["value"][0] == item["value"][1]:
        embed.add_field(name="Est. Value", value=f"`{await commait(item['value'][0])}` coins", inline=False)
    else:
        embed.add_field(name="Est. Value", value=f"`{await commait(item['value'][0])} - {await commait(item['value'][1])}` coins", inline=False)
    embed.set_thumbnail(url=f"attachment://item.png")
    file = discord.File(f"items/{item['name']}.png", filename="item.png")
    if not via:
        await ctx.send(embed=embed, file=file)
    else:
        return {"embed":embed, "file":file}

@bot.command(aliases=['itemsinv'])
@commands.check(general_checks_loop)
async def items(ctx, *, everything=None):
    if everything is None:
        rarity = None
        user_page_orignal = 1
    else:
        everything = str(everything).split(' ')
        try:
            user_page_orignal = int(everything[-1])
            rarity = everything[0]

            if str(user_page_orignal) == rarity:
                rarity = None
        except:
            user_page_orignal = 1
            rarity = everything[0]

    updinv = await update_sorted_inv(str(ctx.author.id))
    if updinv == "userinv": return await ctx.reply('You have an empty inventory bro..')
    if updinv == "itemsinv": return await ctx.reply('You don\'t own any items yet. Why not go and unbox?')

    sorted_inv = updinv
    item_count = 0
    max_pages = 1
    while True:
        if max_pages < len(sorted_inv)/6: max_pages += 1
        else: break
    max_pages -= 1
    if max_pages == 0: max_pages += 1
    if user_page_orignal <= 0: user_page_orignal = 1
    if user_page_orignal > max_pages: user_page_orignal = max_pages
    user_page = (user_page_orignal-1)*6
    if rarity is not None:
        rarity = rarity.lower()
        if rarity not in ["common", "rare", "legendary"]:
            return await ctx.reply("The rarity can be `common`, `rare` or `legendary` only.")
    components= await inv_components(str(ctx.author.id), user_page_orignal, rarity)
    embed = discord.Embed(title=f"{economysuccess} Your Inventory:",
                          description=f"Items Owned: `{len(sorted_inv)}/50`\n"
                                      "Click on the item for item info!",
                          color=3553599)
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_footer(text=f'Page {user_page_orignal} of {max_pages}')
    a = await ctx.send(embed=embed, components=components)
    while True:
        res = await bot.wait_for("button_click")
        if res.channel == ctx.channel:
            if res.user != ctx.author:
                await res.respond(type = InteractionType.ChannelMessageWithSource, content="Oops! You cant sell other's items lol")
            else:
                await res.respond(type=InteractionType.DeferredUpdateMessage)
                if "info" in res.component.id:
                    via_iteminfo = await iteminfo(ctx, name=res.component.label, via=True)
                    resmsg = await ddb.send_component_msg(channel=ctx.channel, content='', embed=via_iteminfo["embed"], file=via_iteminfo["file"])
                #await res.respond(type=InteractionType.ChannelMessageWithSource, embed=via_iteminfo["embed"], file=via_iteminfo["file"])

@bot.command(aliases=["test"])
@commands.check(is_dev)
async def _test(ctx):
    item1 = Option(label="This is 1", value="Value?")
    item2 = Option(label="This is 2", value="IDK")
    item3 = Option(label="This is 3", value="lmao")
    dropdown = Select(options=[item1, item2, item3], placeholder="IDK bruh whats this", min_values=1, max_values=1)
    await ctx.send("Select:", components=[dropdown])

@bot.command(pass_context=True)
@commands.check(general_checks_loop)
async def sell(ctx, *, item):
    a = str(item).split(' ')
    qty = 1
    try:
        fqty = a[-1]
        item_name = a[0]
        if fqty != item_name:
            qty = int(fqty)
            a.pop(-1)
            item = ' '.join(a)
    except: pass
    userid = str(ctx.author.id)
    inv = await get_inv()
    userinv = inv.get(userid)
    if userinv is None:
        return await ctx.reply('You have an empty inventory bro..')
    itemsinv = userinv.get("items", [])
    invlower = [x.lower() for x in itemsinv]
    if item.lower() not in invlower:
        embed = discord.Embed(description=f"{economyerror} You don\'t own `{item}`", color=error_embed)
        return await ctx.send(embed=embed)
    userqty = invlower.count(item.lower())
    for i in bot.items.keys():
        for j in bot.items[i]["items"]:
            if j["name"].lower() == item.lower():
                item_main = j
                break

    if qty > userqty:
        embed = discord.Embed(description=f"{economyerror} Dude, you don\'t own `{qty}` quantity of `{item_main['name']}`. What are you even thinking?", color=error_embed)
        return await ctx.send(embed=embed)
    itemsinv.remove(item_main["name"])
    userinv["items"] = itemsinv
    inv[userid] = userinv
    value = random.randint(item_main["value"][0], item_main["value"][1])*qty
    embed = discord.Embed(title=f'{economysuccess} Success!',
                          description=f'You sold `{qty}` {item_main["name"]} for {await commait(value)} coins!')
    data = await get_data()
    datauser = data[userid]
    datauser["wallet"] += value
    data[userid] = datauser

    await update_data(data)
    await ctx.send(embed=embed)
    await update_inv(inv)

@bot.command()
async def games(ctx):
    ttt = Button(style=ButtonStyle.green, label="Tic-Tac-Toe", emoji="👀", id="ttt")
    mine = Button(style=ButtonStyle.green, label="Minesweeper", emoji="💣", id="mine")

    msg = await ctx.send(f"**Welcome to Gamebot Arcade <:gamepad:849117058875916308>**\nChoose your game below:", components=[ttt, mine])
    while True:
        res = await bot.wait_for("button_click")
        if res.channel != ctx.channel and res.user != ctx.author: pass
        else: break
    if res.component.id == "mine":
        await res.respond(type=InteractionType.DeferredUpdateMessage)
        await msg.delete()
        await minesweeper(ctx)
    elif res.component.id == "ttt":
        await res.respond(type=7, content="Tag your friend with whom you will like to play")
        def check(c):
            return c.author == ctx.author and c.channel == ctx.channel
        c = await bot.wait_for("message", timeout=60, check=check)
        person = c.mentions[0]
        confirm_p = await ctx.send(f'{person.mention} Hey, {ctx.author.mention} wants to challenge you for a game of'
                                   f' Tic-Tac-Toe. Click "Accept" to start!', components=[Button(label="Accept", style=ButtonStyle.green)])
        while True:
            res = await bot.wait_for("button_click")
            if res.user != person and res.id != confirm_p.id:
                await res.respond(type=InteractionType.DeferredUpdateMessage)
            else:
                await res.respond(type=7, content=f"Challenge Accepted! "
                                                  f"{ctx.author.mention} to select betting amount:",
                                  components=[[Button(label=x, style=ButtonStyle.grey) for x in [100, 200, 250, 500, 1000]],
                                              [Button(label=x, style=ButtonStyle.grey) for x in [2000, 2500, 5000, 10000, 20000]]])
                break
        while True:
            res = await bot.wait_for("button_click")
            if res.user not in [ctx.author] and res.id != confirm_p.id: continue
            await res.respond(type=InteractionType.DeferredUpdateMessage)
            break
        await confirm_p.delete()
        await tictactoe(ctx, bot.get_user(person.id), int(res.component.label))

@bot.command()
async def flip(ctx, bet:int):
    if bet < 50:
        return await ctx.reply("Minimum bet amount is 50 coins")

    data = await get_data()
    user = data[str(ctx.author.id)]
    if bet > user["wallet"]:
        return await ctx.send(f"{ctx.author.mention} Imagine betting more than you have in your pockets..")
    embed = discord.Embed(description=f"Call your side! Amount at stake: `{bet}` coins", color=embedcolor)
    msg = await ctx.send(embed=embed,
                   components=[[Button(label="Heads", style=ButtonStyle.blue), Button(label="Tails", style=ButtonStyle.green)]])
    while True:
        res = await bot.wait_for("button_click")
        if res.user != ctx.author and res.id != msg.id: continue
        break
    win = random.choice(["Heads", "Tails"])
    if win == res.component.label:
        cont = f"Congratulations! You win back {int(bet/2)} coins"
        color= success_embed
        user["wallet"] += bet*0.5
    else:
        cont = f"You lose hahaha. Nothing for you!"
        color= error_embed
        user["wallet"] -= bet
    data[str(ctx.author.id)] = user
    embed=discord.Embed(title=win,
                        description=f"{cont}", color=color)
    await res.respond(type=7, embed=embed)
    await update_data(data)

bot.connected_ = False
@bot.event
async def on_connect():
    if not bot.connected_:
        print("Entering on_connect()")
        bot.connected_ = True
        await create_stuff()

bot.run("ODMyMDgzNzE3NDE3MDc0Njg5.YHeoWQ._O5uoMS_I7abKdI_YzVb9BuEHzs")
