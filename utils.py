from datetime import datetime
import re

def get_today_string():
    return datetime.now().strftime("%Y-%m-%d")

def sanitize_filename(text):
    return re.sub(r'\W+', '_', text)
