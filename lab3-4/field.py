def field(items, *args):
    assert len(args) > 0, "Необходимо передать хотя бы один ключ"

    if len(args) == 1:
        key = args[0]
        for item in items:
            val = item.get(key)
            if val is not None:
                yield val
    else:
        for item in items:
            filtered = {key: item[key] for key in args if item.get(key) is not None}
            if filtered:
                yield filtered


if __name__ == '__main__':
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'color': 'black'},
        {'title': 'Стул', 'price': None, 'color': 'white'},
        {'color': 'red'}
    ]

    for title in field(goods, 'title'):
        print(title)

    for item in field(goods, 'title', 'price'):
        print(item)
