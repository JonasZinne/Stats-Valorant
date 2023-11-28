def set_window_styles(window):
    window.title("Stats Valorant")
    window.configure(bg="#483D8B")

def set_label_styles(label):
    label.config(font=("Arial", 14, "bold"), pady=5, bg="#483D8B")

def set_entry_styles(entry):
    entry.config(font=("Arial", 12))

def set_button_styles(button):
    button.config(font=("Arial", 12))

def set_title_label_styles(label):
    label.config(font=("Arial", 24, "bold"), pady=20, bg="#483D8B")

def set_data_label_styles(label):
    label.config(font=("Arial", 14), padx=20, pady=10, bg="#483D8B")

def set_error_label_styles(label):
    label.config(font=("Arial", 18, "bold"), padx=20, pady=10, bg="#483D8B", fg="red")

def set_credits_label_styles(label):
    label.config(font=("Arial", 9), bg="#483D8B")

def set_version_label_styles(label):
    label.config(font=("Arial", 8), pady=5, bg="#483D8B")
