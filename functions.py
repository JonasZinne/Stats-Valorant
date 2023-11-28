import requests
from bs4 import BeautifulSoup
import tkinter as tk 

def fetch_data(labels, entries, event=None):
    riot_name = entries['riot_name_entry'].get()
    riot_tag = entries['riot_tag_entry'].get()

    if not riot_name or not riot_tag:
        labels['error_label'].config(text="Felder nicht ausgefüllt")
        labels['title_label'].config(text=f"")
        reset_data(labels)
        return
    
    if len(riot_name) > 20 or len(riot_tag) > 5:
        labels['error_label'].config(text="zu viele Zeichen eingegeben")
        labels['title_label'].config(text=f"")
        reset_data(labels)
        return
    
    user = f"{riot_name}%23{riot_tag}"
    url = f'https://tracker.gg/valorant/profile/riot/{user}/overview?playlist=competitive'
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    if check_for_errors(soup, labels):
        labels['title_label'].config(text=f"")
        reset_data(labels)
        return
    
    display_player_data(soup, labels)

def check_for_errors(soup, labels):
    error = soup.find('div', class_='content--error')
    if error:
        error_element = error.find('span', class_='lead') # Player not found
        if error_element:
            error_message = error.find('span', class_='lead').text.strip()
            
        error_element = error.find('span', class_='font-light') # Profile private
        if error_element: 
            error_message = error.find('span', class_='font-light').text.strip()
                   
        labels['error_label'].config(text=error_message)
        return True
    
    return False

