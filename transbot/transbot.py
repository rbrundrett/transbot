import os
from string import join
import time
import random
from slackclient import SlackClient
from mstranslator import Translator
import config
import alify

#initialize translator API
translator = Translator(config.MSTRANS_ID)

# instantiate Slack & Twilio clients AAAAAND
# bot's ID as an environment variable or constant
######### STARTERBOT / BRUNDRETTFAMILY SLACK
#slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN')) #brundrettfamily starterbot
#BOT_ID = os.environ.get("BOT_ID") #starterbot brundrettfamily
#BOT_NAME = "StarterBot"

######### TRANSBOT / PIZZABALLS SLACK
slack_client = SlackClient(config.TRANS_BOT_TOKEN) #pizzaballs transbot
BOT_ID = config.TRANS_BOT_ID    #transbot / pizzaballs
BOT_NAME = "TransBot"

# constants
AT_BOT = "<@" + BOT_ID + ">"
EXAMPLE_COMMAND = "do"
TRANS_COMMAND = "nazify"




def handle_trans_cmd(command, channel):
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """
    if command.startswith("nazify"):
        message = command.split(' ', 1)[1]
        response = translator.translate(message, lang_from='en', lang_to='de')
    elif command.startswith("-nazify"):
        message = command.split(' ', 1)[1]
        response = translator.translate(message, lang_from='en', lang_to='de')
        response = translator.translate(response, lang_from='de', lang_to='en')
    elif command.startswith("rusify"):
        message = command.split(' ', 1)[1]
        response = translator.translate(message, lang_from='en', lang_to='ru')
    elif command.startswith("-rusify"):
        message = command.split(' ', 1)[1]
        response = translator.translate(message, lang_from='en', lang_to='ru')
        response = translator.translate(response, lang_from='ru', lang_to='en')
    elif command.startswith("hindify"):
        message = command.split(' ', 1)[1]
        response = translator.translate(message, lang_from='en', lang_to='hi')
    elif command.startswith("-hindify"):
        message = command.split(' ', 1)[1]
        response = translator.translate(message, lang_from='en', lang_to='hi')
        response = translator.translate(response, lang_from='hi', lang_to='en')
    else:
        response = alify(command, channel)
    slack_client.api_call("chat.postMessage", channel=channel,
                            text=response, as_user=True)



def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                       output['channel']
    return None, None


if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
#    slack_client.rtm_send_message("#slackbottest", "test message", True)
    if slack_client.rtm_connect():
        print(BOT_NAME + " connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_trans_cmd(command,channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")





