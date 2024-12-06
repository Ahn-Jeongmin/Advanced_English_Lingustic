# This is a code for a data preprocession for the network analysis using gephi toolkit

import nltk
from nltk.corpus import stopwords 
from collections import Counter
import itertools
import pandas as pd


#definition of the function for creating combinations

def make_combination(textinput):
    # 1. tokenization -> word
    tokens = nltk.word_tokenize(textinput)

    # 2. 품사 태깅
    tagged_tokens = nltk.pos_tag(tokens)  # [('word', 'POS'), ...]

    # 3. 유의미한 품사 필터링 (명사, 형용사, 동사)
    valid_pos = {'NN', 'NNS', 'NNP', 'NNPS', 'JJ', 'JJR', 'JJS'}
    filtered_tokens = [(word.lower(), pos) for word, pos in tagged_tokens if pos in valid_pos]

    # 4. 불용어 제거
    stop_words = set(stopwords.words('english')) | {'be', 'is', 'are', 'was', 'were', 'been', 'being', "'re", "'s", "'ve"}
    filtered_tokens = [(word, pos) for word, pos in filtered_tokens if word not in stop_words]

    # 5. 단어가 2개 미만인 경우 빈 DataFrame 반환
    if len(filtered_tokens) < 2:
        return pd.DataFrame(columns=['source', 'target', 'weight'])

    # 6. 단어 쌍 생성 및 필터링
    word_pairs = list(itertools.combinations(filtered_tokens, 2))
    filtered_pairs = []
    for (word1, pos1), (word2, pos2) in word_pairs:
        if word1 == word2:  # 동일 노드 제거
            continue
        if (pos1.startswith('NN') and pos2.startswith('NN')) or (pos1.startswith('JJ') and pos2.startswith('JJ')):
            continue  # 둘 다 명사 또는 둘 다 형용사 제거
        filtered_pairs.append((word1, word2))

    # 7. DataFrame 생성 전 필터링
    if not filtered_pairs:  # 유효한 쌍이 없으면 빈 DataFrame 반환
        return pd.DataFrame(columns=['source', 'target', 'weight'])

    # 8. 조합 빈도 계산
    pair_counts = Counter(filtered_pairs)

    # 9. DataFrame으로 변환
    try:
        df_edges = pd.DataFrame(pair_counts.items(), columns=['pair', 'weight'])
        df_edges[['source', 'target']] = pd.DataFrame(df_edges['pair'].tolist(), index=df_edges.index)
        df_edges = df_edges[['source', 'target', 'weight']]
    except Exception as e:
        print(f"Error while creating DataFrame: {e}")
        return pd.DataFrame(columns=['source', 'target', 'weight'])

    return df_edges



# 2.load csv file
file_path = 'CCF9_10_utf8.csv'
data = pd.read_csv(file_path, encoding = 'utf-8')

all_dataframes = []
sentcount = 0 #분석에 사용된 총 문장 개수 변수

# 반복문으로 각 text 열 데이터 처리
for rawtext in data['text']:
    tmp = nltk.sent_tokenize(rawtext)  # 문장을 분리
    sentcount+=len(tmp) #문장 수 업데이트
    for sent_text in tmp:
        if not sent_text.strip():  # 빈 문자열 체크
            continue
        dfdata = make_combination(sent_text)  # 문장 단위로 조합 생성
        if not dfdata.empty:  # 빈 DataFrame 무시
            all_dataframes.append(dfdata)

if all_dataframes:
    # 모든 데이터프레임 합치기
    combined_df = pd.concat(all_dataframes, ignore_index=True)

    # 횟수(weight) 기준 내림차순 정렬
    sorted_df = combined_df.sort_values(by='weight', ascending=False)

    # 정렬 결과 출력
    print(sorted_df.head(50))

    # 정렬된 데이터 저장 (선택 사항)
    sorted_df.to_csv('sorted_network.csv', index=False, encoding='utf-8')
    print("Sorted network data saved to 'sorted_network.csv'")
else:
    print("No valid data to combine.")

print()
print(sentcount)







