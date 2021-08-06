from collections import Counter
language = ['PHP', 'PHP', 'Python', 'PHP', 'Python', 'JS', 'Python', 'Python','PHP', 'Python']
print(language)

cnt = Counter(language).most_common()[0][0]
print(cnt)