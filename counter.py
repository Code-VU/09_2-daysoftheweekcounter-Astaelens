def countDayOfTheWeek():
    # This first line is provided for you
    file_name = input("Enter a file name: ")

    counter=dict()
    fhand= open(file_name)
    for line in fhand:
        if line.startswith('From '):
            word=line.split()
            #print(word)
            if word[2] not in counter:
                counter[word[2]]=1
            else:
                counter[word[2]]+=1

    print(counter)

## if you want to test locally run > python payCalculator.py
if __name__ == "__main__":
    countDayOfTheWeek()
