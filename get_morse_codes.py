import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Morse_code"

response = requests.get(url=url)
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")

morse_table = soup.select(selector="#mw-content-text div.mw-content-ltr.mw-parser-output table tbody")[0]
table_rows = morse_table.find_all('tr')

morse_dict = {}
for row in table_rows:
    char = row.select_one("td b a")
    punc = row.select("td a b")
    if char:
        character = char.get_text(strip=True).split(",")[-1].strip()
        code_found = row.select_one(selector="span .oo-ui-labelElement-label")
        morse_code = code_found.getText().replace('\xa0', ' ').strip()
        morse_dict[character] = morse_code
    if punc:
        punctuation = punc[-1].get_text(strip=True)
        code_found = row.select_one(selector="span .oo-ui-labelElement-label")
        morse_code = code_found.getText().replace('\xa0', ' ').strip()
        morse_dict[punctuation] = morse_code