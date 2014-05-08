#!/usr/bin/env python3

import argparse
import random
import string
import sys

def main():
    # Set defaults
    default_length = 10
    default_seed = None
    default_population = string.ascii_letters + string.digits + '!%+=.,'

    # Set up and parse arguments
    p = argparse.ArgumentParser(
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    p.add_argument('length', default=default_length, type=int,
                   help="Length of the password.")
    p.add_argument('--population', '-p', default=default_population,
                   help="List of characters to generate the password from.")
    p.add_argument('--seed', '-s', default=default_seed,
                   help="Seed for the pseudo-random number generator. If "
                        "omitted, the current system time is used.")
    args = p.parse_args()

    # Seed the number generator
    random.seed(args.seed)

    # Generate password
    pw = ''
    for i in range(1, args.length):
        pw += random.choice(args.population)

    # Print password
    print(pw)


if __name__ == '__main__':
    sys.exit(main())
