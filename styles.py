def set_window_styles(window):
    window.title("Spielerübersicht")
    window.configure(bg="#CECEF6")

def set_label_styles(label):
    label.config(font=("Arial", 14, "bold"), pady=5, bg="#CECEF6")

def set_entry_styles(entry):
    entry.config(font=("Arial", 12))

def set_button_styles(button):
    button.config(font=("Arial", 12))

def set_title_label_styles(label):
    label.config(font=("Arial", 24, "bold"), pady=20, bg="#CECEF6")

def set_data_label_styles(label):
    label.config(font=("Arial", 14), padx=20, pady=10, bg="#CECEF6")

def set_error_label_styles(label):
    label.config(font=("Arial", 18, "bold"), padx=20, pady=10, bg="#CECEF6", fg="red")

def set_credits_label_styles(label):
    label.config(font=("Arial", 9), bg="#CECEF6")

def set_version_label_styles(label):
    label.config(font=("Arial", 8), pady=5, bg="#CECEF6")
