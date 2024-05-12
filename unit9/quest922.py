def copy_file_content(source, destination):
    with open(source, "rt") as source_file, open(destination, "wt") as dest_file:
        for line in source_file:
            dest_file.write(line)
