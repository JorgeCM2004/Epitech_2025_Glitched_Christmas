from pathlib import Path

from exif import Image

IMAGE_NAME = "challenge5.jpg"


def main():
	image = Image(Path(__file__).parent / IMAGE_NAME)

	with open(Path(__file__).parent / "output.txt", "w") as file:
		file.write(image.get("camera_owner_name"))


if __name__ == "__main__":
	main()
