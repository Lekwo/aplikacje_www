def f(data_text):
    return {'length': len(data_text),
            'letters': list(set(list(data_text))),
            'big_letters': data_text.upper(),
            'small_letters': data_text.lower(),
            }


data_text = "Rafał"
print(f(data_text))
