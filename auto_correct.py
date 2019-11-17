from spellchecker import SpellChecker

spell = SpellChecker()


def fix_sentence(sentence):
    words = sentence.split(' ')

    for i, word in enumerate(words):
        words[i] = spell.correction(word)

    return ' '.join(words)
