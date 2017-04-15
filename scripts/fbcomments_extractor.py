import facebook
import unicodecsv

### Small helper script to extract comments for given FB posts into a CSV.
### The resulting CSV has two columns:
### - message
### - sentiment (this is set to a default of '2', and will be reviewed and updated per comment)

output_csv = "data/tatort_reviews.csv"
my_access_token = "yourfacebookaccesstoken"

# these IDs have the format profilePageId_postId
# e.g. https://www.facebook.com/DasErste/posts/10154756104298232
fb_post_ids = ["176772398231_10155003108798232",
               "176772398231_10154893279488232",
               "176772398231_10154870567618232",
               "176772398231_10154781611828232",
               "176772398231_10154756104298232" ]
data_limit = 400

graph = facebook.GraphAPI(access_token=my_access_token)
comments = []

# loop through different IDs to pull comments
for post_id in fb_post_ids:
    comments += graph.get_connections(post_id, 'comments', limit=data_limit)['data']

with open(output_csv, 'wb') as csvfile:
    comments_writer = unicodecsv.writer(csvfile, delimiter=',')
    for comment in comments:
        comments_writer.writerow([comment['message'].lower(), 2])
