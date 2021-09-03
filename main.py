import time
t1 = time.time()
import datetime, csv, threading, functools, asyncio, discord, operator, math
import json, random, os, traceback, difflib, discord_files, requests, aiohttp
from discord.ext import commands, tasks
from discord.ext.commands import *
from prettytable import PrettyTable
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter
from io import BytesIO
from concurrent.futures import ThreadPoolExecutor
from asteval import Interpreter
aeval = Interpreter()
print(f"Imports Complete in {float('{:.2f}'.format(time.time()-t1))} secs")
tnew = time.time()

class EconomyBot(commands.Bot):
    def __init__(self):
        self.help_json = {}
        self.phrases = {}
        self.current_stock = []
        self.total_lines = 0
        self.pfp = ''
        self.raw_status = ''
        self.shopc = {}
        self.items = {}
        self.emotes = {}
        self.unboxbgs = {}
        self.allitems = {}
        self.cachedinv = {}
        self.used = {}
        self.ms = {}
        self.activems = {"users": [], "games":[]}
        self.waitings = {}
        self.status = []
        self.globaltrades = []
        self.random_status = True
        self.maint = False
        self.cooldown = {}
        with open("files/average.json", "r") as f: self.avg = json.load(f)
        with open("files/admin.json", "r") as f: self.admin = json.load(f)
        with open("files/estates.json", "r") as f: self.estates = json.load(f)
        with open("files/alerts.json", "r") as f: self.alertsinfo = json.load(f)
        with open("files/xp.json", "r") as f: self.xp = json.load(f)
        with open("files/statements.json", "r") as f: self.statements = json.load(f)
        with open("files/stocks.json", "r") as f: self.stocks = json.load(f)
        with open("files/accounts.json", "r") as f: self.accounts = json.load(f)
        with open("files/badges.json", "r") as f: self.badges = json.load(f)
        with open("files/inventory.json", "r") as f: self.inventory = json.load(f)
        with open("files/awards.json", "r") as f: self.awards = json.load(f)

        super().__init__(command_prefix=bot.when_mentioned_or("e.", "E."), intents=discord.Intents.all(), case_insensitive=True)

bot = EconomyBot()
uploader = discord_files.ConcurrentUploader(bot)
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
invite_url = 'https://discord.com/api/oauth2/authorize?client_id=832083717417074689&permissions=392256&scope=bot'
all_commands = []
bank_details = {
    1: {"name":'Common Finance Bank Ltd.', "rate":3, "tier":"I"},
    2: {"name":'National Bank Pvt. Ltd.', "rate":5, "tier":"II"},
    3: {"name":'International Bank of Finance Ltd.', "rate":7, "tier":"III"}
}
getestates_thumb = {
  "1": "https://cdn.discordapp.com/attachments/837564505952747520/863096662813573160/file.png",
  "2": "https://cdn.discordapp.com/attachments/837564505952747520/863096678865305620/file.png",
  "3": "https://cdn.discordapp.com/attachments/837564505952747520/863096689282908201/file.png",
  "4": "https://cdn.discordapp.com/attachments/837564505952747520/863096698753777715/file.png",
  "5": "https://cdn.discordapp.com/attachments/837564505952747520/863096712674279464/file.png",
  "6": "https://cdn.discordapp.com/attachments/837564505952747520/863096721550213120/file.png",
  "7": "https://cdn.discordapp.com/attachments/837564505952747520/863096735307661328/file.png",
  "8": "https://cdn.discordapp.com/attachments/837564505952747520/863096749349797939/file.png",
  "9": "https://cdn.discordapp.com/attachments/837564505952747520/863096755993575424/file.png",
  "10": "https://cdn.discordapp.com/attachments/837564505952747520/863096769843953694/file.png",
  "11": "https://cdn.discordapp.com/attachments/837564505952747520/863096776131477514/file.png",
  "12": "https://cdn.discordapp.com/attachments/837564505952747520/863096790915219456/file.png",
  "13": "https://cdn.discordapp.com/attachments/837564505952747520/863096799425331200/file.png",
  "14": "https://cdn.discordapp.com/attachments/837564505952747520/863096816592355328/file.png",
  "15": "https://cdn.discordapp.com/attachments/837564505952747520/863096830647468082/file.png",
  "16": "https://cdn.discordapp.com/attachments/837564505952747520/863096839246708786/file.png",
  "17": "https://cdn.discordapp.com/attachments/837564505952747520/863096852215234640/file.png",
  "18": "https://cdn.discordapp.com/attachments/837564505952747520/863096868589404170/file.png",
  "19": "https://cdn.discordapp.com/attachments/837564505952747520/863096879696445470/file.png",
  "20": "https://cdn.discordapp.com/attachments/837564505952747520/863096898818277436/file.png",
  "21": "https://cdn.discordapp.com/attachments/837564505952747520/863096905348153374/file.png",
  "22": "https://cdn.discordapp.com/attachments/837564505952747520/863096918074982460/file.png",
  "23": "https://cdn.discordapp.com/attachments/837564505952747520/863096933940461588/file.png",
  "24": "https://cdn.discordapp.com/attachments/837564505952747520/863096949799649280/file.png",
  "25": "https://cdn.discordapp.com/attachments/837564505952747520/863096964958388245/file.png",
  "26": "https://cdn.discordapp.com/attachments/837564505952747520/863096978476761128/file.png",
  "27": "https://cdn.discordapp.com/attachments/837564505952747520/863096996974166037/file.png",
  "28": "https://cdn.discordapp.com/attachments/837564505952747520/863097011842449458/file.png",
  "29": "https://cdn.discordapp.com/attachments/837564505952747520/863097028343103508/file.png",
  "30": "https://cdn.discordapp.com/attachments/837564505952747520/863097044230864896/file.png"
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
items_imgs = {'A wallet': 'https://cdn.discordapp.com/attachments/839080243485736970/881416732621819954/A_wallet.PNG', 'Antique Painting': 'https://cdn.discordapp.com/attachments/839080243485736970/881416745473146920/Antique_Painting.png', 'Black Pen': 'https://cdn.discordapp.com/attachments/839080243485736970/881416749159940096/Black_Pen.png', 'Book Stand': 'https://cdn.discordapp.com/attachments/839080243485736970/881416752653807677/Book_Stand.png', 'Broken CD': 'https://cdn.discordapp.com/attachments/839080243485736970/881416761101156383/Broken_CD.PNG', 'Broken Mouse': 'https://cdn.discordapp.com/attachments/839080243485736970/881416764582408212/Broken_Mouse.PNG', 'Broken String': 'https://cdn.discordapp.com/attachments/839080243485736970/881416769489739796/Broken_String.PNG', 'Broken Television': 'https://cdn.discordapp.com/attachments/839080243485736970/881416771985371146/Broken_Television.png', 'Bronze Spoon': 'https://cdn.discordapp.com/attachments/839080243485736970/881416774883622973/Bronze_Spoon.PNG', 'Charger': 'https://cdn.discordapp.com/attachments/839080243485736970/881416789026811964/Charger.PNG', 'Cloth Piece': 'https://cdn.discordapp.com/attachments/839080243485736970/881416792302555186/Cloth_Piece.PNG', 'Coffee Mug': 'https://cdn.discordapp.com/attachments/839080243485736970/881416796933062727/Coffee_Mug.png','Copper Wire': 'https://cdn.discordapp.com/attachments/839080243485736970/881416805887918130/Copper_Wire.PNG', 'Dead Calculator': 'https://cdn.discordapp.com/attachments/839080243485736970/881416811512487936/Dead_Calculator.PNG', 'Eaten Chocolate': 'https://cdn.discordapp.com/attachments/839080243485736970/881416814901477406/Eaten_Chocolate.PNG', 'Electric Drums': 'https://cdn.discordapp.com/attachments/839080243485736970/881416826326753350/Electric_Drums.png', 'Electric Guitar': 'https://cdn.discordapp.com/attachments/839080243485736970/881416831989088336/Electric_Guitar.PNG', 'Flower Vase': 'https://cdn.discordapp.com/attachments/839080243485736970/881416836938350602/Flower_Vase.PNG', 'Gaming Chair': 'https://cdn.discordapp.com/attachments/839080243485736970/881416841984081950/Gaming_Chair.png', 'Gold Brick': 'https://cdn.discordapp.com/attachments/839080243485736970/881416848481062982/Gold_Brick.png', 'Gold Chain': 'https://cdn.discordapp.com/attachments/839080243485736970/881416854814482472/Gold_Chain.PNG', 'Gold Spectacles': 'https://cdn.discordapp.com/attachments/839080243485736970/881416858589339668/Gold_Spectacles.png', 'Headphones': 'https://cdn.discordapp.com/attachments/839080243485736970/881416862645252117/Headphones.PNG', 'Hourglass': 'https://cdn.discordapp.com/attachments/839080243485736970/881416864968896522/Hourglass.PNG', 'Laptop': 'https://cdn.discordapp.com/attachments/839080243485736970/881416869666512926/Laptop.png', 'Laser Printer': 'https://cdn.discordapp.com/attachments/839080243485736970/881416872342462514/Laser_Printer.png', 'Leather Shoes': 'https://cdn.discordapp.com/attachments/839080243485736970/881416883201536000/Leather_Shoes.PNG', 'Lighter': 'https://cdn.discordapp.com/attachments/839080243485736970/881416891137159258/Lighter.PNG', 'Lollipop': 'https://cdn.discordapp.com/attachments/839080243485736970/881416896375828510/Lollipop.PNG', 'Magnifying Glass': 'https://cdn.discordapp.com/attachments/839080243485736970/881416901983612988/Magnifying_Glass.PNG', 'Maths Book': 'https://cdn.discordapp.com/attachments/839080243485736970/881416909491404820/Maths_Book.PNG', 'Mini Boom Box': 'https://cdn.discordapp.com/attachments/839080243485736970/881416916013551677/Mini_Boom_Box.png', 'Mobile Phone': 'https://cdn.discordapp.com/attachments/839080243485736970/881416920623099924/Mobile_Phone.PNG', 'Money Bag': 'https://cdn.discordapp.com/attachments/839080243485736970/881416925425569792/Money_Bag.PNG', 'Mouse Pad': 'https://cdn.discordapp.com/attachments/839080243485736970/881416932576878602/Mouse_Pad.PNG', 'N95 Mask': 'https://cdn.discordapp.com/attachments/839080243485736970/881416936993460254/N95_Mask.PNG', 'Office Bag': 'https://cdn.discordapp.com/attachments/839080243485736970/881416941741436938/Office_Bag.PNG', 'Party Speakers': 'https://cdn.discordapp.com/attachments/839080243485736970/881416946749431848/Party_Speakers.PNG', 'Pen Stand': 'https://cdn.discordapp.com/attachments/839080243485736970/881416951916802068/Pen_Stand.PNG', 'Piano': 'https://cdn.discordapp.com/attachments/839080243485736970/881416959286181978/Piano.png', 'RC Drone': 'https://cdn.discordapp.com/attachments/839080243485736970/881416970019414056/RC_Drone.PNG', 'Rotten Tomato': 'https://cdn.discordapp.com/attachments/839080243485736970/881416973660082236/Rotten_Tomato.PNG', 'Rubics Cube': 'https://cdn.discordapp.com/attachments/839080243485736970/881416977443323934/Rubics_Cube.PNG', 'Spray Can': 'https://cdn.discordapp.com/attachments/839080243485736970/881416986448523284/Spray_Can.PNG', 'Tennis Ball': 'https://cdn.discordapp.com/attachments/839080243485736970/881416990139490384/Tennis_Ball.png', 'Travel Bag': 'https://cdn.discordapp.com/attachments/839080243485736970/881416993671114752/Travel_Bag.PNG', 'Wall Clock': 'https://cdn.discordapp.com/attachments/839080243485736970/881416997743788032/Wall_Clock.PNG', 'War Sword': 'https://cdn.discordapp.com/attachments/839080243485736970/881417004106539028/War_Sword.png', 'WIFI Router': 'https://cdn.discordapp.com/attachments/839080243485736970/881417011522064405/WIFI_Router.png', 'Wooden Stick': 'https://cdn.discordapp.com/attachments/839080243485736970/881417017154998372/Wooden_Stick.PNG'}

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
    return
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

async def close_admin():
    with open('files/admin.json', 'w') as f:
        f.write(json.dumps(bot.admin, indent=2))

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

async def get_data_stock(file):
    with open(f'stocks/{file}', 'r') as f:
        return list(csv.reader(f))

async def update_awards():
    with open("files/awards.json", "w") as f:
        f.write(json.dumps(bot.awards, indent=2))

async def update_inv():
    with open('files/inventory.json', 'w') as e:
        e.write(json.dumps(bot.inventory, indent=2))

async def update_stockinfo(data):
    with open('files/stock_config.json', 'w') as stc:
        stc.write(json.dumps(data, indent=2))

async def update_stock_data():
    with open('files/stocks.json', 'w') as avgbal:
        avgbal.write(json.dumps(bot.stocks, indent=2))

async def update_badges(data):
    with open('files/badges.json', 'w') as b:
        b.write(json.dumps(data, indent=2))

async def update_avg():
    with open('files/average.json', 'w') as avgbal:
        avgbal.write(json.dumps(bot.avg, indent=2))

async def update_est():
    with open('files/estates.json', 'w') as f:
        f.write(json.dumps(bot.estates, indent=2))

async def update_alerts():
    with open('files/alerts.json', 'w') as f:
        f.write(json.dumps(bot.alertsinfo, indent=2))

async def update_logs(stuff: str):
    with open('files/logs.txt', 'a') as logs:
        logs.write(f'\n{stuff}')

async def update_accounts():
    with open('files/accounts.json', 'w') as f:
        f.write(json.dumps(bot.accounts, indent=2))

async def update_statements():
    with open('files/statements.json', 'w') as w:
        w.write(json.dumps(bot.statements, indent=2))

async def update_xp():
    with open('files/xp.json', 'w') as w:
        w.write(json.dumps(bot.xp, indent=2))

def update_sorted_inv(userid):
    userinv = bot.inventory.get(userid)
    if userinv is None:
        bot.cachedinv[userid] = ()
        return "userinv"
    itemsinv = userinv.get("items")
    embed = discord.Embed(color=embedcolor)
    if itemsinv is None:
        bot.cachedinv[userid] = ()
        return "itemsinv"

    done = []
    for items in userinv["items"]: done.append(items)
    invdict = {}
    for i in set(done):
        invdict[i] = done.count(i)
    bot.cachedinv[userid] = sorted(invdict.items(), key=lambda x: x[1], reverse=True)
    return bot.cachedinv[userid]

async def clear_dues():

    for i in bot.stocks:
        person = bot.accounts[str(i)]
        value = bot.stocks[str(i)]
        if value == 0:
            continue
        current_price = int(bot.current_stock[-1][5])

        bulk = int(current_price*value)
        person['bank'] += bulk
        bot.accounts[str(i)] = person
        bot.stocks[str(i)] = 0
        user = bot.get_user(i)
        if user is None:
            continue
        embed = discord.Embed(title='Stock Ended', description=f'The current stock ended and `{await commait(bulk)}` coins have been added to your bank.')
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_author(name=f'{user.name}', icon_url=user.display_avatar.url)
        embed.set_footer(text='Economy Bot', icon_url=bot.pfp)
        await user.send(embed=embed)
        await create_statement(user, bot.user, bulk, f"Sold {value} Stocks", "Credit")

    await update_accounts()
    await update_stock_data()
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

@tasks.loop(minutes=5)
async def est_update():
    keys = [x for x in bot.estates.keys()]

    for i in keys:
        person = bot.estates[i]
        lm = person['lm']
        pending = person['p']

        cur = time.time()
        diff = cur - lm

        if diff >= 172800:
            persona = bot.alertsinfo.get(i)
            if persona is None:
                continue

            state, last = persona['state'], persona['last']
            dm_diff = cur - last

            person['p'] = diff - 172800
            bot.estates[str(i)] = person
            await update_est()

            if state == 'on' and dm_diff > 21600:
                embed = discord.Embed(title='Maintenance Reminder',
                                      description='Your Hotel Maintenance is due. Use `e.maintain` to pay for it.\n'
                                                  'Note: You will get less revenue if maintenance isn\'t done!',
                                      colour=embedcolor)
                fetched = bot.get_user(int(i))
                if fetched is None:
                    continue
                embed.timestamp = datetime.datetime.utcnow()
                embed.set_author(name=f'{fetched.name}', icon_url=fetched.display_avatar.url)
                embed.set_footer(text='Economy Bot', icon_url=bot.pfp)

                persona['last'] = cur
                bot.alertsinfo[str(i)] = persona
                await update_alerts()
                await fetched.send(embed=embed)

@tasks.loop(minutes=5)
async def avg_update():
    data_keys = bot.accounts.keys()
    avg_keys = bot.avg.keys()

    for key in data_keys:
        if key not in avg_keys:
            bot.avg[key] = {'sum': 0, 'avg': 0, 'i': 1, 'claimed':0}

    for x in bot.avg:
        person_avg = bot.avg[x]

        newbal = bot.accounts.get(x, {"bank":None}).get('bank')
        if newbal is None: continue
        sum = person_avg['sum']

        newsum = sum + newbal
        person_avg['sum'] = newsum
        i = int(person_avg['i'])

        person_avg['avg'] = int(newsum / i)
        person_avg['i'] = i + 1
        bot.avg[x] = person_avg

    await update_avg()

@tasks.loop(minutes=5)
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

async def stock_update():
    while True:
        await update_stocks()
        await perform_stuff(bot.current_stock)
        await asyncio.sleep(86400/bot.total_lines)

async def check_storetime():
    with open('files/bot_data.json', 'r') as c:
        config = json.load(c)
    return config["shop"]["updated"]

async def open_account(userid):
    if bot.accounts.get(str(userid)) is None:
        bot.accounts[str(userid)] = {'bank_type':1, 'wallet':0, 'bank':1000, 'joined':datetime.date.today().strftime('%d-%m-%Y')}
        await update_accounts()

async def open_estates(userid):
    if bot.estates.get(str(userid)) is None:
        user = bot.get_user(userid)
        bot.estates[f'{userid}'] = {'level':1, 'name':f'{user.name}', 'lm':time.time(), 'lr':time.time(), 'p':0, 'c':0}

    await update_est()

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
    userid = str(userid)
    person = bot.alertsinfo.get(userid)
    if person is None:
        person = {'state':0, 'last':0}

    person['state'] = state
    bot.alertsinfo[userid] = person

    await update_alerts()

async def commait(val):
    return "{:,}".format(val)

async def current_time():
    return datetime.datetime.today().replace(microsecond=0)

async def create_statement(user, person, amount, reason, type):
    user_s = bot.statements.get(f'{user.id}')
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

    bot.statements[str(user.id)] = user_s
    await update_statements()

async def load_shop():
    with open('files/bot_data.json', 'r') as s:
        config = json.load(s)
    for i in config["shop"]["value"]:
        storeitems.append(i)

@tasks.loop(minutes=10)
async def bot_status():
    current_status = random.choice(bot.status)
    while True:
        if current_status["status"] == bot.raw_status: continue
        else: break

    guilds = len(bot.guilds)
    users = len(bot.users)
    s_type = current_status["type"]
    bot.raw_status = current_status["status"]
    s_status = bot.raw_status.format(users=await commait(users), guilds=await commait(guilds))
    if s_type == "p":
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=s_status))
    elif s_type == "w":
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=s_status))
    elif s_type == "l":
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=s_status))

