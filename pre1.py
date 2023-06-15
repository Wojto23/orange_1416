import argparse
import configparser
import sys

def main(number, other_number, output):
    result = number + other_number
    print("Result: ", result, file=output)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n1', '--number1', type=int, help='first number', default=1)
    parser.add_argument('-n2', '--number2', type=int, help='second number', default=1)
    parser.add_argument('-o', help='plik na dane wyjsciowe', default=sys.stdout, type=argparse.FileType('w'),
                        dest='output')
    parser.add_argument('--config', '-c', dest="config", help='ścieżka do pliku konfiguracyjnego', type=argparse.FileType('r'))

    args = parser.parse_args()
    if args.config:
        config = configparser.ConfigParser()
        config.read_file(args.config)
        args.number1 = int(config['ARGS']['n1'])
        args.number2 = int(config['ARGS']['n2'])
    main(args.number1, args.number2, args.output)
