def generate_params(toponym_longitude, toponym_lattitude, spn):
    map_params = {
        "ll": ",".join([toponym_longitude, toponym_lattitude]),
        "spn": ",".join([spn, spn]),
        "l": "map",
        "pt": ",".join([toponym_longitude, toponym_lattitude, 'pm2rdm'])}
    return map_params