import requests
from lxml import html


def main():
    url = ""
    payload = {"topic": "t"}
    r = requests.get(url, params=payload)
    root = html.fromstring(r.content)
    texts = root.xpath('//*[@id="kashi_area"]/text()')
    texts = [text.replace("\u3000", " ") for text in texts]
    print(texts)
    with open("text/out.txt", "w") as f:
        f.write("\n".join(texts))


if __name__ == "__main__":
    main()
