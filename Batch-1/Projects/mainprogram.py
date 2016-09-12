import argparse


def is_even(number):
    """
    This function is capable of finding whether number is even or odd
    :param number: any integer
    :return: true if even false otherwise
    """
    return int(number) % 2 == 0


def is_odd(number):
    return not is_even(number)


def write_to_file(message,path):
    """
    This method writes the text to file
    :param message:
    :param path:
    :return:
    """
    fo=open(path,"w")
    print("type is ",type(fo))
    print("Name of the file",fo.name)
    print("Closed or not",fo.closed)
    #print("Mode of opening file",fo.mode)
    fo.write(message)
    fo.close()
    return


def read_from_file(path):
    """
    This method reads the text from file
    :param path:
    :return:
    """
    return


def main(argument):
    """
    this method is an entry point
    :return:
    """
    print("checking for even:", is_even(argument))
    print("checking for odd:", is_odd(argument))
    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--number", help="Enter any number", type=int)
    parser.add_argument("--other", help="Enter other number", type=int)
    args = parser.parse_args()
    main(args.number)
    main(args.other)
