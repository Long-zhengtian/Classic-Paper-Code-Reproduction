def output2File(filename, wORa, add_text):
    with open(filename, wORa) as external_file:
        print(add_text, file=external_file)
        external_file.close()
    pass