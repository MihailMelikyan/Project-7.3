class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names
        self.all_words = self.get_all_words()

    def get_all_words(self):
        all_words = {}# создаем пустой словарь
        punctuation_to_remove = [',', '.', '=', '!', '?', ';', ':', ' - ']

        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file: # Перебераем названия файлов и открываем файл
                    file_words = []
                    for line in file:
                        line = line.lower()#переводим в нижний регистр каждое слово
                        for punct in punctuation_to_remove:
                            line = line.replace(punct, '')
                        words = line.split()
                        file_words.extend(words)

                    all_words[file_name] = file_words

            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")

        return all_words

    def find(self, word):
        word = word.lower()
        found_positions = {}

        for file_name, words in self.all_words.items():
            if word in words:
                position = words.index(word)
                found_positions[file_name] = position

        return found_positions

    def count(self, word):
        word = word.lower()
        word_counts = {}

        for file_name, words in self.all_words.items():
            count = words.count(word)
            word_counts[file_name] = count

        return word_counts

finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
print(finder1.get_all_words())
print(finder1.find('Child'))
print(finder1.count('Child'))

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

