import json
import requests


def information(pk: int, next_api: str, category: str = None) -> dict:
	if category is None:
		response = requests.get(f"http://127.0.0.1:8000/api/{next_api}")
		data = json.loads(response.text)
		try:
			return data[pk]
		except IndexError:
			return {"message": f"{pk} not found in {next_api}"}
	response = requests.get(f"http://127.0.0.1:8000/api/{next_api}/?category={category}")
	data = json.loads(response.text)
	try:
		return data[pk]
	except IndexError:
		return {"message": f"{pk} not found in {next_api}'s category"}


if __name__ == "__main__":
	pass
