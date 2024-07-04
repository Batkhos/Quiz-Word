import random
words = [
      {"spanish": "el", "english": "the"},
      {"spanish": "de", "english": "of"},
      {"spanish": "que", "english": "that"},
      {"spanish": "y", "english": "and"},
      {"spanish": "a", "english": "to"},
      {"spanish": "en", "english": "in"},
      {"spanish": "un", "english": "an"},
      {"spanish": "ser", "english": "to be"},
      {"spanish": "se", "english": "oneself"},
      {"spanish":"no", "english": "not"},
      {"spanish": "haber", "english": "to have"},
      {"spanish": "por", "english": "for"},
      {"spanish": "con", "english": "with"},
      {"spanish": "su", "english": "his"},
      {"spanish": "para", "english": "for"},
      {"spanish": "como", "english": "like"},
      {"spanish": "estar", "english": "to be"},
      {"spanish": "tener", "english": "to have"},
      {"spanish": "le", "english": "him"},
      {"spanish": "lo", "english": "it"},
]

def quiz(words):
    random.shuffle(words)
    score = 0
    for x in words:
        print(f'translatebthis word{x["spanish"]}')
        answer = input('its translation in english is : ')
        correct_answer = x['english'].lower()
        if answer == correct_answer:
            score += 1
            print("goood job that' s right!!!")
        else:
            print('wronnnnnng!!')
    print(f'you got {score}/{len(words)}')
quiz(words)