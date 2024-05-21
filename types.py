from typing import Any, Optional, Union, Literal


# Instance that shows how to use type annotation 'Any'
def anyTypeFunc(argument: Any) -> None:
    pass


# Optional accepts one specific argument or none
def optionalTypeAnnotation(str: Optional[str]) -> str | None:
    pass


# Union combines a number of possible type annotations as an argument
var_Union: Union[bool, None, list]
var_UnionAlternative: bool | None | list



# Literal type annotation is used when specific values for an argument(s) expected
arg: dict[Literal["username"] | Literal["email"] | Literal["password"], str]

""" Classes and dataclasses """

class Person():
    def __init__(self, person_id: int, age: int, name: str, email: str):
        self.person_id = person_id
        self.age = age
        self.name = name
        self.email = email

def get_person_info(person: Person) -> str:
    return f"{person.name} is {person.age} " \
            f"years old. He/She has an email {person.email}"

person_1: Person = Person(109387, 26, "Eugene", "eugene@gmail.com")
# print(get_person_info(person_1), end= "\n-------------------------------------------\n")
# print(Person.__init__.__annotations__)
from dataclasses import dataclass

@dataclass(frozen= True)
class EthernetProtocolStructure():
    preamble: int
    SFD: int
    destination: int
    source: int
    type: int
    data_and_padding: str
    FCS: int

    def __str__(self):
        return f"Preamble: {self.preamble}\nSFD: {self.SFD}\nDestination: {self.destination}\nSource: {self.source}\n" \
                f"Data and Padding: {self.data_and_padding}\nFCS: {self.FCS}"

ether_1 = EthernetProtocolStructure(7, 1, 6, 6, 2, "46 - 1500", 4)
# print(ether_1)
""" Below assignment won't work because of the instance's frozen state."""
# ether_1.data_and_padding = "1000"
# print(ether_1)

# import requests

# request = requests.get("http://api.open-notify.org/iss-now.json")
#
# if request.status_code == 200:
#     print(f"Request successful\n"
#           f"{request.text}.")
#     coordinates = request.json().get('iss_position')
#     formatted_coordinates = f"{coordinates['longitude']}%2C{coordinates['latitude']}"
#     map_url = f"https://yandex.com/maps/?||={formatted_coordinates}&z=10"
#     print(map_url)
# else:
#     print(f"Response code - {request.status_code}")
#
#
# response_number43 = requests.get("http://numbersapi.com/43?json")
# print(response_number43.json().get('text'))

" ---------------------------------------------------------------------- "
# import json
# import time
#
# url = "https://api.telegram.org/bot"
# token = "7189166713:AAFplUTZndRgivPEkLAj9nQFfd0bHw2bibI"
#     # chat_id = "1600526965"
# offset: int = -5
# counter: int = 0
# max_limit: int = 100
# text = "Update has been processed. Thank you"
#
# response_dict = requests.get(f"{url + token}/getUpdates").json()
# print(json.dumps(response_dict, indent= 2, sort_keys= True))
#
# print(type(response_dict['result']))
#
# while counter < max_limit:
#     print(f"Attempt: {counter}")
#
#     response = requests.get(f"{url + token}/getUpdates?offset={offset + 1}&limit=100").json()
#
#     if response['result']:
#         if offset <= -1:
#             for result in response['result']:
#                 offset += 1
#                 chat_id: int = result['message']['chat']['id']
#                 bot_message = requests.get(f"{url + token}/sendMessage?chat_id={chat_id}&text={text}")
#         else:
#             for result in response['result']:
#                 offset: int = result['update_id']
#                 chat_id: int = result['message']['chat']['id']
#                 bot_message = requests.get(f"{url + token}/sendMessage?chat_id={chat_id}&text="
#                                            f"{text + result['message']['text']}")
#     counter += 1
#     time.sleep(1)


" ---------------------------------------------------------------------------------------------------- "

