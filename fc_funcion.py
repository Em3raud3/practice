# def square(x):
#     return x*x


# def cube(x):
#     return x * x * x


# def my_map(func, arg_list):
#     result = []
#     for i in arg_list:
#         result.append(func(i))
#     return result


# squares = my_map(square, [1, 2, 3, 4, 5])

# print(squares)

# cubed = my_map(cube, [1, 2, 3, 4, 5])
# print(cubed)

###############################################################################

# def logger(msg):
#     def log_message():
#         print("Log:", msg)

#     return log_message()


# log_hi = logger("Hi!")

# log_hi()

# ! This part takes advantage of closure

def html_tag(tag):

    def wrap_test(msg):
        print(f"<{tag}>{msg}</{tag}>")

    return wrap_test


print_h1 = html_tag("h1")
print_h1("Test Headline!")
print_h1("Another Headline!")

print()

print_p = html_tag("p")
print_p("Test Paragraph!")
