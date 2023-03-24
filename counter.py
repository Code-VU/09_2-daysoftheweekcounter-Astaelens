def countDayOfTheWeek():
    # This first line is provided for you
    file_name = input("Enter a file name: ")

    counter=dict()
    fhand= open(file_name)
    for line in fhand:
        if line.startswith('From '):
            word=line.split()
            #print(word)
            counter[word[2]]=counter.get(word[2],0)+1

    print(counter)

## if you want to test locally run > python payCalculator.py
if __name__ == "__main__":
    countDayOfTheWeek()
