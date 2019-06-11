from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split()
    word_dictionary = {}

    for word in words:
        if word in word_dictionary:
            #increase
            word_dictionary[word]+=1
        else:
            #add to dictionary
            word_dictionary[word]=1

    return render(request, 'result.html', {'full': text, 'total': len(words), 'dictionary' : word_dictionary.items()})