async def create_stuff():
    tnew = time.time()
    await bot.wait_until_ready()
    print("Ready")
    mybot = bot.get_user(832083717417074689)
    bot.pfp = mybot.display_avatar.url
    tnew = time.time()
    await load_shop()
    with open('files/bot_data.json', 'r') as c:
        data = json.load(c)
    bot.status = data["status"]
    asyncio.create_task(stock_update())
    avg_update.start()
    shop_update.start()
    est_update.start()
    bot_status.start()
    await refresh()
    print(f'Caching done in {float("{:.2f}".format(time.time() - tnew))} secs')
    print(f'Loops created! Boot Time: {float("{:.2f}".format(time.time()-t1))} secs')

async def calculate_level(xp:int):
    level_found = -1
    for i in xp_levels.keys():
        if xp < i:
            for key, value in xp_levels.items():
                if i == key:
                    level_found = value
                    break
            if level_found != -1:
                break
        else:
            xp -= i
    return level_found, xp

async def calculate_networth(userid):
    userid = str(userid)
    networth = 0

    user = bot.accounts.get(userid, {"wallet":0, "bank":0})
    networth += user["wallet"] + user["bank"]

    user = bot.estates.get(userid, {"level":1})
    networth += (user["level"]-1)*10000

    user = bot.inventory.get(userid, {"inv":[], "items":[]})
    itemslist = user.get("items", [])
    invlist = user.get("inv", [])

    chestnetworths = {
        "Common Chest": 1000,
        "Rare Chest": 3500,
        "Legendary Chest": 10000,
        "Bronze Lock": 2500,
        "Silver Lock": 6000,
        "Gold Lock": 15000
    }
    for i in invlist:
        networth += chestnetworths[i]

    for i, rar in bot.items.items():
        for j in rar["items"]:
            while True:
                if j["name"] in itemslist:
                    networth += int((j["value"][0] + j["value"][1])/2)
                    itemslist.remove(j["name"])
                else:
                    break

    user = bot.stocks.get(userid, 0)
    networth += int(float(bot.current_stock[3]) * user)
    return networth

async def networth_lb(worth):
    all_networths = []
    for i in bot.accounts.keys():
        net = await calculate_networth(i)
        all_networths.append(net)

    all_networths.sort(reverse=True)
    rank = 1
    for ppl in all_networths:
        if worth >= ppl:
            break
        rank += 1

    return rank

async def add_xp_tm(userid):
    xp_timeout.append(userid)
    await asyncio.sleep(50)
    xp_timeout.remove(userid)

async def perform_stuff(data):
    stock_data = await get_stockconfigs()
    highest = float(stock_data.setdefault('highest', data[1]))
    lowest = float(stock_data.setdefault('lowest', data[2]))
    current = float(data[3])
    if highest < current:
        highest = current
    if lowest > current:
        lowest = current

    volume = 0
    for i in bot.stocks.values():
        volume += i
    stock_data['volume'] = volume
    stock_data['lowest'] = lowest
    stock_data['highest'] = highest
    await update_stockinfo(stock_data)

    return stock_data

async def get_avatar(user):
    return Image.open(BytesIO(await user.display_avatar.read())).resize((140, 140))

async def profile_image(member, level, userxp, xp, total_xp, guildid):
    font = ImageFont.truetype("badges/font2.ttf", 19)
    font_rank = ImageFont.truetype("badges/font2.ttf", 24)
    fontm = ImageFont.truetype("badges/font2.ttf", 13)
    fonts = ImageFont.truetype("badges/font2.ttf", 10)
    gadugi = ImageFont.truetype("badges/gadugi.ttf", 16)
    gadugi_b = ImageFont.truetype("badges/oswald.ttf", 26)

    img = Image.open("badges/levelbg.png")
    member_colour = (255, 42, 84)
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

    if str(member.id) in bot.badges['staff']: staff = True
    else: staff = False
    location = 710
    if staff:
        staff_icon = Image.open('badges/staff.png')
        pixdata = staff_icon.load()
        for y in range(staff_icon.size[1]):
            for x in range(staff_icon.size[0]):
                pixdata[x, y] = tuple(list((0, 255, 230)) + [pixdata[x, y][-1]])
        staff_icon = staff_icon.resize((37, 37))
        img.paste(staff_icon, (location, 55), staff_icon)
        staff_icon.close()
        location -= 45
    server_r, global_r = await xp_ranks(member.id, guildid)
    if global_r > 1000:
        global_r = 'Unknown'
    else:
        global_r = f'#{global_r}'
    draw = ImageDraw.Draw(img)
    newimg = Image.new('RGBA', img.size, (0,0,0,0))
    newdraw = ImageDraw.Draw(newimg)

    userinv = bot.inventory.get(str(member.id), [])
    if len(userinv) != 0:
        eq_lock = userinv.get('eq_lock')
        eq_boost = userinv.get('eq_boost')
        paste_loc = 332
        if eq_lock is None and eq_boost is None:
            newdraw.text((335, 145), 'None', font=ImageFont.truetype("badges/font2.ttf", 15), fill=(0,0,0))
    else:
        newdraw.text((335, 145), 'None', font=ImageFont.truetype("badges/font2.ttf", 15), fill=(0,0,0))
    networth = await calculate_networth(member.id)
    newdraw.text((180, 34), f'{member.name}#{member.discriminator}', font=font, fill='#000000')
    newdraw.text((180, 70), f"Level {level} | XP: {userxp}", font=fontm, fill='#000000')
    newdraw.text((120, 210), f'Server Rank', font=font, fill='#000000')
    newdraw.text((530, 210), f'Global Rank', font=font, fill='#000000')
    newdraw.text((120, 250), f'#{server_r}', font=font_rank, fill='#000000')
    newdraw.text((530, 250), f'{global_r}', font=font_rank, fill='#000000')
    newdraw.text((50, 355), f"Net Worth:  {await commait(networth)} coins", font=gadugi_b, fill='#000000')
    newdraw.text((50, 395), f"Join Date: {bot.accounts[str(member.id)]['joined']}", font=gadugi_b, fill='#000000')

    awards = {"estates": 'badges/awards/estates_{colortype}.png',
              "games":'badges/awards/games_{colortype}.png',
              "stocks":'badges/awards/stocks_{colortype}.png',
              "unbox":'badges/awards/unbox_{colortype}.png',
              "global":'badges/awards/global_{colortype}.png'}
    awardsdesc = {"estates":"Estates level 30",
                  "games":"Win 1000 games",
                  "stocks":"Buy 1 mil stocks",
                  "unbox":"Unbox every item",
                  "global":"           ???"}

    x2_loc = 50
    for i in awards.keys():
        newdraw.text((x2_loc, 585), awardsdesc[i], font=gadugi, fill=(0,0,0))
        x2_loc += 148

    newimg = newimg.filter(ImageFilter.GaussianBlur(radius=2))
    newimg = newimg.filter(ImageFilter.GaussianBlur(radius=4))
    img.paste(newimg, (0, 0), newimg)

    draw.text((180, 34), f'{member.name}#{member.discriminator}', (255, 255, 255), font=font)
    draw.text((180, 70), f"Level {level} | XP: {userxp}", font=fontm)
    draw.text((120, 210), f'Server Rank', font=font)
    draw.text((530, 210), f'Global Rank', font=font)
    draw.text((120, 250), f'#{server_r}', (255, 243, 0), font=font_rank)
    draw.text((530, 250), f'{global_r}', (255, 243, 0), font=font_rank)
    draw.text((50, 355), f"Net Worth:  {await commait(networth)} coins", font=gadugi_b)
    draw.text((50, 395), f"Join Date: {bot.accounts[str(member.id)]['joined']}", font=gadugi_b)

    twidth, theight = draw.textsize(f"{await commait(xp)}/{await commait(total_xp)}", fonts)
    draw.text((468 - (twidth / 2), 121 - (theight / 2)), f"{await commait(xp)}/{await commait(total_xp)}", (255, 255, 255), font=fonts, stroke_width=1, stroke_fill=(0, 0, 0))

    achi = bot.awards.get("achievements", {})
    user_a = achi.get(str(member.id), [])
    x_loc = 70
    x2_loc = 50
    for i in awards.keys():
        if i in user_a: colortype = "color"
        else: colortype = "bw"
        award = Image.open(awards[i].format(colortype=colortype)).resize((80, 80))
        img.paste(award, (x_loc, 500), award.convert("RGBA"))
        award.close()
        draw.text((x2_loc, 585), awardsdesc[i], font=gadugi, fill=(255, 255, 255))
        x_loc += 148
        x2_loc += 148

    if len(userinv) != 0:
        eq_lock = userinv.get('eq_lock')
        eq_boost = userinv.get('eq_boost')
        paste_loc = 332
        if eq_lock is not None:
            for i in storeitems:
                if eq_lock == i["name"]:
                    lock = Image.open(f'store/{i["icon"]}').resize((27, 27))
                    img.paste(lock, (paste_loc, 142), lock.convert('RGBA'))
                    lock.close()
        if eq_boost is not None:
            for i in storeitems:
                if eq_lock == i["name"]:
                    lock = Image.open(i["icon"]).resize((30, 30))
                    img.paste(lock, (paste_loc, 140), lock.convert('RGBA'))
                    lock.close()
        if eq_lock is None and eq_boost is None:
            draw.text((335, 145), 'None', font=ImageFont.truetype("badges/font2.ttf", 15))
    else:
        draw.text((335, 145), 'None', font=ImageFont.truetype("badges/font2.ttf", 15))
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
    return image_bytes

async def xp_ranks(member, guild):
    userid = str(member)
    xp_sorted_desc = sorted(bot.xp.items(), key=operator.itemgetter(1), reverse=True)
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
    server = bot.admin.get(str(guildid))
    if server is None: return True
    if len(server) == 0: return True
    if chlid in server: return True
    else: return False

async def get_errorfile():
    with open('files/errors.json', 'r') as f:
        return json.load(f)

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
    return image_bytes

async def inventory_image(userid):
    userid = str(userid)
    userinv = bot.inventory.get(userid, {"inv":[]})
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
    return image_bytes

async def general(ctx):
    state = await spam_protect(ctx.author.id)
    toreturn = True
    if state == 'warn':
        embed = discord.Embed(description=f'{economyerror} You are being rate-limited for using commands too fast!\nTry again in few secs..', color=error_embed)
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
    cmd = bot.cooldown[ctx.command.name]
    ifuser = [i for i in cmd["users"] if i[0] == ctx.author.id]
    if len(ifuser) != 0:
        left = cmd["duration"] - (time.time() - ifuser[0][1])
        if left > 0:
            final = datetime.datetime.strptime(str(datetime.timedelta(seconds=left)), '%H:%M:%S.%f')
            colon_format = str(final).split(" ")[1].split(':')
            ms = colon_format[2].split('.')
            mss = float("{:.2f}".format(float(ms[1])/6000))
            timeleft = f'{colon_format[1]}m {ms[0]}s {int(mss)}ms'
            await ctx.reply(f'{random.choice(bot.phrases["cooldown"]).format(timeleft=timeleft)}')
            raise IgnoreError
        else:
            bot.cooldown[ctx.command.name]["users"].remove(ifuser[0])
    else:
        bot.cooldown[ctx.command.name]["users"].append((ctx.author.id, time.time()))
    if ctx.author.id not in xp_timeout:
        userid = ctx.author.id
        xp = bot.xp.setdefault(str(userid), 0)
        togive = random.randint(10, 25)
        bot.xp[str(userid)] = xp + togive
        await update_xp()
        asyncio.create_task(add_xp_tm(userid))
    return toreturn

async def ttt_end(id1, id2, bet, ctx):
    winner = bot.accounts[str(id1.id)]
    winner["wallet"] += int(1.5*bet)
    bot.accounts[str(id1.id)] = winner
    games = bot.awards["games"]
    a = games.setdefault(str(id1.id), 0)
    games[str(id1.id)] = a+1
    bot.awards["games"] = games
    if a+1 == 1000: await achievement(ctx, id1.id, "games")

    await create_statement(id1, bot.user, 0.5*bet, "Won Tic-Tac-Toe", 'Credit')
    await create_statement(id2, bot.user, bet, "Lost Tic-Tac-Toe", 'Debit')
    await update_accounts()
    await update_awards()

async def ttt_tie(id1, id2, bet):
    winner1 = bot.accounts[str(id1)]
    winner1["wallet"] += bet
    bot.accounts[str(id1)] = winner1

    winner2 = bot.accounts[str(id2)]
    winner2["wallet"] += bet
    bot.accounts[str(id2)] = winner2

    await update_accounts()

async def achievement(ctx, userid, field):
    types = {
        "estates":"Estates Level 30",
        "games":"Win 1000 games",
        "stocks":"Buy 1 million stocks"
    }
    achi = bot.awards["achievements"]
    userid = str(userid)

    user_a = achi.setdefault(userid, [])
    user_a.append(field)
    achi[userid] = user_a

    bot.awards["achievements"] = achi
    user_d = bot.accounts[userid]
    user_d["wallet"] += 25000
    bot.accounts[userid] = user_d
    embed = discord.Embed(title="🏆 Achievement Unlocked!",
                          description=f"{ctx.author.mention} completed achievement- **{types[field]}!**\n"
                               f"Reward: `25,000` coins", color=embedcolor)
    embed.set_footer(text="Type e.pf to check your new badge!")
    await ctx.send(embed=embed)
    await update_awards()
    await update_accounts()

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if bot.dev == 1 and message.author.id not in (devs+staff): return
    if message.author.id in disregarded:
        if message.author.id not in devs: return
    if bot.maint and message.author.id not in devs:
        embed= discord.Embed(description=f"⚠️ The bot is in maintainance mode. Please retry later", color=error_embed)
        await message.reply(embed=embed)
        return
    if message.content.lower() == 'e.' or all(msg in message.content.lower() for msg in ["<@!832083717417074689>", "help"]):
        await message.reply('Do you need my help?\nGet started using `e.help`')
    await open_account(message.author.id)
    await bot.process_commands(message)

