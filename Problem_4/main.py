import re
from pathlib import Path

import requests

URL = "https://www.epitech-it.es"


def main():
	response = requests.get(URL)
	if response.ok:
		text = response.text
	else:
		raise Exception("Failed to connect to the page")
	out = re.search(r"\{FLAG.*?\}", text)
	with open(Path(__file__).parent / "output.txt", "w") as file:
		file.write(out.group())


if __name__ == "__main__":
	main()
