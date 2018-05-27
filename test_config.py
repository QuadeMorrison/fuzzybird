# these are part of the standard library.
import argparse
import configparser

def arg_logic():
    # this is just in the standard library.
    parser = argparse.ArgumentParser(prog="py-web-serv",description = "A simple python web server.")

    # arguments
    parser = argparse.ArgumentParser(prog="fuzzybird",description = "A twitter fuzzy finder :).")
    parser.add_argument("--config", metavar='F', help="Override the config file.", default="~/.fuzzybirdrc")
    args = parser.parse_args()
    parse_config(args.config)

def parse_config(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    print(config['keys'])

arg_logic()
