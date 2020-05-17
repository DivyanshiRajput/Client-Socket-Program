import pickle
import random
import time
from socket import *
from questions_list import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("server is ready.")
players = []  # list for storing connections and addresses
names = []  # list for storing names
score = [0, 0, 0]
connections = []
response = []


def enCode(msg):  # function to encode the text which we send
    return bytes(msg, 'utf-8')


def deCode(msg):  # function to decode the text which we receive
    return msg.decode('utf-8')


def receive_msg(client_socket):  # function to receive any comments from the client side
    try:
        message = client_socket.recv(1024)
        message = deCode(message)
        return message
    except:
        return False


def broadcast(string):  # function to send a message to all the clients
    string = enCode(string)
    for client in connections:
        try:
            client.send(string)
        except:
            client.close


def send_scores2(lst):  # to send the list of scores to all the clients
    points = pickle.dumps(lst)
    for i in connections:
        i.send(points)


def check_and_update(answer_lists):  # function which returns the index the of the players who pressed the buzzer first
    tim = [d[1] for d in answer_lists]
    t = min(tim)
    i = tim.index(t)
    return i


def quiz():  # main function which initiates the quiz
    while max(score) < 5:
        time.sleep(5)
        number = random.randint(0, len(questions) - 1)
        question = questions[number]
        questions.pop(number)
        answer = answers[number]
        answers.pop(number)
        broadcast(question)
        del response[:]
        for i in connections:
            ans = i.recv(1024)
            ans = pickle.loads(ans)
            response.append(ans)

        j = check_and_update(response)
        if str(response[j][0]) == str(answer):
            score[j] += 1
        elif str(response[j][0]) == '0':
            pass
        else:
            score[j] -= 0.5

        time.sleep(13)
        send_scores2(score)

    for c in connections:
        c.close()

u=0
while len(players) < 3:  # main loop which connects the clients to the server and then calls the quiz function
    connectionSocket, addr = serverSocket.accept()
    players.append([connectionSocket, addr])
    connections.append(connectionSocket)
    name = deCode(connectionSocket.recv(1024))
    u += 1
    message = enCode("Hey " + str(name) + "! You are player"+ str(u) + "\nWelcome to the game show\nWait for other players to join...\n")
    connectionSocket.send(message)
    names.append(name)
    print("Connection has been established: " + str(names[0]) + ' ' + str(connections[0]))

broadcast("All players are ready.\nLet us start the quiz!!!\nPress enter as a buzzer.")
time.sleep(1)
quiz()
serverSocket.close()
