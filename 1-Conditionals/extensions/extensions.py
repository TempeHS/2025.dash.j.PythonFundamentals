def main():
    file = input("what file do you have? ")
    file = file.lower()
    if file.endswith(".jpg"):
        print("image/jpg ")
    elif file.endswith(".gif"):
        print("image/gif ")
    elif file.endswith(".jpeg "):
        print("image/jpeg")
    elif file.endswith(".pdf"):
        print("image/pdf")
    elif file.endswith(".txt"):
        print("text/txt")
    elif file.endswith(".zip"):
        print("file/zip")
    elif file.endswith(".png"):
        print("image/png")
    else:
        print("application/octet-stream")


main()
