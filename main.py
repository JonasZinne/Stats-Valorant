import tkinter as tk
from functions import *
from styles import *

VERSION = 1.41
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

# Top Frame (Input fields and Buttons)
top_frame = tk.Frame(scrollable_frame, bg=BACKGROUND)
top_frame.pack(side="top", fill="x")

top_frame.columnconfigure(0, weight=1)
top_frame.columnconfigure(1, weight=1)

# Input Fields
riot_name_label = tk.Label(top_frame, text="Riot Name:")
set_label_styles(riot_name_label)
riot_name_label.grid(row=0, column=0, sticky="e", pady=10, padx=10)
riot_name_entry = tk.Entry(top_frame)
set_entry_styles(riot_name_entry)
riot_name_entry.grid(row=0, column=1, sticky="w")

riot_tag_label = tk.Label(top_frame, text="Riot Tag:")
set_label_styles(riot_tag_label)
riot_tag_label.grid(row=1, column=0, sticky="e", pady=10, padx=10)
riot_tag_entry = tk.Entry(top_frame)
set_entry_styles(riot_tag_entry)
riot_tag_entry.grid(row=1, column=1, sticky="w")

entries = {
    "riot_name_entry": riot_name_entry,
    "riot_tag_entry": riot_tag_entry
}

# Buttons (retrieve data)
fetch_button = tk.Button(top_frame, text="Daten abrufen", command=lambda: fetch_data(labels, entries))
set_button_styles(fetch_button)
fetch_button.grid(row=2, column=0, columnspan=2, pady=(10,5))
window.bind('<Return>', lambda event: fetch_data(labels, entries))

kampfi_riot_id_button = tk.Button(top_frame, text="Stats Kampfi", command=lambda: kampfi_riot_id(entries))
set_button_styles(kampfi_riot_id_button)
kampfi_riot_id_button.grid(row=3, column=0, columnspan=2, pady=(5,10))

# UI elements for player data
data_frame = tk.Frame(scrollable_frame, bg=BACKGROUND)
data_frame.pack(padx=(0,75))

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
labels["title_label"].grid(row=0, column=0, sticky="w")

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

# Bottom Frame (Credits and Version)
bottom_frame = tk.Frame(scrollable_frame, bg=BACKGROUND)
bottom_frame.pack(side="bottom", fill="x")

bottom_frame.columnconfigure(0, weight=1)
bottom_frame.columnconfigure(1, weight=1)

credits_label = tk.Label(bottom_frame, text="Credits gehen raus an Clarala")
set_credits_label_styles(credits_label)
credits_label.grid(row=0, column=0, sticky="ew")

toggle_site_button = tk.Button(bottom_frame, text="Seite wechseln", command=lambda: toggle_site())
set_button_styles(toggle_site_button)
toggle_site_button.grid(row=0, column=1, padx=20)

version_label = tk.Label(bottom_frame, text=f"Version:\t{VERSION}")
set_version_label_styles(version_label)
version_label.grid(row=1, column=0, sticky="ew")

# Pack the canvas and scrollbar
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# UI window launched
window.mainloop()
