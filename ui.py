import json
from tkinter import *
from tkinter import messagebox
data_file = open("data.json")
data = json.load(data_file)


class UI:
    def __init__(self):
        self.window = Tk()
        self.website_entry = Entry(width=data["WEBSITE_ENTRY_WIDTH"])
        self.email_entry = Entry(width=data["EMAIL_ENTRY_WIDTH"])
        self.password_entry = Entry(width=data["PASSWORD_ENTRY_WIDTH"])

        self.window_creation()

    def save(self):

        website = self.website_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        new_pass = {
            website: {
                "Email": email,
                "Password": password
            }
        }

        if len(website) == data["MINIMUM_VALUE"] or len(email) == data["MINIMUM_VALUE"] \
                or len(password) == data["MINIMUM_VALUE"]:
            messagebox.showinfo(title=data["ERROR_TITLE"], message=data["ERROR_MESSAGE"])
        else:
            is_ok = messagebox.askokcancel(title=website,
                                           message=f"These are the details entered: \nEmail: {email} "
                                                   f"\nPassword: {password}")

            # check if entered values are correct
            if is_ok:
                with open(data["SAVED_PASSWORDS_FILE"], "r") as fp:
                    saved_pass = json.load(fp)
                    saved_pass.update(new_pass)

                with open(data["SAVED_PASSWORDS_FILE"], 'w') as json_file:
                    json.dump(saved_pass, json_file, indent=data["INDENT_VALUE"], separators=(',', ':'))
                    self.website_entry.delete(data["START_INDEX"], END)
                    self.email_entry.delete(data["START_INDEX"], END)
                    self.password_entry.delete(data["START_INDEX"], END)

    # window
    def window_creation(self):
        self.window.title(data["WINDOW_TITLE"])
        self.window.config(padx=data["WINDOW_PAD_X"], pady=data["WINDOW_PAD_Y"])

        # image
        canvas = Canvas(height=data["CANVAS_HEIGHT"], width=data["CANVAS_WIDTH"])
        logo_img = PhotoImage(file=data["LOGO_FILEPATH"])
        canvas.create_image(data["CANVAS_X"], data["CANVAS_Y"], image=logo_img)
        canvas.grid(row=data["CANVAS_ROW"], column=data["CANVAS_COLUMN"])

        # labels
        website_label = Label(text=data["WEBSITE_LABEL"])
        website_label.grid(row=data["WEBSITE_ROW"], column=data["WEBSITE_COLUMN"])

        email_label = Label(text=data["EMAIL_LABEL"])
        email_label.grid(row=data["EMAIL_ROW"], column=data["EMAIL_COLUMN"])

        password_label = Label(text=data["PASSWORD_LABEL"])
        password_label.grid(row=data["PASSWORD_ROW"], column=data["PASSWORD_COLUMN"])

        # entries

        self.website_entry.grid(row=data["WEBSITE_ENTRY_ROW"], column=data["WEBSITE_ENTRY_COLUMN"],
                                columnspan=data["WEBSITE_ENTRY_SPAN"])
        self.website_entry.var = self.website_entry
        self.website_entry.focus()

        self.email_entry.grid(row=data["EMAIL_ENTRY_ROW"], column=data["EMAIL_ENTRY_COLUMN"],
                              columnspan=data["EMAIL_ENTRY_SPAN"])

        self.password_entry.grid(row=data["PASSWORD_ENTRY_ROW"], column=data["PASSWORD_ENTRY_COLUMN"])

        # buttons
        add_button = Button(text=data["ADD_BUTTON_TEXT"], width=data["ADD_BUTTON_WIDTH"], command=self.save)
        add_button.grid(row=data["ADD_BUTTON_ROW"], column=data["ADD_BUTTON_COLUMN"],
                        columnspan=data["ADD_BUTTON_SPAN"])

        self.window.mainloop()
