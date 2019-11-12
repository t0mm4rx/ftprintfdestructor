import sys
import subprocess
import inputs
import random

N = 1000
M = 20
COMP = "gcc -Wall -Wextra -Werror -g3 -fsanitize=address "

tests = []

if (len(sys.argv) != 2):
    print("Wrong usage: sh run.sh <path-of-ftprintf>")
    exit()

PATH = sys.argv[1]
if (PATH[-1] != "/"):
    PATH += "/"

def compile_lib():
    result = subprocess.run("make -C {}".format(PATH), shell=True)

def function_content():
    format = ""
    args = []
    for _ in range(random.randint(0, 10)):
        if (random.random() < .6):
            format += inputs.random_string(random.randint(1, 5))
        else:
            temp = inputs.random_arg()
            format += temp[0]
            for arg in temp[1]:
                args.append(arg)
    res = "\"{}\"".format(format)
    for arg in args:
        if (arg != ""):
            res += ", " + arg
    return res

def generate_test():
    content = function_content()
    res1 = "\tft_printf(\"-- %d --\\n\", ft_printf({}));\n".format(content)
    res2 = "\tprintf(\"-- %d --\\n\", printf({}));\n".format(content)
    tests.append(content)
    return (res1, res2)

def generate_tests():
    res1 = ""
    res2 = ""
    for _ in range(N):
        test = generate_test()
        res1 += test[0]
        res2 += test[1]
    return (res1, res2)

def generate_mains():
    content = ""
    with open("main_template.c", "r") as file:
        content = file.read()
    tests = generate_tests()
    content_ftprintf = content.replace("$$$1", tests[0])
    content_printf = content.replace("$$$1", tests[1])
    with open("main_ftprintf.c", "w+") as file:
        file.write(content_ftprintf)
    with open("main_printf.c", "w+") as file:
        file.write(content_printf)

def launch_tests():
    result1 = subprocess.run("{} -L{} -lftprintf -o tests_ftprintf main_ftprintf.c".format(COMP, PATH[:-1]), shell=True)
    result2 = subprocess.run("{} -L{} -lftprintf -o tests_printf main_printf.c".format(COMP, PATH[:-1]), shell=True)
    result3 = subprocess.run("./tests_ftprintf > ftprintf_output", shell=True)
    result3 = subprocess.run("./tests_printf > printf_output", shell=True)

def diff():
    ok = True
    print("Comparing outputs:")
    print()
    ftprintf_output = open("ftprintf_output", "r").readlines()
    printf_output = open("printf_output", "r").readlines()
    for i in range(len(tests)):
        if (ftprintf_output[i] != printf_output[i]):
            ok = False
            print("Diff for printf({});".format(tests[i]))
            print("  printf: |{}|".format(printf_output[i][:-1]))
            print("ftprintf: |{}|".format(ftprintf_output[i][:-1]))
            print()
    if (ok):
        print("No differences, well done !")

compile_lib()

for i in range(M):
    print()
    print("Generating mains of {} tests ({}/{})".format(N, i + 1, M))
    tests = []
    generate_mains()
    launch_tests()
    diff()
