display text
import tkinter as tk

root = tk.Tk()

T = tk.Text(root, height=10, width=100)

T.pack()
T.tag_configure('big', font=('Verdana', 20, 'bold'))
T.tag_configure('color', foreground='#476042')
T.insert(tk.END,'\nTyping Test\n', 'big')
quote = """After the death of king, everyone wanted to be the king."""
T.insert(tk.END, quote)
lbl = tk.Label(
    root,
    text="00",
    fg="black",
    bg='#299617',
    font="Verdana 40 bold"
    )

#take input from user

inputtxt = tk.Text(root, height=10,
                width=25,
                bg="light yellow")

Output = tk.Text(root, height = 5,
              width = 25,
              bg = "light cyan")
start_typing = tk.Button(root, height=2,
                 width=20,
                 text="Start Typing Test",
                 command=lambda: StartTimer(lbl))
Display = tk.Button(root, height=2,
                 width=20,
                 text="Show",
                 command=lambda: StopTimer())
inputtxt.pack()
start_typing.pack()
Display.pack()
Output.pack()
#when user click start timer should start
counter = -1
running = False

def counter_label(lbl):
    def count():
        if running:
            global counter
            if counter == -1:
                display = "00"
            else:
                display = str(counter)

            lbl['text'] = display

            lbl.after(1000, count)
            counter += 1

    count()


def StartTimer(lbl):
    global running
    running = True
    counter_label(lbl)


#once user clicks okay timer should end and returns the seconds
def StopTimer():
    global running
    global counter
    running = False
    INPUT = inputtxt.get("1.0", "end-1c")
    print(INPUT)
    print(counter)
    # apply the formula and calculate rpm
    wpm = len(INPUT) * 60 / (5 * counter)
    if (INPUT == quote):
        Output.insert(tk.END, f'Correct and wpm is {wpm}')
    else:
        Output.insert(tk.END, "Wrong answer")



tk.mainloop()
