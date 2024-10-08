import turtle
from CONSTANTS import *
import pandas
pen = turtle.Turtle()
screen = turtle.Screen()
pen.penup()
pen.hideturtle()
screen.colormode(255)
screen.setup(width=500, height=500)
screenTk = screen.getcanvas().winfo_toplevel()
screenTk.attributes("-fullscreen", True)
screen.bgcolor(LOGIN_BGCOLOR)
pen.pencolor(LOGIN_TEXT_COLOR)
pen.goto(0, 430)
def create_log_in_screen():
   
   pen.write("WELCOME!", align="center", font=LOGIN_TEXT_FONT)
   email = screen.textinput(title="Email", prompt="Please enter your email.")
   password = screen.textinput("Password", "Please Enter Your Password")





def create_register_screen():
   pen.write("WELCOME!", align="center", font=LOGIN_TEXT_FONT)
   name = screen.textinput("Full Name", "Please Enter Your Full Name").title()
   email = screen.textinput(title="Email", prompt="Please enter your email.").lower()
   password = screen.textinput("Password", "Please Create A Password")
   user_type = screen.textinput("User Type", "Are You a Patient or a Caregiver?").lower()
   login_dict = {
       "first name": name.split(" ")[0],
       "surname": " ".join(name.split(" ")[1:]),
       "email": email,
       "password": password,
       "user_type": user_type
   }
   df = pandas.DataFrame([login_dict])
   df.to_csv("register_details.csv", index=False)
create_register_screen()





screen.exitonclick()
