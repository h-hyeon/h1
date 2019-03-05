from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split()
    word_dictionary = {}

    for word in words:
        if word in word_dictionary:
            # increase
            word_dictionary[word]+=1
        else:
            # add to dictionary
            word_dictionary[word]=1

    return render(request, 'result.html', {'full' : text, 'total' : len(words), 'dictionary': word_dictionary.items()})

    # render 는 세개의 인자를 받을 수 있다. 
    # 첫번째 인자는 request, 두번째 인자는 html을 세번째 인자는 딕셔내리(사전) 형 변수를 받을 수 있다.사전) 형 변수를 받을 수 있다.