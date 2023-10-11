url = input("сайт: ")
res = reversed(url.split('.'))
[print(domain) for domain in res]