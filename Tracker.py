import requests # pip install requests
import tkinter as tk # pip install tkinter
from bs4 import BeautifulSoup # pip install BeautifulSoup

version = 0.8

# retrieve and show data
def display_data():
    # dynamic URL
    riot_id = riot_id_entry.get()
    tag = tag_entry.get()
    user = f"{riot_id}%23{tag}"

    url = f'https://tracker.gg/valorant/profile/riot/{user}/overview'

    # HTML code of the page
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # colour count
    red_count = 0
    yellow_count = 0
    green_count = 0
    
    # Error message
    error = soup.find('div', class_='content--error')
    if error:
        error_element = error.find('span', class_='lead') # Player not found
        if error_element:
            error_message = error.find('span', class_='lead').text.strip()
            
        error_element = error.find('span', class_='font-light') # Profile private
        if error_element: 
            error_message = error.find('span', class_='font-light').text.strip()
                   
        error_label.config(text=error_message)

        # reset data
        title_label.config(text=f"")
        rank_label.config(text=f"Rank (momentan):\t{rank_placeholder}")
        peak_rank_label.config(text=f"Peak Rank:\t{peak_rank_placeholder}")
        damage_label.config(text=f"Damage/Round:\t{damage_placeholder}")
        kd_label.config(text=f"K/D Ratio:\t\t{kd_placeholder}")
        headshot_label.config(text=f"Headshot%:\t{headshot_placeholder}")
        acs_label.config(text=f"ACS:\t\t{acs_placeholder}")
        kad_label.config(text=f"KAD Ratio:\t{kad_placeholder}")
        tracker_score_label.config(text=f"Tracker Score:\t{tracker_score_placeholder}")
        color_count_label.config(text=f"")
        
        # reset colours
        damage_label.config(fg="black")
        kd_label.config(fg="black")
        headshot_label.config(fg="black")
        acs_label.config(fg="black")
        kad_label.config(fg="black")
        tracker_score_label.config(fg="black")
        return

    # Player name (title)
    name_element = soup.find('span', class_='trn-ign__username')
    name = name_element.text.strip()
    title_label.config(text=name)

    # Rank
    rank_element = soup.find('div', class_='valorant-rank-bg')
    rank = rank_element.text.strip()
    rank_label.config(text=f"Rank (momentan):\t{rank}")

    # Peak Rank
    peak_rank = soup.find('h3', string='Peak Rating')
    peak_rank_element = peak_rank.find_next('div', class_='rating-entry')
    rank_value = peak_rank_element.find('div', class_='value').text.strip()
    rank = ' '.join(rank_value.split())  # Gap between "Rank" and "xxRR"
    episode = peak_rank_element.find('div', class_='subtext').text.strip()
    peak_rank_label.config(text=f"Peak Rank:\t{rank} / {episode}")

    # Damage/Round
    damage_element = soup.select_one('div.numbers:-soup-contains("Damage/Round")')
    damage = damage_element.find_next('span', class_='value').text.strip()
    damage_label.config(text=f"Damage/Round:\t{damage}")
    if float(damage) <= 120:
        damage_label.config(fg="red")
        red_count += 1
    elif float(damage) > 120 and float(damage) < 140:
        damage_label.config(fg="yellow")
        yellow_count += 1
    elif float(damage) >= 140:
        damage_label.config(fg="green")
        green_count += 1

    # K/D Ratio
    kd_element = soup.select_one('div.numbers:-soup-contains("K/D Ratio")')
    kd = kd_element.find_next('span', class_='value').text.strip()
    kd_label.config(text=f"K/D Ratio:\t\t{kd}")
    if float(kd) <= 0.9:
        kd_label.config(fg="red")
        red_count += 1
    elif float(kd) > 0.9 and float(kd) < 1.0:
        kd_label.config(fg="yellow")
        yellow_count += 1
    elif float(kd) >= 1.0:
        kd_label.config(fg="green")
        green_count += 1

    # Headshot%
    headshot_element = soup.select_one('div.numbers:-soup-contains("Headshot%")')
    headshot = headshot_element.find_next('span', class_='value').text.strip()
    headshot_label.config(text=f"Headshot%:\t{headshot}")
    if float(headshot.strip('%')) <= 20:
        headshot_label.config(fg="red")
        red_count += 1
    elif float(headshot.strip('%')) > 20 and float(headshot.strip('%')) < 25:
        headshot_label.config(fg="yellow")
        yellow_count += 1
    elif float(headshot.strip('%')) >= 25:
        headshot_label.config(fg="green")
        green_count += 1

    # ACS
    acs_element = soup.select_one('div.numbers:-soup-contains("ACS")')
    acs = acs_element.find_next('span', class_='value').text.strip()
    acs_label.config(text=f"ACS:\t\t{acs}")
    if float(acs) <= 180:
        acs_label.config(fg="red")
        red_count += 1
    elif float(acs) > 180 and float(acs) < 220:
        acs_label.config(fg="yellow")
        yellow_count += 1
    elif float(acs) >= 220:
        acs_label.config(fg="green")
        green_count += 1

    # KAD Ratio
    kad_element = soup.select_one('div.numbers:-soup-contains("KAD Ratio")')
    kad = kad_element.find_next('span', class_='value').text.strip()
    kad_label.config(text=f"KAD Ratio:\t{kad}")
    if float(kad) <= 1.3:
        kad_label.config(fg="red")
        red_count += 1
    elif float(kad) > 1.3 and float(kad) < 1.4:
        kad_label.config(fg="yellow")
        yellow_count += 1
    elif float(kad) >= 1.4:
        kad_label.config(fg="green")
        green_count += 1  

    # Tracker Score
    tracker_score_element = soup.find('div', class_='label', string='Tracker Score')
    tracker_score = tracker_score_element.find_next('div', class_='value').text.strip()
    tracker_score_label.config(text=f"Tracker Score:\t{tracker_score}")
    if int(tracker_score.split()[0]) <= 350:
        tracker_score_label.config(fg="red")
        red_count += 1
    elif int(tracker_score.split()[0]) > 350 and int(tracker_score.split()[0]) < 500:
        tracker_score_label.config(fg="yellow")
        yellow_count += 1
    elif int(tracker_score.split()[0]) >= 500:
        tracker_score_label.config(fg="green")
        green_count += 1

    # Summary (colours)
    if green_count >= 2: # only one case (2/2/2)
        color_count_label.config(text=f"Fazit: \t\tStabil")

    if red_count >= 3:
        color_count_label.config(text=f"Fazit: \t\tSchlecht")
    if yellow_count >= 3:
        color_count_label.config(text=f"Fazit: \t\tDurchschnittlich")
    if green_count >= 3:
        color_count_label.config(text=f"Fazit: \t\tGut")

    if red_count >= 5:
        color_count_label.config(text=f"Fazit: \t\tBoosted")   
    if yellow_count >= 5:
        color_count_label.config(text=f"Fazit: \t\tKomplett Average")
    if green_count >= 5:
        color_count_label.config(text=f"Fazit: \t\tStark")
        
    if red_count >= 6:
        color_count_label.config(text=f"Fazit: \t\tAbsolut Boosted")   
    if yellow_count >= 6:
        color_count_label.config(text=f"Fazit: \t\tAbsolutes Mittelmaß")
    if green_count >= 6:
        color_count_label.config(text=f"Fazit: \t\tGöttlich") 

    error_label.config(text="")  # reset error message

