import spgt.ready_service
import spgt.pause_service
import spgt.core_service
import spgt.config as config

from engines.server import global_vars

def load():
    config.current_map = global_vars.map_name

def unload():
    pass
