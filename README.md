# discord-bot

A multifunctional Discord bot named "AttaBOT" that I designed with fun commands, helpful tools, and unique features. 

## 📚 Stack

- **Language:** Python
- **Libraries:** 
  - [discord.py](https://github.com/Rapptz/discord.py)
  - [pytz](https://pythonhosted.org/pytz/)
  - [BeautifulSoup (bs4)](https://www.crummy.com/software/BeautifulSoup/)
  - [wikipedia](https://pypi.org/project/wikipedia/)
  - [requests](https://docs.python-requests.org/en/latest/)

## 📦 Features

### 👋 Greetings
- **Command:** `-hello`
- **Description:** Replies with a friendly "Hello" and mentions the user.

---

### 📅 Date Joined
- **Command:** `-datejoined [@user]`
- **Description:** Displays the exact date and time a user joined the server. Defaults to the command issuer if no user is mentioned.
- **Usage:** `-datejoined @exampleuser`

---

### 📊 Total Messages
- **Command:** `-messages`
- **Description:** Counts the total number of non-bot messages in all text channels across the server.

---

### 💰 Stock Price
- **Command:** `-stockprice [stock symbol]`
- **Description:** Fetches the live stock price for a given symbol using Yahoo Finance.
- **Usage:** `-stockprice AAPL`

---

### 🎲 Random Picker
- **Command:** `-pick [option1], [option2], ...`
- **Description:** Randomly selects an option from a list.
- **Usage:** `-pick option1, option2, option3`

---

### 🗨️ Say Command
- **Command:** `-say [message]`
- **Description:** Makes the bot repeat the provided message.
- **Usage:** `-say Hello, world!`

---

### 🏆 Attaboy Tracker
- **Command:** `-atbys [@user]`
- **Description:** Tracks the number of times "attaboy" has been said in the server, by users, bots, and the specified user.
- **Usage:** `-atbys @exampleuser`

---

### 📝 Wikipedia Lookup
- **Command:** `-whatis [topic]`
- **Description:** Provides a summary of the specified topic using Wikipedia. Displays an image if available.
- **Usage:** `-whatis Python programming`

---

### 📜 Help
- **Command:** `-help`
- **Description:** Displays a list of available commands with usage instructions.

---
