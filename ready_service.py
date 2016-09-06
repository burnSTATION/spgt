from listeners import OnClientFullyConnect, OnClientDisconnect
from messages import SayText2
from players.entity import Player
from commands.say import SayCommand
 
players = {}
chat_prefix = "[\x02eSN\x01]"
maps = ["de_dust2", "de_cache", "de_mirage", "de_overpass", "de_cbble", "de_train", "de_nuke"]
 

class CreatePlayer():
    def __init__(self, username):
        self.username = username;
        self.is_ready = False;
        self.permission_level = 0;
        self.steam_id = "";

def try_start_match(index):
    if len(players) >= 10:
        SayText2(chat_prefix + "The match will now begin").send(index)
    else:
        SayText2(chat_prefix + "Still waiting for 10 players to be ready to start the match").send(index)
 
@EOnClientFullyConnect
def on_client_fully_connect(index):
    player = Player(index)
    players[player.index] = CreatePlayer(player.name)
 
@OnClientDisconnect
def on_client_disconnect(index):
    player = Player(index)
    players.pop(player.index)
 
@SayCommand('.players')
def list_players(command, index, team):
    SayText2(chat_prefix + str(players[keys].username)+ ", ").send(index)
 
@SayCommand('.ready')
def make_player_ready(command, index, team):
    key = Player(index).index
    current_player = players[key]

    if not current_player.is_ready:
        current_player.is_ready = True
        SayText2(chat_prefix + "You have been marked as \x06READY").send(index)
        try_start_match(index)
    elif current_player.is_ready:
        SayText2(chat_prefix + "You're already \x06READY").send(index)

@SayCommand('.notready')
def make_player_notready(command, index, team):
    key = Player(index).index
    current_player = players[key]

    if current_player.is_ready:
        current_player.is_ready = False
        SayText2(chat_prefix + "You have been marked as \x02NOT READY").send(index)
    elif not current_player.is_ready:
        SayText2(chat_prefix + "You're already \x02NOT READY").send(index)