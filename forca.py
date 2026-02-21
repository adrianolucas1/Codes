import random


def hangman():
    words = [
        "python",
        "programacao",
        "desenvolvimento",
        "jogo",
        "forca",
        "computador",
    ]
    word = random.choice(words).lower()
    guessed = set()
    attempts = 6
    hangman_stages = [
        """
          +---+
          |   |
              |
              |
              |
              |
        =========""",
        """
          +---+
          |   |
          O   |
              |
              |
              |
        =========""",
        """
          +---+
          |   |
          O   |
          |   |
              |
              |
        =========""",
        """
          +---+
          |   |
          O   |
         /|   |
              |
              |
        =========""",
        """
          +---+
          |   |
          O   |
         /|\  |
              |
              |
        =========""",
        """
          +---+
          |   |
          O   |
         /|\  |
         /    |
              |
        =========""",
        """
          +---+
          |   |
          O   |
         /|\  |
         / \  |
              |
        =========""",
    ]

    print("Bem-vindo ao Jogo da Forca!")
    while attempts > 0:
        display = " ".join([c if c in guessed else "_" for c in word])
        print("\nPalavra: ", display)
        if "_" not in display:
            print("Parabéns! Você acertou a palavra:", word)
            break
        print(f"Tentativas restantes: {attempts}")
        guess = input("Digite uma letra: ").strip().lower()
        if not guess or len(guess) != 1 or not guess.isalpha():
            print("Entrada inválida, digite apenas uma letra.")
            continue
        if guess in guessed:
            print("Você já tentou essa letra.")
            continue
        guessed.add(guess)
        if guess not in word:
            attempts -= 1
            print("Letra não está na palavra.")
        print(hangman_stages[6 - attempts])
    else:
        print("\nVocê perdeu! A palavra era:", word)


if __name__ == "__main__":
    hangman()
