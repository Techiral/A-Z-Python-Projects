words = {
}

newWord = ""
newDefintion = ""
print("Welcome to a quizzing app! Let's start by adding words to our vocabulary, to start quizzing enter a new word with the name \"stop!\"")
while(newWord != "stop!"):
    newWord = input("What is the word?: ") 
    if newWord == "stop!": break
    newDefintion = input(f"What is the definition of {newWord}?: ")
    words[newWord] =  newDefintion


redo = []
score = 0


def checkWord(word, uInput):
    if(uInput.lower() == words.get(word).lower()): return 1
    elif(uInput == "skip" or uInput == None or uInput == ""): return 0
    else: return -1

print("welcome")



for word in words:
    userInput = input(f"What is the definition of {word}? (type skip to skip): ").lower()
    result = checkWord(word, userInput)
    match result:
        case -1:
            print(f"Wrong answer. The answer was: {words.get(word)}")
        case 0:
            print(f"Skipped! The answer was: {words.get(word)}")
            redo.append(word)
        case 1:
            score += 1
            print("correct +1")

if redo: 
    for skip in redo:
        userInput = input(f"What is the definition of {skip}?: ").lower()
        result = checkWord(skip, userInput)
        match result:
            case -1:
               print(f"Wrong answer. The answer was: {words.get(skip)}")
            case 0:
                print(f"Wrong answer. The answer was: {words.get(skip)}")
            case 1:
                score += 1
                print("correct +1")

print(f"Your score is: {score}/{len(words)}")

