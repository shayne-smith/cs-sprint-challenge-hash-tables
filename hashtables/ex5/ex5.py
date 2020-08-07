# Your code here

queries_table = {}
files_table = {}
output = []

def finder(files, queries):

    # {file: key}
    for k, f in enumerate(files):
        files_table[f] = k

    # print(files_table)
    
    # {key: query}
    for k, q in enumerate(queries):
        queries_table[k] = q

    # print(queries_table)

    # if "blah" in someString:
    #     continue

    for f in files:
        for k, v in queries_table.items():
            if v in f:
                output.append(f)

    for q in queries:
        if q in files_table:
            # output.append(files[files_table[q]])
            print("hello")



        # if q in files_table:
            # output.append(files[files_table[q]])
            # print(f"running{q}")
            
    return output
    # return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
