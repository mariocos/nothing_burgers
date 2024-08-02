import praw

# Initialize PRAW with your credentials
reddit = praw.Reddit(
    user_agent="True",
    client_id="LyrlsBJZh2Q9tMQLD2mb1w",
    client_secret="Tqbc_iRFnxxGJdro6ZLTF7kCtqBtuQ",
    username='DefinetlyNotAScraper',
    password='mamaco123!'
)

# Specify the subreddit
subreddit_name = 'justnomil'  # Subreddit name should be in quotes

# Get the top 5 posts of the day
subreddit = reddit.subreddit(subreddit_name)
top_posts = subreddit.top(time_filter='day', limit=5)

# Print details of the top 5 posts
for post in top_posts:
    print(f'Title: {post.title}')
    print(f'Score: {post.score}')
    print(f'Author: {post.author}')
    print(f'URL: {post.url}')
    print(f'Subreddit: {post.subreddit}')
    print(f'Created: {post.created_utc}')
    print(f'Number of Comments: {post.num_comments}')
    print('-' * 40)