# import time
# import json
#
# url: str = "https://api.telegram.org/bot"
# token: str = "7189166713:AAFplUTZndRgivPEkLAj9nQFfd0bHw2bibI"
# max_number: int = 100
# counter: int = 0
# offset: int = -1
#
# kitties_api: str = "https://api.thecatapi.com/v1/images/search"
#
# kitties_api_response = requests.get(f"{kitties_api}").json()[0]['url']
# foxies_response: str = "https://randomfox.ca/floof/"
# # print(kitties_api_response)
#
# while counter < max_number:
#     response = requests.get(f"{url + token}/getUpdates?offset={offset + 1}&limit=100").json()
#
#     if response['result']:
#         for result in response['result']:
#             # kitties_api_response = requests.get(f"{kitties_api}")
#             print("TEST")
#             foxies_api_response = requests.get(f"{foxies_response}")
#             print(foxies_api_response)
#             chat_id = result['message']['chat']['id']
#             offset = result['update_id']
#
#             print("Below is a response code")
#             print(foxies_api_response.status_code)
#             if foxies_api_response.status_code == 200:
#                 photo = requests.get(f"{url + token}/sendPhoto?chat_id={chat_id}&photo={foxies_api_response.json()['image']}")
#             else:
#                 requests.get(f"{url + token}/sendMessage?chat_id={chat_id}&text=You should have received a photo instead of this message :(")
#
#     print(offset)
#     print(counter)
#     counter += 1
#     time.sleep(1)


" ------------------------------------------------------------------------------------------------------------- "

# import time
#
#
# url = "https://api.telegram.org/bot"
# token = "7189166713:AAFplUTZndRgivPEkLAj9nQFfd0bHw2bibI"
# counter = 0
# offset = -3
#
# while counter < 100:
#     start_time = time.time()
#
#
#     def was_update() -> None:
#         print("Was update")
#
#     response = requests.get(f"{url + token}/getUpdates?timeout=-15.22&offset={offset + 1}").json()
#     if response['result']:
#         for result in response['result']:
#             print(str(result['update_id']) + "\n" + result['message']['text'])
#             offset = result['update_id']
#
#
#     end_time = time.time()
#     print(f"It took {end_time - start_time} seconds to implement this iteration\n"
#           f"Counter: {counter}")
#
#     time.sleep(3)

" ------------------------------------------------------------------------------------------------- "
# Echo - bot

from aiogram import Bot, Dispatcher
from aiogram.filters import Command, Filter
from aiogram.types import Message
from aiogram.methods import SendMessage


# cat_api: str = "https://api.thecatapi.com/v1/images/search"
# fox_api: str = "https://randomfox.ca/floof/"
#
# BOT_TOKEN = "7189166713:AAFplUTZndRgivPEkLAj9nQFfd0bHw2bibI"
# bot = Bot(token=BOT_TOKEN)
# dp = Dispatcher()


# @dp.message(Command(commands=['start']))
# async def process_start_command(message: Message) -> Message:
#     answer_return = await message.answer(text=f"Hello, {message.chat.first_name} {message.chat.last_name}! Pleasure to meet you.\n"
#                                               "This is the start of our conversation. Enter:\n"
#                                               "'/help' - to get help")
#     print(answer_return)
#     print(type(answer_return))
#     return answer_return
#
# @dp.message(Command(commands=['help']))
# async def process_help_command(message: Message):
#     await message.answer(text=f"'help':\n"
#                          f"This bot will reply/echo with the same message you have sent to the chat.")
#
# @dp.message(Command(commands=["fox", "Fox", 'foxie', "Foxie", "Лис", "лис", "Лиса", "лиса", "Лисенок", "лисенок"]))
# async def send_fox_photo(message: Message):
#     fox_api_response = requests.get(fox_api)
#     print(fox_api_response)
#     if fox_api_response.status_code == 200:
#         await message.answer_photo(
#             photo= fox_api_response.json()['image'],
#             caption= "Хочу кушать < '!' >"
#         )
#     else:
#         await message.answer(
#             text=f"To my deep regret, we had an unexpected error in the internetwork :(\n\nCome again and later for another attempt :=)"
#         )
#
# @dp.message(Command(commands=["Cat", "cat", "kitten", "Kitten", "Kittie", "kittie", "Meow", "meow",
#                               "Кот", "кот", "Кошка", "кошка", "Котенок", "котенок", "Кошак", "кошак", "Кошара", "кошара",
#                               "Мур", "мур", "Мяу", "мяу"]))
# async def send_cat_photo(message: Message):
#     cat_api_response = requests.get(cat_api)
#     if cat_api_response.status_code == 200:
#         await message.answer_photo(
#             photo= cat_api_response.json()[0]['url'],
#             caption= "Мяу (=◑ᆺ◐=)"
#         )
#     else:
#         await message.answer(
#             text= "No response from the API :(\nCome back later for another attempt ^_^"
#         )
#
# @dp.message()
# async def send_echo(message: Message):
#     await message.reply(
#         text= f"{message.text}"
#     )

