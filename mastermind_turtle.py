import turtle,random
l=["cyan","blue","red","green","orange","lime","yellow","grey","brown"]
index=0
lists=["cyan","blue","red","green","orange","lime","yellow","grey","brown"]
l_guess=[0,0,0,0]
guesses=[]
no_guesses=0
def highlight_color(number,color):
	global t,l,index
	t.pu()
	t.seth(90)
	t.setpos(426,-250+number*60)
	t.color(color)
	t.pd()
	t.circle(16)
	t.color(l[index])
	t.pu()
def make_black_border():
	global t,l,index
	for i in range(9):
		highlight_color(i,"black")
def get_key():
    global lists
    random.shuffle(lists)
    return lists[:4]
def make_square(x,y):
    global l,t,index
    t.pu()
    t.setpos(x,y-50)
    t.pd()
    t.seth(45)
    t.color("white")
    t.circle(50,360,4)
    t.color(l[index])
    t.pu()
def make_square_black():
    global t,l,index
    for i in range(-1,3):
        t.pu()
        t.setpos(i*100-1,-50+1)
        t.pd()
        t.color("black","black")
        t.seth(45)
        t.begin_fill()
        t.circle(49,360,4)
        t.end_fill()
        t.pu()
    t.color(l[index])
def goto(x,y):
    global t,l,index,l_guess
    if x>=396:
        make_black_border()
        if y>-250+0*60-15 and y<-250+0*60+15:
            highlight_color(0,"white")
            index=0
            t.color(l[0])
        if y>-250+8*60-15 and y<-250+8*60+15:
           highlight_color(8,"white")
           index=8
           t.color(l[8])
        if y>-250+7*60-15 and y<-250+7*60+15:
            highlight_color(7,"white")
            index=7
            t.color(l[7])
        if y>-250+6*60-15 and y<-250+6*60+15:
            highlight_color(6,"white")
            index=6
            t.color(l[6])
        if y>-250+5*60-15 and y<-250+5*60+15:
            highlight_color(5,"white")
            index=5
            t.color(l[5])
        if y>-250+4*60-15 and y<-250+4*60+15:
           highlight_color(4,"white")
           index=4
           t.color(l[4])
        if y>-250+3*60-15 and y<-250+3*60+15:
            highlight_color(3,"white")
            index=3
            t.color(l[3])
        if y>-250+2*60-15 and y<-250+2*60+15:
            highlight_color(2,"white")
            index=2
            t.color(l[2])
        if y>-250+1*60-15 and y<-250+1*60+15:
           highlight_color(1,"white")
           index=1
           t.color(l[1])
    if y>-25*2**0.5 and y<25*2**0.5:
        if x>-100-50*2**0.5 and x<-100:
            t.color(l[index],l[index])
            t.pu()
            t.seth(45)
            t.goto(-100-1,-50+1)
            t.begin_fill()
            t.pd()
            t.circle(49,360,4)
            t.end_fill()
            t.pu()
            l_guess[0]=l[index]
        elif x>-50*2**0.5 and x<0:
            t.color(l[index],l[index])
            t.pu()
            t.seth(45)
            t.goto(-1,-50+1)
            t.begin_fill()
            t.pd()
            t.circle(49,360,4)
            t.end_fill()
            t.pu()
            l_guess[1]=l[index]
        elif x>100-50*2**0.5 and x<100:
            t.color(l[index],l[index])
            t.pu()
            t.seth(45)
            t.goto(100-1,-50+1)
            t.begin_fill()
            t.pd()
            t.circle(49,360,4)
            t.end_fill()
            t.pu()
            l_guess[2]=l[index]
        elif x>200-50*2**0.5 and x<200:
            t.color(l[index],l[index])
            t.pu()
            t.seth(45)
            t.goto(200-1,-50+1)
            t.begin_fill()
            t.pd()
            t.circle(49,360,4)
            t.end_fill()
            t.pu()
            l_guess[3]=l[index]
        else:
            t.pu()
            t.setpos(x,y)
    else:
        t.pu()
        t.setpos(x,y)
    main2()
def check_guess(l):
    global guesses
    length=len(l)
    for i in range(length):
        for j in range(length):
            if i!=j and l[i]==l[j]:
                print("must be unique colors")
                return False
    for i in range(len(guesses)):
        if l==guesses[i]:
            return False
    return True
def main2():
    global l,index,t,l_guess,guesses,key,no_guesses
    condition=1
    if no_guesses==12:
        game_over()
    for i in range(4):
        if l_guess[i]==0:
            condition=0
    if condition:
        valid=check_guess(l_guess)
        if valid:
            if key==l_guess:
                won()
                turtle.bye()
            else:
                correct_number,correct_order=scan_guess(key,l_guess)
                if correct_number!=0:
                    guesses.append([l_guess,correct_number,correct_order])
                    make_options(guesses)
                l_guess=[0,0,0,0]
                make_square_black()
                no_guesses+=1
        else:
            make_square_black()
            l_guess=[0,0,0,0]
def scan_guess(key,guess):
    order=0
    count=0
    for i in range(4):
        if guess[i] in key:
            count+=1
            if guess[i]==key[i]:
                order+=1
    return count,order
def game_over():
    print("GAME OVER")
    turtle.bye()
def won():
    global no_guesses
    print("CONGRATS!")
    print("you won in",no_guesses+1,"moves")
def make_options(guesses):
    global t,index,l
    length=len(guesses)
    t.pu()
    colors=guesses[length-1][0]
    correct=guesses[length-1][1]
    order=guesses[length-1][2]
    t.pd()
    make_clues(-500+10,-300+length*50+25,colors,correct,order)
def make_clues(x,y,color,correct,order):
	global t,index,l
	t.pu()
	t.setpos(x,y)
	t.seth(0)
	t.color(color[0])
	t.pd()
	t.dot(size=10)
	t.pu()
	t.fd(10)
	t.pd()
	t.color(color[1])
	t.dot(size=10)
	t.pu()
	t.fd(10)
	t.pd()
	t.color(color[2])
	t.dot(size=10)
	t.pu()
	t.fd(10)
	t.pd()
	t.color(color[3])
	t.dot(size=10)
	t.pu()
	t.color("white")
	t.fd(10)
	t.setpos(x+40,y-5)
	t.pd()
	string="correct colors: "+str(correct)+"  correct order: "+str(order)
	t.write(string,False,align="left",font=("Arial",10,"normal"))
	t.pu()
	t.color(l[index])
def make_colors():
	global l,t,index
	t.pu()
	t.seth(90)
	t.setpos(425,-300+50)
	for i in range(0,len(l)):
		t.color(l[i],l[i])
		t.pd()
		t.begin_fill()
		t.circle(15)
		t.end_fill()
		t.pu()
		t.fd(60)
	t.color(l[index])
	t.setpos(0,100)
def main():
    global l,index,t,l_guess,key
    s=turtle.Screen()
    turtle.setup(width=1020,height=620)
    turtle.screensize(1000,600)
    t=turtle.Turtle()
    turtle.tracer(2)
    t.shape("blank")
    t.pu()
    t.speed(0)
    s.title("mastermind")
    s.bgcolor("black")
    t.color("cyan")
    make_square(-100,0)
    make_square(0,0)
    make_square(100,0)
    make_square(200,0)
    t.setpos(0,100)
    make_colors()
    turtle.onscreenclick(goto)
    t.seth(0)
    turtle.mainloop()
key=get_key()
main()
