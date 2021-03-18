f = open('input.dat', mode='rb')


def reverse():
    global f
    data = None
    try:
        a = f.read()
        data += a
    except Exception:

        f1 = open("files/example.txt", mode='wb')
        f1.write(data)
        f1.close()

    else:
        f.close()
