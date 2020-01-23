
def create_game_server_interface():
    """
    Call like:
    interface = base_interface.decorator("http:/...")(create_game_server_interface())
    """
    class GameServerInterface:

        def add_player_to_game(token):
            """
            Called by lobby.
            Adds player with given id.
            """

        def get_player_role(token):
            """
            Called by all players.
            Returns current role ("gm" or "player").
            """

        def start_game():
            """
            Called by all players.
            Starts game, joining is not possible afterwards.
            """

        def get_task():
            """
            Called by GM and players.
            """

        def send_answer(token, code_file):
            """
            Called by players.
            Sends player's code to the game server.
            """

        def get_answers_from_players(token):
            """
            Called by GM.
            Collects all answers sent by players.
            """

        def choose_winner(token, winner_token):
            """
            Called by GM.
            Select code to be run on a VM.
            """

        def get_round_results(token):
            """
            Called by GM and Players.
            Returns scores after a round.
            """
    return GameServerInterface
