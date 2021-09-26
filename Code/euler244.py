# Project Euler 244: Slider
# Dated: 25-09-21

def calculate_checksum(checksum, input_str):
    return checksum * 243 + ord(input_str) % 100000007
def main(steps):
    checksum = 0
    for step in steps:
        checksum = calculate_checksum(checksum, step)

    print("checksum: {}".format(checksum))
if __name__ == '__main__':
    main('AB')
