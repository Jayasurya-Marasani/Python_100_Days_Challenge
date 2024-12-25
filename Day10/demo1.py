def format_name(fname, lname):
    return fname.title(), lname.title()

f_name, l_name = format_name("jAya", "suRya")

print(f"The title name is {f_name} {l_name}")

# Multiple Returns

def _format_name(fname, lname):
    if fname == "" or lname == "":
        return

    f_name = fname.title()
    l_name = lname.title()
    return f"Result: {f_name} {l_name}"


print(_format_name(input("What is your first name?"), input("What is your last name?")))