# if __name__ == "__main__":
#     dp.run_polling(bot)

" ------------------------------------------------------------------------------------ "
"""
import json


from aiogram import Dispatcher, Bot, F
from aiogram.types import Message, ContentType
from aiogram.filters import Command

cat_api: str = "https://api.thecatapi.com/v1/images/search"
fox_api: str = "https://randomfox.ca/floof/"

BOT_TOKEN = "7189166713:AAFplUTZndRgivPEkLAj9nQFfd0bHw2bibI"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Start handler
async def process_start_command(message: Message):
    print("Start", message.model_dump_json(indent= 4), sep="\n")
    await message.answer(
        text=f"Hi, {message.from_user.first_name } {message.from_user.last_name}!\n"
             f"That's the start of our wonderful conversation. Please enter:\n"
             f"'/help' - to get help"
    )

async def process_help_command(message: Message):
    print("Help", message.json(), sep="\n")
    await message.reply(
        text= f"This bot echoes your commands resembling you a feeling of what having a parrot is like"
    )


async def prosess_fox_command(message: Message):
    print("Fox\n", message)
    fox_api_response = requests.get(fox_api).json()['image']
    await message.answer_photo(
        photo= f"{fox_api_response}",
        caption= f"Хочу кушать < '!' >\n"
    )

async def process_cat_command(message: Message):
    print("Cat\n", message)
    cat_api_response = requests.get(cat_api).json()[0]['url']
    cat = await message.answer_photo(
        photo=f"{cat_api_response}",
        caption= f"Мяу (=◑ᆺ◐=)\n"
    )
    print(cat)



async def echo_photo(message: Message):
    print("Photo\n", message)
    photo = message.photo[0]
    await message.reply_photo(
        photo= photo.file_id,
        caption= f"First photo, size: {photo.file_size}"
    )
    # await message.reply_photo(
    #     photo= photo_2.file_id,
    #     caption= f"Last photo, size: {photo_2.file_size}"
    # )


async def process_voice(message: Message):
    print("Voice\n", message, end="\n--------------------------------\n")
    await message.reply_voice(
        voice= message.voice.file_id,
        caption= f"File size: {message.voice.file_size}, duration: {message.voice.duration}"
    )

async def process_sticker(message: Message):
    print("Sticker", message, sep="\n")
    await message.reply_sticker(
        sticker=message.sticker.file_id
    )

import datetime

async def process_animation(message: Message):
    print("Animation")
    print(message)
    await message.reply_animation(
        animation= message.animation.file_id
    )

async def process_document(message: Message):
    print("Document")
    print(message.document)
    await message.reply_document(
        document= message.document.file_id
    )


async def process_audio(message: Message):
    print("Audio\n", message.audio)
    await message.reply_audio(
        audio= message.audio.file_id,
        caption= f"File name: {message.audio.file_name}\n"
                 f"File size: {message.audio.file_size}"
    )

async def process_video(message: Message):
    print("Video\n", message.video)
    await message.reply_video(
        video= message.video.file_id,
        caption= f"Video name: {message.video.file_name}\n"
                 f"Size: {message.video.file_size}"
    )


async def echo_text(message: Message):
    print("Echo_text\n", message)
    await message.reply(
        text= message.text
    )


# async def echo_message(message: Message):
#     print(f"send_copy message")
#     print(message)
#     await message.send_copy(
#         chat_id= message.chat.id,
#         reply_to_message_id= message.message_id
#     )

"Registering all the filters for the function handlers"
dp.message.register(process_start_command, Command(commands=["start"]))
dp.message.register(process_help_command, Command(commands=["help"]))
dp.message.register(prosess_fox_command, Command(commands=["fox"]))
dp.message.register(process_cat_command, Command(commands=["cat"]))
dp.message.register(echo_photo, F.photo)
dp.message.register(process_voice, F.voice)
dp.message.register(process_sticker, F.sticker)
dp.message.register(process_animation, F.animation)
dp.message.register(process_document, F.document)
dp.message.register(process_audio, F.audio)
dp.message.register(process_video, F.video)
dp.message.register(echo_text)
# dp.message.register(echo_message)



if __name__ == "__main__":
    dp.run_polling(bot)
"""


