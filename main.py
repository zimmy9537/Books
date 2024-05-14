from fastapi import Body, FastAPI

app = FastAPI()

Books = [
    {'title': 'The Da Vinci Code', 'author': 'Dan Brown', 'category': 'Mystery'},
    {'title': 'The Alchemist', 'author': 'Paulo Coelho', 'category': 'Adventure'},
    {'title': 'The Monk Who Sold His Ferrari', 'author': 'Robin Sharma', 'category': 'Self-help'},
    {'title': 'The psychology of money', 'author': 'Morgan Housel', 'category': 'Finance'},
    {'title': 'The Lean Startup', 'author': 'Eric Ries', 'category': 'Business'},
    {'title': 'The 4-Hour Workweek', 'author': 'Tim Ferriss', 'category': 'Self-help'},
    {'title': 'The Subtle Art of Not Giving a F*ck', 'author': 'Mark Manson', 'category': 'Self-help'},
    {'title': 'The 7 Habits of Highly Effective People', 'author': 'Stephen Covey', 'category': 'Self-help'},
    {'title': 'The ikigai', 'author': 'Héctor García', 'category': 'Self-help'},
]


@app.get('/books')
async def get_books():
    return Books


@app.get('/books/title/{title}')
async def get_books(title: str):
    books_to_return = []
    for book in Books:
        if book['title'] == title:
            books_to_return.append(book)
    return books_to_return


@app.get('/books/category/{category}')
async def get_books(category: str):
    books_to_return = []
    for book in Books:
        if book['category'] == category:
            books_to_return.append(book)
    return books_to_return


@app.get('/books/author/{author}')
async def get_books(author: str):
    books_to_return = []
    for book in Books:
        if book['author'] == author:
            books_to_return.append(book)
    return books_to_return
