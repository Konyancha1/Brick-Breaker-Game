# import libraries
import _tkinter
import tkinter as tk
from tkinter import font as tkfont
from tkinter import *
from PIL import Image, ImageTk
import os
import pygame
from tkinter import messagebox


# Create parent class for the windows
class GameCanvas(tk.Tk):
    # Initialize a function that allows a variable number, keyworded and
    # variable-length arguments to be passed
    """These are used because the functions to be created will take a
    bunch of arguments that we wouldn't initialize in the initial parameters
    It will also make the arguments initialized be iterable"""

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # Create a container that with a fixed features
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # place all the pages in the same location;
        # so that the one on the top of the stacking order
        # will be the one that is visible.
        self.frames = {}
        for F in (StartPage, PageOne):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        """Show a frame for the given page name"""
        frame = self.frames[page_name]
        frame.tkraise()


# First child class
class StartPage(tk.Frame):
    """Parent and controller are the new arguments added to this class
     This class is used to create dimension, the frame title"""

    def __init__(self, parent, controller):
        # Raise Exception incase the user didnt't have the image in the same directory as this program file
        try:
            tk.Frame.__init__(self, parent)
            self.controller = controller
            self.controller.title('Ball and Bricks')
            self.controller.geometry('700x500')
            self.configure(bg='purple')

            # These lines of code are used to create a perfect yet easy to
            # navigate interface for the user

            # Create background for the canvas
            load = Image.open('new.png')
            photo = ImageTk.PhotoImage(load)

            # Put the background in a label
            label = tk.Label(self, image=photo)
            label.image = photo

            # Place the label in a fixed position on the canvas
            label.place(x=0, y=0)

            # Create a frame that will hold a label
            frame = tk.Frame(self, bg='purple', bd=3)
            frame.place(relx=0.5, rely=0.01, relwidth=1, relheight=0.05, anchor='n')

            # Create a label that will hold the information
            label = tk.Label(frame, bg='white', fg='purple', font=('Ariel', 9, 'bold'),
                             text='This is the summative project of Beauty Ikudehinbu and Kevin Onyancha. We hope you '
                                  'love it!')
            label.place(relwidth=1, relheight=1)

            lower_frame = tk.Frame(self, bg='purple', bd=6)
            lower_frame.place(relx=0.5, rely=0.35, relwidth=0.5, relheight=0.25, anchor='n')

            label = tk.Label(lower_frame, font=('Verdana', 9), bg='white', fg='purple',
                             text='Welcome to the Brick and Board Game!')
            label.place(relwidth=1, relheight=0.7)

            # Create a button that will navigate the user to page one
            button1 = tk.Button(lower_frame, text="Click to Start", bg='purple', fg='white', activebackground='pink',
                                font=('Verdana', 10), command=lambda: controller.show_frame("PageOne"))

            # Place the button in a desired location on the frame
            button1.place(relx=0, rely=0.7, relheight=0.35, relwidth=1)

            # Create a button that will quit the game and end the program
            exit_code = tk.Button(self, text='Exit', bg='purple', fg='white', activebackground='pink',
                                  font=('Verdana', 10),
                                  command=self.quit)
            exit_code.place(relx=0.87, rely=0.87, relheight=0.11, relwidth=0.11)

            pygame.mixer.init()
            game_sound = pygame.mixer.Sound('GameLevel (1).wav')
            game_sound.play()

        # This exception creates a frame on the window/canvas informing the player
        # and print out the exception on the console/terminal
        except Exception as e:

            frame = tk.Frame(self, bg='purple', bd=3)
            frame.place(relx=0.5, rely=0.01, relwidth=1, relheight=0.05, anchor='n')

            label = tk.Label(frame, bg='white', fg='purple', font=('Ariel', 9, 'bold'),
                             text='This is the summative project of Beauty Ikudehinbu and Kevin Onyancha. We hope you '
                                  'love it!')
            label.place(relwidth=1, relheight=1)

            lower_frame = tk.Frame(self, bg='purple', bd=6)
            lower_frame.place(relx=0.5, rely=0.35, relwidth=1, relheight=0.25, anchor='n')

            label = tk.Label(lower_frame, font=('Verdana', 9, 'bold'), bg='white', fg='purple',
                             text='Kindly put the images in the same directory as this program!')
            label.place(relwidth=1, relheight=0.7)

            print('Images or music not found in the directory, Kindly include the image in the directory', e)


