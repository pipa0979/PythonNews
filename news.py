'''
$ sudo apt-get install libxml2-dev libxslt-dev
sudo apt-get install libjpeg-dev zlib1g-dev libpng12-dev
pip install newspaper
curl https://raw.githubusercontent.com/codelucas/newspaper/master/download_corpora.py | python2.7

'''



import newspaper
cnn_paper = newspaper.build('http://cnn.com/', language='en', memoize_articles=False)
for i,article in enumerate(cnn_paper.articles):
	if(i==10):
		break
	print article.title
	print article.url
	print article.text
	print article.summary



'''
from hackernews import HackerNews
hn = HackerNews()


'''