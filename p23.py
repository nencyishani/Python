#frequency of the words from the input
#name :Nency ishani ,enroolment:92400527179

text = "Hello There this is Python. Python is good"

text = text.replace(".","").replace(",","")
words = text.split()

freq = {}

for word in words:
    word = word.capitalize()
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

for word in sorted(freq):
    print(word, ":", freq[word])