# UI window
window = tk.Tk()
window.title("Spielerübersicht ")
window.configure(bg="#CECEF6") # Background

# function Kampfi
def set_riot_id():
    riot_id_entry.delete(0, tk.END)
    tag_entry.delete(0, tk.END)
    riot_id_entry.insert(0, "Kampfi")
    tag_entry.insert(0, "noo")

# input fields
riot_id_label = tk.Label(window, text="Riot ID:", font=("Arial", 14, "bold"), pady=5, bg="#CECEF6")
riot_id_label.pack()
riot_id_entry = tk.Entry(window, font=("Arial", 12))
riot_id_entry.pack()

tag_label = tk.Label(window, text="Tag (ohne #):", font=("Arial", 14, "bold"), pady=5, bg="#CECEF6")
tag_label.pack()
tag_entry = tk.Entry(window, font=("Arial", 12))
tag_entry.pack()

# Button to retrieve data
fetch_button = tk.Button(window, text="Daten abrufen", command=display_data, font=("Arial", 12))
fetch_button.pack(pady=10)

# Button Kampfi 
set_riot_id_button = tk.Button(window, text="Stats Kampfi", command=set_riot_id, font=("Arial", 12))
set_riot_id_button.pack(pady=10)

# UI elements for player data
data_frame = tk.Frame(window, bg="#CECEF6")
data_frame.pack()

