def generate_affiliation_link(url):
    amazon = 'http://www.amazon.com/dp/'
    tag = '/?tag=pyb0f-20'
    split_url = url.split('/')
    shortlink = ''
    for i, part in enumerate(split_url):
        if part == 'dp':
            shortlink = split_url[i+1]
            break
    return f'{amazon}{shortlink}{tag}'
