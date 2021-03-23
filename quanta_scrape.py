from graphql import GraphqlClient
from print_to_pdf import print_to_pdf
import json
import sys

SPECIAL_CHARS = ['\\', '/', ':', '?', '*', '<', '>', '|']
CHROMEDRIVER_PATH = 'chromedriver.exe'


def articles_to_pdf(filename):
    with open(filename) as f:
        data = json.load(f)
        print('Number of articles: [%s]' % len(data))
        for article in data:
            title = '_'.join(article['title'].split(' '))
            link = article['link']
            for char in title:
                if char in SPECIAL_CHARS:
                    title = title.replace(char, '')
            print('Downloading: [%s]' % title)
            print_to_pdf(link)


def get_articles(output_filename='articles.json'):
    query = gql(
        """
        query ($offset: Int){
            operationName: getPostPageArchive(offset: $offset, type: "archive"){
                meta{
                    max_num_pages
                }
                data{
                    ...on Post{
                        title
                        link
                    }
                }
            }
        }
        """
    )
    articles = []
    url = "https://www.quantamagazine.org/graphql"
    client = GraphqlClient(url)
    print('Getting articles...')
    for page in range(1, data['operationName']['meta']['max_num_pages']+1):
        data = client.execute(query, {"offset": page})
        articles.extend(data['operationName']['data'])

    print('Writing %s' % output_file)
    with open(output_filename, 'w') as f:
        f.write(json.dumps(articles, indent=4))
        print('% written.' % output_file)


if __name__ == '__main__':
    if sys.argv[1] == 'download':
        articles_to_pdf(sys.argv[2])
    else:
        get_articles(output_filename=sys.argv[1])
