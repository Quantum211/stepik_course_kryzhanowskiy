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

import requests

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


cat_api: str = "https://api.thecatapi.com/v1/images/search"
fox_api: str = "https://randomfox.ca/floof/"

BOT_TOKEN = "7189166713:AAFplUTZndRgivPEkLAj9nQFfd0bHw2bibI"
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command(commands=['start']))
async def process_start_command(message: Message) -> Message:
    answer_return = await message.answer(text=f"Hello, {message.chat.first_name} {message.chat.last_name}! Pleasure to meet you.\n"
                                              "This is the start of our conversation. Enter:\n"
                                              "'/help' - to get help")
    print(answer_return)
    print(type(answer_return))
    return answer_return

@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(text=f"'help':\n"
                         f"This bot will reply/echo with the same message you have sent to the chat.")

@dp.message(Command(commands=["fox", "Fox", 'foxie', "Foxie", "Лис", "лис", "Лиса", "лиса", "Лисенок", "лисенок"]))
async def send_fox_photo(message: Message):
    fox_api_response = requests.get(fox_api)
    print(fox_api_response)
    if fox_api_response.status_code == 200:
        await message.answer_photo(
            photo= fox_api_response.json()['image'],
            caption= "Хочу кушать < '!' >"
        )
    else:
        await message.answer(
            text=f"To my deep regret, we had an unexpected error in the internetwork :(\n\nCome again and later for another attempt :=)"
        )

@dp.message(Command(commands=["Cat", "cat", "kitten", "Kitten", "Kittie", "kittie", "Meow", "meow",
                              "Кот", "кот", "Кошка", "кошка", "Котенок", "котенок", "Кошак", "кошак", "Кошара", "кошара",
                              "Мур", "мур", "Мяу", "мяу"]))
async def send_cat_photo(message: Message):
    cat_api_response = requests.get(cat_api)
    if cat_api_response.status_code == 200:
        await message.answer_photo(
            photo= cat_api_response.json()[0]['url'],
            caption= "Мяу (=◑ᆺ◐=)"
        )
    else:
        await message.answer(
            text= "No response from the API :(\nCome back later for another attempt ^_^"
        )

@dp.message()
async def send_echo(message: Message):
    await message.reply(
        text= f"{message.text}"
    )

if __name__ == "__main__":
    dp.run_polling(bot)


















