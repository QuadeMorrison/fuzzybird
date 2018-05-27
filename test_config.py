#!/usr/bin/env python3
# these are part of the standard library.
import argparse
import configparser
import sys

g_keys = {}

def arg_logic():
    # this is just in the standard library.
    parser = argparse.ArgumentParser(prog="py-web-serv",description = "A simple python web server.")

    # arguments
    parser = argparse.ArgumentParser(prog="fuzzybird",description = "A twitter fuzzy finder :).")
    parser.add_argument("--config", metavar='F', help="Override the config file.", default="~/.fuzzybirdrc")
    return parser.parse_args()

# sets some config variables
def parse_config(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)

    if not 'keys' in config:
        error("There were no keys found in '{:s}'.".format(config_file))

    g_keys = config['keys']

    for key in ['consumerkey', 'consumersecretkey', 'accesstoken', 'accesstokenkey']:
        if not key in g_keys:
            error("'{:s}' key not found in config.".format(key))

def error(s):
    sys.exit("Error: " + s)

if __name__ == "__main__":
    args = arg_logic()
    parse_config(args.config)