" ----------------------------------------------------------------------------------- "

"""
import random
import requests

from aiogram import Dispatcher, Bot, F
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery



BOT_TOKEN = "7189166713:AAFplUTZndRgivPEkLAj9nQFfd0bHw2bibI"
countries_api = "https://documenter.getpostman.com/view/1134062/T1LJjU52#4d1b73b4-06fb-4031-b04b-e586a156f7aa"
capitals_API = "https://countriesnow.space/api/v0.1/countries/capital"
countries_flag_API = "https://countriesnow.space/api/v0.1/countries/flag/images"



bot = Bot(token= BOT_TOKEN)
dp = Dispatcher()


# This section of the code composes a dictionary with countries and their capitals
capitals = requests.get(capitals_API).json()['data']
countries = {}
for line in capitals:
    countries[line['name']] = {'capital' : line['capital'], 'iso2' : line['iso2'], 'iso3' : line['iso3']}
# else:
#     print(countries, len(countries.keys()), sep='\n')

# This section of the code adds a link to countries' national flags:
countries_flag = requests.get(countries_flag_API).json()['data']
# print(countries_flag)
flags = {}
for item in countries_flag:
    countries[item['name']]['flag'] = item['flag']
# else:
#     print(countries)

print(len(countries.keys()))
print(countries.values())
user_stats = {}
random_country_number = 1
random_country = ""



# This section begins async part of the program:
async def process_start(message: Message):
    await message.answer(
        text= "Добро пожаловать в игру 'Угадай столицу'!\n\n"
              "Выберите одно из нижепредложенных опций для продолжения:\n"
              "'/начать' - для начала игры\n"
              "'/статистика' - статистические данные\n"
              "'/правила' - правила игры"
    )

async def process_help(message: Message):
    await message.answer(
        text= "Игроку в случайном порядке будет предложено название страны столицу которой предстоит отгадать."
              "В случае правильного ответа значения параметров 'Общее кол-во ответов' и 'Кол-во правильных ответов' увеличатся на 1 единицу\n\n"
              "'/начать' - для начала игры;\n"
              "'/сбросить' - для сброса вашего прогресса после чего отсчет попыток начнется с нуля;\n"
              "/выйти - для выхода из игры"
    )

async def process_reset(message: Message):
    user_stats[message.from_user.id]['total_answers'] = 0
    user_stats[message.from_user.id]['correct_answers'] = 0
    await message.answer(
        text= "Your progress has been reset. Woho \\0/\n\n"
              f"Общее кол-во ответов: {user_stats[message.from_user.id]['total_answers']};\n"
              f"Кол-во правильных ответов: {user_stats[message.from_user.id]['correct_answers']}"
    )

async def process_exit(message: Message):
    if not user_stats[message.from_user.id]['state']:
        await message.answer(
            text= f"{message.from_user.first_name} {message.from_user.last_name}, вы, на данный момент, игру не начинали, "
                  "но вы всегда можете ввести '/начать' для ее запуска"
        )
    else:
        user_stats[message.from_user.id]['state'] = False
        await message.answer(
            text= f"Выход из игры выполнен.\nВведите '/начать'"
        )



async def process_stats(message: Message):
    await message.answer(
        text= f"Статы:\n\n"
              f"Общее кол-во ответов: {user_stats[message.from_user.id]['total_answers']}\n"
              f"Кол-во правильных ответов: {user_stats[message.from_user.id]['correct_answers']}"
    )



async def process_game_start(message: Message):
    if message.from_user.id not in user_stats:
        user_stats[message.from_user.id] = {
            'state' : False,
            'total_answers' : 0,
            'correct_answers' : 0
        }
    if user_stats[message.from_user.id]['state']:
        inline_keyboard_markup = InlineKeyboardMarkup(
            inline_keyboard= [[
                InlineKeyboardButton(
                    text= "Next country",
                    callback_data= "next"
                ),
                InlineKeyboardButton(
                    text= "Выйти из игры",
                    callback_data= "exit"
                )

                ]]
        )
        await message.answer(
            text= f"Вы уже в игре.\n\n"
                  f"Выберите 'Next country' или 'Выйти из игры' для обозначения ваших дальнейших действий:",
            reply_markup= inline_keyboard_markup
        )
    else:
        user_stats[message.from_user.id]['state'] = True
        global random_country_number
        random_country_number = random.randint(1, len(countries.keys()))
        global random_country
        random_country = list(countries.keys())[random_country_number - 1]
        await message.answer(
            text= f"Страна: {random_country}\n"
                  f"Флаг: {countries[random_country]['flag']}\n"
                  f"Осталось отгадать: {len(countries.keys())}\n\n"
                  "Введите на английском название столицы:"
        )
    print("When Starting: ", user_stats)

async def process_user_answer(message: Message):
    inline_keyboard_markup = InlineKeyboardMarkup(
        inline_keyboard=[[
            InlineKeyboardButton(
                text="Next country",
                callback_data="next"
            ),
            InlineKeyboardButton(
                text="Выйти из игры",
                callback_data="exit"
            )

        ]]
    )
    if (message.text.lower() == countries[random_country]['capital'].lower()) and (user_stats[message.from_user.id]['state']):
        user_stats[message.from_user.id]['total_answers'] += 1
        user_stats[message.from_user.id]['correct_answers'] += 1
        del countries[random_country]
        await message.answer(
            text= f"Верно!\n"
                  f"Столица {random_country} - {message.text.capitalize()}\n\n"
                  f"Общее кол-во ответов: {user_stats[message.from_user.id]['total_answers']}\n"
                  f"Кол-во правильных ответов: {user_stats[message.from_user.id]['correct_answers']}\n"
                  f"Выберите одно из следующих действий:",
            reply_markup= inline_keyboard_markup
        )
    elif (message.text.lower() != countries[random_country]['capital'].lower()) and (user_stats[message.from_user.id]['state']):
        user_stats[message.from_user.id]['total_answers'] += 1
        await message.answer(
            text=f"Не угадали :(\n"
                 f"Столица {random_country} - {countries[random_country]['capital']}\n\n"
                 f"Общее кол-во ответов: {user_stats[message.from_user.id]['total_answers']}\n"
                 f"Кол-во правильных ответов: {user_stats[message.from_user.id]['correct_answers']}\n"
                 f"Выберите одно из следующих действий:",
            reply_markup=inline_keyboard_markup
        )
    else:
        await message.answer(
            text= f"Вы вне игры. Нажмите '/начать' чтобы продолжить играть"
        )

async def user_choice(callback: CallbackQuery):
    if callback.data == "next":
        global random_country_number
        random_country_number = random.randint(1, len(countries.keys()))
        global random_country
        random_country = list(countries.keys())[random_country_number - 1]
        try:
            flag_link = countries[random_country]['flag']
        except KeyError:
            flag_link = "N/A"
        await callback.message.edit_text(
            text= f"Страна: {random_country}\n"
                  f"Флаг: {flag_link}\n"
                  f"Осталось отгадать: {len(countries.keys())}\n\n"
                  "Введите на английском название столицы:"
        )
    elif callback.data == "exit":
        user_stats[callback.from_user.id]['state'] = False
        print("When exiting", user_stats, sep= ": ")
        user_stats[callback.from_user.id]['total_answers'] = 0
        user_stats[callback.from_user.id]['correct_answers'] = 0
        await callback.message.edit_text(
            text= f"Вы вышли из игры, а данные были сброшены\n"
                  f"Помните, что команда '/начать' ждет не дождется чтобы быть напечатанной"
        )




dp.message.register(process_start, Command(commands= ["start"]))
dp.message.register(process_help, Command(commands= ["правила"]))
dp.message.register(process_reset, Command(commands= ['сбросить']))
dp.message.register(process_exit, Command(commands= ['выйти']))
dp.message.register(process_stats, Command(commands= ["статистика"]))
dp.message.register(process_game_start, Command(commands= ["начать"]))
dp.message.register(process_user_answer)
dp.callback_query.register(user_choice)
# dp.message.register(other_messages)
"""


