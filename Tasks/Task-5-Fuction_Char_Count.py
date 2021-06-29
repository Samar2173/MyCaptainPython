def most_frequent(word):
    word = word.lower()
    freq = {}
    for i in word:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    
    sort_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    for i in sort_freq:
        print(f'{i[0]} = {i[1]}', end = ' ')

most_frequent(input("Enter String: "))