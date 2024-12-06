import nltk
from collections import Counter
from myfunctions import findtags
import matplotlib.pyplot as plt

#데이터
filelist = [
    "(1-2) Charlie and the Chocolate Factory.txt",
    "(9-10) Charlie and the Chocolate Factory.txt",
    "(1-2) Willy Wonka & the Chocolate Factory.txt",
    "(9-10) Willy Wonka & the Chocolate Factory.txt"
]

#시각화 그래프 색상
colorlist = ['#A8D5BA', '#8FC1A9', '#74A390', '#5E8C71']
coloridx = 0

for filepath in filelist:
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            text = file.read()

        tokens = nltk.word_tokenize(text)

        pos_tags = nltk.pos_tag(tokens)

        jj_tags = findtags('JJ', pos_tags)
        jjr_tags = findtags('JJR', pos_tags)
        jjs_tags = findtags('JJS', pos_tags)

        #태그 일단 다 통합
        all_adjectives = []
        for tag_dict in [jj_tags, jjr_tags, jjs_tags]:
            for word_list in tag_dict.values():
                all_adjectives.extend(word_list)

        combined_adjectives = Counter(dict(all_adjectives))

        #빈도수 상위 10개 형용사 추출해서 저장
        most_common_adjectives = combined_adjectives.most_common(10)

        print(f"\nTop adjectives in {filepath}:")
        for word, freq in most_common_adjectives:
            print(f"{word}: {freq}")

        if most_common_adjectives:
            words, frequencies = zip(*most_common_adjectives)
            plt.figure(figsize=(10, 6))
            plt.bar(words, frequencies, color = colorlist[coloridx])
            plt.title(f"Top 10 Adjectives in {filepath}")
            plt.xlabel("Adjectives")
            plt.ylabel("Frequency")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        
        #그래프 색상 변경 인덱스 조정
        coloridx+=1

    except FileNotFoundError:
        print(f"File {filepath} not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred while processing {filepath}: {e}")
