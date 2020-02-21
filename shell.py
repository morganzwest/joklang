import jok

while True:
    text = input('jok > ')

    if text.lower() == "stop":
        
        break

    result, error = jok.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)