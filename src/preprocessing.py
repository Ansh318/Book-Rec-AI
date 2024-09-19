import pandas as pd

df = pd.read_csv("/Users/anshagarwal/GitHub /Virtual Library/Book-Rec-AI/data/Books.csv")
df = df[['ISBN', 'Book-Title', 'Book-Author', 'Year-Of-Publication', 'Publisher']]


empty_list = []
for index, row in df.iterrows():
    book_title = row['Book-Title']
    book_author = row['Book-Author']
    publisher = row['Publisher']
    year_of_publishement = row['Year-Of-Publication']
    isbn = row['ISBN']

    template = f"The Book named {book_title} who's author is {book_author} was published by {publisher} in {year_of_publishement} having ISBN no. {isbn}"
    empty_list.append(template)



with open("/Users/anshagarwal/GitHub /Virtual Library/Book-Rec-AI/data/books.txt", 'w') as file:
    for desc in empty_list:
        file.write(desc + '\n')
    