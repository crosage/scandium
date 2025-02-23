import jieba


def is_valid_sentence(sentence):
    words = jieba.cut(sentence)
    valid_word_count = 0
    total_word_count = 0

    for word in words:
        total_word_count += 1
        if len(word) > 1 and all('\u4e00' <= char <= '\u9fff' for char in word):
            valid_word_count += 1

    if total_word_count == 0:
        return 0
    return valid_word_count / total_word_count


def test_encoding(text: str) -> None:
    encodings = [
        'utf-8', 'gbk', 'big5', 'latin1', 'utf-16', 'utf-32', 'GB2312',
        'ascii', 'ISO-8859-1', 'ISO-8859-2', 'ISO-8859-3', 'ISO-8859-5', 'ISO-8859-15',
        'windows-1252', 'windows-1251', 'windows-1250', 'shift-jis', 'euc-jp', 'euc-kr',
        'macroman', 'hz', 'koi8-r'
    ]
    print("Attempting to decode text with various encodings...\n")

    best_validity = 0
    best_decoded_text = ""
    best_encoding = ""
    origin_encoder = ""
    for encode_method in encodings:
        try:

            text_bytes = text.encode(encode_method, errors='ignore')
            for decode_method in encodings:
                try:
                    decoded_text = text_bytes.decode(decode_method, errors='replace')
                    score = is_valid_sentence(decoded_text)
                    # print(f"编码方式为{encode_method} 解码方式为{decode_method} 分数为{score} 解码文本{decoded_text}")
                    if score > best_validity:
                        best_validity = score
                        best_decoded_text = decoded_text
                        origin_encoder = encode_method
                        best_encoding = decode_method
                except UnicodeDecodeError as e:
                    continue
        except UnicodeEncodeError as e:
            continue

    print("\nBest decoding result:")
    if best_validity > 0:
        print(f"原本编码方式 {origin_encoder}")
        print(f"应使用编码方式: {best_encoding}")
        print(f"解码内容: {best_decoded_text}")
    else:
        print("No valid decoded text found.")


text_with_garbage = '濡傛灉鏈夋晥璇嶆眹鐨勬暟閲� / 鎬昏瘝姹囨暟閲忓ぇ浜庢煇涓槇鍊硷紝璁や负鏄湁鏁堝彞瀛�'

test_encoding(text_with_garbage)
