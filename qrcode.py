import pyqrcode

s = "https://forms.gle/zq1KgWBArZZuMnfe8"
url = pyqrcode.create(s)

url.svg("mysqr.svg", scale=8)
url.png("myqr.png")
