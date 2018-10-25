"""
Labour work #2
 Check spelling of words in the given  text
"""
from lab_1.main import calculate_frequences

LETTERS = 'abcdefghijklmnopqrstuvwxyz'
REFERENCE_TEXT = ''

if __name__ == '__main__':
    with open('very_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()
        freq_dict = calculate_frequences(REFERENCE_TEXT)


def propose_candidates(word: str, max_depth_permutations: int=1) -> list:
    set_candidates = set()
    alph = 'abcdefghijklmnopqrstuvwxyz'
    if max_depth_permutations is None or max_depth_permutations != 1:
        return []
    if word is None or word == '':
        return []
    for i in range(len(word)):
        candidate_1 = word[:i] + word[i+1:]
        set_candidates.add(candidate_1)
    for e in alph:
        for i in range(len(word)+1):
            candidate_2 = word[:i] + e + word[i:]
            set_candidates.add(candidate_2)
    for e in alph:
        for i in range(len(word)):
            candidate_3 = word[:i] + e + word[i+1:]
            set_candidates.add(candidate_3)
    for i in range(len(word)-1):
        candidate_4 = word[:i] + word[i+1] + word[i] + word[i+2:]
        set_candidates.add(candidate_4)
    candidates = list(set_candidates)
    return candidates


def keep_known(candidates: tuple, frequencies: dict) -> list:
    list_known = []
    if candidates is None:
        return []
    if frequencies is None:
        return []
    if type(candidates) != tuple:
        return []
    for i in candidates:
        if i in frequencies.keys():
            list_known.append(i)
    return list_known


def choose_best(frequencies: dict, candidates: tuple) -> str:
    higher_frequencies = []
    interval_dict = {}
    interval_list = []
    if candidates is None or candidates is tuple([]):
        return 'UNK'
    if frequencies is None or frequencies == dict():
        return 'UNK'
    for i in candidates:
        if i in frequencies:
            interval_dict[i] = frequencies[i]
    for key, value in interval_dict.items():
        higher_frequencies.append([value, key])
    higher_frequencies.sort(reverse=True)
    for i in higher_frequencies:
        if i[0] == higher_frequencies[0][0]:
            interval_list.append(i[1])
    interval_list.sort()
    best_word = interval_list[0]
    return best_word


def spell_check_word(frequencies: dict, as_is_words: tuple, word: str) -> str:
    if word is None:
        return 'UNK'
    if frequencies is None:
        return 'UNK'
    if as_is_words is not None:
        if word.upper() in as_is_words or word in frequencies:
            return word
    candidates = propose_candidates(word, 1)
    list_known = keep_known(tuple(candidates), frequencies)
    best_word = choose_best(frequencies, tuple(list_known))
    return best_word