@bot.check
async def is_dm(ctx):
    return ctx.guild != None

@bot.check
async def if_allowed(ctx):
    return await check_channel(ctx.channel.id, ctx.guild.id)

#@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, UnboundLocalError) or isinstance(error, IgnoreError): return
    if isinstance(error, CommandNotFound):
        cmdused = ctx.invoked_with
        match = difflib.get_close_matches(cmdused, all_commands, cutoff=0.7)
        if len(match) == 0:
            embed = discord.Embed(description=f'{economyerror} The command you are trying to use doesn\'t exist.\n'
                                              f'Use `e.help` for list of commands', color=error_embed)
            embed.set_footer(text="No suggestions found")
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=f"<a:Unknown:849189167522381834> Do you mean `{match[0]}`?", color=embedcolor)
            prev = await ctx.send(embed=embed)
            common_yes = ["yes", "ye", "yeah", "yea", "ya", "yah", "ofc", "of course"]
            def check(res):
                return res.author == ctx.author and res.channel == ctx.channel
            res = await bot.wait_for("message", check=check)
            if any(x in res.content.lower() for x in common_yes):
                embed = discord.Embed(title=f"{economysuccess} You meant `{match[0]}`", color=success_embed)
                await prev.edit(embed=embed)
                corrected = ctx.message
                splits = corrected.content.split(' ')
                corrected.content = f"e.{match[0]} {' '.join(splits[1:])}"
                await bot.process_commands(corrected)
            else:
                embed = discord.Embed(title=f"{economyerror} You didn't mean `{match[0]}`", color=error_embed)
                return await prev.edit(embed=embed)
        return
    if isinstance(error, CheckFailure):
        embed = discord.Embed(description=f'{economyerror} You are not qualified to use this command!', color=error_embed)
        return await ctx.send(embed=embed)
    if isinstance(error, MissingRequiredArgument):
        embed = discord.Embed(description=f'{economyerror} Missing an argument! Use `e.help {ctx.invoked_with}` for syntax.', color=error_embed)
        return await ctx.send(embed=embed)
    if isinstance(error, BadArgument):
        embed = discord.Embed(description=f'{economyerror} Bad/Incorrect argument(s)! Use `e.help {ctx.invoked_with}` for syntax.', color=error_embed)
        return await ctx.send(embed=embed)
    code = hex(random.randint(1000, 9999))

    etype = type(error)
    trace = error.__traceback__
    lines = traceback.format_exception(etype, error, trace)
    traceback_text = ''.join(lines)
    a = await debugcode(code, f'{ctx.author} ({ctx.author.id}) =>\n**Command:** `{ctx.command}`\n**Message:** `{ctx.message.content}`\n**Error:** ```py\n{traceback_text}```')
    if not a:
        while True:
            code = hex(random.randint(1000, 9999))
            a = await debugcode(code, f'{ctx.author} ({ctx.author.id}) =>\n\n**Command:** `{ctx.command}`\n**Message:** `{ctx.message.content}`\n**Error:** ```py\n{traceback_text}```')
            if a: break
    embed = discord.Embed(title=f'{economyerror} Oops! You just ran into an error',
                          description=f'Kindly report this error using **`e.report {code}`** for further investigation',
                          color=error_embed)
    embed.set_footer(text='For a unique and error that is never been reported before, you get `1,000` coins!\n'
                          'Sorry for the inconvinience')
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)

@bot.event
async def on_raw_reaction_add(payload):
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

class IgnoreError(commands.CheckFailure):
    pass

@bot.command()
@commands.check(general)
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

@bot.command(hidden=True)
@commands.check(is_dev)
async def debug(ctx, code):
    a = await get_errorfile()
    if code not in a:
        return await ctx.send('No matching code found!')
    desc = a[code]
    if len(desc) > 2048:
        desc = a[code][:2045] + '```'
    embed=discord.Embed(title=f'Error {code}',
                        description=desc,
                        color=success_embed)
    await ctx.send(embed=embed)

@bot.command(hidden=True)
@commands.check(is_dev)
async def dvm(ctx):
    if bot.dev == 1:
        await ctx.reply('Changed Dev Mode state to: **`Off`**')
        bot.dev = 0
    else:
        await ctx.reply('Changed Dev Mode state to: **`On`**')
        bot.dev = 1

@bot.command(hidden=True)
@commands.check(is_dev)
async def maint(ctx):
    if bot.maint:
        await ctx.reply(f"Maintainence mode state: **Off**")
        bot.maint = False
    else:
        await ctx.reply(f"Maintainence mode state: **On**")
        bot.maint = True

@bot.command(hidden=True)
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

@bot.command(aliases=['eval'],hidden=True)
async def evaluate(ctx, *, expression):
    if ctx.author.id == 669816890163724288:
        try:
            await ctx.reply(eval(expression))
        except Exception as e:
            await ctx.reply(f'```\n{e}```')
    elif ctx.author.id == 771601176155783198:
        try:
            calculated = aeval(expression)
            msg = await ctx.send('Evaluating Expression..')
            if len(aeval.error) > 0:
                calculated = ""
                for err in aeval.error:
                    for er2 in err.get_error(): calculated += str(er2) + '\n'
            await msg.edit(content=f'Input:\n```py\n{expression}```\nOutput:\n```py\n{calculated}```')
        except Exception as ex:
            await ctx.send(
                f"```py\n{''.join(traceback.format_exception(etype=type(ex), value=ex, tb=ex.__traceback__))}\n```")

@bot.command(aliases=['exec'],hidden=True)
async def execute(ctx, *, expression):
    if ctx.author.id != 669816890163724288: return
    try:
        exec(expression.replace('```', ''))
    except Exception as e:
        await ctx.reply(f'Command:```py\n{expression}```\nOutput:```\n{e}```')

@bot.command(hidden=True)
@commands.check(is_dev)
async def add(ctx, person:discord.Member, bal:int, *args):
    toadd = bot.accounts.get(f'{person.id}')

    if '-b' in args:
        new_bal = toadd['bank'] + bal
        toadd['bank'] = new_bal
    else:
        new_bal = toadd['wallet'] + bal
        toadd['wallet'] = new_bal
    bot.accounts[f'{person.id}'] = toadd
    await update_accounts()

    await update_logs(f'{ctx.author}-!-add-!-[{person.id}; {await commait(bal)}]-!-{await current_time()}')
    await ctx.send(f'{ctx.author.mention} added `{await commait(bal)}` coins to {person.name}.')

@bot.command(hidden=True)
@commands.check(is_staff)
async def clear(ctx, member:discord.Member):
    userid = str(member.id)

    person = bot.accounts[userid]
    person['bank'] = 0
    person['wallet'] = 0

    bot.accounts[userid] = person
    await update_accounts()
    await update_logs(f'{ctx.author}-!-clear-!-[{member.id}]-!-{datetime.datetime.today().replace(microsecond=0)}')
    await ctx.send(f'{ctx.author.mention} Cleared data of `{member.name}#{member.discriminator}` successfully!')

@bot.command(hidden=True)
@commands.is_owner()
async def release(ctx, title:str, fake:int=0):
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

@bot.command(hidden=True)
@commands.check(is_staff)
async def stockinfo(ctx):
    with open(f'stocks/{await get_todays_stock()}', 'r') as f:
        stock = list(csv.reader(f))
    config = await get_stockconfigs()

    embed = discord.Embed(title='Stock Info', color=embedcolor)
    embed.add_field(name='Total Rows', value=f'{len(stock)}')
    embed.add_field(name='Current Row', value=f'{config["line"]}')
    embed.add_field(name='Approx Refresh Time', value=f'{round(86400/len(stock), 4)} secs')
    secs = int((len(stock)-config["line"])*round(86400/len(stock), 4) + time.time())
    embed.add_field(name='Ending Time', value=f'<t:{secs}:f> (<t:{secs}:R>)')

    await ctx.send(embed=embed)

@bot.command()
@commands.check(general)
async def uptime(ctx):
    delta_uptime = datetime.datetime.utcnow() - bot.launch_time
    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    await ctx.reply(f"I have been up for `{days}d, {hours}h, {minutes}m, {seconds}s`")

async def refresh():
    with open('files/bot_data.json', 'r') as c:
        data = json.load(c)
    bot.phrases = data["phrases"]
    bot.help_json = data["help"]
    bot.shopc = data["shop"]["category"]
    bot.items = data["items"]
    bot.status = data["status"]
    bot.cooldown = data["cooldown"]

    print('Caching Items')
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
    with ThreadPoolExecutor(max_workers=1) as executor:
        await bot.loop.run_in_executor(executor, functools.partial(cache_allitems))

@bot.command(hidden=True)
@commands.check(is_dev)
async def resetdb(ctx):
    with open('files/accounts.json', 'w') as f:
        f.write("{}")
    with open('files/alerts.json', 'w') as f:
        f.write("{}")
    with open('files/average.json', 'w') as f:
        f.write("{}")
    with open('files/awards.json', 'w') as f:
        f.write("{}")
    with open('files/estates.json', 'w') as f:
        f.write("{}")
    with open('files/inventory.json', 'w') as f:
        f.write("{}")
    with open('files/statements.json', 'w') as f:
        f.write("{}")
    with open('files/stocks.json', 'w') as f:
        f.write("{}")
    with open('files/timeouts.json', 'w') as f:
        f.write("{}")
    with open('files/xp.json', 'w') as f:
        f.write("{}")
    await ctx.message.add_reaction(economysuccess)

@bot.command(aliases=['bal'])
@commands.check(general)
async def balance(ctx, member:discord.Member = None):
    if member is None:
        userid = ctx.author.id
    else:
        userid = member.id
    await open_account(userid)
    person = bot.accounts.get(str(userid))
    bank_type = person['bank_type']
    wallet = person['wallet']
    bank = person['bank']
    stocks_num = bot.stocks.get(str(userid), 0)
    embed = discord.Embed(title=f'__{bank_details[bank_type]["name"]}__', colour=embedcolor)
    embed.add_field(name=f'**<:wallet:836814969290358845> Wallet**', value=f'> `{await commait(wallet)}`', inline=False)
    embed.add_field(name=f'**🏦 Bank**', value=f'> `{await commait(bank)}`', inline=False)
    embed.add_field(name=f'**<:stocks:839162083324198942> Stocks**', value=f'> `{await commait(stocks_num)}`', inline=False)
    fetched = bot.get_user(userid)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text='Economy Bot', icon_url=bot.pfp)
    embed.set_author(name=fetched.name, icon_url=fetched.display_avatar.url)

    await ctx.send(embed=embed)

@bot.command(aliases=['dep'])
@commands.check(general)
async def deposit(ctx, amount:str):
    person = bot.accounts.get(f'{ctx.author.id}')
    wallet = person['wallet']
    bank = person['bank']
    if amount == 'all':
        amount = wallet
    elif amount == 'half':
        amount = int(wallet/2)
    else:
        amount = int(amount)
    if amount < 0:
        return await ctx.send(f'{ctx.author.mention} {random.choice(bot.phrases["negative"])}')
    if amount == 0:
        return await ctx.send(f'{ctx.author.mention} {random.choice(bot.phrases["zero"])}')
    if wallet < amount:
        return await ctx.send(f'{ctx.author.mention} {random.choice(bot.phrases["less_bal"])}')

    newbal_w = wallet - amount
    newbal_b = bank + amount

    person['wallet'] = newbal_w
    person['bank'] = newbal_b
    bot.accounts[f'{ctx.author.id}'] = person

    await update_accounts()
    await ctx.send(f'{ctx.author.mention} Successfully deposited `{await commait(amount)}` coins.')

@bot.command(aliases=['with'])
@commands.check(general)
async def withdraw(ctx, amount: str = None):
    if amount is None:
        await ctx.reply('`e.with <amount>`, idiot.')
    person = bot.accounts.get(f'{ctx.author.id}')
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
    bot.accounts[f'{ctx.author.id}'] = person

    await update_accounts()
    await ctx.send(f'{ctx.author.mention} Successfully withdrew `{await commait(amount)}` coins.')

@bot.command()
@commands.check(general)
async def bank(ctx, member:discord.Member = None):
    if member is None:
        userid = ctx.author.id
    else:
        userid = member.id
    await open_account(userid)
    await avg_update()

    person = bot.accounts.get(f'{userid}')
    person2 = bot.avg.get(f'{userid}')
    btype = person['bank_type']

    embed = discord.Embed(description='Here are your bank details:\n\u200b', color=embedcolor)
    embed.add_field(name='Bank Name', value=f'{bank_details[btype]["name"]}')
    embed.add_field(name='Bank Tier', value=f'{bank_details[btype]["tier"]}')
    embed.add_field(name='\u200b', value='\u200b')
    embed.add_field(name='Daily Interest', value=f'{bank_details[btype]["rate"]}%')
    embed.add_field(name='Current Balance', value=f'`{await commait(person["bank"])}`')
    embed.add_field(name='Average Balance', value=f'`{await commait(person2["avg"])}`')
    embed.add_field(name='Note:', value='To claim interest, use `e.daily`.\n'
                                        'Your average balance in last 24 hours will be taken in account for that.')
    fetched = bot.get_user(userid)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text='Economy Bot', icon_url=bot.pfp)
    embed.set_author(name=f'{fetched.name} | 🏦 Know Your Bank!', icon_url=fetched.display_avatar.url)

    view = Bank(ctx)
    msg = await ctx.send(embed=embed, view=view)
    view.msg = msg

class Bank(discord.ui.View):
    def __init__(self, ctx: Context):
        super().__init__()
        self.ctx = ctx
        self.msg = None

    @discord.ui.button(label="Change Tier", style=discord.ButtonStyle.green)
    async def tier(self, button, interaction: discord.Interaction):
        ctx = self.ctx
        x = PrettyTable()
        x.field_names = ["Bank Name", "Tier", "Interest"]
        for i in bank_details.values():
            x.add_row([i["name"], i["tier"], f'{i["rate"]}%'])
        embed = discord.Embed(title='List of Banks',
                              description=f'Choose your bank to get higher interest rate, loans and more benefits!\n```\n{x}```\n',
                              color=embedcolor)
        fetched = bot.get_user(ctx.author.id)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text='Economy Bot', icon_url=bot.pfp)
        embed.set_author(name=fetched.name, icon_url=fetched.display_avatar.url)
        self.clear_items()
        self.add_item(BankTiers(ctx, self.msg))
        await interaction.response.send_message(embed=embed, ephemeral=True, view=self)

    async def on_timeout(self):
        for child in self.children:
            child.disabled = True
        await self.msg.edit(view=self)

class BankTiers(discord.ui.Select):
    def __init__(self, ctx: Context, msg):
        options = [
            discord.SelectOption(label='Tier I', emoji='🏦', description="Common Finance Bank Ltd."),
            discord.SelectOption(label='Tier II', emoji='🏦', description="National Bank Pvt. Ltd."),
            discord.SelectOption(label='Tier III', emoji='🏦', description="International Bank of Finance Ltd."),
        ]
        self.ctx = ctx
        self.msg = msg
        super().__init__(placeholder='Click here to choose tier...', min_values=1, max_values=1,
                         options=options, row=4)

    async def callback(self, interaction: discord.Interaction):
        assert self.view is not None
        view: UpgradeBank = self.view
        if interaction.user != view.ctx.author:
            return await interaction.response.send_message(
                random.choice(bot.phrases["inter"]).format(usertag=str(view.ctx.author)))

        tlist = {'Tier I': 1, 'Tier II': 2, 'Tier III':3}
        tier = tlist[self.values[0]]
        ctx = self.ctx
        user = bot.accounts[str(ctx.author.id)]

        if tier <= 0 or tier > 3:
            return await interaction.response.edit_message(content=f'{ctx.author.mention} Invalid Tier')
        if user['bank_type'] == tier:
            return await interaction.response.edit_message(content=f'{ctx.author.mention} You already own a account in this bank')
        elif user['bank_type'] > tier:
            return await interaction.response.edit_message(content=f'{ctx.author.mention} You cannot downgrade your bank tier')

        bal = user['wallet'] + user['bank']
        price = 5000 if tier == 2 else 10000
        total = int(bal * 0.01 + price)

        x = PrettyTable()
        x.field_names = ['Name', '      ', 'Cost']
        x.align["Cost"] = "l"
        x.add_row(['Account Opening', '      ', price])
        x.add_row(['Transfering', '      ', bal * 0.01])
        x.add_row(['      ', '      ', '      '])
        x.add_row(['Grand Total', '      ', total])

        embed = discord.Embed(title='Upgrade your bank',
                              description=f'Here is the cost for upgrading your bank: \n```\n{x}```',
                              color=embedcolor)
        await interaction.response.edit_message(embed=embed, view=UpgradeBank(ctx, tier, self.msg))

