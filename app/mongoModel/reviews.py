from flask import current_app

def add_review(product_id, user_id, rating, comment):
    mongo = current_app.extensions['pymongo']
    db = mongo.db

    db.product_reviews.update_one(
        {"product_id": product_id},
        {
            "$push": {
                "reviews": {
                    "user_id": user_id,
                    "rating": rating,
                    "comment": comment,
                    "timestamp": mongo.cx.server_info()["localTime"]
                }
            }
        },
        upsert=True
    )
