# Cache Hash Table Use Case

cache = {}

def get_data_from_server(url):
    return "facebook.com/home"

def get_page(url):
    if cache.get(url):
        # returns cached data
        return cache[url]
    else:
        data = get_data_from_server(url)
        # saves this data in cache first
        cache[url] = data
        return data


print(get_page("facebook.com"), "\n")

print(cache)