class UpgradeBank(discord.ui.View):
    def __init__(self, ctx: Context, tier: int, msg):
        super().__init__()
        self.ctx = ctx
        self.tier = tier
        self.msg = msg

    @discord.ui.button(label="Accept", style=discord.ButtonStyle.green)
    async def accept(self, button, interaction: discord.Interaction):
        ctx = self.ctx
        tier = self.tier
        user = bot.accounts[str(ctx.author.id)]
        bal = user['wallet'] + user['bank']
        price = 5000 if tier == 2 else 10000
        total = int(bal * 0.01 + price)
        if total > user["bank"]:
            embed = discord.Embed(title=f'{economyerror} Insufficient Funds in bank!',
                                  description=random.choice(bot.phrases["less_bal"]),
                                  color=error_embed)
        else:
            user["bank"] = user["bank"] - total
            user["bank_type"] = tier
            bot.accounts[str(ctx.author.id)] = user
            await update_accounts()
            embed = discord.Embed(title=f'{economysuccess} Success!',
                                  description=f'Bank upgraded to `Tier {tier}` successfully!',
                                  color=success_embed)
        await interaction.response.edit_message(embed=embed, view=None)

    @discord.ui.button(label="Cancel", style=discord.ButtonStyle.red)
    async def cancel(self, button, interaction: discord.Interaction):
        embed = discord.Embed(title=f'{economyerror} Cancelled!', color=error_embed)
        await interaction.response.edit_message(embed=embed, view=None)

    async def on_timeout(self):
        for child in self.children:
            child.disabled = True
        await self.msg.edit(view=self)

@bot.command()
@commands.check(general)
async def daily(ctx):
    await avg_update()

    avg_p = bot.avg.get(f'{ctx.author.id}')
    data_p = bot.accounts.get(f'{ctx.author.id}')
    if avg_p is not None:
        i = avg_p['i']
    else:
        i = 0
    check = await checktimeout(ctx.author.id, 'daily')
    time_gap = 86400 - check
    if time_gap > 0 and check != 0:
        left = int(time_gap + time.time())
        return await ctx.reply(f'You can claim next daily interest at <t:{left}:f> (<t:{left}:R>).')
    btype = data_p['bank_type']
    avgbal = avg_p['avg']
    bank_d = data_p['bank']
    multiplier = (bank_details[btype]["rate"])/100

    newbal = bank_d + int(avgbal * multiplier)
    data_p['bank'] = newbal
    bot.accounts[f'{ctx.author.id}'] = data_p
    avg_p['claimed'] = 1
    avg_p['sum'] = int(avgbal)
    avg_p['i'] = 1

    bot.avg[f'{ctx.author.id}'] = avg_p

    await update_avg()
    await update_accounts()
    await add_timeout(ctx.author.id, 'daily')
    embed = discord.Embed(title=f'{economysuccess} Claimed Successfully!', description=f'Daily interest payout of `{await commait(int(avgbal * multiplier))}` coins credited successfully!', color=success_embed)
    await ctx.send(embed=embed)

@bot.command()
@commands.check(general)
async def give(ctx, member:discord.Member, amount:int):
    await open_account(member.id)
    await open_account(ctx.author.id)
    author = bot.accounts.get(f'{ctx.author.id}')
    person = bot.accounts.get(f'{member.id}')

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
    bot.accounts[f'{ctx.author.id}'] = author

    p_wallet = person['wallet']
    person['wallet'] = p_wallet + amount
    bot.accounts[f'{member.id}'] = person

    await update_accounts()

    embed = discord.Embed(title=f'{economysuccess} Success!', color=embedcolor,
                          description=f'You gave `{await commait(amount)}` coin(s) to {member.mention}. What an act of generosity!')
    fetched = bot.get_user(ctx.author.id)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text='Economy Bot', icon_url=bot.pfp)

    await ctx.send(embed=embed)

@bot.command(aliases=['property'])
@commands.check(general)
async def estates(ctx, member:discord.Member=None):
    if member is None:
        userid = ctx.author.id
    else:
        userid = member.id

    await open_estates(userid)
    person = bot.estates[f'{userid}']
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
    embed.set_author(name=f'{fetched.name} | {name} Hotel', icon_url=fetched.display_avatar.url)
    url = getestates_thumb[str(level)]
    embed.set_image(url=f"{url.replace('cdn.discordapp.com', 'media.discordapp.net')}?width=500&height=400")
    view = Estates(ctx)
    msg = await ctx.send(embed=embed, view=view)
    view.msg = msg

class Estates(discord.ui.View):
    def __init__(self, ctx: Context):
        super().__init__()
        self.ctx = ctx
        self.msg = None
    
    @discord.ui.button(label="Upgrade", style=discord.ButtonStyle.blurple)
    async def upgrade(self, button, interaction: discord.Interaction):
        ctx = self.ctx
        if interaction.user != ctx.author:
            return await interaction.response.send_message(
                random.choice(bot.phrases["inter"]).format(usertag=str(ctx.author)),
                ephemeral=True)
        userid = ctx.author.id
        await open_estates(userid)
        eperson = bot.estates[f'{ctx.author.id}']
        level = eperson['level']
        name = eperson['name']
        if level == 30:
            embed = discord.Embed(title='Maxed Out!',
                                  description='You are already at the maximum level, Chill down mate!',
                                  color=embedcolor)
            fetched = bot.get_user(ctx.author.id)
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text='Economy Bot', icon_url=bot.pfp)
            embed.set_author(name=f'{fetched.name} | {name} Hotel', icon_url=fetched.display_avatar.url)

            return await interaction.response.send_message(embed=embed, ephemeral=True)

        rev_now = await get_revenue(level)
        rev_after = await get_revenue(level + 1)
        main_now = await get_maint(level)
        main_after = await get_maint(level + 1)

        cost = await get_cost(level)

        embed = discord.Embed(title='Upgrade Hotel', colour=embedcolor)
        if level < 30:
            embed.add_field(name='Level Change', value=f'`{level} => {level + 1}`')
        else:
            embed.add_field(name='Level Change', value=f'``{level} => Maxed Out!`')
        embed.add_field(name='Revenue Boost',
                        value=f'`{await commait(rev_now)} + {await commait(rev_after - rev_now)}` coins')
        embed.add_field(name='Maintainance Increase',
                        value=f'`{await commait(main_now)} + {await commait(main_after - main_now)}` coins')
        embed.add_field(name='Upgrade Cost', value=f'`{await commait(cost)}` coins')
        embed.add_field(name='Confirm?', value=f'Click {economysuccess} to confirm or {economyerror} to cancel',
                        inline=False)
        embed.add_field(name='\u200b', value='Here is the look after upgrade:', inline=False)
        url = getestates_thumb[str(level + 1)]
        embed.set_image(url=f"{url.replace('cdn.discordapp.com', 'media.discordapp.net')}?width=500&height=400")
        fetched = bot.get_user(ctx.author.id)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text='Economy Bot', icon_url=bot.pfp)
        embed.set_author(name=f'{fetched.name} | {name} Hotel', icon_url=fetched.display_avatar.url)

        msg = await interaction.response.send_message(embed=embed, ephemeral=True, view=EstatesUpgrade(ctx, self.msg, cost, level))

    @discord.ui.button(label="Collect Revenue", style=discord.ButtonStyle.green)
    async def revenue(self, button, interaction: discord.Interaction):
        ctx = self.ctx
        if interaction.user != ctx.author:
            return await interaction.response.send_message(
                random.choice(bot.phrases["inter"]).format(usertag=str(ctx.author)),
                ephemeral=True)
        embed = await revenue(ctx, via=True)
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @discord.ui.button(label="Maintain", style=discord.ButtonStyle.red)
    async def maintain(self, button, interaction: discord.Interaction):
        ctx = self.ctx
        if interaction.user != ctx.author:
            return await interaction.response.send_message(
                random.choice(bot.phrases["inter"]).format(usertag=str(ctx.author)),
                ephemeral=True)
        embed = await maintain(ctx, via=True)
        await interaction.response.send_message(embed=embed, ephemeral=True)

class EstatesUpgrade(discord.ui.View):
    def __init__(self, ctx: Context, msg: discord.Message, cost: int, level: int):
        super().__init__()
        self.ctx, self.msg = ctx, msg
        self.cost, self.level = cost, level

    @discord.ui.button(label="Accept", style=discord.ButtonStyle.green)
    async def accept(self, button, interaction: discord.Interaction):
        ctx = self.ctx
        cost = self.cost
        level = self.level
        person = bot.accounts[f'{ctx.author.id}']
        wallet = person['wallet']
        bank = person['bank']

        if cost > wallet:
            left = cost - wallet
            new_wallet = 0
            if left > bank:
                embed = discord.Embed(title=f'{economyerror} Oopsie!',
                                      description='Looks like there aren\'t enough coins in your bank. Please deposit or earn more.',
                                      color=error_embed)
                return await interaction.response.edit_message(embed=embed)
            new_bank = bank - left
        else:
            new_wallet = wallet - cost
            new_bank = bank

        eperson = bot.estates[f'{ctx.author.id}']
        person['wallet'] = new_wallet
        person['bank'] = new_bank
        eperson['level'] = level + 1

        bot.estates[f'{ctx.author.id}'] = eperson
        bot.accounts[f'{ctx.author.id}'] = person

        await update_accounts()
        await update_est()
        embed = discord.Embed(title=f'{economysuccess} Success!',
                              description='Wohoo! Your upgrade was successful! Use `e.estates` to see newly upgraded property!',
                              color=success_embed)
        await interaction.response.edit_message(embed=embed, view=None)
        if level + 1 == 30: await achievement(ctx, ctx.author.id, "estates")

    @discord.ui.button(label="Decline", style=discord.ButtonStyle.red)
    async def decline(self, button, interaction: discord.Interaction):
        embed = discord.Embed(title=f'{economyerror} Cancelled!', color=error_embed)
        await interaction.response.edit_message(embed=embed, view=None)

@bot.command(hidden=True)
@commands.check(is_dev)
async def disregard(ctx, member:discord.Member):
    if member.id in disregarded: disregarded.remove(member.id)
    else: disregarded.append(member.id)
    await ctx.message.add_reaction(economysuccess)

@bot.command()
@commands.check(general)
async def revenue(ctx, via=False):
    userid = ctx.author.id
    await open_estates(userid)
    await est_update()
    person = bot.estates[f'{ctx.author.id}']

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
    embed.set_author(name=f'{fetched.name} | {name} Hotel', icon_url=fetched.display_avatar.url)

    persona = bot.accounts[f'{ctx.author.id}']
    bank_ = persona['bank']
    persona['bank'] = bank_ + totalpay
    bot.accounts[f'{ctx.author.id}'] = persona
    person['lr'] = time.time()
    person['pending'] = 0
    person['c'] = 1
    bot.estates[f'{ctx.author.id}'] = person

    await update_est()
    await update_accounts()
    if via: return embed
    await ctx.send(embed=embed)

@bot.command()
@commands.check(general)
async def maintain(ctx, via=False):
    userid = ctx.author.id
    await open_estates(userid)
    userid = str(ctx.author.id)

    persona = bot.accounts[userid]
    person = bot.estates[userid]

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
        bot.accounts[userid] = persona

        person['lm'] = time.time()
        person['p'] = 0
        bot.estates[userid] = person

        await update_accounts()
        await update_est()

        embed = discord.Embed(title=f'{economysuccess} Success!',
                              description=f'`{cost_d}.00` coins have been deducted and your hotel looks shining new!\n```css\n{x}```',
                              color=success_embed)

    fetched = bot.get_user(ctx.author.id)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text='Economy Bot', icon_url=bot.pfp)
    embed.set_author(name=f'{fetched.name} | {name} Hotel', icon_url=fetched.display_avatar.url)
    if via: return embed
    await ctx.send(embed=embed)

@bot.command()
@commands.check(general)
async def alerts(ctx):
    embed = discord.Embed(title='Alerts System',
                          description='Get Alerts on pending loans, hotel maintainance, robberies etc straight to your DMs',
                          color=embedcolor)
    current = bot.alertsinfo.get(str(ctx.author.id), 'off')

    embed.add_field(name='Current State', value=current)
    fetched = bot.get_user(ctx.author.id)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_author(name=f'{fetched.name}', icon_url=fetched.display_avatar.url)
    embed.set_footer(text='Economy Bot', icon_url=bot.pfp)
    view = Alerts(ctx)
    msg = await ctx.send(embed=embed, view=view)
    view.msg = msg

class Alerts(discord.ui.View):
    def __init__(self, ctx: Context):
        super().__init__()
        self.ctx = ctx
        self.msg = None

    async def on_timeout(self) -> None:
        for i in self.children:
            i.disabled = True
        await self.msg.edit(view=self)

    @discord.ui.button(label="Turn On", style=discord.ButtonStyle.green)
    async def turnOn(self, button, interaction: discord.Interaction):
        ctx = self.ctx
        embed = discord.Embed(title=f'{economysuccess} Success!',
                              description='Alerts are switched **On**. Make sure you have your DMs open',
                              colour=success_embed)

        await interaction.response.send_message(embed=embed, ephemeral=True)
        await alerts_state(ctx.author.id, 'on')

    @discord.ui.button(label="Turn Off", style=discord.ButtonStyle.red)
    async def turnOff(self, button, interaction: discord.Interaction):
        ctx = self.ctx
        embed = discord.Embed(title=f'{economysuccess} Success!',
                              description='Alerts are switched **Off**. "Yay no more DMs" huh?',
                              colour=success_embed)
        await interaction.response.send_message(embed=embed, ephemeral=True)
        await alerts_state(ctx.author.id, 'off')

@bot.command()
@commands.check(general)
async def transfer(ctx, togive:discord.Member = None, amount = None, *, reason = None):
    await open_account(togive.id)
    await open_account(ctx.author.id)
    if togive is None or amount is None:
        return await ctx.send(f'{ctx.author.mention} The format for the command is: `e.transfer @user <amount> [reason]`')
    current = bot.accounts[f'{ctx.author.id}']
    person = bot.accounts[f'{togive.id}']

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

    bot.accounts[f'{togive.id}'] = person
    bot.accounts[f'{ctx.author.id}'] = current

    await update_accounts()
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
    embed.set_author(name=f'{fetched.name}', icon_url=fetched.display_avatar.url)

    await ctx.send(embed=embed)

@bot.command(aliases=['transactions'])
@commands.check(general)
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

    all_s = bot.statements.get(str(member.id))
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

@bot.command(aliases=['pf', 'level', 'p'])
@commands.check(general)
async def profile(ctx, member:discord.Member = None):
    if member is None:
        member = ctx.author

    xp = bot.xp.setdefault(f'{member.id}', 0)
    lev, newxp = await calculate_level(xp)

    max_xp = 0
    for key, value in xp_levels.items():
        if lev == value:
            max_xp = key
            break
    bytes = await profile_image(member, lev, xp, newxp, max_xp, ctx.guild.id)
    await uploader.upload_file(ctx.channel, bytes, filename="level.png")

@bot.command()
@commands.check(general)
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

    fig = plt.gcf()
    fig.set_size_inches(6, 4.5)
    plt.savefig('graph.png', transparent=True)
    plt.close()

    secs = int((len(stock_data) - config["line"]) * round(86400 / len(stock_data), 4) + time.time())
    holdings = bot.stocks.get(str(ctx.author.id), 0)
    embed = discord.Embed(title='Today\'s Stock', description=f'```\n{x}```', color=embedcolor)
    embed.add_field(name='Your Holdings', value=f'`{await commait(holdings)}` stocks')
    embed.add_field(name='Current Value', value=f'`{await commait(int(holdings*float(details[3])))}` coins')
    embed.add_field(name='Time Left', value=f'<t:{secs}:f> (<t:{secs}:R>)')

    embed.set_image(url="attachment://graph.png")
    view = StocksBuySell(ctx)
    msg = await ctx.send(embed=embed, file=discord.File('graph.png', filename="graph.png"), view=view)
    view.msg = msg

