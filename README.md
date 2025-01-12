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

![image](https://github.com/user-attachments/assets/7a2592dd-2895-4213-9004-c837f5b5e988)

---

### 📅 Date Joined
- **Command:** `-datejoined [@user]`
- **Description:** Displays the exact date and time a user joined the server. Defaults to the command issuer if no user is mentioned.
- **Usage:** `-datejoined @exampleuser`

![image](https://github.com/user-attachments/assets/346998e8-0329-4f0f-9f43-71999d5c6cc0)

---

### 💰 Stock Price
- **Command:** `-stockprice [stock symbol]`
- **Description:** Fetches the live stock price for a given symbol using Yahoo Finance.
- **Usage:** `-stockprice AAPL`

  ![image](https://github.com/user-attachments/assets/d6629c20-1e2f-49e4-a71c-0e3a5cf2b5f8)

---

### 🎲 Random Picker
- **Command:** `-pick [option1], [option2], ...`
- **Description:** Randomly selects an option from a list.
- **Usage:** `-pick option1, option2, option3`

![image](https://github.com/user-attachments/assets/f5c37c09-a9ee-4ccf-9149-3e7939fc45b9)

---

### 🗨️ Say Command
- **Command:** `-say [message]`
- **Description:** Makes the bot repeat the provided message.
- **Usage:** `-say Hello, world!`

![image](https://github.com/user-attachments/assets/250ae7de-d31f-41c9-9966-98a513c5e9b4)

---

### 🏆 Attaboy Tracker
- **Command:** `-atbys [@user]`
- **Description:** Tracks the number of times "attaboy" has been said in the server, by users, bots, and the specified user. If no username is given, the user who said the command is chosen.
- **Usage:** `-atbys @exampleuser`

  ![image](https://github.com/user-attachments/assets/4c7a0dfc-fd7b-4813-b1f6-6ed30c6f615c)

---

### 📝 Wikipedia Lookup
- **Command:** `-whatis [topic]`
- **Description:** Provides a summary of the specified topic using Wikipedia. Displays an image if available.
- **Usage:** `-whatis Python programming`

  ![image](https://github.com/user-attachments/assets/6ce68429-6442-4d01-b17d-96c5f100d667)

---

### 📜 Help
- **Command:** `-help`
- **Description:** Displays a list of available commands with usage instructions.

  ![image](https://github.com/user-attachments/assets/aac2e4a3-362c-44d1-90a6-f31203289d27)

---
