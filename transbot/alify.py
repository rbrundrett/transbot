from string import join
import random

def alify(command, channel):
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """
    ' '.join(i.capitalize() for i in command.split(' '))
    xs = command.split(" ")
    for x in xs:
        if  x.lower()=="laptop":
            new_word=random.sample(["LAB-top","Lab=Top","lab Top","LAB_TOP"],1)[0]
            xs[xs.index(x)]=new_word
            x=new_word
        if "mind" in x.lower():
            new_word=x.lower()
            new_word=new_word.replace("mind","mine")
            xs[xs.index(x)]=new_word
            x=new_word
        #add random hyphen
        if random.randint(1, 10)<2:
            i=random.randint(1,len(x))
            new_word=x[:i] + "-" + x[i:]
            xs[xs.index(x)]=new_word
            x=new_word
        #add random apostrophe
        if random.randint(1, 100)<6:
            i=random.randint(1,len(x))
            new_word=x[:i] + "'" + x[i:]
            xs[xs.index(x)]=new_word
            x=new_word
        #add random quotes
        if random.randint(1, 10)<2:
            new_word='"' + x + '"'
            xs[xs.index(x)]=new_word
            x=new_word
        #add random casing
        if random.randint(1, 10)<6:
            new_word=x.title()
            xs[xs.index(x)]=new_word
            x=new_word
        #add random upper case
        if random.randint(1, 100)<6:
            new_word=x.upper()
            xs[xs.index(x)]=new_word
            x=new_word
        #add random commas
        if random.randint(1, 100)<5 or x[-1:]==",":
            new_word=x + "," * random.randint(1,10)
            xs[xs.index(x)]=new_word
            x=new_word
    response = " ".join(xs)
    if command == "version":
        response = "transbot version 1.3"

    #slack_client.api_call("chat.postMessage", channel=channel,
    #                      text=response, as_user=True)
    return response
