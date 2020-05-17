import pickle
import time
from socket import *
from threading import Thread, Timer
import sys

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
status = [1]
CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'


def enCode(message):  # function to encode the text which we send
    return bytes(message, 'utf-8')


def deCode(message):  # function to decode the text which we receive
    return message.decode('utf-8')


def receive():  # function to receive any comments from the server side
    message = clientSocket.recv(1024)
    print(deCode(message))


def receive_ques():  # function to receive question from the server side
    ques = clientSocket.recv(1024)
    print(deCode(ques))


def receive_score2():  # function to receive score from the server side
    score = clientSocket.recv(1024)
    score = pickle.loads(score)
    print("SCOREBOARD")
    for i in range(len(score)):
        print("player" + str(i + 1) + ": " + str(score[i]))

    max_score = max(score)

    if max(score) >= 5:
        print("Player %d WON" % (score.index(max_score) + 1))
        print("******GAME-OVER******")
        status[0] = 0
        clientSocket.close()


def delete_last_lines(n=1):  # system function to delete the last line which was printed on the terminal
    for _ in range(n):
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(ERASE_LINE)


def send_answer():  # main function to send the reponse to server
    answer = None

    def buzzer():  # target function for buzzer thread
        time.sleep(10)
        if answer is None:
            delete_last_lines()
            print("PRESS ENTER TO CONTINUE")
            msg = ['0', 30]
            msg = pickle.dumps(msg)
            clientSocket.send(msg)
            return
        else:
            t = None

            def function():  # target function for timed answer input
                time.sleep(10)
                if t is not None:
                    msg = [t, t2 - t1]
                    msg = pickle.dumps(msg)
                else:
                    delete_last_lines()
                    print("Sorry! You've taken more than 10 seconds to answer.\nPRESS ENTER TO CONTINUE")
                    msg = ['e', 30]
                    msg = pickle.dumps(msg)
                clientSocket.send(msg)

            Thread(target=function).start()  # thread to take a timed input for answer
            t = input("ENTER YOUR OPTION\n")
            return

    Thread(target=buzzer).start()  # thread to keep a timed buzzer
    t1 = time.time()
    print("PRESS BUZZER")
    answer = input()
    t2 = time.time()


name = input('\nEnter your name:')
clientSocket.send(enCode(name))
receive()  # welcome to the game-show
receive()  # all players are ready

while status[0]:  # main loop which runs the quiz
    print('\n')
    receive_ques()
    send_answer()
    receive_score2()
