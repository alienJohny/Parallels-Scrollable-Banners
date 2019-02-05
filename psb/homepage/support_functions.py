from psb.settings import BASE_DIR

def handle_uploaded_file(f, name):
    path = BASE_DIR + "/uploads/" + name
    with open(path, 'wb') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    return path