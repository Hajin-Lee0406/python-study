html_doc="""
<html>
    <head>
    </head>
        <body>
            <p> hello </p>
            <p> good day </p>
        </body>
</html>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser') # <- html_doc은 파싱할 문서고, 'html.parser'는 파싱 방식


# find - tag를 통해 원하는 부분을 찾는다.
for p in soup.find('p'):
    print(p)

# p태그 모두 출력
for p in soup.find('p'):
    print(p)
