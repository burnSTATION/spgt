from engines.server import engine_server
from messages import SayText2
from commands.say import SayCommand

CHAT_PREFIX = "[\x02eSN\x01]"

def get_map_name(map_name):
    maps = {
    #   (aliases)                       : proper map name
        ("dust2", "de_dust2")           : "de_dust2",
        ("inferno", "de_inferno")       : "de_inferno",
        ("cache", "de_cache")           : "de_cache",
        ("train", "de_train")           : "de_train",
        ("mirage", "de_mirage")         : "de_mirage",
        ("cbbl", "cobble", "de_cbbl")   : "de_cbbl",
        ("overpass", "de_overpass")     : "de_overpass"
    }

    for key, value in maps.items():
        if map_name in key:
            return value
    return None

@SayCommand('.map')
def map_command(command, index, team_only):
    try:
        user_input = command[1].lower()
        map = get_map_name(user_input)
        if map:
            SayText2(CHAT_PREFIX + " Changing map to " + map + "...").send()
            engine_server.server_command('changelevel ' + map + ';')
        else:
            SayText2(CHAT_PREFIX + " Invalid map name. Map pool: " +
                     "dust2, inferno, cache, train, mirage, " +
                     "cbbl, overpass").send()

    except IndexError:
    # This exception is raised when the user provides no arguments to the command
        SayText2(CHAT_PREFIX + " Please enter a map name." +
                 " Example: .map de_dust2").send()
