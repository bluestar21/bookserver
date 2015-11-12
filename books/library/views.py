from library.models import Author
from library.models import Book
from django.template import Context
from django.shortcuts import render_to_response

def searchbook(request):
    if 'search' in request.GET and request.GET['search']:        
        q = request.GET['search']
        m = list(Author.objects.filter(Name=q))
        if m != []:
            p = Author.objects.filter(Name=q)[0]
            searchlist = p.book_set.all()
            if list(searchlist) != []:
                e = Context({"searchlist":searchlist})
                return render_to_response("searchbook.html",e)
            else:
                return render_to_response("searcherror.html")
        else:
            return render_to_response("searcherror.html")
    else:
        return render_to_response("searcherror.html")
def book(request):
    book_list = Book.objects.all()
    c = Context({"book_list":book_list,})
    return render_to_response("booklist.html", c)
def delete(request):
    ID = request.GET['id']
    Book.objects.get(id=ID).delete()
    return render_to_response("delete.html")
def theirbook(request):
    ID = request.GET['id']
    itsdetails ={Book.objects.get(id=ID)}
    return render_to_response("theirbook.html",
                              Context({"itsdetails":itsdetails}))
def add(request):
    if request.POST and request.POST['Name'] and request.POST['Title'] and request.POST['ISBN_PK'] and request.POST['AuthorID_FK']:
        post = request.POST
        new_author=Author(
            AuthorID_FK = post['AuthorID_FK'],
            Name = post['Name'],
            Age = post['Age'],
            Country = post['Country'],
            )
        tmp = list(Author.objects.filter(Name=post['Name']))
        tmp0 = list(Author.objects.filter(AuthorID_FK=post['AuthorID_FK']))
        if tmp0 != []:
            return render_to_response("addauerror.html")
        else:
            if tmp == [] :
                new_author.save()
            else:
                new_author=Author.objects.filter(Name=post['Name'])[0]
        new_book = Book(
            ISBN_PK = post["ISBN_PK"],
            Title = post["Title"],
            AuthorID_FK = new_author,
            Publisher = post["Publisher"],
            PublishDate = post["PublishDate"],   
            Price = post["Price"],
            )
        tmp1 = list(Book.objects.filter(ISBN_PK=post['ISBN_PK']))
        if tmp1!=[]:
            return render_to_response("addboerror.html")
        else:
            new_book.save()
        return render_to_response("addbosuccess.html")
    else:
        return render_to_response("addboerror1.html")
def update(request):
    ID = request.GET['id']
    book_list = Book.objects.filter(id = ID)
    d = Context({"book_list":book_list})
    if request.POST :
        post = request.POST
        temp = list(Author.objects.filter(Name=post['Name']))
        if temp != [] :
            new_author=Author.objects.filter(Name=post['Name'])[0]
        else:
            return render_to_response("authoradd.html")
        book_list.update(ISBN_PK = post["ISBN_PK"])
        book_list.update(Title = post["Title"])
        book_list.update(AuthorID_FK = new_author)
        book_list.update(Publisher = post["Publisher"])
        book_list.update(PublishDate = post["PublishDate"])
        book_list.update(Price = post["Price"])
        return render_to_response("updatesuccess.html")
    return render_to_response("update.html",d)
def addauthor(request):
    if request.POST and request.POST['Name'] and request.POST['AuthorID_FK']:
        post = request.POST
        new_author=Author(
            AuthorID_FK = post['AuthorID_FK'],
            Name = post['Name'],
            Age = post['Age'],
            Country = post['Country'],
            )
        tmp2 = list(Author.objects.filter(AuthorID_FK=post['AuthorID_FK']))
        if tmp2!=[]:
            return render_to_response("addauerror.html")
        else:
            new_author.save()
        return render_to_response("addausuccess.html")
    else:
        return render_to_response("addauerror1.html")
def form(request):
    return render_to_response("form.html")