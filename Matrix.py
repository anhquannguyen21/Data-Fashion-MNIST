import turtle
import random
from draw import*
from Project1_AStar import*
#Vẽ ô vuông
def drawBox(t, x, y, size, fill_color):
    t.penup()
    t.goto(x, y)
    t.pendown()

    t.fillcolor(fill_color)
    t.begin_fill()
    for i in range(0, 4):
        board.forward(size)
        board.right(90)
    t.end_fill()

#Tô màu ô vuông
def color(t, x, y, size, fill_color):
    t.penup()
    t.goto(x, y)

    t.fillcolor(fill_color)
    t.begin_fill()

    for i in range(0, 4):
        board.forward(size)  # move forward
        board.right(90)  # turn pen right 90 degrees

    t.end_fill()


def symbols(t,x,y,size,fill_color):
    t.penup()
    t.goto(x, y)
    t.pendown()

    t.fillcolor(fill_color)
    t.begin_fill()
    #for i in range(0, 4):
    board.forward(size)
    board.dot(size=10)
    t.end_fill()

#Đọc file
def readData(f):
    with open(f, "r") as fp:
        line=fp.readline()
        cnt=1
        data=list()
        while line:
            k = line.strip().split(",")
            a = [int(x) for x in k]
            print("Line {}: {}".format(cnt, a))
            data.append((cnt, a))
            line = fp.readline()
            cnt += 1
    return data

data=readData("data.txt")


def drawBlockedUp(board, start_x, start_y, box_size, M,N):
    for u in range(0, M):
        for v in range(N, N+1):
            drawBox(board, start_x + u * box_size, start_y + v * box_size, box_size, "white")

def drawBlockedRight(board, start_x, start_y, box_size, M,N):
    for u in range(M, M+1):
        for v in range(0,N):
            drawBox(board, start_x + u * box_size, start_y + v * box_size, box_size, "white")

def colorBlockedUp(board, start_x, start_y,box_size,M,N):
    for u in range(0, M+1):
        for v in range(N,N + 1):
            color(board, start_x + u * box_size, start_y + v * box_size, box_size, "Light Goldenrod")

def colorBlockedRight(board, start_x, start_y,box_size,M,N):
    for u in range(M, M+1):
        for v in range(0,N + 1):
            color(board, start_x + u * box_size, start_y + v * box_size, box_size, "Light Goldenrod")

def colorBlockedLeft(board, start_x, start_y,box_size,M,N):
    for u in range(0, 1):
        for v in range(0,N + 1):
            color(board, start_x + u * box_size, start_y + v * box_size, box_size, "Light Goldenrod")


def colorBlockedDown(board, start_x, start_y,box_size,M,N):
    for u in range(0, M+1):
        for v in range(0,1):
            color(board, start_x + u * box_size, start_y + v * box_size, box_size, "Light Goldenrod")

