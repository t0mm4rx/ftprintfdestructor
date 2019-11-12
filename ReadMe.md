# ftprintfdestructor

This project is a script that generate thousands of tests for the school 42 project ft_printf.

It doesn't test %p flag.

By **tmarx**
## Usage
```sh
git clone https://github.com/t0mm4rx/ftprintfdestructor
cd ftprintfdestructor
sh run.sh <path-of-ftprintf>
```
If you want to increase the number of tests, edit run.py, at the top of the file there are two constants, M and N. N is the number of tests in each main generated. M is the number of main generated.

## How it works
This script generate hundreds of random test, then create two mains. One calling these tests with printf and the other with ft_printf. Then, it compares line by line and print the tests that failed.

The value between -- X -- is the return value of the function.
