import argparse as ap
import ast
import numpy as np
import re


def main():
    parser = ap.ArgumentParser()
    parser.add_argument('input_file')
    parser.add_argument('output_file')
    args = parser.parse_args()
    disclaimer(args.output_file)
    print("\nThe process has been started.\n\nProcessing...\n")
    open(args.output_file, 'w')
    with open(args.input_file, 'r') as r_file:
        for line in r_file:
            first_compared_file, second_compared_file = line.split()
            with open(args.output_file, 'a') as w_file:
                try:
                    print(
                        round(
                            comparing(
                                first_compared_file,
                                second_compared_file),
                            3),
                        file=w_file)
                except FileNotFoundError:
                    print(
                        "Looks like the files " +
                        first_compared_file +
                        ' or ' +
                        second_compared_file +
                        ' are missing.',
                        file=w_file)
                except BaseException:
                    print(
                        "There's been a problem with analyzing " +
                        first_compared_file +
                        ' and ' +
                        second_compared_file +
                        ' files.',
                        file=w_file)
    print("The process has been finished.\n")


def disclaimer(output_file):
    check_flag = input(
        "\nThe " +
        output_file +
        " file is going to be overwritten. Do you want to proceed?\n" +
        "Type Y if you do; type N otherwise.\n\n").lower()
    if check_flag == 'n':
        print("\nYou have decided to stop the program.\n")
        exit(0)
    elif check_flag != 'y':
        disclaimer(output_file)


def comparing(first_file, second_file):
    first_str = cleaning(first_file)
    second_str = cleaning(second_file)
    return levenshtein_dist(first_str, second_str)


def cleaning(filename):
    parsed = ast.parse(open(filename).read())
    clean_names(parsed)
    cleaned = ast.unparse(parsed)
    cleaned = clean_comments(cleaned)
    cleaned = clean_strings(cleaned)
    return clean_blanks(cleaned)


def clean_names(ast_code):
    for node in ast.walk(ast_code):
        if isinstance(node, ast.Name):
            node.id = 'a'


def clean_blanks(code):
    return re.sub(' + ', ' ', code)


def clean_comments(code):
    return re.sub('#.*', '', clean_single_comments(code))


def clean_single_comments(code):
    return re.sub("'''.*?'''", '',
                  clean_double_comments(code), flags=re.DOTALL)


def clean_double_comments(code):
    return re.sub('""".*?"""', '', code, flags=re.DOTALL)


def clean_strings(code):
    return re.sub('".*?"', "''", clean_single_strings(code), flags=re.DOTALL)


def clean_single_strings(code):
    return re.sub("'.*?'", "''", code, flags=re.DOTALL)


def levenshtein_dist(first_str, second_str):
    len_first = len(first_str)
    len_second = len(second_str)
    matrix = np.zeros((len_first + 1, len_second + 1))
    for i in range(1, len_second + 1):
        matrix[0][i] = matrix[0][i - 1] + 1
    for j in range(1, len_first + 1):
        matrix[j][0] = matrix[j - 1][0] + 1
    for i in range(1, len_first + 1):
        for j in range(1, len_second + 1):
            if first_str[i - 1] == second_str[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1]
            else:
                matrix[i][j] = min(matrix[i - 1][j], matrix[i]
                                   [j - 1], matrix[i - 1][j - 1]) + 1
    return matrix[len_first][len_second] / max(len_first, len_second)


if __name__ == '__main__':
    main()