class StocksBuySell(discord.ui.View):
    def __init__(self, ctx: Context):
        super().__init__()
        self.ctx = ctx
        self.msg = None

    def check(self, msg):
        return msg.author == self.ctx.author and msg.channel == self.ctx.channel

    @discord.ui.button(label="Buy", style=discord.ButtonStyle.green)
    async def buy(self, button, interaction: discord.Interaction):
        await interaction.response.send_message("Enter amount to buy", ephemeral=True)
        msg = await bot.wait_for("message", timeout=180, check=self.check)
        data = await buystocks(self.ctx, msg.content, via=True)
        if isinstance(data, str):
            embed = None
            content = data
        else:
            embed = data
            content = None

        await self.ctx.send(content=content, embed=embed)

    @discord.ui.button(label="Sell", style=discord.ButtonStyle.red)
    async def sell(self, button, interaction: discord.Interaction):
        await interaction.response.send_message("Enter amount to sell" , ephemeral=True)
        msg = await bot.wait_for("message", timeout=180, check=self.check)
        data = await sellstocks(self.ctx, msg.content, via=True)
        if isinstance(data, str):
            embed = None
            content = data
        else:
            embed = data
            content = None

        await self.ctx.send(content=content, embed=embed)

    async def on_timeout(self):
        for child in self.children:
            child.disabled = True
        await self.msg.edit(view=self)

@bot.command()
@commands.check(general)
async def buystocks(ctx, amount, via=False):
    userid = str(ctx.author.id)
    dperson = bot.accounts[userid]
    sperson = bot.stocks.setdefault(userid, 0)
    if dperson['bank'] == 0:
        if via: return f'{ctx.author.mention} You have an empty bank bro..'
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
        except:
            if via: return f'{ctx.author.mention} Dude, the stocks can be bought and sold in integral values only. Provide a valid number.'
            return await ctx.send(f'{ctx.author.mention} Dude, the stocks can be bought and sold in integral values only. Provide a valid number.')

    if amount <= 0:
        if via: return f'{ctx.author.mention} No Fam.'
        return await ctx.send(f'{ctx.author.mention} No Fam.')

    bulk = int(amount * stock_price)
    if bulk > dperson['bank']:
        embed = discord.Embed(title='Oops..',
                              description=f'You don\'t have enough bank balance to buy `{await commait(amount)}` stocks.',
                              color=error_embed)
        embed.set_footer(
            text=f'Your Balance: {await commait(dperson["bank"])} coins\nStock Price: {await commait(bulk)} coins\nDifference: {await commait(bulk - dperson["bank"])} coins')
        if via: return embed
        return await ctx.send(embed=embed)

    dperson['bank'] = dperson['bank'] - bulk
    bot.accounts[userid] = dperson
    bot.stocks[userid] = sperson + amount

    await update_accounts()
    await update_stock_data()
    await create_statement(ctx.author, bot.user, bulk, f"Bought {amount} stock(s)", "Debit")

    embed = discord.Embed(title=f'{economysuccess} Success!',
                          description=f'You bought `{await commait(amount)}` stocks at price of `{stock_price}`.\n'
                                      f'\nCoins Spent: `{await commait(bulk)}` coins', color=success_embed)
    fetched = bot.get_user(ctx.author.id)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text='Economy Bot', icon_url=bot.pfp)
    embed.set_author(name=f'{fetched.name}', icon_url=fetched.display_avatar.url)
    if via: return embed
    await ctx.send(embed=embed)
    sto1 = bot.awards["stocks"]

    user_sto1 = sto1.setdefault(str(ctx.author.id), 0)
    user_sto_upd = user_sto1 + amount
    if user_sto_upd >= 1000000 and user_sto1 < 1000000: await achievement(ctx, ctx.author.id, "stocks")

    sto = bot.awards["stocks"]
    user_sto = sto.setdefault(str(ctx.author.id), 0)
    user_sto += amount
    sto[str(ctx.author.id)] = user_sto
    bot.awards["stocks"] = sto
    await update_awards()

@bot.command()
@commands.check(general)
async def sellstocks(ctx, amount, via=False):
    userid = str(ctx.author.id)
    dperson = bot.accounts[userid]
    sperson = bot.stocks.setdefault(userid, 0)

    stock_price = float(bot.current_stock[3])
    if amount == 'all':
        amount = sperson
    elif amount == 'half':
        amount = int(sperson/2)
    else:
        try: amount = int(amount)
        except:
            if via: return f'{ctx.author.mention} Dude, the stocks can be bought and sold in integral values only. Provide a valid number.'
            return await ctx.send(
                f'{ctx.author.mention} Dude, the stocks can be bought and sold in integral values only. Provide a valid number.')

    if amount <= 0:
        if via: return f'{ctx.author.mention} No Fam.'
        return await ctx.send(f'{ctx.author.mention} No Fam.')
    bulk = int(amount * stock_price)

    if amount > sperson:
        if via: return f'{ctx.author.mention} You don\'t own `{amount}` stocks.'
        return await ctx.send(f'{ctx.author.mention} You don\'t own `{amount}` stocks.')

    dperson['bank'] = dperson['bank'] + bulk
    bot.accounts[userid] = dperson
    bot.stocks[userid] = sperson - amount

    await update_accounts()
    await update_stock_data()
    await create_statement(ctx.author, bot.user, bulk, f"Sold {amount} stock(s)", "Credit")

    embed = discord.Embed(title=f'{economysuccess} Success!',
                          description=f'You sold `{await commait(amount)}` stock(s) at price of `{stock_price}`.\n'
                                      f'\nCoins Earned: `{await commait(bulk)}` coins', color=success_embed)
    fetched = bot.get_user(ctx.author.id)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text='Economy Bot', icon_url=bot.pfp)
    embed.set_author(name=f'{fetched.name}', icon_url=fetched.display_avatar.url)
    if via: return embed
    await ctx.send(embed=embed)

class Help(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        btns = [discord.ui.Button(label="Support Server", url=support_server),
                discord.ui.Button(label="Invite URL", url=invite_url)]
        for i in btns: self.add_item(i)

@bot.command()
@commands.check(general)
async def help(ctx, specify=None):
    embed = discord.Embed(color=embedcolor,
                          description=f'[Support Server]({support_server}) | [Invite Url]({invite_url})\nTo get help on a command, use `e.help <command name>`')
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
        try:
            await ctx.author.send(embed=embed, view=Help())
            embed = discord.Embed(title=f'{economysuccess} You received a mail!', color=success_embed)
            await ctx.reply(embed=embed)
        except:
            await ctx.send(embed=embed, view=Help())
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
                embed = discord.Embed(color=embedcolor, title=f'Command: {j[2:]}', description=info['desc']+f'\n\n**Category:** `{i["category"]}`\n**Cooldown:** `{info["cooldown"]}s`\n**Usage:** `{info["usage"]}`')
                embed.add_field(name='Aliases', value='```less\n'+'\n'.join(alias_list)+'```', inline=False)
                embed.set_footer(text='Syntax: <> = required, [] = optional')
                notfound = False
                await ctx.send(embed=embed)
                break
    if notfound:
        embed = discord.Embed(description=f'{economyerror} No help found or command doesn\'t exist!', color=error_embed)
        await ctx.send(embed=embed)

@bot.command(aliases=['add_chl'])
@commands.check(general)
@commands.has_permissions(manage_channels=True)
async def set_chl(ctx, channel:discord.TextChannel):
    server = bot.admin.get(str(ctx.guild.id), [])
    if channel.id in server:
        embed = discord.Embed(description=f'{economyerror} {channel.mention} is already in list of registered channels!', color=error_embed)
        return await ctx.send(embed=embed)
    server.append(channel.id)
    if ctx.channel.id not in server:
        server.append(ctx.channel.id)
    bot.admin[str(ctx.guild.id)] = server
    await close_admin()
    embed = discord.Embed(description=f'{economysuccess} {channel.mention} added to list of registered channels successfully!', color=success_embed)
    await ctx.send(embed=embed)

@bot.command(aliases=['rem_chl', 'remove_chl', 'delete_chl'])
@commands.check(general)
@commands.has_permissions(manage_channels=True)
async def del_chl(ctx, channel:discord.TextChannel):
    server = bot.admin.get(str(ctx.guild.id), [])
    if channel.id not in server:
        embed = discord.Embed(description=f'{economyerror} {channel.mention} not in list of registered channels!', color=error_embed)
        return await ctx.send(embed=embed)
    server.remove(channel.id)
    bot.admin[str(ctx.guild.id)] = server
    await close_admin()
    embed = discord.Embed(description=f'{economysuccess} {channel.mention} removed from list of registered channels successfully!', color=success_embed)
    await ctx.send(embed=embed)

@bot.command(aliases=['show_chl'])
@commands.check(general)
@commands.has_permissions(manage_channels=True)
async def list_chl(ctx):
    server = bot.admin.get(str(ctx.guild.id), [])
    if len(server) == 0: channels = ['> No channels set']
    else: channels = [f'> <#{x}>' for x in server]
    embed = discord.Embed(title=f'{economysuccess} Allowed Channels for the bot:', description='\n'.join(channels), color=embedcolor)
    embed.set_footer(text='Add a channel using e.set_chl <name>\nRemove a channel using e.del_chl <name>')
    await ctx.send(embed=embed)

@bot.command()
@commands.check(general)
@commands.has_permissions(manage_channels=True)
async def reset_chl(ctx):
    bot.admin[str(ctx.guild.id)] = []
    embed = discord.Embed(title=f'{economysuccess} Done', description='Cleared Successfully!', color=embedcolor)
    await close_admin()
    embed.set_footer(text='Add a channel using e.set_chl <name>\nRemove a channel using e.del_chl <name>')
    await ctx.send(embed=embed)

@bot.command()
@commands.check(general)
async def rob(ctx, member:discord.Member):
    await open_account(member.id)
    await open_account(ctx.author.id)
    if member == bot.user:
        pass
    success = random.randint(0, 100)

    lock = 0
    userinv = bot.inventory.get(str(member.id), {"inv":[], "eq_lock":""})
    user = userinv["inv"]
    eq = userinv['eq_lock']
    if len(user) == 0: pass
    else:
        if eq == 'Bronze Lock': lock = 10
        if eq == 'Silver Lock': lock = 25
        if eq == 'Gold Lock': lock = 40
    wallet = bot.accounts[str(ctx.author.id)]['wallet']
    if wallet < 100:
        return await ctx.send(f'{ctx.author.mention} You need `100` coins to start a robbery!')
    if success > 50+lock:
        if member == ctx.author:
            walleta = bot.accounts[str(ctx.author.id)]['wallet']
            if walleta <= 0:
                return await ctx.reply("Atleast rob someone who doesn't have an empty wallet bro")
            prize = random.randint(int(walleta / 5), int(walleta / 2))
            desc = random.choice(bot.phrases['selfrob_success']).format(prize=f'`{await commait(prize)}`')
        else:
            walletm = bot.accounts[str(member.id)]['wallet']
            if walletm == 0:
                return await ctx.send(f'{ctx.author.mention} Robbing a person with empty wallet.\n**Logic: 100**')
            prize = random.randint(int(walletm / 5), int(walletm / 2))
            walletm -= prize
            walleta = bot.accounts[str(ctx.author.id)]['wallet']
            walleta += prize
            bot.accounts[str(member.id)]['wallet'] = walletm
            bot.accounts[str(ctx.author.id)]['wallet'] = walleta
            await update_accounts()
            desc = random.choice(bot.phrases['rob_success']).format(prize=f'`{await commait(prize)}`', whom=member.mention)
            if str(member.id) in bot.alertsinfo:
                if bot.alertsinfo[str(member.id)]['state'] == 'on':
                    embed = discord.Embed(title=f'{economyerror} You were robbed!',
                                          description=f'You were robbed of `{await commait(prize)}` coins by `{ctx.author.name}#????` in `{ctx.guild.name}`!', color=error_embed)
                    await member.send(embed=embed)
            if lock != 0:
                if lock == 25: user.remove('Silver Lock')
                elif lock == 10: user.remove('Bronze Lock')
                elif lock == 40: user.remove('Gold Lock')
            userinv["inv"] = user
            userinv["eq_lock"] = ''
            bot.inventory[str(member.id)] = userinv
            await update_inv()
        embed = discord.Embed(title=f'{economysuccess} Robbery Successful!', description=desc, color=success_embed)
    else:
        if member == ctx.author:
            walleta = bot.accounts[str(ctx.author.id)]['wallet']
            prize = random.randint(int(walleta / 5), int(walleta / 2))
            desc = random.choice(bot.phrases['selfrob_failed']).format(prize=f'`{await commait(prize)}`')
            walleta -= prize
            bot.accounts[str(ctx.author.id)]['wallet'] = walleta
            await update_accounts()
        else:
            walletm = bot.accounts[str(ctx.author.id)]['wallet']
            prize = random.randint(int(walletm / 5), int(walletm / 3))
            walleta = bot.accounts[str(ctx.author.id)]['wallet']
            walleta -= prize
            bot.accounts[str(ctx.author.id)]['wallet'] = walleta
            await update_accounts()
            desc = random.choice(bot.phrases['rob_failed']).format(prize=f'`{await commait(prize)}`', whom=member.mention)
        embed = discord.Embed(title=f'{economyerror} Robbery Failed!', description=desc, color=error_embed)
    await ctx.send(embed=embed)

@bot.command()
@commands.check(general)
async def find(ctx):
    chance = random.randint(1, 100)
    wallet = bot.accounts[str(ctx.author.id)]['wallet']
    if wallet < 50:
        chance = 1
    if 45 > chance > 0:
        c = random.randint(50, 400)
        embed = discord.Embed(description=economysuccess+ ' ' +random.choice(bot.phrases['find_success']).format(c=c), color=success_embed)
        bot.accounts[str(ctx.author.id)]['wallet'] = wallet + c
    elif 90 > chance >= 45:
        c = random.randint(int(wallet/5), int(wallet/2))
        embed = discord.Embed(description=economyerror+ ' ' +random.choice(bot.phrases['find_failed']).format(c=c), color=error_embed)
        bot.accounts[str(ctx.author.id)]['wallet'] = wallet - c
    else:
        embed = discord.Embed(description=economyerror+ ' ' +random.choice(bot.phrases['find_neutral']), color=error_embed)
    await update_accounts()
    await ctx.send(embed=embed)

@bot.command(aliases=['store'])
@commands.check(general)
async def shop(ctx, page:int=1):
    if page <= 0: page = 1
    while True:
        if page*8 > len(storeitems):
            page -= 1
        else:
            break
    storeimg = await createstore((page)*8,(page+1)*8)
    await uploader.upload_file(ctx.channel, storeimg, "store.png")

@bot.command(aliases=['inv'])
@commands.check(general)
async def inventory(ctx, member:discord.Member = None):
    if member is None: member = ctx.author
    inv = await inventory_image(member.id)
    await uploader.upload_file(ctx.channel, inv, "inventory.png")

@bot.command(aliases=['purchase'])
@commands.check(general)
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
    store_item = {}
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

    if store_item["special"]: price = store_item["disc"]
    else: price = store_item["price"]

    user = bot.accounts[str(ctx.author.id)]
    wallet = user["wallet"]
    qty = int(qty)
    price = int(price.replace(',', ''))
    if price*qty > wallet:
        embed = discord.Embed(title=f'{economyerror} Insufficient Funds',
                              description=f'{random.choice(bot.phrases["less_bal"])}',
                              color=error_embed)
        return await ctx.send(embed=embed)
    member_inv = bot.inventory.get(str(ctx.author.id), {"inv":[]})
    memberinv = member_inv["inv"]
    appends = 0
    while appends < qty:
        memberinv.append(store_item["name"])
        appends += 1
    member_inv["inv"] = memberinv
    bot.inventory[str(ctx.author.id)] = member_inv
    user["wallet"] = wallet - (price*qty)
    bot.accounts[str(ctx.author.id)] = user
    embed = discord.Embed(description=f'{economysuccess} Done! `{qty}` quantity of `{store_item["name"]}` purchased successfully!',
                          color=success_embed)
    await update_accounts()
    await update_inv()
    await ctx.send(embed=embed)

@bot.command()
@commands.check(general)
async def server(ctx):
    embed = discord.Embed(description=f'**Discord Support Server:** [Join Here]({support_server})\n'
                                      f'Server Members: `idk lol`', color=embedcolor)
    embed.set_author(icon_url=bot.pfp, name=f'{bot.user.name}')
    await ctx.send(embed=embed)

@bot.command()
@commands.check(general)
async def invite(ctx):
    guilds = bot.guilds
    members = 0
    for i in guilds:
        members += len(i.members)
    embed = discord.Embed(description=f'Invite the bot: [Invite URL]({invite_url})\n\n'
                                      f'Support Server: [Join]({support_server})\n\n'
                                      f'Servers: `{len(guilds)}`\n'
                                      f'Users: `{members}`\n'
                                      f'Shards: `{bot.shard_count}`',
                          color=embedcolor)
    embed.set_author(icon_url=bot.pfp, name=f'{bot.user.name}')
    await ctx.send(embed=embed)

@bot.command()
@commands.check(general)
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
            allinv.append(chest)
            return await ctx.send(embed=embed)
        file = discord.File(fp=bot.allitems[item_name], filename='unboxing.gif')
        if mychest == 'common': chestcol = 183398
        elif mychest == 'rare': chestcol = 5164244
        elif mychest == 'legendary': chestcol = 16475796
        else: chestcol = 0
        embed = discord.Embed(color=chestcol)
        fetched = bot.get_user(ctx.author.id)
        embed.set_footer(text='Type e.sell <item-name> to sell an item for coins\nType e.iteminfo <item-name> for info!', icon_url=bot.pfp)
        embed.set_author(name=f'{fetched.name} Unboxed: {item_name}', icon_url=fetched.display_avatar.url)
        embed.set_image(url="attachment://unboxing.gif")
        await ctx.send(embed=embed, file=file)

        unbox = bot.awards["unbox"]
        user_a = unbox.setdefault(str(ctx.author.id), [])
        if item_name not in user_a:
            user_a.append(item_name)
            unbox[str(ctx.author.id)] = user_a
            bot.awards["unbox"] = unbox
            await update_awards()

            if len(user_a) == 50:
                await achievement(ctx, str(ctx.author.id), "unbox")

        useritems = userinv.setdefault("items", [])
        useritems.append(item_name)
        userinv["items"] = useritems

    def boost():
        pass

    userinv = bot.inventory.get(str(ctx.author.id), {"inv":[]})
    allinv = userinv["inv"]
    user = [x.lower() for x in allinv]
    if item.lower() not in user:
        embed = discord.Embed(description=f'{economyerror} The item `{item}` isn\'t found. {random.choice(bot.phrases["inv_noitem"])}', color=error_embed)
        return await ctx.send(embed=embed)
    for i in bot.shopc.keys():
        for k in [j for j in bot.shopc[i]]:
            if item.lower() == k.lower():
                if i == "lock": await lock(k)
                elif i == "chest":
                    await chest(k)
                    allinv.remove(k)
                    userinv["inv"] = allinv
    bot.inventory[str(ctx.author.id)] = userinv
    await update_inv()

@bot.command()
@commands.check(general)
async def ping(ctx):
    msg = await ctx.send('Pong!')
    ping = "{:.2f}".format(bot.latency*1000)
    await msg.edit(content=f'Pong! `{ping} ms`')

@bot.command(aliases=["item"], pass_context=True)
@commands.check(general)
async def iteminfo(ctx, *, name:str, via:bool=False):
    found = False
    mychest, item = "", {}
    for k, v in bot.items.items():
        for j in v["items"]:
            if name.lower() == j["name"].lower():
                found = True
                item = j
                mychest = k
                break
    if not found:
        embed = discord.Embed(description=f'{economyerror} The item `{name}` doesn\'t exist.', color=error_embed)
        if not via: return await ctx.send(embed=embed)
        else: return {"embed":embed}
    if mychest == 'common':
        chestcol = 183398
    elif mychest == 'rare':
        chestcol = 5164244
    else:
        chestcol = 16475796
    embed = discord.Embed(title="Item Info", color=chestcol)
    embed.add_field(name="Name", value=f'{item["name"]}', inline=False)
    embed.add_field(name="Description", value=item["desc"], inline=False)
    embed.add_field(name="Rarity", value=mychest.capitalize())
    if item["value"][0] == item["value"][1]:
        embed.add_field(name="Est. Value", value=f"`{await commait(item['value'][0])}` coins", inline=False)
    else:
        embed.add_field(name="Est. Value", value=f"`{await commait(item['value'][0])} - {await commait(item['value'][1])}` coins", inline=False)
    embed.set_thumbnail(url=items_imgs[item["name"]])
    if not via:
        await ctx.send(embed=embed)
    else:
        return {"embed":embed}

@bot.command(aliases=['itemsinv'])
@commands.check(general)
async def items(ctx, user:discord.User = None):
    if user is None: user = ctx.author

    user_page_orignal = 1
    updinv = update_sorted_inv(str(user.id))
    if updinv == "userinv": return await ctx.reply('You have an empty inventory bro..')
    if updinv == "itemsinv": return await ctx.reply('You don\'t own any items yet. Why not go and unbox?')

    sorted_inv = updinv
    del updinv
    item_count = 0
    max_pages = math.ceil(len(sorted_inv)/4)
    if max_pages == 0: max_pages = 1
    embed = discord.Embed(title=f"{economysuccess} Your Inventory:",
                          description=f"Items Owned: `{len(sorted_inv)}/50`\n"
                                      "Click on `Info` for item info!\n"
                                      "Click on `Sell` to sell the item",
                          color=0x2f3136)
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.display_avatar.url)
    embed.set_footer(text=f"Page #{user_page_orignal}/{max_pages}")
    view = ItemsInventory(ctx, user_page_orignal, [], max_pages, user, len(sorted_inv))
    a = await ctx.send(embed=embed, view=view)
    view.msg = a
    right = "▶️"
    left = "◀️"
    stop = "⏹️"
    await a.add_reaction(left)
    await a.add_reaction(stop)
    await a.add_reaction(right)

    while True:
        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in [right, left, stop]

        try:
            reaction, user_ = await bot.wait_for('reaction_add', check=check, timeout=180)
            reaction = str(reaction.emoji)
            if reaction == right:
                await a.remove_reaction(right, user_)
                await view.next_page()
            elif reaction == left:
                await a.remove_reaction(left, user_)
                await view.prev_page()
            else:
                await a.clear_reaction(right)
                await a.clear_reaction(left)
                await a.clear_reaction(stop)
                view.stop()
                break
        except:
            await a.clear_reaction(right)
            await a.clear_reaction(left)
            await a.clear_reaction(stop)
            break

