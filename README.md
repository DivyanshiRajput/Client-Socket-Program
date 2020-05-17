# Client-Socket-Program
SOCKET QUIZ using PYTHON3


	Instructions:
    1. Download the files server.py, client.py ans questions_list.py. 
    2. Run this command on your terminal after going to the directory in which python files are stored python3 server.py. 
    3. Open 3 more terminals and type python3 client.py and continue.


	Project Overview:
    • There is a host(server) who conducts the show and participants/players who provide answers. There are three participants in the show(clients).
    • The host has a long list of questions and correct answers with him. He randomly chooses one of the questions (making sure it is not a repeat of previous questions) and sends it to all three players.
    • The players receive the question, and are given chance to press the buzzer within 10 seconds. If player does not press the buzzer, host moves on to next question.
    • The players who pressed the buzzer are given a chance to provide the answer within 10 seconds. And the answer of the one who pressed the buzzer first is evaluated. 
    • If the answer is correct, he is given 1 point, otherwise -0.5. 
    • Nobody gets chance to answer this question again. The host then proceeds with the next question.
    • The game stops when any player gets 5 or more points and that player is declared the winner.


	Project Description:
    • First the server waits for the connection from 3 clients. The quiz starts when all three players have joined the game.
    • The players enter their name and the quiz begins by initiating quiz() function. After every question scores of all the players will be printed on the client side. 
    • A send_answer() function on the client side keeps track of the buzzer and sends answer back to the server for evaluation.
    • I’ve used two threads, one for timed buzzer and other for timed answer input.
    • If client does not press the buzzer or doesn’t enter a valid answer within time, he/she is asked to press enter to continue.
    • The server receives response from each client and updates the scores and sends it to the client. The first one to score 5 or more points is declared as the winner.

	NOTE: Script will break if any of the client leaves the quiz in between. 

	Points to remember while running the program:
    • Do not press enter more than once.
    • You need to press enter within 10 seconds. 
    • If you don’t press enter or choose an option within the given time, you will be unable to continue the quiz.
    • Don’t press any key while sever is receiving or sending anything.
      

		      
