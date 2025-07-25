def main():
    phrase = input("Write something: ").strip().lower()
    
    counter = {}
    for el in phrase:
        if el not in counter:
            counter[el] = phrase.count(el)
            
    print(counter)

if __name__ == "__main__":
    main()