class InfoButton(discord.ui.Button['ItemsInventory']):
    def __init__(self, y: int, foritem: str):
        super().__init__(style=discord.ButtonStyle.green, row=y, label="Info")
        self.item = foritem

    async def callback(self, interaction: discord.Interaction):
        assert self.view is not None
        view: ItemsInventory = self.view
        data = await iteminfo(view.ctx, name=self.item, via=True)
        embed = data["embed"]
        await interaction.response.send_message(embed=embed, ephemeral=True)

class ItemsSeller(discord.ui.Select):
    def __init__(self, item: str, user: discord.Member):
        self.item = item
        self.user = user

        userinv = bot.inventory.get(str(user.id))
        itemsinv = userinv.get("items", [])
        invlower = [x.lower() for x in itemsinv]
        userqty = invlower.count(item.lower())

        options = []
        for i in range(1, userqty+1):
            options.append((discord.SelectOption(label=str(i))))
        super().__init__(placeholder='Click here to select value', min_values=1, max_values=1,
                         options=options, row=4)

    async def callback(self, interaction: discord.Interaction):
        value = int(self.values[0])
        assert self.view is not None
        view: ItemsInventory = self.view
        if interaction.user != view.ctx.author:
            return await interaction.response.send_message(
                random.choice(bot.phrases["inter"]).format(usertag=str(view.ctx.author)))

        embed = await sell(view.ctx, item=f"{self.item} {value}", via=True)
        await interaction.response.send_message(embed=embed, ephemeral=True)
        await view.upd_page()

class SellButton(discord.ui.Button['ItemsInventory']):
    def __init__(self, y: int, foritem: str, disabled: bool):
        super().__init__(style=discord.ButtonStyle.red, row=y, label="Sell", disabled=disabled)
        self.item = foritem

    async def callback(self, interaction: discord.Interaction):
        assert self.view is not None
        view: ItemsInventory = self.view
        if interaction.user != view.ctx.author:
            return await interaction.response.send_message(
                random.choice(bot.phrases["inter"]).format(usertag=str(view.ctx.author)), ephemeral=True)
        view.clear_items()
        view.add_item(ItemsSeller(self.item, view.user))
        await interaction.response.send_message(content="Select sell quantity:", view=view, ephemeral=True)

class UselessButton(discord.ui.Button):
    def __init__(self, label: str, row: int, emoji: str):
        super().__init__(style=discord.ButtonStyle.blurple, label=label, row=row, emoji=emoji)

    async def callback(self, interaction: discord.Interaction):
        assert self.view is not None
        view: ItemsInventory = self.view
        if interaction.user != view.ctx.author:
            return await interaction.response.send_message(
                random.choice(bot.phrases["inter"]).format(usertag=str(view.ctx.author)))
        await interaction.response.defer()

class ItemsInventory(discord.ui.View):
    def __init__(self, ctx: Context, page: int, rarity: list, max_pages: int, user: discord.Member, owned: int):
        super().__init__()
        if rarity is None: rarity = []
        self.user = user
        self.ctx = ctx
        self.page = page
        self.emojis = {
            "common":"<:Common:847687974414319626>",
            "rare":"<:Rare:847687973202165841>",
            "legendary":"<:Legendary:847687925596160002>"
        }
        self.max_page = max_pages
        self.userid = str(user.id)
        self.data = []
        self.rarity = rarity
        self.filters = None
        self.owned = owned
        self.msg = None

        self.embed = discord.Embed(title=f"{economysuccess} Your Inventory:",
                          description=f"Items Owned: `{owned}/50`\n"
                                      "Click on `Info` for item info!\n"
                                      "Click on `Sell` to sell the item",
                          color=0x2f3136)
        self.embed.set_author(name=ctx.author.name, icon_url=ctx.author.display_avatar.url)
        self.embed.set_footer(text=f"Page #{page}/{max_pages}")

        self.filldata()
        self.addbuttons()

    async def next_page(self):
        if self.page == self.max_page: return

        self.page += 1
        self.filldata()
        self.addbuttons()

        await self.msg.edit(view=self, embed=self.embed)

    async def prev_page(self):
        if self.page == 1: return

        self.page -= 1
        self.filldata()
        self.addbuttons()

        await self.msg.edit(view=self, embed=self.embed)

    async def upd_page(self):
        self.filldata()
        self.addbuttons()

        await self.msg.edit(view=self, embed=self.embed)

    def filldata(self):
        rarity = self.rarity
        inv = update_sorted_inv(self.userid)
        emojis = self.emojis
        self.data.clear()
        for k, v in bot.items.items():
            if (len(rarity) != 0) and (k not in rarity): continue
            for i, j in v.items():
                for item in j:
                    for i in inv:
                        if item["name"] == i[0]:
                            self.data.append((item["name"], item["emoji"], i[1], emojis[k]))
        self.max_pages = math.ceil(len(self.data) / 4)
        self.embed.set_footer(text=f"Page #{self.page}/{self.max_pages}")

    def addbuttons(self):
        self.clear_items()
        page = self.page

        sortlist = []
        final_data = []
        filters = self.filters

        if filters is not None:
            for i in self.data:
                sortlist.append(i[2])

            if filters == "desc":
                sortlist.sort(reverse=True)
            else:
                sortlist.sort()

            for i in range((page - 1) * 4, page * 4):
                try: qty = sortlist[i]
                except: break

                for index, j in enumerate(self.data):
                    if index < i: continue
                    if j in final_data: continue
                    if j[2] == qty:
                        final_data.append(j)
        else:
            for i in range((page - 1) * 4, page * 4):
                try: d = self.data[i]
                except: break
                final_data.append(d)

        if len(final_data) == 0 and self.page != 1:
            self.page -= 1
            self.addbuttons()
        if self.ctx.author == self.user: disable = False
        else: disable = True
        for row, d in enumerate(final_data):
            self.add_item(UselessButton(d[2], row, d[3]))
            self.add_item(UselessButton(d[0], row, d[1]))
            self.add_item(InfoButton(row, d[0]))
            self.add_item(SellButton(row, d[0], disable))
            if row == 3:
                break
        self.add_item(InventoryFilters())

    async def filter(self, interaction: discord.Interaction, rarities, filters):
        self.rarity = rarities
        self.filters = filters
        self.page = 1
        self.filldata()
        self.addbuttons()

        await interaction.response.edit_message(view=self, embed=self.embed)

    async def on_timeout(self):
        for child in self.children:
            child.disabled = True
        await self.msg.edit(view=self)

class InventoryFilters(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label='Rarity: Common', emoji='🇷'),
            discord.SelectOption(label='Rarity: Rare', emoji='🇷'),
            discord.SelectOption(label='Rarity: Legendary', emoji='🇷'),
            discord.SelectOption(label='Sortby: Quantity Descending', emoji='🇸'),
            discord.SelectOption(label='Sortby: Quantity Ascending', emoji='🇸'),
        ]
        super().__init__(placeholder='Click here to add filter(s)', min_values=1, max_values=len(options),
                         options=options, row=4)

    async def callback(self, interaction: discord.Interaction):
        assert self.view is not None
        view: ItemsInventory = self.view
        if interaction.user != view.ctx.author:
            return await interaction.response.send_message(
                random.choice(bot.phrases["inter"]).format(usertag=str(view.ctx.author)))
        rarities = []
        filters = None
        for i in self.values:
            if 'Common' in i: rarities.append("common")
            if 'Rare' in i: rarities.append("rare")
            if 'Legendary' in i: rarities.append("legendary")
            if 'Descending' in i: filters = "desc"
            elif 'Ascending' in i: filters = "asc"

        await view.filter(interaction, rarities, filters)

@bot.command(pass_context=True)
@commands.check(general)
async def sell(ctx, *, item, via=False):
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
    if ctx.author.id in bot.globaltrades:
        embed = discord.Embed(title=f"{economyerror} Error", description="You are already in a trade. Press 'Exit' and try again.", color=error_embed)
        if via: return embed
        await ctx.send(embed=embed)
    userid = str(ctx.author.id)
    userinv = bot.inventory.get(userid)
    if userinv is None:
        return await ctx.reply('You have an empty inventory bro..')
    itemsinv = userinv.get("items", [])
    invlower = [x.lower() for x in itemsinv]
    if item.lower() not in invlower:
        embed = discord.Embed(description=f"{economyerror} You don\'t own `{item}`", color=error_embed)
        return await ctx.send(embed=embed)
    userqty = invlower.count(item.lower())
    item_main = {}
    for i in bot.items.keys():
        for j in bot.items[i]["items"]:
            if j["name"].lower() == item.lower():
                item_main = j
                break

    if qty > userqty:
        embed = discord.Embed(description=f"{economyerror} Dude, you don\'t own `{qty}` quantity of `{item_main['name']}`. What are you even thinking?", color=error_embed)
        return await ctx.send(embed=embed)
    for i in range(qty): itemsinv.remove(item_main["name"])
    userinv["items"] = itemsinv
    bot.inventory[userid] = userinv
    value = random.randint(item_main["value"][0], item_main["value"][1])*qty
    embed = discord.Embed(title=f'{economysuccess} Success!',
                          description=f'You sold `{qty}` {item_main["name"]} for {await commait(value)} coins!',
                          color=embedcolor)
    datauser = bot.accounts[userid]
    datauser["wallet"] += value
    bot.accounts[userid] = datauser

    await update_accounts()
    await update_inv()
    if not via: await ctx.send(embed=embed)
    else: return embed

