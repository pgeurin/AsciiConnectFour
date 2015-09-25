from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


import random
import math
    
def wordCount( filename = None ):
    """ creates and prints the input list of words
    """
    
    text = ''
    if filename == None:
        print "Enter lots o' text. End with a plain '42' line."
        while True:
            nextline = raw_input()
            if nextline == '42': break
            text += nextline + ' '
            
    else:
        f = file( filename, 'r' )  # open a file for 'r'eading
        text = f.read()

    # text is a bunch of space-separated words

    list_of_words = text.split()  # split splits a string
    print "The list of words is", list_of_words
    num_words = len( list_of_words )
    print "There are", num_words, "words."




    

def vocabCount( filename = None ):
    """ creates and returns a dictionary of distinct words """
    
    text = ''
    if filename == None:
        print "Enter lots o' text. End with a plain '42' line."
        while True:
            nextline = raw_input()
            if nextline == '42': break
            text += nextline + ' '
            
    else:
        f = file( filename, 'r' )  # open a file for 'r'eading
        text = f.read()

    # text is a bunch of space-separated words

    list_of_words = text.split()  # split splits a string
    #print "The list of words is", list_of_words
    num_words = len( list_of_words )
    print "There are", num_words, "words."

    D = {}  # an empty dictionary

    for w in list_of_words:
        
        #"""
        for punc in ".,`'\"~!@#$%^&*();:<>|\\/?}{][_+=":
            w = w.replace( punc, '' )
            w = w.lower() # lower-case
        #"""
        
        if D.has_key( w ) == False:  # w was not there!
            D[w] = 1
            
        else: # d.has_key( w ) == True,  so w IS already there!
            D[w] += 1

    num_distinct_words = len( D )
    print "There are", num_distinct_words, "distinct words."

    RevItems = [ x[::-1] for x in D.items() ]
    RevItems.sort()
    RevItems = RevItems[::-1]
    counter = 40
    for item in RevItems:
        if counter < 1: break
        counter -= 1
        print item[1], "\t\t-->", item[0], "times"

    if len(D) < 20:
        return D
    else:
        return  # avoids returning too large a dictionary

def createDictionary( filename=None ):
    """ creates and returns a dictionary of distinct words """
    
    text = ''
    if filename == None:
        print "Enter lots o' text. End with a plain '42' line."
        while True:
            nextline = raw_input()
            if nextline == '42': break
            text += nextline + ' '
            
    else:
        f = file( filename, 'r' )  # open a file for 'r'eading
        text = f.read()

    # text is a bunch of space-separated words

    list_of_words = text.split()  # split splits a string
    num_words = len( list_of_words )
    D = {}  # an empty dictionary
    """
    for w in range(len(list_of_words)):
        
        for punc in ".,`'\"~!@#$%^&*();:<>|\\/?}{][_+=":
            list_of_words[w] = list_of_words[w].replace( punc, '' )
            list_of_words[w] = list_of_words[w].lower() # lower-case
    """
    D['$']=[list_of_words[0]]
    for w in range(len(list_of_words)-1):
        if (punk(list_of_words[w]) in D) == False:  # w was not there!
            D[punk(list_of_words[w])] = [list_of_words[w+1]]
            
        else: # d.has_key( w ) == True,  so w IS already there!
            D[punk(list_of_words[w])] += [list_of_words[w+1]]

                #THIS IS WHEN YOU FIND THE END OF SENTENCES---ANYTHING WITH A punctuation in the word

    num_distinct_words = len( D )

    RevItems = [ x[::-1] for x in D.items() ]
    RevItems.sort()
    RevItems = RevItems[::-1]
    counter = 40
    return D

    """
    for item in RevItems:
        if counter < 1: break
        counter -= 1
        print item[1], "\t\t-->", item[0], "times"
    """
    """
    if len(D) < 20:
        return D
    else:
        return  # avoids returning too large a dictionary
    """

