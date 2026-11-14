import customtkinter as ctk

app = ctk.CTk()
app.title("Guess The Number! V2.00.00")
app.geometry("500x500")

#Function to handle button click
#==== the apps colors are here! ==== dont forget to add it!!!!!!!!!!!!!!!!



#==== Main Menu texts here! ====
label = ctk.CTkLabel(
    app, 
    text="Welcome to Guess The Number!",
    font=("Arial", 24, "bold")
    )
label.pack(pady=50)

label2 = ctk.CTkLabel(
    app, 
    text="Press the start button to start the game!",
    font=("Arial", 20)
    )
label2.pack(pady=0)

#==== Main Menu buttons here! ====
button_row = ctk.CTkFrame(app, fg_color="transparent")
button_row.pack(pady=(50, 20))

start_button = ctk.CTkButton(
    button_row,
    text="Start",
    font=("Arial", 20),
    command=lambda: print("Start button clicked!")
)
start_button.pack(side="left", padx=15)

Score_button = ctk.CTkButton(
    button_row,
    text="Score",
    font=("Arial", 20),
    command=lambda: print("Score button clicked!")
)
Score_button.pack(side="left", padx=15)

exit_button = ctk.CTkButton(
    app,
    text="Exit",
    font=("Arial", 20),
    command=app.destroy
)
exit_button.pack(pady=10)

app.mainloop()