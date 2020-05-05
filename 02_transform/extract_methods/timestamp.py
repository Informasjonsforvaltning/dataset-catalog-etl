from datetime import datetime

def dateFromTimestamp(timestamp):
    date = datetime.fromtimestamp(int(timestamp))
    return date.strftime('%Y-%m-%dT%H:%m:00.000+0000')
