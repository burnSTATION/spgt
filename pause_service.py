from commands.say import SayCommand
from engines.server import engine_server
from messages import SayText2
from events import Event
import time

CHAT_PREFIX = "[\x02eSN\x01]"

ct_pause_remainging = True
t_pause_remaining = True
round = 0
pause_max_length = 90

@Event('round_end')
def round_counter():
	round += 1

def wait_nextround():
	current_round = round
	if round >= current_round:
		pausetimer_start()

def pausetimer_start(time):
	start_time = time.time()
	end_time = start_time + pause_max_length
	if time.time() == end_time:
		engine_server.server_command('mp_unpause_match;')
		SayText2(chat_prefix, "Max pause time reached! Unpausing...").send()

@SayCommand('.pause')
def pause_match(command, team, index):
	engine_server.server_command('mp_pause_match;')
	wait_nextround()

@SayCommand('.unpause')
def unpause_match(command, team, index):
	engine_server.server_command('mp_unpause_match;')