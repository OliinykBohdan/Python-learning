from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery
)

router = Router()


def get_main_reply_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='About')],
            [KeyboardButton(text='Start'), KeyboardButton(text='Help')],
        ],
        resize_keyboard=True
    )

    return keyboard


def get_main_inline_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='Open site', url='https://google.com')],
            [InlineKeyboardButton(text='Read more', callback_data = 'read more')],
        ]
    )

    return keyboard


@router.callback_query(lambda c: c.data == 'read more')
async def more_info(callback: CallbackQuery):
    await callback.message.answer('More info about bot.')
    await callback.answer()


@router.message(Command('start'))
@router.message(F.text.lower() == 'start')
async def start(message: Message):
    await message.answer(f'Hello, {message.from_user.first_name}!\n\n Type /help for assistance.')


@router.message(Command('help'))
@router.message(F.text.lower() == 'help')
async def explorer(message: Message):
    await message.answer('Commands:\n/start - start bot\n/help - list of commands\n/about - about us',
                         reply_markup = get_main_reply_keyboard())


@router.message(Command('about'))
@router.message(F.text.lower() == 'about')
async def about(message: Message):
    await message.answer('Some info about bot.', reply_markup=get_main_inline_keyboard())


@router.message()
async def text_from_user(message: Message):
    await message.answer('Some text.')
