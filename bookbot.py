import sys

def main():
    if len(sys.argv) < 2: 
        print("No File Attached")
        return
    elif len(sys.argv) > 2:
        print("One File at a Time")
        return

    file_path = sys.argv[1]
    characters = {}
    words = 0
    total_char = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                words += len(line.split())
                for char in line.lower():
                    if char.isalpha():
                        total_char += 1
                        if characters.get(char):
                            characters[char] += 1
                        else:
                            characters[char] = 1
        characters_sorted = dict(sorted(characters.items(), key=lambda item: item[1], reverse=True))
        print_output(file_path, words, characters_sorted, total_char)
    except:
        print("Not a Valid Text File")


def print_output(file_path: str, words: int, characters: dict, total_char: int):
    print("==================== BOOKBOT ====================")
    print(f"Analyzing book found at {file_path}...")
    print("------------------- Word Count -------------------")
    print(f"Found {words} total words")
    print("---------------- Character Count ----------------")
    for char in characters:
        print(f"{char}: {str(characters[char])} ({round(characters[char]/total_char * 100, 2)}%)")
    print("==================== END ====================")

if __name__ == "__main__":
    main()
