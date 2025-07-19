
import re
import json

html_content = open('C:/Users/William/EnigmaMachineDev/Repository/EldenRingCharacterRandomizer.github.io/weapons_page.html', 'r', encoding='utf-8').read()
weapons_list = []

# Find the section "Elden Ring All Weapons List"
# The section starts with <h2 class="titlearea"><a id="list"></a>Elden Ring All Weapons List</h2>
# and ends before the next <h2 class="titlearea"> or end of document
all_weapons_list_section_match = re.search(r'(<h2 class="titlearea"><a id="list"></a>Elden Ring All Weapons List</h2>.*?)(?=<h2 class="titlearea">|\Z)', html_content, re.DOTALL)

if all_weapons_list_section_match:
    all_weapons_list_html = all_weapons_list_section_match.group(1)

    # Find all weapon links within this section
    # We are looking for <a class="wiki_link wiki_tooltip" title="Elden Ring Weapon Name" href="/Weapon+Name">Weapon Name</a>
    # The title attribute contains "Elden Ring " followed by the weapon name.
    # The href attribute contains the relative path.
    weapon_matches = re.findall(r'<a class="wiki_link wiki_tooltip"[^>]*?title="Elden Ring ([^"]+)" href="([^"]+)"' , all_weapons_list_html)

    for weapon_name_raw, link_suffix in weapon_matches:
        # Clean up the weapon name (remove "Elden Ring " prefix and replace '+' with space)
        weapon_name = weapon_name_raw.replace('+', ' ')
        # Construct the full link
        full_link = 'https://eldenring.wiki.fextralife.com' + link_suffix
        weapons_list.append({'weapon_name': weapon_name, 'link': full_link})

# Remove duplicates if any (though unlikely with this specific regex)
unique_weapons = []
seen_weapons = set()
for item in weapons_list:
    if item['weapon_name'] not in seen_weapons:
        unique_weapons.append(item)
        seen_weapons.add(item['weapon_name'])

with open('C:/Users/William/EnigmaMachineDev/Repository/EldenRingCharacterRandomizer.github.io/elden_ring_weapons.json', 'w', encoding='utf-8') as f:
    json.dump(unique_weapons, f, indent=2)
