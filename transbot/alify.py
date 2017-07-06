from string import join
import random

"""
Dirty Globals
"""
HYPHEN_FREQ = 6
APOS_FREQ = 20
QUOTE_FREQ = 10
TITLE_CASE_FREQ = 60
UPPERCASE_FREQ = 10
COMMA_FREQ = 5


"""
Utility Functions
"""
def percent_chance():
    """
    Return a random int between 1 and 100
    """
    return random.randint(1, 100)


def laptop(s):
    """
    Given a string, compare it to laptop and randomize return value
    """    
    if s.lower() == "laptop":
        new_word = random.sample(["LAB-top","Lab=Top","lab Top","LAB_TOP"],1)[0]
        s = new_word
    return s


def miner(s):
    """
    Given a string, see if it's mind and switch to mine
    """
    if "mind" in s.lower():
        s = s.replace("mind","mine")
    return s


def rand_hyphen(s1,s2):
    """
    Given two strings, randomly concat them with a random hyphen
    """
    s = "{} {}".format(s1,s2)
    if percent_chance() < HYPHEN_FREQ:
        s = s1 + "-" + s2
    return s


def rand_apos(s):
    """
    Given a string, see if it's plural and make it possessive
    """
    if percent_chance() < APOS_FREQ and s[-1:].lower() == 's':
        s = s.rsplit('s', 1)[0] + "'s"
    return s


def rand_quote(s):
    """
    Given a string, randomly put quotes around it
    """
    if percent_chance() < QUOTE_FREQ:
        s = '"' + s + '"'
    return s


def rand_title(s):
    """
    Given a string, randomly title case it
    """
    if percent_chance() < TITLE_CASE_FREQ:
        s = s.title()
    return s


def rand_upper(s):
    """
    Given a string, randomly uppercase the entire string
    """
    if percent_chance() < UPPERCASE_FREQ:
        s = s.upper()
    return s


def rand_comma(s):
    """
    Given a string, randomly add commas to it
    """
    if percent_chance() < COMMA_FREQ:
        s = s + "," * random.randint(1,10)
    return s


def map_funcs(obj, func_list):
    return reduce((lambda x, y: map(y,x)), func_list, obj)


def alify(command, channel):
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """
    ' '.join(i.capitalize() for i in command.split(' '))
    xs = command.split(" ")
    fList = [laptop, miner, rand_apos, rand_quote, rand_title, rand_upper]
    xs = map_funcs(xs, fList)
    xs = reduce(rand_hyphen, xs)
    return xs
    response = " ".join(xs)
    if command == "version":
        response = "transbot version 1.3"

    #slack_client.api_call("chat.postMessage", channel=channel,
    #                      text=response, as_user=True)
    return response


if __name__ == "__main__":
    print alify("Got to take a laptop and give it always always a piece of my mind!", "")
