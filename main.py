import requests

st_accept = "text/html"

server = "https://vk.com/deceasedep"

st_useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"

headers = {
   "Accept": st_accept,
   "User-Agent": st_useragent
}

req = requests.get(server, headers)

src = req.text

print(src.find("Р"))

print(src[0:][:1000])