" ----------------------------------------------------------------------------------- "

# st = "яяяяяяяяяЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯ"
# st2 = "яяя"
# print(st.count("я"))
#
# anonymous_filter = lambda string: len([ya for ya in string if ya.lower() == "я"]) > 23
# print(anonymous_filter('яяяяяяяяяяяяяяяяяяяяяяяя, яяяяяяяяяяяяяяяя и яяяяяяяя тоже!'))


"""
from aiogram import Dispatcher, Bot, F
from aiogram.types import Message, Update
from aiogram.filters import Command

import json


BOT_TOKEN = "7189166713:AAFplUTZndRgivPEkLAj9nQFfd0bHw2bibI"

dp = Dispatcher()
bot = Bot(token= BOT_TOKEN)



# Checks if the message includes only the "/start" text
def filter_start_command(message: Message):
    return message.text == "/start"



async def process_start(message: Message):
    await message.answer(
        text= f"Start command has been initiated"
    )


dp.message.register(process_start, lambda msg: msg.text == "/start")


if __name__ == "__main__":
    dp.run_polling(bot)
"""


" ----------------------------------------------------------------------------- "
"""
import json, typing

# from aiogram import Dispatcher, Bot, F
from aiogram.types import Message, ContentType, ChatMemberUpdated
from aiogram.filters import Command, ChatMemberUpdatedFilter, MEMBER, KICKED, IS_MEMBER, IS_NOT_MEMBER



BOT_TOKEN = "7189166713:AAFplUTZndRgivPEkLAj9nQFfd0bHw2bibI"
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# @dp.my_chat_member(ChatMemberUpdatedFilter(member_status_changed= IS_MEMBER >> IS_NOT_MEMBER))
async def bot_kicked(update: ChatMemberUpdated):
    parsed_json = json.loads(update.json())
    processed_json = json.dumps(parsed_json, indent= 4)
    print(processed_json, "Left", sep="\n")


# @dp.my_chat_member(ChatMemberUpdatedFilter(member_status_changed= IS_NOT_MEMBER >> IS_MEMBER))
async def bot_joined(event: ChatMemberUpdated):
    parsed_json = json.loads(event.json())
    processed_json = json.dumps(parsed_json, indent=4)
    print(processed_json, "Joined", sep="\n")


dp.my_chat_member.register(bot_kicked, ChatMemberUpdatedFilter(member_status_changed=IS_MEMBER >> IS_NOT_MEMBER))
dp.my_chat_member.register(bot_joined, ChatMemberUpdatedFilter(member_status_changed= MEMBER))

if __name__ == "__main__":
    dp.run_polling(bot)
"""

