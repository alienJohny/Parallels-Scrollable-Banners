from psb.settings import BASE_DIR

def handle_uploaded_file(f, name):
    with open(BASE_DIR + "/uploads/" + name, 'wb') as destination:
        for chunk in f.chunks():
            destination.write(chunk)