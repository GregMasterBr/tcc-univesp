#encoding: utf-8
import requests
import json
import feedparser
from conf import link_firebase, feed_url,  id_group_whatsapp, number_whatsapp
import pywhatkit

def get_posts_details(rss=None):
    if rss is not None:
        blog_feed = blog_feed = feedparser.parse(rss)
        posts = blog_feed.entries
        post_list = []

        for post in posts:
            temp = dict()
            try:
                id = extractId(post.id)
                temp["title"] = post.title
                temp["link"] = post.link
                temp["author"] = post.author
                temp["time_published"] = post.published
                temp["tags"] = [tag.term for tag in post.tags]
                temp["authors"] = [author.name for author in post.authors]
                temp["summary"] = post.summary
                addPost(id, temp)
            except:
                pass
            post_list.append(temp)
        posts_details = post_list
        return posts_details
    else:
        return None

def addPost(id, dados):
    ''' Adiciona um post no BD. Antes verifica se o POSTAGEM já existe. (POST) '''
    requisicao = requests.get(f'{link_firebase}/posts/{id}/.json')
    if requisicao.text == 'null':
        requisicao = requests.post(f'{link_firebase}/posts/{id}/.json', data=json.dumps(dados))

        msg = rf"""*{dados['title']} | {dados['tags']}*
                                 
                {dados['summary']}

                Leia mais em: {dados['link']}
                
                Por: *{', '.join(dados['authors']) if len(dados['authors']) > 1 else ''.join(dados['authors'])}*
                
            """            
        print(msg)
        pywhatkit.sendwhatmsg_to_group_instantly(group_id=id_group_whatsapp,
                                                 message=(msg), wait_time=20,
                                                 tab_close=True, close_time=10)

def extractId(s):
    split_num = s.split('=')
    if (split_num[1].isdigit()):
        return split_num[1]
    return 0


if __name__ == "__main__":

    data = get_posts_details(rss=feed_url)
    if data:
        # addPost(data)
        # print(json.dumps(data, indent=2))
        print("Adicionado no BD")

    else:
        print("None")
