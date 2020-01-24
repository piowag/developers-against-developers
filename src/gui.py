import tkinter as tk
from tkinter import *

LARGE_FONT= ("Verdana", 12)


class developers_against_developers(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.winfo_toplevel().title("Developers againts Developers")
        self.frames = {}

        for F in (page_start, page_create, page_join, page_game, page_end, page_gm_after_question, page_gm_pick_question):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(page_start)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class page_start(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Welcome to the game!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        label1 = tk.Label(self, text="The Developers against Developers app is a game used to expand knowledge and grinding programming skills in an unusual and attractive way for users.", wraplength=500)
        label1.config(height=5, width=50)
        label1.pack(expand=YES, fill=BOTH)

        button_create = tk.Button(self, text="Create new lobby",
                            command=lambda: controller.show_frame(page_create), padx=40)
        button_create.pack()

        button_join = tk.Button(self, text="Join lobby",
                            command=lambda: controller.show_frame(page_join), padx=65)
        button_join.pack()


class page_create(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="You created a new lobby", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        label_nick = tk.Label(self, text="Enter your name")
        label_nick.pack(pady=10,padx=10)

        nick = Entry(self, width = 50)
        nick.pack()
        nick.insert(0,"Your name")
        button_confirm = tk.Button(self, text="Confirm")
        button_confirm.pack()

        invite = Entry(self, width = 50)
        invite.pack()
        invite.insert(0,"Friends name")

        def invited():
            invited = "Player " + invite.get() + " invited"
            label_invited_players = Label(self, text=invited)
            label_invited_players.pack()

        button_invite = tk.Button(self, text="Invite player", command=invited)
        button_invite.pack()

        button_exit = tk.Button(self, text="Start game",
                            command=lambda: controller.show_frame(page_game))
        button_exit.pack(side=RIGHT, fill=X)

        button_exit = tk.Button(self, text="Exit",
                            command=lambda: controller.show_frame(page_start))
        button_exit.pack(side=LEFT, fill=X)

        button_gm = tk.Button(self, text="Become the Game Master",
                            command=lambda: controller.show_frame(page_gm_pick_question))
        button_gm.pack(side=RIGHT, fill=X)


class page_join(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="You joined lobby", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        label_nick = tk.Label(self, text="Enter your name")
        label_nick.pack(pady=10,padx=10)

        nick = Entry(self, width = 50)
        nick.pack()
        nick.insert(0,"Your name")

        button_confirm = tk.Button(self, text="Confirm")
        button_confirm.pack()

        button_exit = tk.Button(self, text="Exit",
                            command=lambda: controller.show_frame(page_start))
        button_exit.pack(side=LEFT, fill=X)

        button_gm = tk.Button(self, text="Become the Game Master",
                            command=lambda: controller.show_frame(page_gm_pick_question))
        button_gm.pack(side=RIGHT, fill=X)

class page_game(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Game #", font=LARGE_FONT)
        label.grid(row=0, column =0, columnspan=3)

        label_ranking = tk.Label(self, text="Ranking", font=LARGE_FONT)
        label_ranking.grid(row=2, column =1)

        label_player = tk.Label(self, text="Player", font=LARGE_FONT)
        label_player.grid(row=3, column=0)
        label_player = tk.Label(self, text="Nick1")
        label_player.grid(row=4, column=0)
        label_player = tk.Label(self, text="Nick2")
        label_player.grid(row=5, column=0)
        label_player = tk.Label(self, text="Nick3")
        label_player.grid(row=6, column=0)
        label_player = tk.Label(self, text="Nick4")
        label_player.grid(row=7, column=0)
        label_player = tk.Label(self, text="Nick5")
        label_player.grid(row=8, column=0)

        label_points = tk.Label(self, text="Points", font=LARGE_FONT)
        label_points.grid(row=3, column=2)
        label_points = tk.Label(self, text="15")
        label_points.grid(row=4, column=2)
        label_points = tk.Label(self, text="20")
        label_points.grid(row=5, column=2)
        label_points = tk.Label(self, text="35")
        label_points.grid(row=6, column=2)
        label_points = tk.Label(self, text="25")
        label_points.grid(row=7, column=2)
        label_points = tk.Label(self, text="30")
        label_points.grid(row=8, column=2)

        def retrieve_answer():
            answer = my_answer.get("1.0",END)
            #jak wyslac do gma???

        my_answer = Text(self, height=10, width=10)
        my_answer.grid(row=4, column=3, rowspan=5)

        label_player1 = tk.Label(self, text="Player #1")
        label_player1.grid(row=3, column=3)
        player1_answer = Text(self, height=10, width=10)
        player1_answer.grid(row=4, column=5, rowspan=5)

        label_player2 = tk.Label(self, text="Player #2")
        label_player2.grid(row=3, column=4)
        player2_answer = Text(self, height=10, width=10)
        player2_answer.grid(row=4, column=4, rowspan=5)

        label_player3 = tk.Label(self, text="Player #3")
        label_player3.grid(row=3, column=5)
        player3_answer = Text(self, height=10, width=10)
        player3_answer.grid(row=4, column=6, rowspan=5)

        label_player4 = tk.Label(self, text="Player #4")
        label_player4.grid(row=3, column=6)

        label_gm_question = tk.Label(self, text="Question:")
        label_gm_question.grid(row=0, column=3, columnspan=4)
        gm_question = Text(self, height=5, width=42, bg='black', fg='white')
        gm_question.grid(row=1, column=3, columnspan=4, rowspan=2)
        
        button_exit = tk.Button(self, text="Exit",
                            command=lambda: controller.show_frame(page_start), padx=38)
        button_exit.grid(row=9, column=0)

        button_send_answer = tk.Button(self, text="Send answer", command=retrieve_answer(), padx=127)
        button_send_answer.grid(row=9, column=3, columnspan=4)

        button_end = tk.Button(self, text="END",command=lambda: controller.show_frame(page_end), padx=25)
        button_end.grid(row=9, column=2)

class page_end(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="The winner is: ", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

class player(object):
    def __init__(self, name):
        self.name = name
        self.points = points
    
    def receive_task():
        return
    def send_answer():
        return

class game_master(object):
    def __init__(self, name):
        self.name = name
        self.points = points
    
    def ask_task():
        return
    def get_answer():
        return
    def pick_answer():
        return

class page_gm_pick_question(tk.Frame):

   def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Game #", font=LARGE_FONT)
        label.grid(row=0, column =0, columnspan=3)

        label_ranking = tk.Label(self, text="Ranking", font=LARGE_FONT)
        label_ranking.grid(row=2, column =1)

        label_player = tk.Label(self, text="Player", font=LARGE_FONT)
        label_player.grid(row=3, column=0)
        label_player = tk.Label(self, text="Nick1")
        label_player.grid(row=4, column=0)
        label_player = tk.Label(self, text="Nick2")
        label_player.grid(row=5, column=0)
        label_player = tk.Label(self, text="Nick3")
        label_player.grid(row=6, column=0)
        label_player = tk.Label(self, text="Nick4")
        label_player.grid(row=7, column=0)
        label_player = tk.Label(self, text="Nick5")
        label_player.grid(row=8, column=0)

        label_points = tk.Label(self, text="Points", font=LARGE_FONT)
        label_points.grid(row=3, column=2)
        label_points = tk.Label(self, text="15")
        label_points.grid(row=4, column=2)
        label_points = tk.Label(self, text="20")
        label_points.grid(row=5, column=2)
        label_points = tk.Label(self, text="35")
        label_points.grid(row=6, column=2)
        label_points = tk.Label(self, text="25")
        label_points.grid(row=7, column=2)
        label_points = tk.Label(self, text="30")
        label_points.grid(row=8, column=2)

        def pick_question1():
            pick_question = question1_answer.get("1.0",END)
        def pick_question2():
            pick_question = question2_answer.get("1.0",END)
        def pick_question3():
            pick_question = question3_answer.get("1.0",END)
        def pick_question4():
            pick_question = question4_answer.get("1.0",END)
            #jak wyslac do gma???

        label_question1 = tk.Label(self, text="question #1")
        label_question1.grid(row=3, column=3)
        question1_answer = Text(self, height=10, width=10,bg='black', fg='white')
        question1_answer.grid(row=4, column=3, rowspan=5)

        label_question2 = tk.Label(self, text="question #2")
        label_question2.grid(row=3, column=4)
        question2_answer = Text(self, height=10, width=10,bg='black', fg='white')
        question2_answer.grid(row=4, column=4, rowspan=5)

        label_question3 = tk.Label(self, text="question #3")
        label_question3.grid(row=3, column=5)
        question3_answer = Text(self, height=10, width=10,bg='black', fg='white')
        question3_answer.grid(row=4, column=5, rowspan=5)

        label_question4 = tk.Label(self, text="question #4")
        label_question4.grid(row=3, column=6)
        question4_answer = Text(self, height=10, width=10,bg='black', fg='white')
        question4_answer.grid(row=4, column=6, rowspan=5)

        #label_gm_question = tk.Label(self, text="Question:")
        #label_gm_question.grid(row=0, column=3, columnspan=4)

        
        button_exit = tk.Button(self, text="Exit",
                            command=lambda: controller.show_frame(page_start), padx=38)
        button_exit.grid(row=9, column=0)



        button_accept_question1 = tk.Button(self, text="Choose", command=lambda:[ controller.show_frame(page_gm_after_question),pick_question1(),], padx=16)
        button_accept_question1.grid(row=9, column=3)
        button_accept_question2 = tk.Button(self, text="Choose", command=lambda:[ controller.show_frame(page_gm_after_question),pick_question2(),], padx=16)
        button_accept_question2.grid(row=9, column=4)
        button_accept_question3 = tk.Button(self, text="Choose", command=lambda:[ controller.show_frame(page_gm_after_question),pick_question3(),], padx=16)
        button_accept_question3.grid(row=9, column=5)
        button_accept_question4 = tk.Button(self, text="Choose", command=lambda:[ controller.show_frame(page_gm_after_question),pick_question4(),], padx=16)
        button_accept_question4.grid(row=9, column=6)

        button_end = tk.Button(self, text="END",command=lambda: controller.show_frame(page_end), padx=25)
        button_end.grid(row=9, column=2)


class page_gm_after_question(tk.Frame):

   def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Game #", font=LARGE_FONT)
        label.grid(row=0, column =0, columnspan=3)

        label_ranking = tk.Label(self, text="Ranking", font=LARGE_FONT)
        label_ranking.grid(row=2, column =1)

        label_player = tk.Label(self, text="Player", font=LARGE_FONT)
        label_player.grid(row=3, column=0)
        label_player = tk.Label(self, text="Nick1")
        label_player.grid(row=4, column=0)
        label_player = tk.Label(self, text="Nick2")
        label_player.grid(row=5, column=0)
        label_player = tk.Label(self, text="Nick3")
        label_player.grid(row=6, column=0)
        label_player = tk.Label(self, text="Nick4")
        label_player.grid(row=7, column=0)
        label_player = tk.Label(self, text="Nick5")
        label_player.grid(row=8, column=0)

        label_points = tk.Label(self, text="Points", font=LARGE_FONT)
        label_points.grid(row=3, column=2)
        label_points = tk.Label(self, text="15")
        label_points.grid(row=4, column=2)
        label_points = tk.Label(self, text="20")
        label_points.grid(row=5, column=2)
        label_points = tk.Label(self, text="35")
        label_points.grid(row=6, column=2)
        label_points = tk.Label(self, text="25")
        label_points.grid(row=7, column=2)
        label_points = tk.Label(self, text="30")
        label_points.grid(row=8, column=2)

        def accept_answer1():
            answer = player1_answer.get("1.0",END)
        def accept_answer2():
            answer = player2_answer.get("1.0",END)
        def accept_answer3():
            answer = player3_answer.get("1.0",END)
        def accept_answer4():
            answer = player4_answer.get("1.0",END)
            #jak wyslac do gma???

        label_player1 = tk.Label(self, text="Player #1")
        label_player1.grid(row=3, column=3)
        player1_answer = Text(self, height=10, width=10)
        player1_answer.grid(row=4, column=3, rowspan=5)

        label_player2 = tk.Label(self, text="Player #2")
        label_player2.grid(row=3, column=4)
        player2_answer = Text(self, height=10, width=10)
        player2_answer.grid(row=4, column=4, rowspan=5)

        label_player3 = tk.Label(self, text="Player #3")
        label_player3.grid(row=3, column=5)
        player3_answer = Text(self, height=10, width=10)
        player3_answer.grid(row=4, column=5, rowspan=5)

        label_player4 = tk.Label(self, text="Player #4")
        label_player4.grid(row=3, column=6)
        player4_answer = Text(self, height=10, width=10)
        player4_answer.grid(row=4, column=6, rowspan=5)

        label_gm_question = tk.Label(self, text="Question:")
        label_gm_question.grid(row=0, column=3, columnspan=4)
        question_gm = Text(self, height=5, width=45, bg='black', fg='white')
        question_gm.grid(row=1, column=3, columnspan=4, rowspan=2)
        
        button_exit = tk.Button(self, text="Exit",
                            command=lambda: controller.show_frame(page_start), padx=38)
        button_exit.grid(row=9, column=0)

        button_accept_answer1 = tk.Button(self, text="Accept", command=accept_answer1(),padx=18)
        button_accept_answer1.grid(row=9, column=3)
        button_accept_answer2 = tk.Button(self, text="Accept", command=accept_answer2(),padx=18)
        button_accept_answer2.grid(row=9, column=4)
        button_accept_answer3 = tk.Button(self, text="Accept", command=accept_answer3(),padx=18)
        button_accept_answer3.grid(row=9, column=5)
        button_accept_answer4 = tk.Button(self, text="Accept", command=accept_answer4(),padx=18)
        button_accept_answer4.grid(row=9, column=6)

        button_end = tk.Button(self, text="END",command=lambda: controller.show_frame(page_end), padx=25)
        button_end.grid(row=9, column=2)

app = developers_against_developers()
#img = PhotoImage(file='icon.ico')
#app.tk.call('wm', 'iconphoto', root._w, img)
#app.iconbitmap('@ico-5.xbm')
app.geometry("500x250")
app.mainloop()