# Create a class for the second page of the window/frame
class PageOne(tk.Frame):
    """Parent and controller are the new arguments added to this class
         This class is used to create dimension, the frame title for frame 2
         which will be stacked onto the first page when activated"""

    def __init__(self, parent, controller):
        # Raise an exception where the image for this frame is not in the same directory with this program

        tk.Frame.__init__(self, parent)
        self.controller = controller

        try:
            # These lines of code are used to create a perfect yet easy to
            # navigate interface for the use

            # Create background for the canvas
            load = Image.open('page 2.jpg')
            photo = ImageTk.PhotoImage(load)
            label = tk.Label(self, image=photo)
            label.image = photo
            label.place(x=0, y=0)


            # register section.
            # This takes the user input and store it permanently in a file.
            #The files Keeps updating every time a player plays the game
            def user_info():
                #Get the user input from the entry
                name_info = Name.get()
                surname_info = S_name.get()
                #Display a message to the user that their input have been stored
                messagebox.showinfo(title='Status', message='Your info have been stored')
                #Print on the console the user's input(This line isn't necessary)
                print(name_info, surname_info)
                #Open user.txt file and append the user input, if user.txt isn't availabe,
                # create a file that will automatically take the name and store the data
                storage = open('user.txt', 'a')
                # create a new line after every set of data
                storage.write('\n')
                #Write the data on the file created
                storage.write('First Name:' + name_info)
                storage.write('\n')
                storage.write('Last Name:' + str(surname_info))
                #Close the file
                storage.close()
                #destroy the frame and widgets after the user have successfull input their information
                frame.destroy()

            #Create frame for the Registration
            frame = tk.Frame(self, bg='purple', bd=6)
            frame.place(relx=0.5, rely=0.8, relwidth=0.5, relheight=0.2, anchor='n')

            label = tk.Label(frame, font=('Verdana', 10, 'bold'), bg='purple', fg='white',
                             text='Register')
            label.place(relwidth=0.2, relheight=0.2)
            label = tk.Label(frame, font=('Verdana', 8, 'bold'), bg='purple', fg='white',
                             text='Last Name')
            label.place(relwidth=0.2, relheight=0.2, relx=0, rely=0.3)

            label = tk.Label(frame, font=('Verdana', 8, 'bold'), bg='purple', fg='white',
                             text='First Name')
            label.place(relwidth=0.2, relheight=0.2, relx=0, rely=0.6)

            #
            Name = StringVar()
            S_name = StringVar()

            #Create an entry widget taht will take the user input
            name_info = Entry(frame, textvariable=Name, width='30')
            s_name_info = Entry(frame, textvariable=S_name, width='30')

            name_info.place(relwidth=0.6, relheight=0.2, relx=0.22, rely=0.3)
            s_name_info.place(relwidth=0.6, relheight=0.2, relx=0.22, rely=0.6)

            #create a button that will run the user_info function when clickec
            save_button = tk.Button(frame, text='save', bg='purple', fg='white', activebackground='pink',
                                    font=('Verdana', 10), command=user_info)
            save_button.place(relwidth=0.2, relheight=0.2, relx=0.8, rely=0.82)


            # Other part of the window
            lower_frame = tk.Frame(self, bg='purple', bd=6)
            lower_frame.place(relx=0.5, rely=0.15, relwidth=0.5, relheight=0.09, anchor='n')

            label = tk.Label(lower_frame, font=('Verdana', 12, 'bold'), bg='purple', fg='white',
                             text='Pick a level!')
            label.place(relwidth=1, relheight=0.7)

            frame1 = tk.Frame(self, bg='purple', bd=3)
            frame1.place(relx=0.15, rely=0.5, relwidth=0.1, relheight=0.1, anchor='w')

            frame2 = tk.Frame(self, bg='purple', bd=3)
            frame2.place(relx=0.45, rely=0.5, relwidth=0.126, relheight=0.1, anchor='w')

            frame3 = tk.Frame(self, bg='purple', bd=3)
            frame3.place(relx=0.75, rely=0.5, relwidth=0.11, relheight=0.1, anchor='w')

            # Create buttons that uses os methods to run/execute
            # the game program created on a seperate file this directory
            button1 = tk.Button(frame1, text="Beginner", bg='purple', fg='white', activebackground='pink',
                                font=('Verdana', 10),
                                command=lambda: os.system('python Beginner.py'))

            button2 = tk.Button(self, text="Intermediate", bg='purple', fg='white', activebackground='pink',
                                font=('Verdana', 9),
                                command=lambda: os.system('python IntermediateTry.py'))

            button3 = tk.Button(self, text="Advance", bg='purple', fg='white', activebackground='pink',
                                font=('Verdana', 10),
                                command=lambda: os.system('python AdvanceTry.py'))

            button1.place(relx=0.01, rely=0.5, relwidth=1, relheight=1, anchor='w')
            button2.place(relx=0.453, rely=0.5, relwidth=0.12, relheight=0.09, anchor='w')
            button3.place(relx=0.755, rely=0.5, relwidth=0.1, relheight=0.09, anchor='w')

            # Create a button that will return the start page and stack it over the present page
            exit_page = tk.Button(self, text='Quit', bg='purple', fg='white', activebackground='pink',
                                  font=('Verdana', 10),
                                  command=lambda: controller.show_frame("StartPage"))
            exit_page.place(relx=0.87, rely=0.87, relheight=0.11, relwidth=0.11)

            # Handle the error(can't find file or directory) that might arise if the files
            # linked to the to the buttons are not downloaded or in the same
            # directory as this file

            if os.path.isfile('Beginner.py'):
                f = open('Beginner.py')
                f.close()
            else:
                #Open a file present inthe directory and read the content when the other files are not available
                info = "Game_Info"
                with open(info, 'r') as f:
                    for line in f:
                        print(line)
                    f.close()

                # Show on the frame/canvas that a task need to be perform
                # When acknowledged the program ends
                response = messagebox.showerror(title='ERROR!',
                                                message="Kindly put the all the files in the same directory")
                if response:
                    quit()

            # Handle the error(can't find file or directory) that might arise if the files
            # linked to the to the buttons are not downloaded or in the same
            # directory as this file
            if os.path.isfile('IntermediateTry.py'):
                f = open('IntermediateTry.py')
                f.close()
            else:
                # Open a file present inthe directory and read the content when the other files are not available
                info = "Game_Info"
                with open(info, 'r') as f:
                    for line in f:
                        print(line)
                    f.close()
                print("Some File(s) do not exist! Kindly put all the required files in the same directory.")
                # Show on the frame/canvas that a task need to be perform
                # When acknowledged the program ends
                response = messagebox.showerror(title='ERROR!',
                                                message="Kindly put the all the files in the same directory")
                if response:
                    quit()

            # Handle the error(can't find file or directory) that might arise if the files
            # linked to the to the buttons are not downloaded or in the same
            # directory as this file
            if os.path.isfile('AdvanceTry.py'):
                f = open('AdvanceTry.py')
                f.close()
            else:
                # Open a file present inthe directory and read the content when the other files are not available
                info = "Game_Info"
                with open(info, 'r') as f:
                    for line in f:
                        print(line)
                    f.close()
                print("Some File(s) do not exist! Kindly put all the required files in the same directory.")
                # Show on the frame/canvas that a task need to be perform
                # When acknowledged the program ends
                response = messagebox.showerror(title='ERROR!',
                                                message="Kindly put the all the files in the same directory")
                if response:
                    quit()

            button1 = tk.Button(frame1, text="Beginner", bg='purple', fg='white', activebackground='pink',
                                font=('Verdana', 10),
                                command=lambda: os.system('python Beginner.py'))

            button2 = tk.Button(self, text="Intermediate", bg='purple', fg='white', activebackground='pink',
                                font=('Verdana', 9),
                                command=lambda: os.system('python IntermediateTry.py'))

            button3 = tk.Button(self, text="Advance", bg='purple', fg='white', activebackground='pink',
                                font=('Verdana', 10),
                                command=lambda: os.system('python AdvanceTry.py'))

            button1.place(relx=0.01, rely=0.5, relwidth=1, relheight=1, anchor='w')
            button2.place(relx=0.453, rely=0.5, relwidth=0.12, relheight=0.09, anchor='w')
            button3.place(relx=0.755, rely=0.5, relwidth=0.1, relheight=0.09, anchor='w')

            # Create a button that will return the start page and stack it over the present page
            exit_page = tk.Button(self, text='Quit', bg='purple', fg='white', activebackground='pink',
                                  font=('Verdana', 10),
                                  command=lambda: controller.show_frame("StartPage"))
            exit_page.place(relx=0.87, rely=0.87, relheight=0.11, relwidth=0.11)

        # This exception creates a frame on the window/canvas informing the player
        # and print out the exception on the console/terminal
        except Exception as e:
            frame = tk.Frame(self, bg='purple', bd=3)
            frame.place(relx=0.5, rely=0.01, relwidth=1, relheight=0.05, anchor='n')

            label = tk.Label(frame, bg='white', fg='purple', font=('Ariel', 9, 'bold'),
                             text='This is the summative project of Beauty Ikudehinbu and Kevin Onyancha. We hope you '
                                  'love it!')
            label.place(relwidth=1, relheight=1)

            lower_frame = tk.Frame(self, bg='purple', bd=6)
            lower_frame.place(relx=0.5, rely=0.35, relwidth=1, relheight=0.25, anchor='n')

            label = tk.Label(lower_frame, font=('Verdana', 9, 'bold'), bg='white', fg='purple',
                             text='Kindly put the images in the same directory as this program!')
            label.place(relwidth=1, relheight=0.7)

            print('Images not found in the directory, Kindly include the image in the directory', e)


# read source code file before executing
if __name__ == "__main__":
    # Call functions
    app = GameCanvas()
    app.maxsize(700, 500)
    app.mainloop()
