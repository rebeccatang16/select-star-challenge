from django.db import models

# Create your models here.

class Prefix(models.Model):
    name = models.CharField(max_length=128)
    # def __init__(self, prefix, word_strings=[]):
    #     self.name = prefix
    #     self.words = []
    #     self.add_words(word_strings)

    # def add_word(self, word):
    #     # word can be string or Word
    #     if isinstance(word, Word):
    #         self.words.append(word)
    #     elif isinstance(word, str):
    #         self.words.append(Word(word, self))

    # def add_words(self, word_strings):
    #     for word_string in word_strings:
    #         self.add_word(word_string)

    # def remove_word(self, word):
    #     # word can be string or Word
    #     self.words.remove(word)

    # def create_all_from_dict(data):
    #     # Class method for mass generating Prefix instances
    #     # from JSON data in dict form
    #     prefixes = []
    #     for prefix_name in data:
    #         prefixes.append(Prefix(prefix_name, data[prefix_name]))
    #     return prefixes


class Word(models.Model):
    word = models.CharField(max_length=128)
    prefix = models.ForeignKey(Prefix, on_delete=models.CASCADE)

    def __eq__(self, other):
        if isinstance(other, Word):
            return self.word == other.word
        elif isinstance(other, str):
            return self.word == other
