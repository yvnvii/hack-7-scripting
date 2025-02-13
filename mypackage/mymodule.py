#!/usr/bin/env python
"magic eight ball function to tell your future."

import random

def magic_eight_ball():
    """
    Returns a random statement from a magic eight ball containing
    a 10 sided die (I was too lazy to write all 20 typical answers)
    https://en.wikipedia.org/wiki/Magic_8-Ball
    """
    RESPONSES = {
        0: "It is certain.",
        1: "It is decidedly so.",
        2: "Without a doubt.",
        3: "Yes – definitely.",
        4: "You may rely on it.",
        5: "Reply hazy, try again.",
        6: "Better not tell you now.",
        7: "Cannot predict now.",
        8: "My reply is no",
        9: "Outlook not so good",
        10: "Very doubtful",
    }
    return RESPONSES[random.choice(range(10))]
