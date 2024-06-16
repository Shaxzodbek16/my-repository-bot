from readAPI import information


def shaxzodbek(page: int, category: str = None):
	if category is None:
		return information(page, "shaxzodbek")
	return information(page, "shaxzodbek", category)


def people(page: int):
	return information(page, "person")


def wish(page: int):
	return information(page, "wish")


if __name__ == '__main__':
	a = wish(0)
	print(a["title"])
