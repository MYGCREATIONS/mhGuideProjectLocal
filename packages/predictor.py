__author__ = 'sbedework'
import argparse
import ConfigParser
from wsmainFile import WSFileManager

if __name__ == "__main__":
    main = WSFileManager()
    config = ConfigParser.RawConfigParser()
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--arg', nargs='+')
    # parser.add_argument('-v', '--argd')
    args = parser.parse_args()
    test_plan_list = args.arg

    for test_plan in test_plan_list:
        try:
            test_results = main.wstask_manager(test_plan)
        except RuntimeError:
            pass
