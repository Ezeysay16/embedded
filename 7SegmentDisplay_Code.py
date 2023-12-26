CircuitPython Logo
 Connect
New
Open
Save As
[New Document]
Save + Run
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
⌄
⌄
⌄
⌄
⌄
⌄
⌄
⌄
⌄
⌄
⌄
⌄
⌄
⌄
⌄
⌄
⌄
⌄
⌄
⌄
⌄
⌄
⌄
⌄
⌄
import board
import digitalio
import time

# 7-SEGMENT
A = digitalio.DigitalInOut(board.D2)
B = digitalio.DigitalInOut(board.D3)
C = digitalio.DigitalInOut(board.D4)
D = digitalio.DigitalInOut(board.D5)
E = digitalio.DigitalInOut(board.D6)
F = digitalio.DigitalInOut(board.D7)
G = digitalio.DigitalInOut(board.D8)

switchUpPin = digitalio.DigitalInOut(board.D21)
switchUpPin.switch_to_input(pull=digitalio.Pull.DOWN)
switchDownPin = digitalio.DigitalInOut(board.D20)
switchDownPin.switch_to_input(pull=digitalio.Pull.DOWN)
counter = 0
buttonUpState = False
lastButtonUpState = False
buttonDownState = False
lastButtonDownState = False

segments = [A, B, C, D, E, F, G]

for segment in segments:
    segment.switch_to_output(value=False)

def changeNumber(buttonPress):
    for segment in segments:
        segment.value = True
    #time.sleep(0.3)
    if buttonPress == 0:
        G.value = False
    elif buttonPress == 1:
        A.value = D.value = E.value = F.value = G.value = False
    elif buttonPress == 2:
        F.value = C.value = False
    elif buttonPress == 3:
        E.value = F.value = False
    elif buttonPress == 4:
        A.value = D.value = E.value = False
    elif buttonPress == 5:
        B.value = E.value = False
    elif buttonPress == 6:
        B.value = False
    elif buttonPress == 7:
        D.value = E.value = F.value = G.value = False
    elif buttonPress == 8:
        pass
    elif buttonPress == 9:
        D.value = E.value = False
    time.sleep(0.3)

try:
    while True:
        buttonUpState = switchUpPin.value
        buttonDownState = switchDownPin.value
        print("switchUpPin:", buttonUpState, "\tswitchDownPin:", buttonDownState)
        print(counter)
        if buttonUpState != lastButtonUpState:
            if buttonUpState:
                counter += 1
                if counter >= 9:
                    counter = 9
                time.sleep(0.3)
            else:
                print("ON")
            time.sleep(0.05)

        if buttonDownState != lastButtonDownState:
            if buttonDownState:
                counter -= 1
                if counter <= 0:
                    counter = 0
                time.sleep(0.3)
            else:
                print("ON")
            time.sleep(0.05)

        changeNumber(counter)

finally:
    for segment in segments:
        segment.deinit()
    switchUpPin.deinit()
    switchDownPin.deinit()
Editor
Serial
Info
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
Copilot
CircuitPython Code Editor
code.circuitpython.org
Ask a follow-up question
GPT-3.5
GPT-4

Summary