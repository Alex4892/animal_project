import asyncio
import os
from os import getenv
from asgiref.sync import sync_to_async
from aiogram import Bot, Dispatcher
from aiogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    CallbackQuery
)
from aiogram.filters import Command as Com
from django.core.management.base import BaseCommand
from animals_app.models import Animal

TELEGRAM_API_TOKEN = getenv("TG_BOT_TOKEN")
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

@sync_to_async
def get_animals():
    return Animal.objects.all()

class Command(BaseCommand):
    help = "Запуск Telegram бота"

    def handle(self, *args, **kwargs):
        asyncio.run(run_bot())


async def create_animals_keyboard() -> InlineKeyboardMarkup:
    animals = await get_animals()  
    inline_keyboard = []


    for animal in animals:
        button = InlineKeyboardButton(
            text=animal.nickname, 
            callback_data=f"animal_{animal.id}"  
        )
        inline_keyboard.append([button])  

    keyboard = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
    return keyboard



async def start_command(message: Message):
    keyboard = await create_animals_keyboard()
    await message.answer(
        "Выберите объявление, чтобы просмотреть информацию", 
        reply_markup=keyboard 
    ) 


async def animal_details(callback_query: CallbackQuery):
    animal_id = int(callback_query.data.split("_")[-1])  
    animals = await get_animals() 
    animal = next((a for a in animals if a.id == animal_id), None)  
    
    if animal:
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(
                    text="Назад", callback_data="back_to_main")] 
            ]
        )

        await callback_query.message.edit_text(
            f"Описание: {animal.description}\n"
            f"Приметы: {animal.signs}\n"
            f"Город: {animal.city}\n"
            f"Номер телефона: {animal.phone_number}\n"
            f"Контактное лицо: {animal.contact_people}",
            reply_markup=keyboard
        )
    else:
        await callback_query.message.edit_text("Объявление не найдено.")
    await callback_query.answer()  


async def back_to_main_menu(callback_query: CallbackQuery):
    keyboard = await create_animals_keyboard() 
    await callback_query.message.edit_text(
        "Выберите объявление, чтобы просмотреть информацию",
        reply_markup=keyboard 
    )
    await callback_query.answer()


async def run_bot():
    bot = Bot(token=TELEGRAM_API_TOKEN)
    dp = Dispatcher()

    dp.message.register(start_command, Com(commands=["start"]))
    dp.callback_query.register(
        animal_details, lambda c: c.data.startswith("animal_")
    )
    dp.callback_query.register(
        back_to_main_menu, lambda c: c.data == "back_to_main"
    )
    print("Бот запущен. Нажмите CTRL+C для остановки")
    try:
        await dp.start_polling(bot)
    finally: 
        await bot.session.close()
