import json

def update_memo(old_memo, updates):

    new_memo = old_memo.copy()

    for key, value in updates.items():
        new_memo[key] = value

    return new_memo