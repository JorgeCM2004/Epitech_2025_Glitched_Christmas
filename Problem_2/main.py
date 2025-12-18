from pathlib import Path

VALID_CHARS = {"s", "x", "-", "f"}
CHAR_NUM = {"s": 1, "x": -1, "-": 0, "f": 2}


def main():
	out = ""
	data = []
	with open(Path(__file__).parent / "input.txt", "r") as file:
		for i, line in enumerate(file.readlines()):
			data.append([])
			for char in line:
				if char.lower() in VALID_CHARS:
					data[i].append(CHAR_NUM[char.lower()])

	first_pos = None
	for i, line in enumerate(data):
		for j, char in enumerate(line):
			if char == 1:
				first_pos = (i, j)
				break
		if first_pos:
			break

	pos = first_pos
	movements = [((0, 1), "D"), ((0, -1), "I"), ((1, 0), "B"), ((-1, 0), "A")]
	while data[pos[0]][pos[1]] != 2:
		for movement, direction in movements:
			new_pos = (pos[0] + movement[0], pos[1] + movement[1])
			if (
				new_pos[0] >= 0
				and new_pos[1] >= 0
				and new_pos[0] < len(data)
				and new_pos[1] < len(data[0])
				and (
					data[new_pos[0]][new_pos[1]] == 0
					or data[new_pos[0]][new_pos[1]] == 2
				)
			):
				data[pos[0]][pos[1]] = -1
				pos = new_pos
				out += direction
				break
	with open(Path(__file__).parent / "output.txt", "w") as file:
		file.write(out)


if __name__ == "__main__":
	main()
