import facebook
import unicodecsv

### Small helper script to extract comments for given FB posts into a CSV.
### The resulting CSV has two columns:
### - message
### - sentiment (this is set to a default of '2', and will be reviewed and updated per comment)

output_csv = "data/tatort_reviews.csv"
my_access_token = "yourfacebookaccesstoken"

# e.g. https://www.facebook.com/Tatort/posts/10154600148961693
fb_post_ids = ["38246844868_10154672524546693", "38246844868_10154645692951693", "38246844868_10154600148961693"]
data_limit = 200

graph = facebook.GraphAPI(access_token=my_access_token)
comments = []

# loop through different IDs to pull comments
for post_id in fb_post_ids:
    comments += graph.get_connections(post_id, 'comments', limit=data_limit)['data']

with open(output_csv, 'wb') as csvfile:
    comments_writer = unicodecsv.writer(csvfile, delimiter=',')
    for comment in comments:
        comments_writer.writerow([comment['message'], 2])