#
# my_telefram_data = {
#     "id": 1600526965,
#     "text": "HI! This message is sent from the search bar"
# }
#
# async def process_start(message: Message):
#     await message.answer(
#         text= f"Hi, Mr(s).{message.from_user.first_name}. You started the bot with the default prefix '/'"
#     )
#     parsed_json = json.loads(message.json())
#     processed_json = json.dumps(parsed_json, indent=4)
#     print(processed_json)
#
# async def process_start_pipe(message: Message):
#     await message.answer(
#         text= f"Hi, Mr(s) {message.from_user.first_name}. You started the command with the custom prefix '|'"
#     )
#
#
# async def process_photo(message: Message):
#     raw_json = message.json()
#     parsed_json = json.loads(raw_json)
#     processed_json = json.dumps(parsed_json, indent= 4)
#     print(processed_json)
#     await message.answer(
#         text= "Photo was received. I appreciate this kind gesture :=)"
#     )
#
# async def process_video_voice(message: Message):
#     await message.answer(
#         text="You forwarded a video or voice"
#     )
#
# async def not_member(event: ChatMemberUpdated):
#     parsed_json = json.loads(event.json())
#     processed_json = json.dumps(parsed_json, indent=4)
#     print(processed_json)
#     print(f"User {event.from_user.first_name} blocked the bot")
#
# async def is_member(event: ChatMemberUpdated):
#     parsed_json = json.loads(event.json())
#     processed_json = json.dumps(parsed_json, indent=4)
#     print(processed_json)
#
#
#
# async def other(message: Message):
#     parsed_json = json.loads(message.json())
#     processed_json = json.dumps(parsed_json, indent=4)
#     print(processed_json)
#
# dp.message.register(process_start, Command(commands=["start"]))
# dp.message.register(process_start_pipe, Command(commands=["start"], prefix="|"))
# dp.message.register(process_photo, F.content_type == ContentType.PHOTO)
# dp.message.register(process_video_voice, F.content_type.in_({
#     "video",
#     "voice"
# }))
# dp.chat_member.register(not_member, ChatMemberUpdatedFilter(member_status_changed=KICKED))
# dp.chat_member.register(is_member, ChatMemberUpdatedFilter(IS_NOT_MEMBER >> IS_MEMBER))
# dp.message.register(other)

