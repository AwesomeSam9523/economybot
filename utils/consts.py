import json

allItems = {'Rotten Tomato': 'https://cdn.discordapp.com/attachments/837564505952747520/884298671930372096/unboxing.gif', 'Cloth Piece': 'https://cdn.discordapp.com/attachments/837564505952747520/884298761008975892/unboxing.gif', 'Office Bag': 'https://cdn.discordapp.com/attachments/837564505952747520/884298815513952307/unboxing.gif', 'Spray Can': 'https://cdn.discordapp.com/attachments/837564505952747520/884298871495344168/unboxing.gif', 'Black Pen': 'https://cdn.discordapp.com/attachments/837564505952747520/884298928277835826/unboxing.gif', 'Broken Mouse': 'https://cdn.discordapp.com/attachments/837564505952747520/884298985580408862/unboxing.gif', 'N95 Mask': 'https://cdn.discordapp.com/attachments/837564505952747520/884299042614554694/unboxing.gif', 'Dead Calculator': 'https://cdn.discordapp.com/attachments/837564505952747520/884299094749745152/unboxing.gif', 'Leather Shoes': 'https://cdn.discordapp.com/attachments/837564505952747520/884299151947468850/unboxing.gif', 'Wooden Stick': 'https://cdn.discordapp.com/attachments/837564505952747520/884299205814943804/unboxing.gif', 'Broken String': 'https://cdn.discordapp.com/attachments/837564505952747520/884299266439405599/unboxing.gif', 'Mouse Pad': 'https://cdn.discordapp.com/attachments/837564505952747520/884299319820288020/unboxing.gif', 'Bronze Spoon': 'https://cdn.discordapp.com/attachments/837564505952747520/884299381682102292/unboxing.gif', 'Flower Vase': 'https://cdn.discordapp.com/attachments/837564505952747520/884299441077637120/unboxing.gif', 'Maths Book': 'https://cdn.discordapp.com/attachments/837564505952747520/884299498698965062/unboxing.gif', 'Charger': 'https://cdn.discordapp.com/attachments/837564505952747520/884299557301800960/unboxing.gif', 'Wall Clock': 'https://cdn.discordapp.com/attachments/837564505952747520/884299620279279696/unboxing.gif', 'Pen Stand': 'https://cdn.discordapp.com/attachments/837564505952747520/884299691716640808/unboxing.gif', 'Book Stand': 'https://cdn.discordapp.com/attachments/837564505952747520/884299761048506458/unboxing.gif', 'Magnifying Glass': 'https://cdn.discordapp.com/attachments/837564505952747520/884299815809327124/unboxing.gif', 'Lollipop': 'https://cdn.discordapp.com/attachments/837564505952747520/884299882087723038/unboxing.gif', 'Eaten Chocolate': 'https://cdn.discordapp.com/attachments/837564505952747520/884299941256777779/unboxing.gif', 'Lighter': 'https://cdn.discordapp.com/attachments/837564505952747520/884300000534872104/unboxing.gif', 'Tennis Ball': 'https://cdn.discordapp.com/attachments/837564505952747520/884300063340372058/unboxing.gif', 'Rubics Cube': 'https://cdn.discordapp.com/attachments/837564505952747520/884300126347210792/unboxing.gif', 'Hourglass': 'https://cdn.discordapp.com/attachments/837564505952747520/884300185558220800/unboxing.gif', 'Coffee Mug': 'https://cdn.discordapp.com/attachments/837564505952747520/884300253384306698/unboxing.gif', 'Broken CD': 'https://cdn.discordapp.com/attachments/837564505952747520/884300312574304266/unboxing.gif', 'A wallet': 'https://cdn.discordapp.com/attachments/837564505952747520/884300386612158464/unboxing.gif', 'RC Drone': 'https://cdn.discordapp.com/attachments/837564505952747520/884300449354764318/unboxing.gif', 'Copper Wire': 'https://cdn.discordapp.com/attachments/837564505952747520/884300511413694464/unboxing.gif', 'Gold Chain': 'https://cdn.discordapp.com/attachments/837564505952747520/884300577046159410/unboxing.gif', 'Headphones': 'https://cdn.discordapp.com/attachments/837564505952747520/884300644171788298/unboxing.gif', 'Party Speakers': 'https://cdn.discordapp.com/attachments/837564505952747520/884300701260460073/unboxing.gif', 'Mobile Phone': 'https://cdn.discordapp.com/attachments/837564505952747520/884300759464833044/unboxing.gif', 'Electric Guitar': 'https://cdn.discordapp.com/attachments/837564505952747520/884300815634956328/unboxing.gif', 'Travel Bag': 'https://cdn.discordapp.com/attachments/837564505952747520/884300870706151454/unboxing.gif', 'Mini Boom Box': 'https://cdn.discordapp.com/attachments/837564505952747520/884300922396758086/unboxing.gif', 'Broken Television': 'https://cdn.discordapp.com/attachments/837564505952747520/884300982572425286/unboxing.gif', 'Gaming Chair': 'https://cdn.discordapp.com/attachments/837564505952747520/884301042056056932/unboxing.gif', 'Antique Painting': 'https://cdn.discordapp.com/attachments/837564505952747520/884301102491783188/unboxing.gif', 'WIFI Router': 'https://cdn.discordapp.com/attachments/837564505952747520/884301170707922954/unboxing.gif', 'Gold Spectacles': 'https://cdn.discordapp.com/attachments/837564505952747520/884301226626388028/unboxing.gif', 'Piano': 'https://cdn.discordapp.com/attachments/837564505952747520/884301290157510707/unboxing.gif', 'Electric Drums': 'https://cdn.discordapp.com/attachments/837564505952747520/884301353571213383/unboxing.gif', 'Laptop': 'https://cdn.discordapp.com/attachments/837564505952747520/884301429873979432/unboxing.gif', 'Laser Printer': 'https://cdn.discordapp.com/attachments/837564505952747520/884301503706312744/unboxing.gif', 'Money Bag': 'https://cdn.discordapp.com/attachments/837564505952747520/884301568390873108/unboxing.gif', 'Gold Brick': 'https://cdn.discordapp.com/attachments/837564505952747520/884301655678525510/unboxing.gif', 'War Sword': 'https://cdn.discordapp.com/attachments/837564505952747520/884301729921896499/unboxing.gif'}
devs = [669816890163724288, 771601176155783198, 713056818972066140]
staff = [669816890163724288, 771601176155783198, 619377929951903754, 713056818972066140, 517402093066256404, 459350068877852683]
disregarded = []
embedcolor = 3407822
loading = "<a:EconomyLoading:884701041097060382>"

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
phrases = {
  "selfrob_success": [
      "You tried robbing yourself and got {prize} coins. But surprisingly {prize} coins were missing from your wallet too!",
      "You robbed yourself of {prize} coins. WHat did ya achieve by this?",
      "You fought yourself and stole {prize} coins from your own wallet. Tiring day!",
      "You thought of robbing yourself. Even got hands on {prize} coins! But they were missing from your wallet. Mystery..?",
      "Your wallet was missing {prize} coins, know why? Because you robbed yourself of it!"
  ],
  "selfrob_failed": [
      "You bonked your head to rob yourself, but you fainted right after it. Hospital cost {prize*2} coins",
      "You punched your own face because you thought of robbing yourself. Medication cost {prize} coins",
      "You tried stealing money from your own wallet, but dropped the coins in drain. Lost {prize} coins!",
      "You gave yourself poison to rob, but ended up being in hospital. Spent {prize*5} coins for treatment"
  ],
  "rob_success": [
      "You robbed {whom} and got {prize} coins. Shhh!",
      "You sneaked quietly from behind and robbed {whom} of {prize} coins",
      "You DDOSed {whom}'s just to get {prize} coins. Quite big crime for it!",
      "{whom} was robbed of {prize} coins. Don't know who did it",
      "You robbed {whom} by punching him for mere {prize} coins. Got them, though."
  ],
  "rob_failed": [
      "You tried robbing {whom}, but he was alert and you got caught. Lost {prize} coins.",
      "You punched {whom} to rob, but he was stronger. You lost {prize} coins in medication",
      "You sneaked in your {whom}'s house, but he caught you. Payed {prize} fine to cops to get off",
      "You missed the pick-pocket to {whom} and got caught. Payed {prize} to police to escape",
      "You tried to rob {whom} but he caught and complained about you. Payed {prize} as a fine"
  ],
  "find_success": [
      "Yoo I found {c} coins in my sofa!",
      "I wonder who left {c} coins on the bus seat?",
      "Did anyone see me picking up {c} coins from footpath?",
      "Damn, imagine leaving {c} coins in the trash!",
      "Did my cat pooped out {c} coins? Must have eaten in dinner..",
      "Sheesh I found {c} coins in my coat pockets!",
      "Is sock a place to keep {c} coins? Nevermind I ll just take it",
      "Yeah! {c} coins on top of refrigerator ain't a joke"
  ],
  "find_failed": [
      "Well I went to find coins, but lost {c} instead",
      "What a bad day, lost {c} coins due to greed",
      "I shouldn't be greedy, lost {c} coins to a thief. oof",
      "Well I searched the drain for coins, but lost {c} of my own!",
      "Noo! Lost {c} coins in search of more",
      "Did I just lose {c} coins? Oh yes, I did.",
      "I don't know how I ended up losing {c} coins today"
  ],
  "find_neutral": [
      "Well I expected something this time",
      "0? R.I.P. my expectations",
      "Comeon I found nothing again!?",
      "How come I searched and searched but found absolutely nothing?",
      "And here I went to find coins, but came back empty handed"
  ],
  "shop_noitem": [
      "Maybe you should wear spectacles?",
      "Did you even read the name properly?",
      "Time to send you back to 1st grade to learn how to read",
      "Why didn't you cross-check the item name before bothering me?",
      "Bro, just go and re-check the name!"
  ],
  "less_bal": [
      "Aww my poor soul, you don't have coins lmao",
      "Oh No! Not enough money? Go beg from our mum haha",
      "Imagine not having enough money but still trying lmfao",
      "Ew you poor, go and do something worthwhile!",
      "Bro, atleast check with your wallet before bothering me",
      "Why you bother me when you don't have enough coins?"
  ],
  "negative": [
      "Ah, so the counting is 0, -1, -2... Don't mind but you should learn basic stuff first",
      "No man, we count from 0 in positive direction",
      "Negative? Are you drunk or what lmao",
      "Wow. I am amazed how 1st graders are playing with me, don't even know counting!",
      "Time to send you back to 1st grade so you learn counting lol",
      "Dude, have you ever tried to mess but failed? Yes, now!",
      "Lmfao, its 0, 1, 2, 3... Go and learn it first"
  ],
  "zero": [
      "0? Did I ask your math test marks?",
      "No man, 0 isn't the way to mess with me",
      "Lmao 0. I accept positive number only, take it or leave it",
      "Do I look your mum? Because I dont want to know your marks",
      "You should go and take up a course for common sense.. wait is there even any??",
      "Atleast enter a positive number bruh",
      "Did Aryabhatta invent `0` for this purpose?"
  ],
  "inv_noitem": [
      "Do you even own this??",
      "Damn, imagine trying to use thin air",
      "Well, what now?",
      "Dude why do you bother me with such useless things?",
      "Imagine trying to use what you don't own lmao"
  ],
  "cooldown": [
      "Oi why in so much hurry? Come again after `{timeleft}`",
      "I guess your mom is calling you, come after `{timeleft}`",
      "Oh no, let me rest. I will look into it after `{timeleft}`",
      "Please not now. Wait for `{timeleft}`",
      "Yeah sure, but after `{timeleft}`, please!",
      "I will be happy if you will retry after `{timeleft}`",
      "All I would say is- wait `{timeleft}` for it. Thanks!"
  ],
  "inter": [
      "Smh are you `{usertag}`? No. So stop clicking buttons!",
      "Bruh man this isn't for you",
      "Dude, why are you poking nose in things which ain't yours.",
      "Hey hey, shoo. This isn't for you",
      "Hi `{usertag}`! No, as it was for him only..",
      "Idk man why you touching things with aren't yours",
      "Ok ok, I know its interesting but ||THIS IS NOT FOR YOU!!||"
  ]
}