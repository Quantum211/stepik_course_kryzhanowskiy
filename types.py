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

request = requests.get("http://api.open-notify.org/iss-now.json")

if request.status_code == 200:
    print(f"Request successful\n" 
          f"{request.text}.")
    coordinates = request.json().get('iss_position')
    formatted_coordinates = f"{coordinates['longitude']}%2C{coordinates['latitude']}"
    map_url = f"https://yandex.com/maps/?||={formatted_coordinates}&z=10"
    print(map_url)
else:
    print(f"Response code - {request.status_code}")


response_number43 = requests.get("http://numbersapi.com/43?json")
print(response_number43.json().get('text'))































