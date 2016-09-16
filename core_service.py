from engines.server import engine_server
from messages import SayText2
from commands.say import SayCommand
from listeners import OnLevelInit
from listeners.tick import Delay

import spgt.config as config

def get_map_name(map_name):
    """ Given a map_name, checks for it against a "list" of dictionary keys. If
    a match is found, return the value -- the map name accepted by the CSGO
    console -- of said the matched key. If no match is found, return nothing.
    """
    maps = {
    #   (aliases)                       : proper map name
        ("dust2", "de_dust2")           : "de_dust2",
        ("inferno", "de_inferno")       : "de_inferno",
        ("cache", "de_cache")           : "de_cache",
        ("train", "de_train")           : "de_train",
        ("mirage", "de_mirage")         : "de_mirage",
        ("cbble", "cobble", "de_cbble") : "de_cbble",
        ("overpass", "de_overpass")     : "de_overpass"
    }

    for key, value in maps.items():
        if map_name in key:
            return value
    return None

def changemap(map_name):  # Callback function for Delay in .map
    engine_server.server_command('changelevel ' + map_name + ';')

@OnLevelInit
def on_level_init(map_name):  # Update current_map on each map change
    config.current_map = map_name

@SayCommand('.map')
def map_command(command, index, team_only):
    """ Allows the user to change the current map without using the CSGO
    console. Syntax: '.map <map_name>'.
    """
    try:
        user_input = command[1].lower()
        map = get_map_name(user_input)
        if map:
            if map != config.current_map:
                SayText2(config.CHAT_PREFIX + " Changing map to " + map + " in 5 seconds...").send()
                Delay(5, changemap, map)
            else:
                SayText2(config.CHAT_PREFIX + " Current map is already " + map + ".").send()
        else:
            SayText2(config.CHAT_PREFIX + " Invalid map name. Allowed maps: " +
                     "dust2, inferno, cache, train, mirage, " +
                     "cbbl, overpass").send()

    except IndexError:
    # This exception is raised when the user provides no arguments to the command
        SayText2(config.CHAT_PREFIX + " Please enter a map name." +
                 " Example: .map de_dust2").send()
