from pathlib import Path


def main():
	with open(Path(__file__).parent / "input.txt", "r") as file:
		out = "".join(
			map(chr, map(lambda x: int(x, 2), file.read().strip().split(" ")))
		)

	with open(Path(__file__).parent / "output.txt", "w") as file:
		file.write(out)


if __name__ == "__main__":
	main()
