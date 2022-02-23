from config.celery import app


@app.task
def check_posts_creations():
    print("Post has been created!")
