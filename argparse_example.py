#CLI application that allows you to echo messages with an intuitive interface

import argparse

#argparse used for creation of command-line interfaces.

'''
The description passed in as an argument of the ArgumentParser class will be used as the help 
message when the user either runs the tools incorrectly or asks for help on how to use the tool.
'''
parser = argparse.ArgumentParser(description="""Prints out the words passed in,
    capitalize them if required and repeats them in as many lines as requested.
    """)

'''
By passing nargs="+", you tell argparse that we require at least one message to be passed in. 
Other options include ? for optional, and * for 0 or more. You can also use any natural number 
to require a specific number of parameters.
'''
parser.add_argument("message", help="Messages to be echoed", nargs="+")

#Make it a Boolean flag option by changing the default action to store_true
parser.add_argument("-c", "--capitalize", action="store_true")

'''
Adds a new option, repeat, which allows us to pass an integer that defaults to one, and that will 
control the number of times the words are repeated.
'''
parser.add_argument("--repeat", type=int, default=1)

'''
Call parse_args, which will take the arguments passed in the command line, validate them, 
and expose them as attributes of args.
'''

args = parser.parse_args()


if args.capitalize:
    messages = [m.capitalize() for m in args.message]
else:
    messages = args.message

for _ in range(args.repeat):
    print(" ".join(messages))