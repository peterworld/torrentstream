import requests

movie_name=input("Enter the name of the movie\n")
base_url=f"https://api/sumanjay.cf/torrent?query=(movie_name)"
torrent_results=request.get(base_url).json()
for result in torrent_result:
if 'movie' in result['type'].lower():
print(result['name'])
print(result['size'])
print(result['magnet'])
break
