# mathbot
this is a program built with flask library in python that will solve from basic geometry like perimeter, area, surface area, volume, circumference, etc. to algebra 1 and trig 

run it from main.py

if the program doesn't run make sure that you have installed pythin3 and flask

install flask by typing in terminal or comand prompt, pip3 install flask
there are also some great youtube videos on installing python and flask

if you wish for whatever reason to put this in regular python (like you can't get flask or it's just easier than a server) then :
1. copy the algorithm which you want to use from auth.py copy from def to the return right before the next function
2. switch the way to get variables: the way that this code gets variables is by extracting them from html by setting them to request.get[''] but you don't have that in plain python so set them equal to float(input('prompt'))
3. set a good prompt: don't make your prompt coeficiant1 because they have no idea what that means so before defining the variables do something like print('use for reference Ax + B = Cx + D') and then with your input make the prompt 'fill in A' and set that equal to coeficiant1 etc.
4. the exception shouldn't return render_template because that sends you to html which you don't have, instead return something like 'error please rerun the code and make sure that you filled in only numbers'
5. when it says return render_template at the end switch it to something like return('your answer is' + solution)

If you have trouble with any of these steps then google it or watch a youtube video

if you want to copy and edit this, I recomend vscode if you're using flask or the standard python idle for just python

