from commands.say import SayCommand
from engines.server import engine_server
from messages import SayText2
from events import Event
import time

CHAT_PREFIX = "[\x02eSN\x01]"

ct_pause_remaining = True
t_pause_remaining = True
round = 0
pause_max_length = 90
_round_status = False

@Event('round_announce_last_round_half')
def round_announce_last_round_half(game_event):
    global _round_status
    _round_status = True

@Event('round_end')
def round_end(game_event):
	if not _round_status:
		ct_pause_remaining = True
		t_pause_remaining = True

@SayCommand('.pause')
def pause_match(command, team, index):
	engine_server.server_command('mp_pause_match;')
	wait_nextround()

@SayCommand('.unpause')
def unpause_match(command, team, index):
	engine_server.server_command('mp_unpause_match;')