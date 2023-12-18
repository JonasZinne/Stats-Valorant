import tkinter as tk
from functions import *
from styles import *

VERSION = 1.28
BACKGROUND = "#483D8B"

# UI window
window = tk.Tk()
set_window_styles(window)

# Create canvas and scrollbar
canvas = tk.Canvas(window)
scrollbar = tk.Scrollbar(window, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg=BACKGROUND)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set, bg=BACKGROUND)

def _on_mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")
scrollable_frame.bind_all("<MouseWheel>", _on_mousewheel)

# input fields
riot_name_label = tk.Label(scrollable_frame, text="Riot Name:")
set_label_styles(riot_name_label)
riot_name_label.pack(pady=(10,5))
riot_name_entry = tk.Entry(scrollable_frame)
set_entry_styles(riot_name_entry)
riot_name_entry.pack()

riot_tag_label = tk.Label(scrollable_frame, text="Riot Tag:")
set_label_styles(riot_tag_label)
riot_tag_label.pack(pady=(10,5))
riot_tag_entry = tk.Entry(scrollable_frame)
set_entry_styles(riot_tag_entry)
riot_tag_entry.pack()

entries = {
    "riot_name_entry": riot_name_entry,
    "riot_tag_entry": riot_tag_entry
}

# Button to retrieve data
fetch_button = tk.Button(scrollable_frame, text="Daten abrufen", command=lambda: fetch_data(labels, entries))
set_button_styles(fetch_button)
fetch_button.pack(pady=(20,0))

window.bind('<Return>', lambda event: fetch_data(labels, entries))

# Button Kampfi 
kampfi_riot_id_button = tk.Button(scrollable_frame, text="Stats Kampfi", command=lambda: kampfi_riot_id(entries))
set_button_styles(kampfi_riot_id_button)
kampfi_riot_id_button.pack(pady=(10,20))

# UI elements for player data
data_frame = tk.Frame(scrollable_frame, bg=BACKGROUND)
data_frame.pack(padx=(0,70))

labels = {
    "title_label": tk.Label(data_frame, text=""),
    "rank_label": tk.Label(data_frame, text=""),
    "peak_rank_label": tk.Label(data_frame, text=""),
    "damage_label": tk.Label(data_frame, text=""),
    "kd_label": tk.Label(data_frame, text=""),
    "headshot_label": tk.Label(data_frame, text=""),
    "acs_label": tk.Label(data_frame, text=""),
    "kad_label": tk.Label(data_frame, text=""),
    "tracker_score_label": tk.Label(data_frame, text=""),
    "color_count_label": tk.Label(data_frame, text=""),
    "error_label": tk.Label(scrollable_frame, text="")
}

for label in labels.values():
    set_data_label_styles(label)

set_title_label_styles(labels["title_label"])

labels["title_label"].grid(row=0, column=0, columnspan=2, sticky="w")
labels["rank_label"].grid(row=1, column=0, sticky="w")
labels["peak_rank_label"].grid(row=2, column=0, sticky="w")
labels["damage_label"].grid(row=3, column=0, sticky="w")
labels["kd_label"].grid(row=4, column=0, sticky="w")
labels["headshot_label"].grid(row=5, column=0, sticky="w")
labels["acs_label"].grid(row=6, column=0, sticky="w")
labels["kad_label"].grid(row=7, column=0, sticky="w")
labels["tracker_score_label"].grid(row=8, column=0, sticky="w")
labels["color_count_label"].grid(row=9, column=0, sticky="w")

set_error_label_styles(labels["error_label"])
labels["error_label"].pack()

reset_data(labels)

# Credits and Version
credits_label = tk.Label(scrollable_frame, text="Credits gehen raus an Clarala")
set_credits_label_styles(credits_label)
credits_label.pack()

version_label = tk.Label(scrollable_frame, text=f"Version:\t{VERSION}")
set_version_label_styles(version_label)
version_label.pack()

# Pack the canvas and scrollbar
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# UI window launched
window.mainloop()
