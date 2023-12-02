import oseti

with open('text/青春コンプレックス.txt', 'r') as f:
    lyric = f.read()
    print(lyric)

analyzer = oseti.Analyzer()
results  = analyzer.analyze(lyric)
print(results)

total_score = 0
for result in results:
    total_score += result
print(total_score)