# if __name__ == "__main__":
#     dp.run_polling(bot)



" ----------------------------------------------------------------------------------------- "
"""
# class MyClass():
#     def __init__(self) -> None:
#         self.name = "Aly"
#         pass
#
#     def __call__(self):
#         return "Result of calling the instance of MyClass ^_^"
#
# class1 = MyClass()
# class2 = MyClass()
# class3 = MyClass
#
#
# print(MyClass()())
# print(class1())
# print(class2)


from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import BaseFilter

TOKEN = "7189166713:AAFplUTZndRgivPEkLAj9nQFfd0bHw2bibI"
bot = Bot(token= TOKEN)
dp = Dispatcher()
admin_ids = [1600526965]


class IsAdmin(BaseFilter):
    def __init__(self, admin_ids: list[int]) -> None:
        self.admin_ids = admin_ids

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admin_ids


# @dp.message(IsAdmin(admin_ids))
async def greet_admin(message: Message):
    await message.answer(
        text= f"Hi, {message.from_user.first_name}. You've passed an admin test"
    )

# @dp.message()
async def greet_user(message: Message):
    await message.answer(
        text= f"Hi, {message.from_user.first_name}. Any plans for today?"
    )

dp.message.register(greet_admin, IsAdmin(admin_ids))
dp.message.register(greet_user)


if __name__ == "__main__":
    dp.run_polling(bot)
"""

" ---------------------------------------------------------------------------------------------------- "

# text = "hwiefunwi....wieowi.".replace(".", "")
# print(text)
#
# text2 = "3".isdigit()
# print(text2)
#
# print(float("32.4"))
# print("32.3".isdigit())

from aiogram import Bot, Dispatcher, F
from aiogram.filters import BaseFilter, CommandStart
from aiogram.types import Message



TOKEN = "7189166713:AAFplUTZndRgivPEkLAj9nQFfd0bHw2bibI"
bot = Bot(token=TOKEN)
dp = Dispatcher()


class IsDigit(BaseFilter):
    async def __call__(self, message: Message) -> bool | dict[str, list[int]]:

        words = message.text.split()
        processed_words = []
        for word in words:
            processed_words.append(word.strip().replace(",", "").replace(".", ""))
        else:
            if processed_words:
                numbers = []
                for word in processed_words:
                    if word.isdigit():
                        numbers.append(int(word))
                return {"numbers" : numbers}
            return False

class IsEven(BaseFilter):
    async def __call__(self, message: Message, numbers) -> bool | dict[str, list[str]]:
        if not numbers:
            return False
        even_numbers = []
        for number in numbers:
            if number % 2 == 0:
                even_numbers.append(str(number))
        else:
            if even_numbers:
                print(even_numbers)
                return {"numbers" : even_numbers}
            return False

@dp.message(
            F.text,
            IsDigit(),
            IsEven())
async def process_display_numbers(message: Message, numbers):
    print(numbers)
    await message.answer(
        text= f"Here are you numbers: {', '.join([str(num) for num in numbers])}"
    )





# message = "anijq qiwdnq jsd 8 211 902921, 9, sdmosf."
# class GetNumbers(BaseFilter):
#     async def __call__(self, message: Message) -> bool | dict[str, list[int]]:
#         words = message.text.replace(",", "").replace(".", "").split()
#         numbers = [int(num.strip()) for num in words if num.isdigit()]
#         if numbers:
#             return {"numbers" : numbers, "letters" : "abcdefghijklmnopqrstuvwxyz"}
#         return False
#
# @dp.message(F.text.lower().startswith("find numbers"), GetNumbers())
# async def choose_numbers(message: Message, numbers, letters):
#     await message.answer(
#         text= f"Здесь ваши числа: {', '.join([str(num) for num in numbers])}\n"
#               f"Here are your letters: {letters}"
#     )





if __name__ == "__main__":
    dp.run_polling(bot)



















