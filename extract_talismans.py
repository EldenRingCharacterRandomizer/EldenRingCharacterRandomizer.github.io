import re
import json

def extract_talismans(html_file_path, json_file_path):
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    talismans = []
    # Regex to find <h4><a class="wiki_link" title="..." href="...">Talisman Name</a></h4>
    # It captures the href and the text content of the <a> tag.
    pattern = re.compile(r'<h4><a class="wiki_link" title="Elden Ring (.*?)" href="(/.*?)"[^>]*>(.*?)</a></h4>')

    for match in pattern.finditer(html_content):
        # Group 2 is the href, Group 3 is the talisman name
        talisman_name = match.group(3)
        talisman_link = "https://eldenring.wiki.fextralife.com" + match.group(2)
        talismans.append({"name": talisman_name, "link": talisman_link})

    json_output = json.dumps(talismans, indent=2)

    with open(json_file_path, 'w', encoding='utf-8') as f:
        f.write(json_output)

if __name__ == "__main__":
    html_input_path = "C:/Users/William/EnigmaMachineDev/Repository/EldenRingCharacterRandomizer.github.io/temp_talismans_html.html"
    json_output_path = "C:/Users/William/EnigmaMachineDev/Repository/EldenRingCharacterRandomizer.github.io/elden_ring_talismans.json"
    extract_talismans(html_input_path, json_output_path)