def createDictionaryFromString( text ):
    """ creates and returns a dictionary of distinct words """
    list_of_words = text.split()  # split splits a string
    num_words = len( list_of_words )
    D = {}  # an empty dictionary
    """
    for w in range(len(list_of_words)):
        
        for punc in ".,`'\"~!@#$%^&*();:<>|\\/?}{][_+=":
            list_of_words[w] = list_of_words[w].replace( punc, '' )
            list_of_words[w] = list_of_words[w].lower() # lower-case
    """
	
    D['$']=[list_of_words[0]]
    for w in range(len(list_of_words)-1):
        if (punk(list_of_words[w]) in D) == False:  # w was not there!
            D[punk(list_of_words[w])] = [list_of_words[w+1]]
            
        else: # d.has_key( w ) == True,  so w IS already there!
            D[punk(list_of_words[w])] += [list_of_words[w+1]]

                #THIS IS WHEN YOU FIND THE END OF SENTENCES---ANYTHING WITH A punctuation in the word

    num_distinct_words = len( D )

    RevItems = [ x[::-1] for x in D.items() ]
    RevItems.sort()
    RevItems = RevItems[::-1]
    counter = 40
    return D

    """
    for item in RevItems:
        if counter < 1: break
        counter -= 1
        print item[1], "\t\t-->", item[0], "times"
    """
    """
    if len(D) < 20:
        return D
    else:
        return  # avoids returning too large a dictionary
    """

	
def punk(mystring):
    """takes a string input, then outputs '$' if there is a '?','.', or
'!' in the string and outputs the origional string if not. """
    if ('!') in mystring:
        return '$'
    elif ('.') in mystring:
        return '$'
    elif ('?') in mystring:
        return '$'
    else:
        return mystring

def generateText( D, n ):
    """take in a dictionary or word transitions d (generated in your
createDictionary function, above) and a positive integer, n. Then,
generateText should print a string of n words"""
    choice=random.choice(D['$'])
    string=choice
    for count in range(n):
        choice=random.choice(D[punk(choice)])
        string=string+' '+choice
    return string

from django.template import RequestContext, loader

"""
def index(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        else:
            predictions = Prediction.objects.filter(name__icontains=q)
            return render_to_response('prediction/search_results.html',
                {'predictions': predictions, 'query': q})
    return render_to_response('prediction/search_results.html',{'errors': errors})
"""

def index(request):
	#take in the entry
	#if ('q' in request.GET) and request.GET['q'].strip():
    #    q = request.GET['q']
    #    q.string()
    if 'q' in request.GET and len(request.GET['q'].split())!=0:
        q = request.GET['q']
        if len(q.split())>50:
            poem = generateText( createDictionaryFromString( q ), 50)
        else:
            poem = generateText( createDictionaryFromString( q ), len(q.split())-1)
            poem =  poem + " (If there aren't any repeating words in your text, the only possible emulation IS the the text you entered. Might we suggest adding a PILE of text instead of testing us?)"
    else: #this is just to make sure any input works
        poem = "Insert Text above!"
        q= ""
	#process a poem
	#d = createDictionary( 'shakespeare.txt' ) #(later change shakespeare to their entry above!)
    #poem = generateText( d, 50)
    #poem = generateText( createDictionary( 'shakespeare.txt' ), 50)
    template = loader.get_template('emulate/home.html')
    context = RequestContext(request, {
        'poem': poem, #I need to access poem in there! will this do it?
		'q': q, 
    })
    return HttpResponse(template.render(context)) 
	
"""
def index(request):
	#take in the entry
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        entry_query = get_query(query_string, ['title', 'body',])        
        found_entries = Entry.objects.filter(entry_query).order_by('-pub_date')

	#process a poem
	#d = createDictionary( 'shakespeare.txt' ) #(later change shakespeare to their entry above!)
    #poem = generateText( d, 50)
    poem = generateText( createDictionary( 'shakespeare.txt' ), 50)
	
    template = loader.get_template('emulate/home.html')
    context = RequestContext(request, {
        'poem': poem, #I need to access poem in there! will this do it?
		'query_string': query_string, 
		'found_entries': found_entries,
    })
    return HttpResponse(template.render(context)) 
"""