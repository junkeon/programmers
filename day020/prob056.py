def solution(phone_book):
    N=len(phone_book)
    phone_book.sort()
    for word1, word2 in zip(phone_book, phone_book[1:]):
            if word2.startswith(word1):
                return False            
    return True