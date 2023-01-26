import os

def fileOpen(filePath):
    with open(os.path.join(os.path.abspath('./docs'), filePath), 'r') as f:
        lines = f.readlines()
    return lines


def main():
    lipsumFile = fileOpen("..\docs\lipsum.txt")
    while True:
        wordInput = input("Enter a word: ")
        wordFound = False
        if wordInput == "q":
            break
        for lineIndex in range(len(lipsumFile)):
            for columnIndex in range(len(lipsumFile[lineIndex].split("-"))):
                for word in lipsumFile[lineIndex].split("-")[columnIndex].split(" "):
                    if word == wordInput:
                        print(f"The word: {wordInput} it is located in row number {lineIndex+1} and in column {columnIndex+1}")
                        wordFound = True
            if lineIndex == len(lipsumFile)-1 and not wordFound:
                print("Word not found")



if __name__ == "__main__":
    main()
