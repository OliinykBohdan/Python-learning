from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import (
    Message
)
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

router = Router()


class Form(StatesGroup):
    name = State()
    age = State()
    phone_number = State()


@router.message(Command('start'))
async def start(message: Message, state: FSMContext):
    await message.answer('Hello! Enter your name:')
    await state.set_state(Form.name)


@router.message(Command('cancel'))
async def cancel_form(message: Message, state: FSMContext):
    await state.clear()
    await message.answer('Cancelled')


@router.message(Form.name, F.text)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)

    await message.answer('Enter your age:')
    await state.set_state(Form.age)


@router.message(Form.age, F.text)
async def process_age(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer('Enter the number:')
        return

    if int(message.text) < 1 or int(message.text) > 100:
        await message.answer('Age must be between 1 and 100.')
        return

    await state.update_data(age=int(message.text))

    await message.answer('Enter your phone number:')
    await state.set_state(Form.phone_number)


@router.message(Form.phone_number, F.text)
async def process_phone_number(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer('Enter the phone number:')
        return

    await state.update_data(phone_number=int(message.text))
    await state.set_state(Form.phone_number)

    data = await state.get_data()
    name = data['name']
    age = data['age']
    phone_number = data['phone_number']

    await message.answer(f'Your details:\n name - {name}\n age - {age}\n phone number - {phone_number}')
    await state.clear()
