#!/usr/bin/env python
from __future__ import print_function


def main():
    age = int(raw_input("How old are you? "))

    if age < 0:
        print("That isn't possible.")
    elif age == 0:
        print("You were just born!!!! You're mommy and daddy are never going to sleep again.")
    elif 1 <= age < 3:
        print("You're a toddler! Can you poop yet?")
    elif 3 <= age < 13:
        print("'Sup Kid. Yep. I'm talking to you, kid. You're a child.")
    elif 13 <= age < 19:
        print("How's puberty? You are an adolescent, which is a fancy schmancy way of saying teenager.")
    elif 19 <= age < 30:
        print("Welcome to adulthood. You are a young adult. Enjoy it while it lasts...")
    elif 30 <= age < 50:
        print("It's all downhill from here. You are middle aged.")
    elif 50 <= age < 80:
        print("You are OLD!")
    elif 80 <= age < 85:
        print("You are within the age range that is the current average life expectancy.")
    elif 85 <= age < 100:
        print("You are very old. There is a very good chance you are dead.")
    elif 100 <= age < 122:
        print("You are extremely old. It is extremely likely that you are dead.")
    elif age == 122:
        print("Jeanne Calment (1875-1997) was a French woman who allegedly died at the age of 122. ")
        print("According to wikipedia at the time of this writing, this is the oldest living person ever ")
        print("You're that old. Haha, just kidding, you're dead.")
    elif age > 122:
        print("You are either a vampire or some sort of wizard.")
    else:
        print("You are some interdimensional creature that measures time in non-numeric ASCII characters.")


if __name__ == '__main__':
    main()
