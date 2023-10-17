# python-study
파이썬 기본 문법, 크롤링 학습하기
</br></br></br>


### 파이썬 기초 문법
https://software-creator.tistory.com/18

### 파이썬 기초 크롤링
https://software-creator.tistory.com/20 </br></br>
- 파이썬 라이브러리 설치(request, Beautiful Soup)</br>
`pip3 install beautifulsoup4 requests`
</br></br>
- 네이버 블로그 크롤링</br>

        for links in soup.select('ul.lst_total > li.bx'):
                title = links.select_one('a.api_txt_lines.total_tit').get_text(strip=True)
                author = links.select_one('a.sub_txt.sub_name').get_text(strip=True)
                date = links.select_one('span.sub_time.sub_txt').get_text(strip=True)
                
                # 정보를 딕셔너리로 저장
                info = {
                    'title': title,
                    'author': author,
                    'date': date
                }
                
                data.append(info)
        
          for item in data:
                print("제목:", item['title'])
                print("작성자:", item['author'])
                print("날짜:", item['date'])
                print()


    ![Alt text](image.png)![Alt text](image-2.png)
