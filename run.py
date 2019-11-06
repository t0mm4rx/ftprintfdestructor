import sys
import subprocess

N = 100
COMP = "gcc -Wall -Wextra -Werror -g3 -fsanitize=address "

if (len(sys.argv) != 2):
    print("Wrong usage: sh run.sh <path-of-ftprintf>")
    exit()

PATH = sys.argv[1]
if (PATH[-1] != "/"):
    PATH += "/"

def compile_lib():
    result = subprocess.run("make -C {}".format(PATH), shell=True)

def generate_test():
    res1 = "\tft_printf(\"\");\n"
    res2 = "\tprintf(\"\");\n"
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

compile_lib()
generate_mains()
launch_tests()
