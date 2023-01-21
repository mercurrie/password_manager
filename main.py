import json
from tkinter import *
from tkinter import messagebox
data_file = open("data.json")
data = json.load(data_file)


# save() gets input values from website, email, and password. Loads data file from json.
#  appends new data to list, writes the updated list back to json file.
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == data["MINIMUM_VALUE"] or len(email) == data["MINIMUM_VALUE"]\
            or len(password) == data["MINIMUM_VALUE"]:
        messagebox.showinfo(title=data["ERROR_TITLE"], message=data["ERROR_MESSAGE"])
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} " 
                                                      f"\nPassword: {password}")

        # check if entered values are correct
        if is_ok:
            with open(data["SAVED_PASSWORDS_FILE"]) as fp:
                stored_passwords = json.load(fp)

            stored_passwords.append({
                "Website": website,
                "Email": email,
                "Password": password
            })

            with open(data["SAVED_PASSWORDS_FILE"], 'w') as json_file:
                json.dump(stored_passwords, json_file, indent=data["INDENT_VALUE"], separators=(',', ':'))
                website_entry.delete(data["START_INDEX"], END)
                email_entry.delete(data["START_INDEX"], END)
                password_entry.delete(data["START_INDEX"], END)


# window
window = Tk()
window.title(data["WINDOW_TITLE"])
window.config(padx=data["WINDOW_PAD_X"], pady=data["WINDOW_PAD_Y"])

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
website_entry = Entry(width=data["WEBSITE_ENTRY_WIDTH"])
website_entry.grid(row=data["WEBSITE_ENTRY_ROW"], column=data["WEBSITE_ENTRY_COLUMN"],
                   columnspan=data["WEBSITE_ENTRY_SPAN"])
website_entry.focus()
email_entry = Entry(width=data["EMAIL_ENTRY_WIDTH"])
email_entry.grid(row=data["EMAIL_ENTRY_ROW"], column=data["EMAIL_ENTRY_COLUMN"], columnspan=data["EMAIL_ENTRY_SPAN"])
password_entry = Entry(width=data["PASSWORD_ENTRY_WIDTH"])
password_entry.grid(row=data["PASSWORD_ENTRY_ROW"], column=data["PASSWORD_ENTRY_COLUMN"])

# buttons
add_button = Button(text=data["ADD_BUTTON_TEXT"], width=data["ADD_BUTTON_WIDTH"], command=save)
add_button.grid(row=data["ADD_BUTTON_ROW"], column=data["ADD_BUTTON_COLUMN"], columnspan=data["ADD_BUTTON_SPAN"])

window.mainloop()


