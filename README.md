<p align="center">
  <a href="" rel="noopener">
  <img width=200px height=200px src="https://github.com/pupubird/42kl-stalker-bot/blob/master/img/logo.png" alt="Project logo"></a>
</p>

<h3 align="center">42KL Stalker Bot 😈</h3>

> _Icons made by [Nhor Phai](https://www.flaticon.com/authors/nhor-phai) from [www.flaticon.com](www.flaticon.com)_

---

<p align="center"> Easily stalk any student's location within the campus 🥳 (JK It's just a bot that tells you where the user is currently sitting at)
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Built Using](#built_using)
- [Authors](#authors)

## 🧐 About <a name = "about"></a>

Having issues with knowing where a person is for your evaluation? Here are a few scenarios where this bot would be helpful:

```joke
A: @XXX May I know where you? I have an evaluation with you in 10 minutes!

B: *Disappeared for 1 hour as he / she did not check discord*

A: *Project failed because couldn't get evaluation done within the period of time*
```

Now, with this bot,

```
A: /find XXX

Wonderful generous 42kl stalker bot: XXX is currently sitting at YYY!

A: *Evaluation gets done in time and got 100 points! 💯*
```

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

You need `python3` and a discord bot!

### Installing

```
pip3 install -r requirements.txt
```

or

```
pip3 install pip-tools
pip-compile
pip3 install -r requirements.txt
```

Copy `.env.example` and paste in `.env` and fill up all the information!

Then...

```
python3 main.py
```

And you are done!

## 🎈 Usage <a name="usage"></a>

Just add the bot into your Discord channel, type `/find <username>` and enjoy!

## ⛏️ Built Using <a name = "built_using"></a>

- [discord.py](https://pypi.org/project/discord.py/) - Python Discord SDK
- [Requests](https://pypi.org/project/requests/) - The most famous python HTTP library

## ✍️ Authors <a name = "authors"></a>

- [@pupubird](https://github.com/pupubird) - Dealing with 42 API and writing SDK
- [@easonchai](https://github.com/easonchai) - Created Discord bot, Discord commands & editing
