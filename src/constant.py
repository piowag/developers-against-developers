import enum

# TODO: redefine these
LOBBY_SCHEME = 'http://'
LOBBY_DOMAIN_NAME = '18.156.174.32'
LOBBY_PORT = 7231
LOBBY_URL = LOBBY_SCHEME + LOBBY_DOMAIN_NAME + ':' + str(LOBBY_PORT)

GAME_SERVER_SCHEME = 'http://'
GAME_SERVER_DOMAIN_NAME = '0.0.0.0'
GAME_SERVER_PORT = 80
GAME_SERVER_URL = GAME_SERVER_SCHEME + GAME_SERVER_DOMAIN_NAME + ':' + str(LOBBY_PORT)

STATUS_ERROR = "ERROR"
STATUS_OK = "OK"


class Role(enum.Enum):
    player = 1
    gm = 2


class GameState(enum.Enum):
    waiting_for_players = 1
    waiting_for_answers = 2
    waiting_for_game_master = 3
    game_ended = 4


class Mode(enum.Enum):
    local = 1
    prod = 2

SETTINGS_MODE = Mode.prod
SERVER_URL_FOR_LOCAL_TESTS = 'http://0.0.0.0:' + str(7200)
