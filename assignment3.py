#!/usr/bin/env python3

# Created by Samuel Webster
# Created on March 2022
# This program tells user what quadrant a coordinate pair is in


def main():
    # I check which quadrant

    # input
    string_x_coordinate = input("Please enter X coordinate: ")
    string_y_coordinate = input("Please enter Y coordinate: ")

    # process&output
    try:
        int_x_coordinate = int(string_x_coordinate)
        int_y_coordinate = int(string_y_coordinate)
        if int_x_coordinate > 0:
            if int_y_coordinate > 0:
                print("Point is in the 1st quadrant.")
            elif int_y_coordinate < 0:
                print("Point is in the 4th quadrant.")
            else:
                print("On y axis")
        elif int_x_coordinate < 0:
            if int_y_coordinate > 0:
                print("Point is in the 2nd quadrant.")
            elif int_y_coordinate < 0:
                print("Point is in the 3rd quadrant.")
            else:
                print("On y axis")
        else:
            print("On x axis")
    except Exception:
        print("Please enter integers!")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
