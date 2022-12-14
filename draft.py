def get_posts_details(rss=None):
    if rss is not None:
        import feedparser
        blog_feed = blog_feed = feedparser.parse(rss)
        posts = blog_feed.entries
        posts_details = {"Blog title": blog_feed.feed.title,
                         "Blog link": blog_feed.feed.link}
        post_list = []

        for post in posts:
            temp = dict()
            try:
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

if __name__ == "__main__":
    import json

    feed_url = "https://bairroalerta.gregmaster.com.br/feed/"

    data = get_posts_details(rss=feed_url)

    if data:
        print(json.dumps(data, indent=2))
    else:
        print("None")