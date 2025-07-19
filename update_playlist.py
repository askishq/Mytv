import requests

def fetch_latest_playlist():
    url = "https://iptv-org.github.io/iptv/countries/bd.m3u"  # আপনার সোর্স লিংক
    response = requests.get(url)
    if response.status_code == 200:
        with open("playlist.m3u", "w", encoding="utf-8") as f:
            f.write(response.text)
        print("Playlist updated successfully.")
    else:
        print("Failed to fetch playlist")

if __name__ == "__main__":
    fetch_latest_playlist()
  
