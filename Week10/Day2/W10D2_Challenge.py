import translators as ts
french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
for word in french_words:
    print(word, ts.google(word), sep=': ')

