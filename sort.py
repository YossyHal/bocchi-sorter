"""ネガポジのスコアが低い順に曲をソートする
"""
from pathlib import Path

import oseti
import pandas as pd


def main():
    p = Path("text")
    df = pd.DataFrame(columns=["曲名", "score", "positive_words", "negative_words"])
    for path in p.glob("*.txt"):
        score, positive_words, negative_words = get_lyric_score(path)
        df = df._append(
            {
                "曲名": path.stem,
                "score": score,
                "positive_words": positive_words,
                "negative_words": negative_words,
            },
            ignore_index=True,
        )
    df = df.sort_values("score")
    df["score"] = df["score"].round(1)
    df.index = range(1, len(df) + 1)
    print(df)
    df.to_csv("result.csv", encoding="sjis", errors="ignore")


def get_lyric_score(path):
    with open(path, "r") as f:
        lyric = f.read()
        analyzer = oseti.Analyzer()
        results = analyzer.analyze_detail(lyric)

        total_score = 0
        positive_words = []
        negative_words = []
        for result in results:
            score = result["score"]
            total_score += score
            if score > 0.5:
                positive_words.append(result["positive"])
            elif score < -0.5:
                negative_words.append(result["negative"])

        positive_words_str = ""
        if len(positive_words) > 0:
            positive_words = [item for sublist in positive_words for item in sublist]
            positive_words = [word for word in positive_words if "-" not in word]
            positive_words_str = ",".join(positive_words)
        negative_words_str = ""

        if len(negative_words) > 0:
            negative_words = [item for sublist in negative_words for item in sublist]
            negative_words = [word for word in negative_words if "-" not in word]
            negative_words_str = ",".join(negative_words)

        return total_score, positive_words_str, negative_words_str


if __name__ == "__main__":
    main()
