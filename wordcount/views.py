from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html', {'hithere': 'This is python and anaconda combo'})


def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()
    text_len = len(fulltext)
    worddict = {}
    for word in wordlist:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1
    sorted_worddict = sorted(worddict.items(), key=operator.itemgetter(1))
    return render(request, 'count.html', {'fulltext': fulltext, 'wordict': sorted_worddict, 'wordlist': len(wordlist), 'textLen': text_len})
