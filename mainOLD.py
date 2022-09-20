import requests
import json
link_firebase = "https://tcc-bairro-alerta-default-rtdb.firebaseio.com/"
feed_url = "https://bairroalerta.gregmaster.com.br/feed/"

def get_posts_details(rss=None):
    if rss is not None:
        import feedparser
        blog_feed = blog_feed = feedparser.parse(rss)
        posts = blog_feed.entries
        #print(posts)
        posts_details = {"Blog title": blog_feed.feed.title,
                         "Blog link": blog_feed.feed.link}
        post_list = []

        for post in posts:
            print(post.title,post.id)
            temp = dict()
            try:
                temp["id"] = extractId(post.id)
                temp["title"] = post.title
                temp["link"] = post.link
                temp["author"] = post.author
                temp["time_published"] = post.published
                temp["tags"] = [tag.term for tag in post.tags]
                temp["authors"] = [author.name for author in post.authors]
                temp["summary"] = post.summary
            except:
                pass
            post_list.append(temp)
        posts_details["posts"] = post_list
        return posts_details
    else:
        return None

def addPost(dados):
    ''' Criar uma venda (POST) '''
    requisicao = requests.post(f'{link_firebase}/posts/.json', data=json.dumps(dados))
    print(requisicao)
    print(requisicao.text)


def extractId(s):
    split_num = s.split('=')
    if (split_num[1].isdigit()):
        return split_num[1]
    return 0


if __name__ == "__main__":

    data = get_posts_details(rss=feed_url)
    if data:
        addPost(data)
        #print(json.dumps(data, indent=2))

    else:
        print("None")


