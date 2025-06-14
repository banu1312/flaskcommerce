from flask import current_app

def add_logs(user_id, action, product_id=None):
    mongo = current_app.extensions['pymongo']
    db = mongo.db

    log_entry = {
        "action": action,
        "timestamp": mongo.cx.server_info()["localTime"]
    }
    if product_id:
        log_entry["product_id"] = product_id

    db.user_logs.update_one(
        {"user_id": user_id},
        {"$push": {"logs": log_entry}},
        upsert=True
    )
