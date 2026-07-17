user_sessions = {}


def save_dataset(user_id, dataset_path):
    if user_id not in user_sessions:
        user_sessions[user_id] = {}

    user_sessions[user_id]["dataset"] = dataset_path


def get_dataset(user_id):
    if user_id in user_sessions:
        return user_sessions[user_id].get("dataset")
    return None


def save_report(user_id, report_path):
    if user_id not in user_sessions:
        user_sessions[user_id] = {}

    user_sessions[user_id]["report"] = report_path


def get_report(user_id):
    if user_id in user_sessions:
        return user_sessions[user_id].get("report")
    return None


def clear_dataset(user_id):
    if user_id in user_sessions:
        del user_sessions[user_id]