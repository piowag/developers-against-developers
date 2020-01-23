import enum
import uuid
import base_handler
import constant


class Role(enum.Enum):
    player = 1
    gm = 2


class GameState(enum.Enum):
    waiting_for_players = 1
    waiting_for_answers = 2
    waiting_for_game_master = 3


class Player:
    def __init__(self):
        self.role = Role.player
        self.points = 0
        self.answer = None

    def set_role(self, role):
        self.role = role

    def get_role(self):
        return self.role

    def add_points(self, points):
        self.points += points

    def get_points(self):
        return self.points

    def add_answer(self, code_file):
        self.answer = code_file

    def get_answer(self):
        return self.answer

    def is_gm(self):
        return self.get_role() == Role.gm


class GameServerHandler:
    def __init__(self, public_uuid):
        self.public_uuid = public_uuid
        self.players = dict()
        self.state = GameState.waiting_for_players

    def add_player_to_game(self, token):
        if self.state is not GameState.waiting_for_players:
            return {'msg': "Game already running"}
        elif token in self.players:
            return {'msg': "Player already in the game"}

        self.players[token] = Player()
        return {'msg': "Player added"}

    def get_player_role(self, token):
        if token not in self.players:
            return {'msg': "Player not in game"}

        return {'role': self.players[token].get_role().name,
                'msg': "Role: {}".format(self.players[token].get_role().name)}

    def start_game(self):
        if self.state is not GameState.waiting_for_players:
            return {'msg': "Game already started"}
        if len(self.players.keys()) <= 1:
            return {'msg': "Not enough players"}

        # TODO: Change gm after rounds
        self.players[list(self.players.keys())[0]].set_role(Role.gm)
        self.state = GameState.waiting_for_answers
        return {'msg': "Game started"}

    def get_task(self):
        if self.state is GameState.waiting_for_players:
            return {'msg': "Game not yet started"}

        return {'msg': "No task implemented yet"}

    def send_answer(self, token, code_file):
        if token not in self.players:
            return {'msg': "Player not in game"}
        elif self.players[token].is_gm():
            return {'msg': "Player is gm, can't send answers"}
        elif self.state is not GameState.waiting_for_answers:
            return {'msg': "Sending answers currently not possible"}

        self.players[token].add_answer(code_file)
        for p in self.players.keys():
            if not self.players[p].get_answer():
                if not self.players[p].is_gm():
                    return {'msg': "Code file received successfully"}
        self.state = GameState.waiting_for_game_master
        return {'msg': "Code file received successfully"}

    def get_answers_from_players(self, token):
        if token not in self.players:
            return {'msg': "Player not in game"}
        elif not self.players[token].is_gm():
            return {'msg': "Player is not gm"}
        elif self.state is not GameState.waiting_for_game_master:
            return {'msg': "Answers not yet available"}

        return {t: p.get_answer() for t, p in self.players.items() if t != token}

    def choose_winner(self, token, winner_token):
        if token not in self.players:
            return {'msg': "Player not in game"}
        elif winner_token not in self.players:
            return {'msg': "Chosen player not in game"}
        elif not self.players[token].is_gm():
            return {'msg': "Player is not gm"}
        elif self.state is not GameState.waiting_for_game_master:
            return {'msg': "Answers not yet available"}

        # TODO: Run code on a VM, currently assumes the code passes
        self.players[winner_token].add_points(1)
        for p in self.players.keys():
            self.players[p].add_answer(None)
        self.state = GameState.waiting_for_answers
        return {'msg': "Winner given points"}

    def get_round_results(self, token):
        if token not in self.players:
            return {'msg': "Player not in game"}
        elif self.state is not GameState.waiting_for_answers:
            return {'msg': "Round is ongoing"}

        return {'msg': self.players[token].get_points()}


if __name__ == '__main__':
    base_handler.run(
        GameServerHandler(uuid.uuid4()),
        address=constant.GAME_SERVER_DOMAIN_NAME,
        port=constant.GAME_SERVER_PORT)
