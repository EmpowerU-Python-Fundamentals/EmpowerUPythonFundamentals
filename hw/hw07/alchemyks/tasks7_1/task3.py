

def calc_num_cha(word: str):
    out_dict = dict()
    lower_word = word.lower()
    for cha in lower_word:
        if not cha in out_dict:
            out_dict[cha] = lower_word.count(cha)
    return out_dict