class BetButtons(discord.ui.Button):
    def __init__(self, x: int, y: int, ctx):
        super().__init__(style=discord.ButtonStyle.secondary, label=str(y), row=x)
        self.x = x
        self.y = y
        self.ctx = ctx

    async def callback(self, interaction: discord.Interaction):
        assert self.view is not None
        view: InteractiveTTT = self.view
        if interaction.user != view.ctx.author:
            return await interaction.response.send_message(
                random.choice(bot.phrases["inter"]).format(usertag=str(view.ctx.author)),
                ephemeral=True)
        for i in view.children: i.disabled = True
        view.stop()
        bot.waitings[view.ctx.author.id] = [view.ctx.author, view.person]
        await interaction.response.edit_message(content=f"{view.ctx.author.mention} vs {view.person.mention}\n" \
           f"Bet Amount: `{await commait(int(self.label))}`\n" \
           f"Click 'Accept' to start. Waiting on: {' '.join([x.mention for x in bot.waitings[view.ctx.author.id]])}",
                                                view=ConfirmTTT(view.ctx.author, view.person, int(self.label), self.ctx))

class InteractiveTTT(discord.ui.View):
    def __init__(self, ctx: Context, person: discord.Member):
        super().__init__()
        self.ctx = ctx
        self.person = person
        self.confirm_p = None

    @discord.ui.button(label="Accept", style=discord.ButtonStyle.green)
    async def accept(self, button, interaction: discord.Interaction):
        if interaction.user != self.person:
            return await interaction.response.send_message(
                random.choice(bot.phrases["inter"]).format(usertag=str(self.person)),
                ephemeral=True)
        self.clear_items()
        options = [[100, 200, 250, 500, 1000],
                        [2000, 2500, 5000, 10000, 20000]]
        for i in range(2):
            for j in options[i]:
                self.add_item(BetButtons(i, j, self.ctx))
        await interaction.response.edit_message(content=f"Challenge Accepted! "
                                          f"{self.ctx.author.mention} to select betting amount:",
                                                view=self)

    @discord.ui.button(label="Decline", style=discord.ButtonStyle.red)
    async def decline(self, button, interaction: discord.Interaction):
        if interaction.user != self.person:
            return await interaction.response.send_message(
                random.choice(bot.phrases["inter"]).format(usertag=str(self.person)),
                ephemeral=True)
        for i in self.children: i.disabled = True
        self.stop()
        await interaction.response.edit_message(content="LOL the man declined!", view=self)

class Games(discord.ui.View):
    def __init__(self, ctx: Context):
        super().__init__()
        self.ctx = ctx
        self.msg = None

    @discord.ui.button(label="Minesweeper", emoji="💣", style=discord.ButtonStyle.blurple)
    async def mine(self, button, interaction: discord.Interaction):
        await interaction.response.defer()
        await minesweeper(self.ctx)
        self.stop()

    @discord.ui.button(label="Tic-Tac-Toe", emoji="⭕", style=discord.ButtonStyle.blurple)
    async def tic(self, button, interaction: discord.Interaction):
        ctx = self.ctx
        await interaction.response.send_message("Tag your friend with whom you will like to play")

        def check(c):
            return c.author == ctx.author and c.channel == ctx.channel and len(c.mentions) != 0
        try:
            c = await bot.wait_for("message", timeout=60, check=check)
        except:
            return

        person = c.mentions[0]
        if person == ctx.author:
            return await ctx.send(f"{person.mention} Lmao starting a game with yourself? How lonely..")
        if person.bot:
            return await ctx.send("You can't challenge a bot lmao. You'll always lose...")

        confirming = InteractiveTTT(ctx, person)
        confirm_p = await ctx.send(f'{person.mention} Hey, {ctx.author.mention} wants to challenge you for a game of'
                                   f' Tic-Tac-Toe. Click "Accept" to proceed!', view=confirming)
        confirming.confirm_p = confirm_p

    @discord.ui.button(label="Hangman", emoji="🪢", style=discord.ButtonStyle.blurple)
    async def hang(self, button, interaction: discord.Interaction):
        ctx = self.ctx
        await interaction.response.defer()
        await hangman(ctx)

    async def on_timeout(self):
        for i in self.children:
            i.disabled = True
        await self.msg.edit(view=self)

@bot.command()
@commands.check(general)
async def games(ctx):
    view = Games(ctx)
    msg = await ctx.send(f"**Welcome to Gamebot Arcade <:gamepad:849117058875916308>**\nChoose your game below:",
                         view=view)
    view.msg = msg

@bot.command(aliases=["ms", "mine"], pass_context=True, invoke_without_command=True)
@commands.check(general)
async def minesweeper(ctx):
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

    back_rows = []
    count = 0
    board = Minesweeper(ctx.author, net)
    minemsg = await ctx.send("**Welcome to Minesweeper!**\n"
                             "Rules:\n"
                             "> For each correct move, you get `1,000` coins\n"
                             "> For each incorrect move, `2,000` coins are taken away!\n"
                             "> Your aim is to click on blocks avoiding any bombs. All the best!\n"
                             f"`Note:` To end the game, react with {economyerror}\n\n"
                             "Total Moves: `0`    Correct: `0`    Incorrect: `0`\n"
                             f"Net Profit: `{net}`\n"
                             "Here is your board:", view=board)
    await minemsg.add_reaction(economyerror)
    bot.activems["users"].append(ctx.author.id)

    def check(reaction, user):
        if user == ctx.author and str(reaction.emoji) == economyerror:
            return True

    try:
        reaction, user = await bot.wait_for('reaction_add', check=check)
        await board.end(minemsg)
    except:
        pass

class Minesweeper(discord.ui.View):
    moves = 0
    correct = 0
    wrong = 0

    def __init__(self, player: discord.Member, net):
        super().__init__()
        self.player = player
        self.board = bot.ms[player.id]["main"]
        self.count = bot.ms[player.id]["count"]
        self.net = net

        for x in range(5):
            for y in range(5):
                self.add_item(MinesweeperButton(x, y))

    async def end(self, msg: discord.Message):
        try: bot.activems["users"].remove(self.player.id)
        except: pass
        bot.accounts[str(self.player.id)]["wallet"] += self.net
        await update_accounts()
        cont = f"**The game ended**\nNet Profit: `{await commait(self.net)}`"
        for i in self.children:
            i.disabled = True
        self.stop()
        await msg.edit(content=cont, view=self)

class MinesweeperButton(discord.ui.Button['Minesweeper']):
    def __init__(self, x: int, y: int):
        super().__init__(style=discord.ButtonStyle.secondary, label='\u200b', row=y)
        self.x = x
        self.y = y
        self.emojisetter = {
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

    async def callback(self, interaction: discord.Interaction):
        assert self.view is not None
        view: Minesweeper = self.view

        if interaction.user != view.player:
            await interaction.response.send_message(random.choice(bot.phrases["inter"]).format(usertag=str(view.player)),
                                                    ephemeral=True)
            return

        state = view.board[self.y][self.x]
        emojis = self.emojisetter
        view.moves += 1
        if state == "bomb":
            self.style = discord.ButtonStyle.red
            self.emoji = "💣"
            self.disabled = True
            view.wrong += 1
            view.net -= 2000
        else:
            self.style = discord.ButtonStyle.blurple
            self.disabled = True
            coun = view.count[self.y][self.x]
            self.emoji = emojis[coun]
            view.correct += 1
            view.net += 1000

        if view.moves == 25:
            try:
                bot.activems["users"].remove(view.player.id)
            except:
                pass
            bot.accounts[str(view.player.id)]["wallet"] += view.net
            await update_accounts()
            cont = f"**The game ended**\nNet Profit: `{await commait(view.net)}`"
            view.stop()
        else:
            cont = f"Total Moves: `{view.moves}`    Correct: `{view.correct}`    Incorrect: `{view.wrong}`\n" \
                   f"Net Profit: `{view.net}`\n"
        await interaction.response.edit_message(content=cont, view=view)

class TicTacToe(discord.ui.View):
    def __init__(self, p1: discord.Member, p2: discord.Member, move, bet:int, ctx):
        super().__init__()
        self.X = p1
        self.O = p2
        self.Tie = 0
        self.current_player = move
        self.msg = None
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]
        self.bet = bet
        self.ctx = ctx

        for x in range(3):
            for y in range(3):
                self.add_item(TicTacToeButton(x, y))

    async def on_timeout(self):
        winner = self.current_player
        view = self
        if winner == view.X:
            content = f'🏆 {view.O.mention} won! 🏆 The other player didn\'t reply in time!'
            bot.accounts[str(view.O.id)]["wallet"] += view.bet * 2
        elif winner == view.O:
            content = f'🏆 {view.X.mention} won! 🏆 The other player didn\'t reply in time!'
            bot.accounts[str(view.X.id)]["wallet"] += view.bet * 2
        else:
            content = "It's a tie!"
        await update_accounts()
        for child in view.children:
            child.disabled = True
        await self.msg.edit(view=view)

    def check_board_winner(self):
        for across in self.board:
            value = sum(across)
            if value == 3:
                return self.O
            elif value == -3:
                return self.X

        for line in range(3):
            value = self.board[0][line] + self.board[1][line] + self.board[2][line]
            if value == 3:
                return self.O
            elif value == -3:
                return self.X

        diag = self.board[0][2] + self.board[1][1] + self.board[2][0]
        if diag == 3:
            return self.O
        elif diag == -3:
            return self.X

        diag = self.board[0][0] + self.board[1][1] + self.board[2][2]
        if diag == 3:
            return self.O
        elif diag == -3:
            return self.X

        if all(i != 0 for row in self.board for i in row):
            return self.Tie

        return None

class TicTacToeButton(discord.ui.Button['TicTacToe']):
    def __init__(self, x: int, y: int):
        super().__init__(style=discord.ButtonStyle.secondary, label='\u200b', row=y)
        self.x = x
        self.y = y

    async def callback(self, interaction: discord.Interaction):
        assert self.view is not None
        view: TicTacToe = self.view
        if interaction.user not in [view.X, view.O]:
            return await interaction.response.send_message(
                random.choice(bot.phrases["inter"]).format(usertag=" or ".join([str(view.X), str(view.O)])),
            ephemeral=True)
        if interaction.user != view.current_player:
            return await interaction.response.send_message("Its not your turn. HaVe PaTiEnCe!", ephemeral=True)
        state = view.board[self.y][self.x]
        if view.current_player == view.X:
            self.style = discord.ButtonStyle.red
            self.emoji = "❌"
            self.disabled = True
            view.board[self.y][self.x] = -1
            view.current_player = view.O
            content = f"{view.O.mention} to move:"
        else:
            self.style = discord.ButtonStyle.green
            self.emoji = "⭕"
            self.disabled = True
            view.board[self.y][self.x] = +1
            view.current_player = view.X
            content = f"{view.X.mention} to move:"

        winner = view.check_board_winner()
        if winner is not None:
            if winner == view.X:
                content = f'🏆 {view.X.mention} won! 🏆'
                await ttt_end(view.X, view.O, view.bet, view.ctx)
            elif winner == view.O:
                content = f'🏆 {view.O.mention} won! 🏆'
                await ttt_end(view.O, view.X, view.bet, view.ctx)
            else:
                await ttt_tie(view.X.id, view.O.id, view.bet)

            for child in view.children:
                child.disabled = True
            await update_accounts()
            view.stop()

        await interaction.response.edit_message(content=content, view=view)

class ConfirmTTT(discord.ui.View):
    def __init__(self, user: discord.Member, user2: discord.Member, bet: int, ctx):
        super().__init__()
        self.user = user
        self.bet = bet
        self.allowed = bot.waitings[self.user.id]
        self.p1 = user
        self.p2 = user2
        self.msg = None
        self.ctx = ctx

    async def on_timeout(self):
        for i in self.children:
            i.disabled = True
        await self.msg.edit(view=self)

    @discord.ui.button(label="Accept", style=discord.ButtonStyle.green)
    async def accept(self, button, interaction: discord.Interaction):
        if interaction.user not in self.allowed:
            return await interaction.response.send_message(random.choice(bot.phrases["inter"]).format(usertag=" or ".join(self.allowed)),
                                                           ephemeral=True)

        per = bot.accounts[str(interaction.user.id)]
        p = per["wallet"]
        bet = self.bet

        if p < bet:
            cont = f"{interaction.user.mention} doesn't have enough coins!"
            await interaction.response.edit_message(content=cont, view=None)
        else:
            per["wallet"] -= bet
            bot.accounts[str(interaction.user.id)] = per
            await update_accounts()

            bot.waitings[self.user.id].remove(interaction.user)
            self.allowed = bot.waitings[self.user.id]

            if len(bot.waitings[self.user.id]) == 0:
                move = random.choice([self.user, interaction.user])
                view = TicTacToe(self.p1, self.p2, move, bet, self.ctx)
                view.msg = self.msg
                await interaction.response.edit_message(content=f"**Game Begins!** {move.mention} to move first:",
                                                        view=view)
            else:
                cont = f"{self.p1.mention} vs {self.p2.mention}\n" \
                       f"Bet Amount: `{await commait(bet)}`\n" \
                       f"Click 'Accept' to start. Waiting on: {' '.join([x.mention for x in bot.waitings[self.user.id]])}"
                await interaction.response.edit_message(content=cont)

@bot.command(aliases=["ttt"])
@commands.check(general)
async def tictactoe(ctx, user:discord.Member, bet:int=100):
    if user == ctx.author:
        return await ctx.send("Bruh you cant start a game with yourself")
    if user.bot:
        return await ctx.send("You can't challenge a bot lmao. You'll always lose...")
    bet = int(bet)
    if bet not in [100, 200, 250, 500, 1000, 2000, 2500, 5000, 10000, 20000]:
        return await ctx.send(f"The betting amount should be {', '.join(str(x) for x in [100, 200, 250, 500, 1000, 2000, 2500, 5000, 10000])} "
                              f"or 20000")
    bot.waitings[ctx.author.id] = [ctx.author, user]

    cont = f"{ctx.author.mention} vs {user.mention}\n" \
           f"Bet Amount: `{await commait(bet)}`\n" \
           f"Click 'Accept' to start. Waiting on: {' '.join([x.mention for x in bot.waitings[ctx.author.id]])}"
    view = ConfirmTTT(ctx.author, user, bet, ctx)
    pre = await ctx.send(cont, view=view)
    view.msg = pre

class HeadTails(discord.ui.View):
    def __init__(self, member: discord.Member, bet: int):
        super().__init__(timeout=10)
        self.user = member
        self.bet = bet
        self.win = random.choice(["Heads", "Tails"])
        self.msg = None

    @discord.ui.button(label="Heads", style=discord.ButtonStyle.green)
    async def heads(self, button: discord.ui.Button, interaction: discord.Interaction):
        if interaction.user != self.user:
            return await interaction.response.send_message(random.choice(bot.phrases["inter"]).format(usertag=str(self.user)),
                                                    ephemeral=True)
        await self.checkfor("Heads", interaction)

    @discord.ui.button(label="Tails", style=discord.ButtonStyle.green)
    async def tails(self, button: discord.ui.Button, interaction: discord.Interaction):
        if interaction.user != self.user:
            return await interaction.response.send_message(random.choice(bot.phrases["inter"]).format(usertag=str(self.user)),
                                                    ephemeral=True)
        await self.checkfor("Tails", interaction)

    async def checkfor(self, win, interaction):
        if win == self.win:
            cont = f"Congratulations! You win back {int(self.bet / 2)} coins"
            color = success_embed
            bot.accounts[str(self.user.id)]["wallet"] += self.bet * 0.5
        else:
            cont = f"You lose hahaha. Nothing for you!"
            color = error_embed
            bot.accounts[str(self.user.id)]["wallet"] -= self.bet
        embed = discord.Embed(title=f"I flipped {self.win}",
                              description=f"{cont}", color=color)
        await interaction.response.edit_message(embed=embed, view=None)
        await update_accounts()

    async def on_timeout(self):
        for i in self.children:
            i.disabled = True
        await self.msg.edit(view=self)

@bot.command(aliases=["bet"])
@commands.check(general)
async def flip(ctx, bet:int=None):
    if bet is None:
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel
        try:
            msg = await bot.wait_for("message", timeout=60, check=check)
            bet = int(msg.content)
        except asyncio.TimeoutError: return
        except:
            await ctx.reply("Bruh thats not a valid integer...")

    if bet > bot.accounts[str(ctx.author.id)]["wallet"]:
        return await ctx.send(f"{ctx.author.mention} Imagine betting more than you have in your pockets..")
    embed = discord.Embed(description=f"Call your side! Amount at stake: `{bet}` coins", color=embedcolor)
    view = HeadTails(ctx.author, bet)
    msg = await ctx.send(embed=embed, view=view)
    view.msg = msg
    
