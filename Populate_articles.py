import  os
import  django
from  faker import Faker
import  random


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crub_blog.settings')
django.setup()

from crud_blog_web.models import Article


def populate(N=100):
    fake = Faker()

    for _ in range(N):
        title = fake.sentence(nb_words=6)
        content = fake.text(max_nb_chars=2000)
        year = random.randint(1900, 2021)


        article = Article(title=title, content=content, year=year)
        article.save()


        if __name__ == '__main__':
            print('Populating the databases ... Please wait')
            populate(100)
            print('Populating complete')