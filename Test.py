from pyxdameraulevenshtein import damerau_levenshtein_distance as distance

# Đọc nội dung từ điển vào một danh sách
with open('vietnamese_dict.txt', encoding='utf-8') as f:
    word_list = f.read().splitlines()

# Kiểm tra chính tả và đưa ra các gợi ý sửa lỗi cho văn bản
def spell_check(text):
    # Phân tách các từ trong văn bản
    words = text.split()

    # Duyệt qua các từ và kiểm tra chính tả
    for word in words:
        # Nếu từ không đúng chính tả, đưa ra các gợi ý để sửa lỗi
        if word not in word_list:
            print(f"Found a spelling error: {word}")
            min_distance = float('inf')
            suggestions = []
            for w in word_list:
                if w.startswith(word[0]) and abs(len(w) - len(word)) <= 2:
                    d = distance(word, w)
                    if d < min_distance:
                        min_distance = d
                        suggestions = [w]
                    elif d == min_distance:
                        suggestions.append(w)
            if suggestions:
                print(f"Suggested corrections: {', '.join(suggestions)}")

# Văn bản có chứa các lỗi chính tả
text = 'Toi thich hpc tieng Viet. Toi rat thich hoc. Toi muon hoc them ve tieng Anh.'

# Kiểm tra chính tả và đưa ra các gợi ý sửa lỗi
spell_check(text)