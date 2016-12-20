# twitter-datamining

This repo includes mining Twitter data for understanding shopping habits of people. 

1. A Twitter Scraper is implemented in order to connect twitter stream API and MongoDB through python. The script to run the scraper is 
```{bash}
 python twitter_stream.py -71.191261,42.227654,-70.804482,42.39698 Boston_db
```
The first argument is the bounding box which you can specify and the second argument is the mongo database name that you want to store the scraped data. 

2. With the scraped Twitter data, the first type of analysis is pulling data directly from Mongodb then analyze some direct statistics, such as word frequency, the most popular hashtags for a specific location. Related work can be found in the notebook  	twitter_from_mongo.ipynb.
3. The second type of analysis includes the twitter mentioning brand names in our brand list. Examples include category-based popularity, brand sentiment score, can be found in twitter_brand_analysis.ipynb
4. The third type of analysis is based on brands' followers. I use LDA model to extract trending topics from brands' followers' twitter timeline. This work is inspired by https://github.com/peimengsui/datatalks. Sample analysis and visualizaiton can be found in twitter_follower_topic.ipynb
5. The last type of analysis is twitter_coocurance.ipynb, analyzing coocurrence of words for specific subset of twitter data. This work can be applied to analyze twitter for specific shopping event. 
