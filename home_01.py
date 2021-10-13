import requests
import bs4

KEYWORDS = ['дизайн', 'фото', 'Web', 'Python',
            'C#', 'JavaScript', 'PHP', 'PostgreSQL', 'Django']
page = 1

# print(KEYWORDS.index('дизайн'))
response = requests.get(f'https://habr.com/ru/all/page{page}')
response.raise_for_status()

soup = bs4.BeautifulSoup(response.text, features='html.parser')

articles = soup.find_all('article')

for article in articles:
    text_prev = article.find(class_='tm-article-body').text.strip()

    for key in KEYWORDS:
        if KEYWORDS[KEYWORDS.index(key)] in text_prev:
            time = article.find(class_="tm-article-snippet__datetime-published").find("time").get("title")
            href = article.find(class_='tm-article-snippet__title-link').attrs['href']
            link = 'https://habr.com' + href
            print(time, '-', article.find('h2').text, '-', link, f'Ключевое слово: {key}')


# Я вынес time по типу title, но можно было и по text
# Плюс добавил ключевых слов для проверки (интересные для меня темы), и переменную page, для выбора страниц (вручную).
# Дописал в конце по какому ключу происходит поиск, для понимания что ключи перебираются правильно
