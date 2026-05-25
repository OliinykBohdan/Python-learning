# Simple telegram bot (Aiogram)

---

## Project Goal

The goal of this project is to create a simple Telegram bot using Aiogram with commands, reply keyboards, inline keyboards, and callback handling.

---

## About

This is a small asynchronous Telegram bot written in Python using the aiogram framework.

The project demonstrates the basics of building Telegram bots with asynchronous programming and includes:
- Command handling
- Reply keyboards
- Inline keyboards
- Callback queries
- Custom text responses

---

## Features

- `/start` command
- `/help` command
- `/about` command
- Reply keyboard support
- Inline keyboard support
- Callback query handling
- Custom text message handling
- Environment variable support with `.env`

---
## How to run

Requirements:
- Python 3.x
- Aiogram 3.x

Install dependencies:

```bash
pip install aiogram python-dotenv

Create a .env file:
BOT_TOKEN=your_bot_token

Run the bot:
python bot.py
```
## Project Structure
```text
.
├── bot.py
├── handlers.py
└── .env
```

## What I learned
- Working with Aiogram routers
- Creating Telegram bot commands
- Using reply and inline keyboards
- Handling callback queries
- Using asynchronous functions (`async/await`)
- Loading environment variables with `dotenv`
