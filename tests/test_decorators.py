import os.path

from src.decorators import log


def test_log_outprint_correct(capsys):
    @log()
    def divide(a, b):
        return a / b

    divide(5, 2)
    captured = capsys.readouterr()
    assert captured.out == f"{divide.__name__} ok\n"


def test_log_outprint_wrong(capsys):
    @log()
    def divide(a, b):
        return a / b

    divide(5, 0)
    captured = capsys.readouterr()
    assert captured.out == f"{divide.__name__} error: <class 'ZeroDivisionError'>. Inputs: (5, 0),{{}}\n"


@log("log.txt")
def divide(a, b):
    return a / b


def test_log_print_in_file_correct():
    log_file = os.path.join(os.getcwd(), "log.txt")

    if os.path.exists(log_file):
        os.remove(log_file)

    divide(5, 2)

    with open(log_file) as file:
        content = file.read()
    assert "divide ok" in content


def test_log_print_in_file_error():
    log_file = os.path.join(os.getcwd(), "log.txt")

    if os.path.exists(log_file):
        os.remove(log_file)

    try:
        divide(5, 0)
    except ZeroDivisionError:
        pass

    assert os.path.exists(log_file)

    with open(log_file, "r") as file:
        content = file.read()

    # print("🔎 Содержимое файла:", content)
    assert "divide error: <class 'ZeroDivisionError'>. Inputs: (5, 0),{}" in content
