# FSM Telegram Bot (Aiogram)

---

## Project Goal

The goal of this project is to practice working with FSM (Finite State Machine) in Aiogram by creating a Telegram bot that collects user data step by step.

---

## About

This is a simple asynchronous Telegram bot written in Python using the aiogram framework.

The bot uses FSM (Finite State Machine) to guide the user through multiple steps of data input and demonstrates:

- State management with FSM
- Step-by-step form handling
- Input validation
- Command handling
- Working with routers
- Asynchronous programming

---

## Features

- `/start` command
- `/cancel` command
- FSM state management
- Multi-step form input
- Name input handling
- Age validation
- Phone number validation
- User data collection
- Custom text responses
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
- Working with FSM in Aiogram
- Creating multi-step forms
- Managing user states
- Validating user input
- Working with routers and handlers
- Using asynchronous functions (`async/await`)
- Loading environment variables with `dotenv`
