import lettuce

__author__ = 'root'
import argparse
import ConfigParser
from mainFile import FileManager

if __name__ == "__main__":
    main = FileManager()
    config = ConfigParser.RawConfigParser()
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--arg', nargs='+')
    args = parser.parse_args()
    test_plan_list = args.arg

    for test_plan in test_plan_list:
        try:
            test_results = main.task_manager(test_plan)

        except RuntimeError:
            pass
