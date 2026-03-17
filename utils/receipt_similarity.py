from difflib import SequenceMatcher

def text_similarity(text1, text2):
    if not text1 or not text2:
        return 0

    text1 = text1.lower().strip()
    text2 = text2.lower().strip()

    similarity = SequenceMatcher(None, text1, text2).ratio()
    return similarity