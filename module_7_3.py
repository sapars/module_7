separators = [',', '.', '=', '!', '?', ';', ':', ' - ']


def split_by_separators(string: str, *separators) -> list[str]:
    for sep in separators:
        string = string.replace(sep, ' ')
    return string.split()


class WordsFinder:

    def __init__(self, *file_names) -> None:
        self.file_names = file_names


    def get_all_words(self) -> None:
        all_words = {}
        for f_name in self.file_names:
            words: list(str) = []
            with open(f_name, 'r', encoding='utf-8') as f:
                for line in f:
                    words.extend(split_by_separators(line.lower(), *separators))
        all_words[f_name] = words
        return all_words

    def find(self, word: str):
        return {k: v.index(word.lower())+1 for k, v in self.get_all_words().items() if word.lower() in v}

    def count(self, word: str):
        return {k: v.count(word.lower()) for k, v in self.get_all_words().items() if word.lower() in v}


finder1 = WordsFinder('Rudyard Kipling - If.txt',)
print(finder1.get_all_words())
print(finder1.find('if'))
print(finder1.count('if'))
