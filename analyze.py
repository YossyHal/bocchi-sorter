import pprint
from pathlib import Path

import oseti


def main():
    p = Path("text")
    d = dict()
    for path in p.glob("*.txt"):
        score = get_lyric_score(path)
        d[path.stem] = score
    d = sorted(d.items(), key=lambda x: x[1])
    pprint.pprint(d)


def get_lyric_score(path):
    with open(path, "r") as f:
        lyric = f.read()
        analyzer = oseti.Analyzer()
        results = analyzer.analyze(lyric)
        # print(results)

        total_score = 0
        for result in results:
            total_score += result
        return total_score


if __name__ == "__main__":
    main()
