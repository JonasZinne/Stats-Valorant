def set_window_styles(window):
    window.title("Stats Valorant")
    window.configure(bg="#483D8B")
    window.geometry("600x771")

def set_label_styles(label):
    label.config(
        font=("Arial", 14, "bold", "underline"), 
        bg="#483D8B", 
        fg="#ff8c00"
    )

def set_entry_styles(entry):
    entry.config(
        font=("Arial", 12), 
        width=20
    )

def set_button_styles(button):
    button.config(
        font=("Arial", 12),
        width=13,
        height=1,
        borderwidth=2,
        relief="solid",
        cursor="hand2"
    )

def set_title_label_styles(label):
    label.config(
        font=("Arial", 24, "bold", "underline"), 
        bg="#483D8B"
    )

def set_data_label_styles(label):
    label.config(
        font=("Arial", 14), 
        bg="#483D8B",
        padx=35, 
        pady=10
    )

def set_error_label_styles(label):
    label.config(
        font=("Arial", 18, "bold"), 
        bg="#483D8B", 
        fg="red",
        padx=20,
        pady=10
    )

def set_credits_label_styles(label):
    label.config(
        font=("Arial", 9), 
        bg="#483D8B"
    )

def set_version_label_styles(label):
    label.config(
        font=("Arial", 8), 
        bg="#483D8B", 
        fg="grey",
        pady=5
    )