def display_player_data(soup, labels):
    red_count = 0
    yellow_count = 0
    green_count = 0

    # Player name (title)
    name_element = soup.find('span', class_='trn-ign__username')
    name = name_element.text.strip()
    labels['title_label'].config(text=name)

    # Rank
    rank_element = soup.find('div', class_='valorant-rank-bg')
    if rank_element:
        rank = rank_element.text.strip()
        labels['rank_label'].config(text=f"Rank (momentan):\t{rank}")
    else:
        error_message = soup.find('span', class_='font-light').text.strip()
        labels['error_label'].config(text=error_message)
        reset_data(labels)
        return

    # Peak Rank
    peak_rank = soup.find('h3', string='Peak Rating')
    peak_rank_element = peak_rank.find_next('div', class_='rating-entry')
    rank_value = peak_rank_element.find('div', class_='value').text.strip()
    rank = ' '.join(rank_value.split())  # Gap between "Rank" and "xxRR"
    episode = peak_rank_element.find('div', class_='subtext').text.strip()
    labels['peak_rank_label'].config(text=f"Peak Rank:\t{rank} / {episode}")

    # Damage/Round
    damage_element = soup.select_one('div.numbers:-soup-contains("Damage/Round")')
    damage = damage_element.find_next('span', class_='value').text.strip()
    labels['damage_label'].config(text=f"Damage/Round:\t{damage}")
    if float(damage) <= 120:
        labels['damage_label'].config(fg="red")
        red_count += 1
    elif float(damage) > 120 and float(damage) < 140:
        labels['damage_label'].config(fg="yellow")
        yellow_count += 1
    elif float(damage) >= 140:
        labels['damage_label'].config(fg="green")
        green_count += 1

    # K/D Ratio
    kd_element = soup.select_one('div.numbers:-soup-contains("K/D Ratio")')
    kd = kd_element.find_next('span', class_='value').text.strip()
    labels['kd_label'].config(text=f"K/D Ratio:\t\t{kd}")
    if float(kd) <= 0.9:
        labels['kd_label'].config(fg="red")
        red_count += 1
    elif float(kd) > 0.9 and float(kd) < 1.0:
        labels['kd_label'].config(fg="yellow")
        yellow_count += 1
    elif float(kd) >= 1.0:
        labels['kd_label'].config(fg="green")
        green_count += 1

    # Headshot %
    headshot_element = soup.select_one('div.numbers:-soup-contains("Headshot %")')
    headshot = headshot_element.find_next('span', class_='value').text.strip()
    labels['headshot_label'].config(text=f"Headshot %:\t{headshot}")
    if float(headshot.strip('%')) <= 20:
        labels['headshot_label'].config(fg="red")
        red_count += 1
    elif float(headshot.strip('%')) > 20 and float(headshot.strip('%')) < 25:
        labels['headshot_label'].config(fg="yellow")
        yellow_count += 1
    elif float(headshot.strip('%')) >= 25:
        labels['headshot_label'].config(fg="green")
        green_count += 1

    # ACS
    acs_element = soup.select_one('div.numbers:-soup-contains("ACS")')
    acs = acs_element.find_next('span', class_='value').text.strip()
    labels['acs_label'].config(text=f"ACS:\t\t{acs}")
    if float(acs) <= 180:
        labels['acs_label'].config(fg="red")
        red_count += 1
    elif float(acs) > 180 and float(acs) < 220:
        labels['acs_label'].config(fg="yellow")
        yellow_count += 1
    elif float(acs) >= 220:
        labels['acs_label'].config(fg="green")
        green_count += 1

    # KAD Ratio
    kad_element = soup.select_one('div.numbers:-soup-contains("KAD Ratio")')
    kad = kad_element.find_next('span', class_='value').text.strip()
    labels['kad_label'].config(text=f"KAD Ratio:\t{kad}")
    if float(kad) <= 1.3:
        labels['kad_label'].config(fg="red")
        red_count += 1
    elif float(kad) > 1.3 and float(kad) < 1.4:
        labels['kad_label'].config(fg="yellow")
        yellow_count += 1
    elif float(kad) >= 1.4:
        labels['kad_label'].config(fg="green")
        green_count += 1  

    # Tracker Score
    tracker_score_element = soup.find('div', class_='label', string='Tracker Score')
    tracker_score = tracker_score_element.find_next('div', class_='value').text.strip()
    labels['tracker_score_label'].config(text=f"Tracker Score:\t{tracker_score}")
    if int(tracker_score.split()[0]) <= 350:
        labels['tracker_score_label'].config(fg="red")
        red_count += 1
    elif int(tracker_score.split()[0]) > 350 and int(tracker_score.split()[0]) < 500:
        labels['tracker_score_label'].config(fg="yellow")
        yellow_count += 1
    elif int(tracker_score.split()[0]) >= 500:
        labels['tracker_score_label'].config(fg="green")
        green_count += 1

    # Summary (colours)
    if green_count >= 2: # only one case (2/2/2)
        labels['color_count_label'].config(text=f"Fazit: \t\tStabil")

    if red_count >= 3:
        labels['color_count_label'].config(text=f"Fazit: \t\tSchlecht")
    if yellow_count >= 3:
        labels['color_count_label'].config(text=f"Fazit: \t\tDurchschnittlich")
    if green_count >= 3:
        labels['color_count_label'].config(text=f"Fazit: \t\tGut")

    if red_count >= 5:
        labels['color_count_label'].config(text=f"Fazit: \t\tBoosted")   
    if yellow_count >= 5:
        labels['color_count_label'].config(text=f"Fazit: \t\tKomplett Average")
    if green_count >= 5:
        labels['color_count_label'].config(text=f"Fazit: \t\tStark")
        
    if red_count >= 6:
        labels['color_count_label'].config(text=f"Fazit: \t\tAbsolut Boosted")   
    if yellow_count >= 6:
        labels['color_count_label'].config(text=f"Fazit: \t\tAbsolutes Mittelmaß")
    if green_count >= 6:
        labels['color_count_label'].config(text=f"Fazit: \t\tGöttlich") 

    labels['error_label'].config(text="")  # reset error message

def reset_data(labels):
    labels['rank_label'].config(text=f"Rank (momentan):\tRank abc")
    labels['peak_rank_label'].config(text=f"Peak Rank:\tRank abc / EPISODE x: ACT x")
    labels['damage_label'].config(text=f"Damage/Round:\tabc.d")
    labels['kd_label'].config(text=f"K/D Ratio:\t\ta.bc")
    labels['headshot_label'].config(text=f"Headshot %:\tab.c%")
    labels['acs_label'].config(text=f"ACS:\t\tabc.d")
    labels['kad_label'].config(text=f"KAD Ratio:\ta.bc")
    labels['tracker_score_label'].config(text=f"Tracker Score:\tabc /1000")
    labels['color_count_label'].config(text=f"")
        
    labels['damage_label'].config(fg="black")
    labels['kd_label'].config(fg="black")
    labels['headshot_label'].config(fg="black")
    labels['acs_label'].config(fg="black")
    labels['kad_label'].config(fg="black")
    labels['tracker_score_label'].config(fg="black")

def kampfi_riot_id(entries):
    entries['riot_name_entry'].delete(0, tk.END)
    entries['riot_tag_entry'].delete(0, tk.END)
    entries['riot_name_entry'].insert(0, "Kampfi")
    entries['riot_tag_entry'].insert(0, "Fire")
