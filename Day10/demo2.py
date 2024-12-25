# Doc Strings


def _format_name(fname, lname):
    """
    Take a Frist and last name and format it to return
    the title case version of the name.
    """
    if fname == "" or lname == "":
        return

    f_name = fname.title()
    l_name = lname.title()
    return f"Result: {f_name} {l_name}"


print(_format_name(input("What is your first name?"), input("What is your last name?")))