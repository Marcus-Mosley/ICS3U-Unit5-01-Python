#!/usr/bin/env python3

# Created by Marcus A. Mosley
# Created on October 2020
# This program converts a celsius temperature to fahrenheit


def fahrenheit():
    # This function converts celsius temperatures to fahrenheit

    # Input

    celsius = int(input("Enter the temperature in celsius: "))

    # Process

    fahrenheit = (9 / 5) * celsius + 32

    # Output
    print("")
    print("{0} degrees celsius is equal to {1:,.1f} degrees fahrenheit!"
          .format(celsius, fahrenheit))


def main():
    # This function calls other functions

    fahrenheit()


if __name__ == "__main__":
    main()
