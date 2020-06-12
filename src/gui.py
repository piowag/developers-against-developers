import argparse
import tkinter as tk
from tkinter import *
import constant
import lobby_interface as li
import base_interface as bi
import game_server_interface as gs


LARGE_FONT= ("Verdana", 12)


class Player:
    def __init__(self):
        self.points = IntVar()
        self.name = StringVar()
        self.role_var = StringVar()
        self.role_var.set(constant.Role.player.name)
        self.role = constant.Role.player

        self.answer = StringVar()
        self.current_task = StringVar()
        self.gm_answers = None

        self.server_url = ""
        self.token = ""
        self.game_server = None


class DevelopersAgainstDevelopers(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.winfo_toplevel().title("Developers Against Developers")
        self.frames = {}
        self.player = Player()

        for f in (PageStart, PageCreate, PageGame, PageEnd, PageGameMasterPickQuestion):
            frame = f(container, self, self.player)
            self.frames[f] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(PageStart)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def prepare_frame(self, cont):
        frame = self.frames[cont]
        frame.prepare(self.player)

        
class PageStart(tk.Frame):

    def __init__(self, parent, controller, player):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Welcome to the game!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        label1 = tk.Label(self, text="Developers Against Developers is a game used to expand knowledge and programming skills in an unusual and attractive way for users.", wraplength=500)
        label1.config(height=5, width=50)
        label1.pack(expand=YES, fill=BOTH)

        button_create = tk.Button(self, text="Start",
                            command=lambda: controller.show_frame(PageCreate), padx=40)
        button_create.pack()


class PageCreate(tk.Frame):

    def __init__(self, parent, controller, player):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Welcome to the lobby", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        label_nick = tk.Label(self, text="Enter your name")
        label_nick.pack(pady=10,padx=10)

        nick = Entry(self, width=50)
        nick.pack()
        nick.insert(0, "Your name")

        def player_nickname():
            player_nickname = nick.get()
            player.name.set(player_nickname)

        def join_game():
            server_info = lobby.find_server()
            if bi.response_is_ok(server_info):
                player.server_url = server_info["address"]
                response = lobby.add_me_to_server(player.server_url)
                if bi.response_is_ok(response):
                    player.token = response["token"]
                    controller.show_frame(PageGame)
                    player.game_server = bi.decorator(player.server_url)(gs.create_game_server_interface())


        button_confirm = tk.Button(self, text="Confirm", width=10, command=player_nickname)
        button_confirm.pack()

        button_exit = tk.Button(self, text="Start game",
                            command=lambda: join_game())
        button_exit.pack(side=RIGHT, fill=X)

        button_exit = tk.Button(self, text="Exit",
                            command=lambda: controller.show_frame(PageStart))
        button_exit.pack(side=LEFT, fill=X)


class PageGame(tk.Frame):

    def __init__(self, parent, controller, player):
        tk.Frame.__init__(self, parent)

        label_player = tk.Label(self, text="Player", font=LARGE_FONT)
        label_player.grid(row=0, column=0)
        label_player = tk.Label(self, textvariable=player.name)
        label_player.grid(row=1, column=0)

        label_points = tk.Label(self, text="Points", font=LARGE_FONT)
        label_points.grid(row=0, column=1)
        label_points = tk.Label(self, textvariable=player.points)
        label_points.grid(row=1, column=1)

        label_points = tk.Label(self, text="Role", font=LARGE_FONT)
        label_points.grid(row=0, column=2)
        label_points = tk.Label(self, textvariable=player.role_var)
        label_points.grid(row=1, column=2)

        my_answer = Text(self, height=15, width=80, bg='grey')
        my_answer.grid(row=6, column=4, columnspan=4, rowspan=3)
        label_player1 = tk.Label(self, text="Your code:")
        label_player1.grid(row=5, column=4, columnspan=4)

        def update():
            player.current_task.set(player.game_server.get_task()["msg"])
            player.role = player.game_server.get_player_role(player.token)["role"]
            player.role_var.set(player.role)

            server_resp = player.game_server.get_round_results(player.token)
            if bi.response_is_ok(server_resp):
                player.points.set(server_resp["msg"])

            if player.role == "gm":
                my_answer.insert(INSERT, "You are the Game Master for this round.", END)
                server_resp = player.game_server.get_answers_from_players(player.token)
                if bi.response_is_ok(server_resp):
                    player.gm_answers = server_resp["answers"]
                    controller.prepare_frame(PageGameMasterPickQuestion)
                    controller.show_frame(PageGameMasterPickQuestion)

        def send_answer():
            ans = my_answer.get("1.0", END)
            player.game_server.send_answer(player.token, ans)

        def start_game():
            player.game_server.start_game()
            player.current_task.set(player.game_server.get_task()["msg"])
            player.role = player.game_server.get_player_role(player.token)["role"]
            player.role_var.set(player.role)

        label_gm_question = tk.Label(self, text="Question:")
        label_gm_question.grid(row=0, column=4, columnspan=4)
        gm_question = tk.Label(self, textvariable=player.current_task, height=10, width=75, bg='black', fg='white')
        gm_question.grid(row=1, column=4, columnspan=4, rowspan=4)

        button_update_game = tk.Button(self, text="Update state", command=lambda: update(), padx=30)
        button_update_game.grid(row=3, column=0, columnspan=2)

        button_send_answer = tk.Button(self, text="Send answer", command=lambda: send_answer(), padx=30)
        button_send_answer.grid(row=4, column=0, columnspan=2)

        button_start_game = tk.Button(self, text="Start game", command=lambda: start_game(), padx=30)
        button_start_game.grid(row=5, column=0, columnspan=2)


class PageEnd(tk.Frame):

    def __init__(self, parent, controller, player):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="The winner is: ", font=LARGE_FONT)
        label.pack(pady=10,padx=10)


