from commands.say import SayCommand
from engines.server import engine_server
from messages import SayText2

@SayCommand('.pause')
def pause_match(command, team, index):
	engine_server.server_command('mp_pause_match;')

@SayCommand('.unpause')
def unpause_match(command, team, index):
	engine_server.server_command('mp_unpause_match;')