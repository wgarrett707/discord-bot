import discord
import datetime, pytz
import time
import bs4 as bs
import urllib.request
import requests
import shutil
import random
import wikipedia
import asyncio

LONG_ID = ''

def checkOnline(message):
    guildMembers = message.guild.members
    for member in guildMembers: 
        print(member, member.status)

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return  
        if message.content.startswith('-hello'):
            await message.channel.send('Hello {0.author.mention}'.format(message))
        elif message.content.startswith('-messages'):
            messageChannel = message.Channel
            index = 0
            counter = 0
            while index < len(message.guild.text_channels):
                for TextChannel in message.guild.text_channels:
                    if TextChannel.position == index:
                        selectedChannel = TextChannel
                print(selectedChannel.name)
            #make sure to add an "after" date in the parentheses below
                async for message in selectedChannel.history(limit=None):
                    if message.author.bot == False:
                        counter = counter + 1
                index = index + 1
            await messageChannel.send('{} messages sent in total'.format(counter))
        #remember to fix this next one 
        elif message.content.startswith('-datejoined'):
            dateAuthor = message.author
            if message.mentions:
                datePerson = message.mentions[0]
            else:
                datePerson = dateAuthor
            dateJoined = datePerson.joined_at.replace(tzinfo=pytz.UTC).astimezone(pytz.timezone("US/Central"))
            datem = dateJoined.strftime("%m")
            dated = dateJoined.strftime("%d")
            dateY = dateJoined.strftime("%Y")
            dateA = dateJoined.strftime("%A")
            dateI = dateJoined.strftime("%I")
            dateM = dateJoined.strftime("%M")
            datep = dateJoined.strftime("%p")
            dateMessage = "{} joined {} on {}-{}-{} ({}) at {}:{} {}".format(datePerson.mention, message.guild.name, datem, dated, dateY, dateA, dateI, dateM, datep)
            await message.channel.send(dateMessage)
            
        elif message.content == '-help':
            await message.channel.send('Here is a list of commands: -atbys, -datejoined, -hello, -help, -messages, -pick, -stockprice, -say')
            if "atbys" in message.content:
                await message.channel.send('*-atbys* counts the number of times the server, users, bots, and a specified user have stated \"attaboy\." \n**Usage:** -atbys [mention user]')
            if "datejoined" in message.content:
                await message.channel.send('*-datejoined* calculates the date and time that a specified user joined the server. \n**Usage:** -datejoined [mentioned user]')
            if "hello" in message.content:
                await message.channel.send('*-hello* simply greets the user saying the command.')
            if " help" in message.content:
                await message.channel.send('*-help* gives a full list of commands that work with AttaBOT')
            if "messages" in message.content:
                await message.channel.send('*-messages* counts all of the messages in the server.')
            if "pick" in message.content:
                await message.channel.send('*-pick* chooses randomly between two or more options given to the bot. \n**Usage:** -pick [option], [option]')
            if "stockprice" in message.content:
                await message.channel.send('*-stockprice* gives the live stock price of any specified stock. \n**Usage:** -stockprice [stock symbol]')
            if "say" in message.content:
                await message.channel.send('*-say* makes the bot repeat your message. \n**Usage:** -say [message]') 
                                           
        elif message.content.startswith('-stockprice'):
            selectedStock = message.content.replace("-stockprice ", "")
            stockURL = 'https://finance.yahoo.com/quote/' + selectedStock
            sauce = urllib.request.urlopen(stockURL).read()
            soup = bs.BeautifulSoup(sauce, 'lxml')
            price = 1
            price = soup.find('span', {"data-reactid": "14"}).text
            if price == None or price == "":
                price = "error"
            nameGrab = soup.title.text
            name = nameGrab.replace(" Stock Price, Quote, History & News", "")
            if name == "Requested symbol wasn't found":
                stockMessage = name
            else:
                stockMessage = name + " has a stock price of $" + price
            if stockMessage == "Symbol Lookup from Yahoo Finance has a stock price of $Stocks (0)":
                stockMessage = "Requested symbol wasn't found"
            await message.channel.send(stockMessage)
        elif message.content.startswith('-say'):
            await message.channel.send(message.content.replace("-say ", ""))
        elif message.content.startswith('-pick'):
            pickList = message.content.replace("-pick ", "")
            pickList = list(pickList.split(", "))
            pickMessage = "I have selected **" + str(random.choice(pickList)) + "**"
            await message.channel.send(pickMessage)
        lowerCaseMessage = message.content.lower()
        containsAttaboy = lowerCaseMessage.find("attaboy")
        if containsAttaboy > -1:
            await message.channel.send("Attaboy {}! :smile:".format(message.author.mention))
        elif message.content.startswith('-atbys'):
            atbysChannel = message.channel
            atbysAuthor = message.author
            index = 0
            attaboyUserCounter = 0
            attaboyBotCounter = 0
            attaboyTotalCounter = 0
            attaboyAuthCounter = 0
            if message.mentions:
                atbysPerson = message.mentions[0]
            else:
                atbysPerson = atbysAuthor
            atbysMessageText = "Calculating... \n\nChannels Scanning:"
            atbysMessage = await atbysChannel.send(atbysMessageText)
            while index < len(message.guild.text_channels):
                for TextChannel in message.guild.text_channels:
                    if TextChannel.position == index:
                        selectedChannel = TextChannel
                print(selectedChannel.name)
                atbysMessageText = atbysMessageText + "\n" + selectedChannel.name
                await atbysMessage.edit(content=atbysMessageText)
            #make sure to add an "after" date in the parentheses below
                async for message in selectedChannel.history(limit=None):
                    lowerCaseAtby = message.content.lower()
                    containsAttaboyAtby = lowerCaseAtby.count("attaboy")
                    if containsAttaboyAtby > 0:
                        if message.author.bot == True:
                            attaboyBotCounter += containsAttaboyAtby
                            attaboyTotalCounter += containsAttaboyAtby
                        if message.author.bot == False:
                            attaboyUserCounter += containsAttaboyAtby
                            attaboyTotalCounter += containsAttaboyAtby
                        if message.author == atbysPerson:
                            attaboyAuthCounter += containsAttaboyAtby
                index += 1
            await atbysChannel.send("Note: This *does* count multiple attaboys per message, unlike using the search bar \n The total amount of attaboys in this server is {} \n The amount of attaboys said by real users is {} \n The amount of attaboys said by bots is {} \n The amount of attaboys that {} said is {}".format(attaboyTotalCounter, attaboyUserCounter, attaboyBotCounter, atbysPerson.mention, attaboyAuthCounter))
        elif message.content.startswith('-testing'):
            print(message.attachments)
            if not message.attachments:
                await message.channel.send("None")
            else:
                await message.channel.send(message.attachments[0].url)
                r = requests.get(message.attachments[0].url, stream=True)
                if r.status_code == 200:
                    with open(str(message.attachments[0].id), 'wb') as f:
                        r.raw.decode_content = True
                        shutil.copyfileobj(r.raw, f)
        elif message.content.startswith('-whatis'):
            wikiTopic = message.content.replace("-whatis ", "")
            try:
                wikiPage = wikipedia.page(wikiTopic)
                #fix how SVG files don't pop up to users on Discord
                wikiImages = wikiPage.images
                print(wikiImages)
                wikiSummary = wikipedia.summary(wikiTopic, sentences=5) + "\n\nImage: " + wikiImages[0]
            except wikipedia.exceptions.DisambiguationError as e:
                eList = ""
                index = 0
                for suggestion in e.options:
                    index = index + 1
                    if index > 20:
                        break
                    eList = eList + "\n" + suggestion
                wikiSummary = "There are several results for \"" + wikiTopic + ".\" Please repeat the command with one of the options below as your query." + eList
            except wikipedia.exceptions.PageError:
                wikiSummary = "There was no results for \"" + wikiTopic + ".\""
            await message.channel.send(wikiSummary)
            print(wikiSummary)
        
client = MyClient()
client.run(LONG_ID)
