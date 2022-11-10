from requests_html import HTMLSession

session = HTMLSession()
url = 'https://news.google.com/publications/CAAiEFVHzDT3IcfbXBRUsEXkj-wqFAgKIhBVR8w09yHH21wUVLBF5I_s/sections/CAQqKggAIhBVR8w09yHH21wUVLBF5I_sKhQICiIQVUfMNPchx9tcFFSwReSP7DCR4qcH?hl=en-US&gl=US&ceid=US%3Aen'

r = session.get(url)

r.html.render(sleep=1, scrolldown=0)

articles = r.html.find('article')

news_list = []

for item in articles:
    try:
        news_item = item.find('h3', first=True)
        news_article = {
            'title' : news_item.text,
            'link' : news_item.absolute_links
            }
        news_list.append(news_article)
    except:
        pass
    
print(news_list[0])
    

    
    