title_label = tk.Label(data_frame, text="", font=("Arial", 24, "bold"), pady=20, bg="#CECEF6")
title_label.grid(row=0, column=0, columnspan=2)

rank_label = tk.Label(data_frame, text="", font=("Arial", 14), padx=20, pady=10, bg="#CECEF6")
rank_label.grid(row=1, column=0, sticky="w")

peak_rank_label = tk.Label(data_frame, text="", font=("Arial", 14), padx=20, pady=10, bg="#CECEF6")
peak_rank_label.grid(row=2, column=0, sticky="w")

damage_label = tk.Label(data_frame, text="", font=("Arial", 14), padx=20, pady=10, bg="#CECEF6")
damage_label.grid(row=3, column=0, sticky="w")

kd_label = tk.Label(data_frame, text="", font=("Arial", 14), padx=20, pady=10, bg="#CECEF6")
kd_label.grid(row=4, column=0, sticky="w")

headshot_label = tk.Label(data_frame, text="", font=("Arial", 14), padx=20, pady=10, bg="#CECEF6")
headshot_label.grid(row=5, column=0, sticky="w")

acs_label = tk.Label(data_frame, text="", font=("Arial", 14), padx=20, pady=10, bg="#CECEF6")
acs_label.grid(row=6, column=0, sticky="w")

kad_label = tk.Label(data_frame, text="", font=("Arial", 14), padx=20, pady=10, bg="#CECEF6")
kad_label.grid(row=7, column=0, sticky="w")

tracker_score_label = tk.Label(data_frame, text="", font=("Arial", 14), padx=20, pady=10, bg="#CECEF6")
tracker_score_label.grid(row=8, column=0, sticky="w")

color_count_label = tk.Label(data_frame, text="", font=("Arial", 14), padx=20, pady=10, bg="#CECEF6")
color_count_label.grid(row=9, column=0, sticky="w")

error_label = tk.Label(window, text="", font=("Arial", 14), padx=20, pady=10, bg="#CECEF6", fg="red")
error_label.pack()

# Placeholder
rank_placeholder = "Rank abc"
peak_rank_placeholder = "Rank abc / EPISODE x: ACT x"
damage_placeholder = "abc.d"
kd_placeholder = "a.bc"
headshot_placeholder = "ab.c%"
acs_placeholder = "abc.d"
kad_placeholder = "a.bc"
tracker_score_placeholder = "abc /1000"

# Placeholder (UI-elements)
rank_label.config(text=f"Rank (momentan):\t{rank_placeholder}")
peak_rank_label.config(text=f"Peak Rank:\t{peak_rank_placeholder}")
damage_label.config(text=f"Damage/Round:\t{damage_placeholder}")
kd_label.config(text=f"K/D Ratio:\t\t{kd_placeholder}")
headshot_label.config(text=f"Headshot%:\t{headshot_placeholder}")
acs_label.config(text=f"ACS:\t\t{acs_placeholder}")
kad_label.config(text=f"KAD Ratio:\t{kad_placeholder}")
tracker_score_label.config(text=f"Tracker Score:\t{tracker_score_placeholder}")

# Credits and Version
credits_label = tk.Label(window, text="Credits gehen raus an Clarala", font=("Arial", 9), bg="#CECEF6")
credits_label.pack()
version_label = tk.Label(window, text=f"Version:\t{version}", font=("Arial", 8), pady=5, bg="#CECEF6")
version_label.pack()

# launch UI window
window.mainloop()