class PageGameMasterPickQuestion(tk.Frame):

   def __init__(self, parent, controller, player):
        tk.Frame.__init__(self, parent)

        def pick_question1():
            if len(player.gm_answers) >= 1:
                player.game_server.choose_winner(player.token, list(player.gm_answers.keys())[0])
        def pick_question2():
            if len(player.gm_answers) >= 2:
                player.game_server.choose_winner(player.token, list(player.gm_answers.keys())[1])
        def pick_question3():
            if len(player.gm_answers) >= 3:
                player.game_server.choose_winner(player.token, list(player.gm_answers.keys())[2])

        label_question1 = tk.Label(self, text="Answer 1")
        label_question1.grid(row=3, column=1)
        self.question1_answer = Text(self, height=10, width=20)
        self.question1_answer.grid(row=4, column=1, rowspan=5)

        label_question2 = tk.Label(self, text="Answer 2")
        label_question2.grid(row=3, column=2)
        self.question2_answer = Text(self, height=10, width=20)
        self.question2_answer.grid(row=4, column=2, rowspan=5)

        label_question3 = tk.Label(self, text="Answer 3")
        label_question3.grid(row=3, column=3)
        self.question3_answer = Text(self, height=10, width=20)
        self.question3_answer.grid(row=4, column=3, rowspan=5)

        button_accept_question1 = tk.Button(self, text="Choose", command=lambda:[ controller.show_frame(PageGame),pick_question1(),], padx=16)
        button_accept_question1.grid(row=9, column=1)
        button_accept_question2 = tk.Button(self, text="Choose", command=lambda:[ controller.show_frame(PageGame),pick_question2(),], padx=16)
        button_accept_question2.grid(row=9, column=2)
        button_accept_question3 = tk.Button(self, text="Choose", command=lambda:[ controller.show_frame(PageGame),pick_question3(),], padx=16)
        button_accept_question3.grid(row=9, column=3)

   def prepare(self, player):
       if len(player.gm_answers) >= 1:
           self.question1_answer.insert(INSERT, player.gm_answers[list(player.gm_answers.keys())[0]], END)
       if len(player.gm_answers) >= 2:
           self.question2_answer.insert(INSERT, player.gm_answers[list(player.gm_answers.keys())[1]], END)
       if len(player.gm_answers) >= 3:
           self.question3_answer.insert(INSERT, player.gm_answers[list(player.gm_answers.keys())[2]], END)


if __name__ == '__main__':
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('-l', help='Lobby url')
    ARGS = PARSER.parse_args()
    lobby_url = ARGS.l
    lobby = li.create_lobby_interface(lobby_url)

app = DevelopersAgainstDevelopers()
app.geometry("500x400")
app.mainloop()
