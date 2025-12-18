from pathlib import Path

ROOT = 3


def main():
	out = ""
	with open(Path(__file__).parent / "input.txt", "r") as file:
		line = file.read().strip()
		for char in line:
			ascii_val = ord(char) - ROOT
			if not (
				ord("A") <= ascii_val <= ord("Z") or ord("a") <= ascii_val <= ord("z")
			):
				ascii_val += 26
			new_char = chr(ascii_val)
			out += new_char
	with open(Path(__file__).parent / "output.txt", "w") as file:
		file.write(out)


if __name__ == "__main__":
	main()
