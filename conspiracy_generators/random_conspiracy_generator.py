import random


def nounGen():
    nouns = [
        "Hitler ",
        "The government ",
        "Aliens ",
        "Merpeople ",
        "Jackelopes ",
        "Bigfoot ",
        "Smoothies ",
        "Stalin ",
        "Daddy ",
        "National Parks ",
        "Eagles ",
        "Jesus ",
        "God ",
        "Satan ",
        "Siri ",
        "Alexa ",
        "Country Music ",
        "Birds ",
        "UAB ",
        "UAB Parking ",
        "President Ray Watts ",
        "The disembodied smell of formaldehyde ",
        "The Bush Administration ",
        "Obama ",
        "Trump ",
        "Mike Pence ",
        "Gay Mike Pence ",
        "The gays ",
        "Home depot lesbians ",
        "McDonalds ",
        "John Cena ",
        "Ninja Turtles ",
        "Laura doing her homework ",
        "Blaze ",
        "Something ",
        "Pro Gamers ",
        "The American Education System ",
        "Ronald Reagan ",
        "ISIS ",
    ]
    i = random.randint(0, len(nouns) - 1)
    return nouns[i]


def verbGen():
    verbs = [
        "killed ",
        "became ",
        "helped ",
        "escaped ",
        "listened to ",
        "lived with ",
        "conspired with ",
        "was cloned by ",
        "hurt ",
        "attempted to arrest ",
        "aided ",
        "conspired against ",
        "spoke out against ",
    ]
    i = random.randint(0, len(verbs) - 1)
    return verbs[i]


def prepGen():
    preps = ["during ", "after ", "before ", "for ", "throughout "]
    i = random.randint(0, len(preps) - 1)
    return preps[i]


def eventGen():
    events = [
        "9/11",
        "The Moon Landing",
        "the JFK Assination",
        "the Cold War",
        "the 60s",
        "the 70s",
        "the 80s",
        "the 90s",
        "Summer 2016",
        "the last presidential election",
        "Dec 21, 2012",
        "Trumps Presidency",
    ]
    i = random.randint(0, len(events) - 1)
    return events[i]


def get_conspiracy():
    return nounGen() + verbGen() + nounGen() + prepGen() + eventGen()
