def read_pass(password_file):
    f = open(password_file)
    lines = f.readlines()
    f.close()

    return lines

if __name__ == "__main__":
    password_file = "pass.txt"
    print(read_pass(password_file))
    