@bot.command()
@commands.check(general)
async def trade(ctx, user: discord.Member= None):
    if user is None:
        await ctx.reply("Mention the user you would like to trade with:")
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel and len(msg.mentions) != 0
        try:
            msg = await bot.wait_for("message", timeout=60, check=check)
            user = msg.mentions[0]
        except:
            return
    view = Trade(ctx, user)
    embed = discord.Embed(title="Trade", color=embedcolor,
                          description="Trade your items with a person!\n"
                          "```css\n"
                          "[C] - Common Item\n"
                          "[R] - Rare Item\n"
                          "[L] - Legendary Item\n"
                          "```\n"
                          "`Ready` to approve your part\n"
                          "`Cancel` to revert back from ready\n"
                          "`Exit` to stop the trade")
    embed.add_field(name=str(ctx.author), value="```\nNo items added```")
    embed.add_field(name="\u200b", value="```\n⇔```")
    embed.add_field(name=str(user), value="```\nNo items added```")
    embed.add_field(name="\\❌ Not Ready \\❌", value="\u200b")
    embed.add_field(name="\u200b", value="\u200b")
    embed.add_field(name="\\❌ Not Ready \\❌", value="\u200b")
    bot.globaltrades.extend([ctx.author.id, user.id])
    msg = await ctx.send(embed=embed, view=view)
    view.msg = msg

class Trade(discord.ui.View):
    def __init__(self, ctx: Context, user: discord.Member):
        super().__init__(timeout=300)
        self.ctx = ctx
        self.user = user
        self.msg = None
        self.embed = discord.Embed(title="Trade")
        self.adder = TradeAdd(ctx.author, user)

    @discord.ui.button(label="Add Item(s)", style=discord.ButtonStyle.blurple)
    async def add(self, button, interaction: discord.Interaction):
        ctx = self.ctx
        user = self.user
        if interaction.user not in [self.ctx.author, self.user]:
           return  await interaction.response.send_message(
                random.choice(bot.phrases["inter"]).format(usertag=" or ".join([str(ctx.author), str(user)])),
           ephemeral=True)
        self.adder.msg = self.msg
        if self.adder.performing: self.adder.interrupt = (True, interaction.user.id)
        await self.adder.new_opts(interaction.user, "add")
        await interaction.response.send_message("Add Items:", view=self.adder, ephemeral=True)

    @discord.ui.button(label="Remove Item(s)", style=discord.ButtonStyle.blurple)
    async def remove(self, button, interaction: discord.Interaction):
        ctx = self.ctx
        user = self.user
        if interaction.user not in [self.ctx.author, self.user]:
            return await interaction.response.send_message(
                random.choice(bot.phrases["inter"]).format(usertag=" or ".join([str(ctx.author), str(user)])),
                ephemeral=True)
        self.adder.msg = self.msg
        if self.adder.performing: self.adder.interrupt = (True, interaction.user.id)
        await self.adder.new_opts(interaction.user, "rem")
        await interaction.response.send_message("Remove Items:", view=self.adder, ephemeral=True)

    @discord.ui.button(label="Ready", style=discord.ButtonStyle.green, row=1)
    async def accept(self, button, interaction: discord.Interaction):
        ctx = self.ctx
        user = self.user
        if interaction.user not in [self.ctx.author, self.user]:
            return await interaction.response.send_message(
                random.choice(bot.phrases["inter"]).format(usertag=" or ".join([str(ctx.author), str(user)])),
                ephemeral=True)
        self.adder.msg = self.msg
        await interaction.response.defer()
        await self.adder.userready(interaction.user.id)

    @discord.ui.button(label="Cancel", style=discord.ButtonStyle.red, row=1)
    async def cancel(self, button, interaction: discord.Interaction):
        ctx = self.ctx
        user = self.user
        if interaction.user not in [self.ctx.author, self.user]:
            return await interaction.response.send_message(
                random.choice(bot.phrases["inter"]).format(usertag=" or ".join([str(ctx.author), str(user)])),
                ephemeral=True)
        self.adder.msg = self.msg
        await interaction.response.defer()
        await self.adder.usercancel(interaction.user.id)

    @discord.ui.button(label="Exit", style=discord.ButtonStyle.red, row=1)
    async def exit(self, button, interaction: discord.Interaction):
        ctx = self.ctx
        user = self.user
        if interaction.user not in [self.ctx.author, self.user]:
            return await interaction.response.send_message(
                random.choice(bot.phrases["inter"]).format(usertag=" or ".join([str(ctx.author), str(user)])),
                ephemeral=True)
        self.adder.msg = self.msg
        await interaction.response.defer()
        for i in self.children:
            i.disabled = True
        await self.msg.edit(view=self)
        bot.globaltrades.remove(interaction.user.id)

    async def on_timeout(self) -> None:
        ctx = self.ctx
        user = self.user

        bot.globaltrades.remove(ctx.author.id)
        bot.globaltrades.remove(user.id)
        for i in self.children:
            i.disabled = True
        await self.msg.edit(view=self)

class TradeAdd(discord.ui.View):
    def __init__(self, user1: discord.Member, user2: discord.Member):
        super().__init__()
        self.user1 = user1
        self.user2 = user2
        self.options_pg1 = []
        self.options_pg2 = []
        self.page1 = True
        self.paging = False

        self.items = {user1.id:[], user2.id:[]}
        self.embed = discord.Embed(title="Trade", color=embedcolor)
        self.msg = None

        self.ready = []
        self.performing = False
        self.interrupt = (False, 0)

    async def userready(self, userid):
        #if userid in self.ready: return
        self.ready.append(userid)
        await self.update_embed()
        await self.update_msg()
        await self.perform_trade()

    async def usercancel(self, userid):
        if userid not in self.ready: return
        self.ready.remove(userid)
        if self.performing:
            self.interrupt = (True, userid)
        else:
            await self.update_embed()
            await self.update_msg()

    async def perform_trade(self):
        if len(self.ready) != 2: return
        self.performing = True
        await asyncio.sleep(0)
        for i in range(5, 0, -1):
            await self.update_embed()
            if self.interrupt[0]:
                self.ready.remove(self.interrupt[1])
                self.interrupt = (False, 0)
                self.performing = False
                await self.update_embed()
                await self.update_msg()
                return

            self.embed.add_field(name="\u200b", value="\u200b")
            self.embed.add_field(name=f"Trading in {i} secs...", value="\u200b")
            self.embed.add_field(name="\u200b", value="\u200b")
            await self.update_msg()
            await asyncio.sleep(1)
        await self.update_embed()
        self.embed.add_field(name="\u200b", value="\u200b")
        self.embed.add_field(name=f"Trade Successful", value="\u200b")
        self.embed.add_field(name="\u200b", value="\u200b")

        user1items = bot.inventory[str(self.user1.id)]["items"]
        user2items = bot.inventory[str(self.user2.id)]["items"]

        user1items.extend([x[1] for x in self.items[self.user2.id]])
        user2items.extend([x[1] for x in self.items[self.user1.id]])

        for i, j in self.items.items():
            if i == self.user1.id:
                for item in j:
                    user1items.remove(item[1])
            else:
                for item in j:
                    user2items.remove(item[1])

        bot.inventory[str(self.user1.id)]["items"] = user1items
        bot.inventory[str(self.user2.id)]["items"] = user2items

        await update_inv()
        bot.globaltrades.remove(self.user1.id)
        bot.globaltrades.remove(self.user2.id)
        await self.msg.edit(embed=self.embed, view=None)

    async def new_opts(self, user, type):
        userinv = []
        if type == "add":
            itemsinv = update_sorted_inv(str(user.id))
            for i in itemsinv:
                userinv.append(i[0])

            for i in self.items[user.id]:
                if i[1] in userinv:
                    userinv.remove(i[1])

            await self.update_opts(userinv, "add")
        else:
            userinv = [i[1] for i in self.items[user.id]]
            await self.update_opts(userinv, "remove")

    async def update_opts(self, opts: list, method: str):
        self.options_pg1.clear()
        self.options_pg2.clear()
        for index, value in enumerate(opts):
            print("opts:", index, value)
            if index > 24:
                self.paging = True
                self.options_pg2.append(value)
            else:
                self.options_pg1.append(value)
        print(f"Len: {len(self.options_pg1)}\nValue: {self.options_pg1}")
        self.clear_items()
        if self.page1:
            newsel = ItemsSelect(self.options_pg1, method)
        else:
            newsel = ItemsSelect(self.options_pg2, method)

        self.add_item(newsel)
        if method == "add" and self.paging:
            self.add_item(PreviousPage())
            self.add_item(NextPage())

    async def update_embed(self):
        user1items = self.items[self.user1.id]
        user2items = self.items[self.user2.id]
        user1 = ""
        user2 = ""

        for i in user1items:
            user1 += f"[{i[0]}] {i[1]}\n"

        for i in user2items:
            user2 += f"[{i[0]}] {i[1]}\n"

        if user1 == "": user1 = "No items added"
        if user2 == "": user2 = "No items added"

        self.embed.clear_fields()
        self.embed.add_field(name=str(self.user1), value=f"```\n{user1}```")
        if self.performing:
            self.embed.add_field(name="\u200b", value="```\n     ⇔```")
        else:
            self.embed.add_field(name="\u200b", value="```\n⇔```")
        self.embed.add_field(name=str(self.user2), value=f"```\n{user2}```")

        state = "\\✅ Ready \\✅"
        if self.user1.id not in self.ready:
            state = "\\❌ Not Ready \\❌"
        self.embed.add_field(name=state, value="\u200b")
        self.embed.add_field(name="\u200b", value="\u200b")
        state = "\\✅ Ready \\✅"
        if self.user2.id not in self.ready:
            state = "\\❌ Not Ready \\❌"
        self.embed.add_field(name=state, value="\u200b")

    async def update_msg(self):
        await self.msg.edit(embed=self.embed)

class ItemsSelect(discord.ui.Select):
    def __init__(self, options: list, method: str):
        final = []

        self.method = method
        options = list(set(options))
        print("Sel:", options)
        for k, v in bot.items.items():
            for i, j in v.items():
                for item in j:
                    for opt in options:
                        if opt == item["name"]:
                            final.append(discord.SelectOption(label=item["name"], emoji=item["emoji"]))
                            options.remove(opt)
        if len(final) < 5: maxval = len(final)
        else: maxval = 5
        super().__init__(placeholder=f'Click here to {method}...', min_values=1, max_values=maxval,
                         options=final, row=4)

    async def callback(self, interaction: discord.Interaction):
        assert self.view is not None
        view: TradeAdd = self.view

        if self.method == "add":
            olditems = view.items[interaction.user.id]
            if len(olditems) == 5:
                return await interaction.response.edit_message(
                    content=f"{economyerror} You can't add more than 5 items",
                    view=None)
            myitems = []
            for k, v in bot.items.items():
                for i, j in v.items():
                    for item in j:
                        for x in self.values:
                            if item["name"] == x:
                                myitems.append((k[0].upper(), item["name"]))

            olditems.extend(myitems)
            olditems = olditems[:5]
            view.items[interaction.user.id] = olditems
            await interaction.response.edit_message(content="Added!", view=None)
        else:
            olditems = view.items[interaction.user.id]
            if len(olditems) == 0:
                return await interaction.response.edit_message(
                    content=f"{economyerror} You can't remove items anymore",
                    view=None)
            for i in olditems:
                if i[1] in self.values:
                    view.items[interaction.user.id].remove(i)
            await interaction.response.edit_message(content="Removed!", view=None)
        await view.update_embed()
        await view.update_msg()

class NextPage(discord.ui.Button):
    def __init__(self):
        super().__init__(label="Next", emoji="▶️", style=discord.ButtonStyle.blurple)

    async def callback(self, interaction: discord.Interaction):
        assert self.view is not None
        view: TradeAdd = self.view

        if not view.page1:
            await interaction.response.defer()
            return

        view.page1 = False
        await view.new_opts(interaction.user, "add")
        await interaction.response.edit_message(view=view)

class PreviousPage(discord.ui.Button):
    def __init__(self):
        super().__init__(label="Prev", emoji="◀️", style=discord.ButtonStyle.blurple)

    async def callback(self, interaction: discord.Interaction):
        assert self.view is not None
        view: TradeAdd = self.view

        if view.page1:
            await interaction.response.defer()
            return

        view.page1 = True
        await view.new_opts(interaction.user, "add")
        await interaction.response.edit_message(view=view)

@bot.command()
async def hangman(ctx):
    bet = 100
    if bet > bot.accounts[str(ctx.author.id)]["wallet"]:
        return await ctx.send(f"{ctx.author.mention} You don't have 100 coins in your wallet. {random.choice(bot.phrases['less_bal'])}")
    load = await ctx.send(f"{economysuccess} Finding a word...")
    bot.accounts[str(ctx.author.id)]["wallet"] -= 100
    session = aiohttp.ClientSession()
    uri = ""
    word = session.put()

    uncovered_word = list(len(word) * '_')
    wrong = 0
    reveal_rand = random.randint(0, len(word)-1)
    for i in range(0, len(word)):
        if word[reveal_rand] == word[i]:
            uncovered_word[i] = word[reveal_rand]

    images = {0:'https://media.discordapp.net/attachments/837564505952747520/883242727117058068/unknown.png',
              1:'https://media.discordapp.net/attachments/837564505952747520/883242763137732668/unknown.png',
              2:'https://media.discordapp.net/attachments/837564505952747520/883242804158021642/unknown.png',
              3:'https://media.discordapp.net/attachments/837564505952747520/883242848781221888/unknown.png',
              4:'https://media.discordapp.net/attachments/837564505952747520/883242883820433408/unknown.png',
              5:'https://media.discordapp.net/attachments/837564505952747520/883242924689739816/unknown.png',
              6:'https://media.discordapp.net/attachments/837564505952747520/883242982592102450/unknown.png'}

    embed = discord.Embed(title="H A N G M A N",
                          description="Enter your guesses, and if the letter is in the word, the bot updates the embed.\n"
                                      "For each wrong guess, the man is closer to getting hanged to death!\n\n"
                                      "Start below (you better protect the poor soul):\n"
                                      f"**`{' '.join(uncovered_word)}`**\n\n"
                                      f"Chances Left: `6`",
                          color=embedcolor)
    embed.set_thumbnail(url=images[wrong])
    msg = await ctx.author.send(embed=embed)
    await load.delete()
    await ctx.reply("In ya DMs!")
    while True:
        def check(msg):
            return msg.author == ctx.author and msg.guild == None

        try:
            msg = await bot.wait_for("message", timeout=60, check=check)
            msgc = msg.content.lower()

            if len(msgc) != 1:
                await msg.reply("Please enter a letter only!")
                continue

            if msgc not in [x for x in word]:
                await msg.reply("Wrong!", delete_after=3)
                wrong += 1
                if wrong == 6:
                    break
            else:
                await msg.reply("Correct!", delete_after=3)
                for i in range(0, len(word)):
                    if msgc == word[i]:
                        uncovered_word[i] = msgc
                if "".join(uncovered_word) == word:
                    break
            embed = discord.Embed(title="H A N G M A N",
                                  description="Enter your guesses, and if the letter is in the word, the bot updates the embed.\n"
                                              "For each wrong guess, the man is closer to getting hanged to death!\n\n"
                                              "Start below (you better protect the poor soul):\n"
                                              f"**`{' '.join(uncovered_word)}`**\n\n"
                                              f"Chances Left: `{6-wrong}`",
                                  color=embedcolor)
            embed.set_thumbnail(url=images[wrong])
            await ctx.author.send(embed=embed)
        except:
            return
    if wrong == 6:
        embed = discord.Embed(title="H A N G M A N",
                              description=f"Ah you lost! The correct word was: `{word}`",
                              color=error_embed)
        embed.set_thumbnail(url=images[wrong])
    else:
        embed = discord.Embed(title="H A N G M A N",
                              description=f"Yay you win! Nice guessing the word `{word}` :D",
                              color=success_embed)
        embed.set_thumbnail(url=images[wrong])
        bot.accounts[str(ctx.author.id)]["wallet"] += 200
    await ctx.author.send(embed=embed)

bot.connected_ = False
@bot.event
async def on_connect():
    if not bot.connected_:
        print("Entering on_connect()")
        await uploader.recreate()
        bot.connected_ = True
        await create_stuff()

for i in bot.commands:
    if i.hidden: continue
    for j in i.aliases:
        all_commands.append(j)
    all_commands.append(i.name)

bot.token = "ODMyMDgzNzE3NDE3MDc0Njg5.YHeoWQ._O5uoMS_I7abKdI_YzVb9BuEHzs"
bot.run(bot.token)
