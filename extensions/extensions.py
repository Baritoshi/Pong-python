# Get the file name from the user
filename = input("File name: ").lower().strip()
#if there's a dot in the filename (the last from the right)
if '.' in filename:
    #divide the filename into a name and extension counting the dots from the right
    name, extension = filename.rsplit(".", maxsplit=1)
    #compare the extension with this list and print the media type. If not listed, type "application/octet-stream"
    match extension:
        case "gif":
            print("image/gif")
        case "jpg":
            print("image/jpeg")
        case "jpeg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
        case _:
            print("application/octet-stream")
# if there's no dot in the filename, print "application/octet-stream"
else:
    print("application/octet-stream")