#Vẽ ma trận
def drawMatrixTable(board,start_x, start_y, box_size,square_color):
    print(data)
    l=data[2][0]
    square_color = "white"
    colors = ["red", "green", "Cyan", "Medium Spring Green", "Rosy Brown", "Aquamarine", "Burlywood",
              "Violet" , "Deep Sky Blue","Lawn Green", "Gold", "Salmon", "Deep Pink",
              "orange", "purple", "pink", "yellow","Light Sea Green", "Light Slate Gray", "Dodger Blue","Maroon","Old Lace","Lemon Chiffon"
              , "Chocolate"                                     ]
    #start_x = -300
    #start_y = -250
    #box_size = 30
    a = [[0 for x in range(data[0][1][1])] for y in range(data[0][1][0])]
    for i in range(0, data[0][1][0]):
        for j in range(0, data[0][1][1]):
            drawBox(board, start_x + i * box_size, start_y + j * box_size, box_size, square_color)
        square_color = 'white'
    # for u in range(17, data[0][1][0]):
    #     for v in range(0, data[0][1][1]+1):
    #      drawBox(board, start_x + u * box_size, start_y + v * box_size, box_size, "white")
    for u in range(0, data[0][1][0]):
        for v in range(18, data[0][1][1]+1):
            drawBox(board, start_x + u * box_size, start_y + v * box_size, box_size, "white")
    drawBlockedUp(board,start_x,start_y,box_size,data[0][1][0], data[0][1][1])
    drawBlockedRight(board, start_x, start_y, box_size, data[0][1][0], data[0][1][1])
    colorBlockedUp(board, start_x, start_y, box_size, data[0][1][0], data[0][1][1])
    colorBlockedLeft(board, start_x, start_y, box_size, data[0][1][0], data[0][1][1])
    colorBlockedRight(board, start_x, start_y, box_size, data[0][1][0], data[0][1][1])
    colorBlockedDown(board, start_x, start_y, box_size, data[0][1][0], data[0][1][1])



    b = [[0 for x in range(data[0][1][0])] for y in range(data[0][1][1])]

    with open('data.txt') as f:
        # read matrix size and create matrix
        r, c = [int(x) for x in next(f).split(',')]
        r += 1
        c += 1
        a = [[0 for x in range(c)] for y in range(r)]
        # read start, goal coordinates
        s, g, pickPoints = readEndpoint(f)
        # read number of polygons
        n = int(next(f))
        # read n polygons and draw
        i = 1
        for line in f:
            co = [int(x) for x in line.split(',')]
            drawPolygon(a, co, i)
            i += 1

        if (len(pickPoints) == 0):
            for x in range(r):
                for y in range(c):
                    if (x == 0 or y == 0 or x == r - 1 or y == c - 1):
                        a[x][y] = 'x'
        result = []
        checkWay = 1
        isFindWay = 0
        robot = Cell(s.x, s.y)
        source = Cell(s.x, s.y)
        colors = ["red", "green", "Cyan", "Medium Spring Green", "Rosy Brown", "Aquamarine", "Burlywood",
                  "Violet", "Deep Sky Blue", "Lawn Green", "Gold", "Salmon", "Deep Pink",
                  "orange", "purple", "pink", "yellow", "Light Sea Green", "Light Slate Gray",
                  "Dodger Blue", "Maroon", "Old Lace", "Lemon Chiffon"
            , "Chocolate"]
        col = [0 for x in range(i)]
        for x in range(i):
            col[x] = random.choice(colors)
            colors.remove(col[x])
        while (checkWay == 1 and isFindWay == 0):
            check, cost, way = aStartSearch2(a, source, g, r, c)
            if (check == 0):
                checkWay = 0
                continue
            for j in range(len(way)):
                if (a[way[j].x][way[j].y] == 0):
                    robot = Cell(way[j].x, way[j].y)
                    result.append(robot)
                    move(a, r, c, robot, source, g, i)
                    a[robot.x][robot.y] = i
                    index = 1
                    while (index <= i):
                        for x in range(r):
                            for y in range(c):
                                if (a[x][y] == index):
                                    color(board, start_x + x * box_size, start_y + y * box_size, box_size, col[index-1].strip())
                        index += 1
                    a[robot.x][robot.y] = 0
                    if (robot.x == g.x and robot.y == g.y):
                        isFindWay = 1
                        break
                    else:
                        turtle.tracer(0, 0)
                        turtle.update()
                        for x in range(r):
                            for y in range(c):
                                drawBox(board, start_x + x * box_size, start_y + y * box_size, box_size, square_color)
                            square_color = 'white'
                        drawBlockedUp(board, start_x, start_y, box_size, r, c)
                        drawBlockedRight(board, start_x, start_y, box_size, r, c)
                        colorBlockedUp(board, start_x, start_y, box_size, r, c)
                        colorBlockedLeft(board, start_x, start_y, box_size, r, c)
                        colorBlockedRight(board, start_x, start_y, box_size, r, c)
                        colorBlockedDown(board, start_x, start_y, box_size, r, c)
                else:
                    source = Cell(robot.x, robot.y)
                    result.remove(robot)
                    break
        cost = 0
        for j in range(len(result) - 1):
            cost += calCost(result[j], result[j + 1])
        if (checkWay == 0):
            print("Can not find a way")
        else:
            print("Cost=", cost)


def readData(f):
    with open(f, "r") as fp:
        line=fp.readline()
        cnt=1
        data=list()
        while line:
            k = line.strip().split(",")
            a = [int(x) for x in k]
            print("Line {}: {}".format(cnt, a))
            data.append((cnt, a))
            line = fp.readline()
            cnt += 1
    return data




def color(t, x, y, size, fill_color):
    t.penup()
    t.goto(x, y)

    t.fillcolor(fill_color)
    t.begin_fill()

    for i in range(0, 4):
        board.forward(size)
        board.right(90)

    t.end_fill()

board = turtle.Turtle()
turtle.speed(1)
turtle.tracer(3,4)
turtle.hideturtle()
turtle.ht()
drawMatrixTable(board,-300,-250,25,"white")
turtle.hideturtle()
turtle.ht()
#turtle.delay(0)
turtle.update()
#Speeds from 1 to 10 enforce increasingly faster animation of line drawing and turtle turning.
turtle.done()
