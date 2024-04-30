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
print(get_person_info(person_1))













