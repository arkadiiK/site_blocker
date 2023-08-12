# OPEN WITH ADMINISTRATOR PERMISSION!!!

from tkinter import *

window = Tk()
window.geometry('650x400')
window.minsize(650, 400)
window.maxsize(650, 400)
window.title('Add blocker')

heading = Label(window, text='Website blocker', font='arial')
heading.pack

host_path = 'C:\Windows\System32\drivers\etc\hosts'
ip_adress = '127.0.0.1'


def blocker():
    website_lists = enter_Website.get(1.0, END)
    website = list(website_lists.split(','))
    with open(host_path, 'r+') as host_file:
        file_content = host_file.read()
        for web in website:
            if web in file_content:
                display = Label(window, text='Already blocked', font='arial')
                display.place(x=200, y=200)
                pass
            else:
                host_file.write(ip_adress + ' ' + web + '\n')
            Label(window, text='Blocked', font='arial').place(x=230, y=200)


def unblock():
    website_lists = enter_Website.get(1.0, END)
    website = list(website_lists.split(','))
    with open(host_path, 'r+') as host_file:
        file_content = host_file.readlines()
        print(file_content)
        with open(host_path, 'w') as output_hostfile:
            for host_weblink in file_content:
                for entry_link in website:
                    if entry_link not in host_weblink:
                        output_hostfile.write(host_weblink)
                        Label(window, text='Unblocked', font='arial').place(x=350, y=200)
                    else:
                        display = Label(window, text='Website not blocked', font='arial')
                        display.place(x=350, y=200)


label1 = Label(window, text='Enter Website: ', font='arial 13 bold')
label1.place(x=5, y=60)

enter_Website = Text(window, font='arial', height='2', width='40')
enter_Website.place(x=150, y=60)

block_button = Button(window, text='Block', font='arial', pady=5, command=blocker, width=6, bg='royal blue1',
                      activebackground='grey')
block_button.place(x=230, y=150)

unblock_button = Button(window, text='Unblock', font='arial', pady=5, command=unblock, width=6, bg='royal blue1',
                        activebackground='grey')
unblock_button.place(x=350, y=150)

window.mainloop()
