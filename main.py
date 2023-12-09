#!/usr/bin/env python3

from brain_module import ChatGPT
import json

months_of_the_year = [
    "January", "February", "March",
    "April", "May", "June",
    "July", "August", "September",
    "October", "November", "December"
]

def set_config():
    color = input("What color best describes your mood today?")
    month = int(input("In which month were you born? Use the numbers from (1-12)"))
    superpower = input("Pick one superpower: flying, invisibility, or telepathy?")
    spirit = input("What animal do you consider your spirit guide?")
    destination = input("In one word, what's your dream travel destination?")
    mystical = input("Choose one mystical creature as your companion: dragon, unicorn, phoenix, gnome, siren ?")
    month_sel = months_of_the_year[month-1]
    content = f'''You are bot that will be a fortuine cookie.\n Generate a fortune cookie message that reflects a sense of calm and insight, akin to the tranquility of the color: {color}. Incorporate elements of wisdom gained from a journey (symbolized by the birth month of {month_sel } and the dream destination of{ destination }), the mystical
    insight of { superpower}, the guidance of a spirit animal like the {spirit}, and the transformative energy of a {mystical}.\n
    - You need to provide a message. \n - You need to provide a lucky number.\n The output is a json where a field message that containes the fortouine message and other field lucky_number \
    Consider the following constrains: A message with no more than 10 words and the style of the message should be like a fortuine chinese cookie. And the lucky number need to be a number of two digits.'''
    return content


if  __name__ == "__main__":
    bot = ChatGPT()
    prompt = set_config()
    response = bot.request_openai(prompt)
    message = json.loads((response.model_dump()['choices'][0]['message']['content']))
    print(f"Today is your lucky day!.\n  MystiCookie said:\n {message['message']}")

