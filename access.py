from app import app

@app.template_filter('nl2br')
def nl2br(item):
    if isinstance(item, str):
        return item.replace('\n','<br>')
    return item


@app.template_filter('nl2br')
def nl2br(item):
    if isinstance(item, str):
        return item.replace('\n','<br>')
    return item
