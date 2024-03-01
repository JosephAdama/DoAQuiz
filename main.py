import math


def is_valid_ip(ip):
    parts = ip.split('/')
    if len(parts) != 2:
        return False
    ip_parts = parts[0].split('.')
    if is_valid_cidr(parts[1]) and len(ip_parts) == 4 and all(
            part.isdigit() and 0 <= int(part) <= 255 for part in ip_parts):
        return True
    return False


def is_valid_cidr(cidr):
    try:
        cidr_value = int(cidr)
        return 0 <= cidr_value <= 32
    except ValueError:
        return False


def Divide_Subnet(ip, divisor, part):
    ip_parts = ip.split('/')
    ip_address = ip_parts[0]
    cidr = int(ip_parts[1])

    res_division = int(2 ** (divisor - 1).bit_length())
    host_b = int(32 - cidr - math.log2(res_division))
    new_cidr = int(32 - host_b)

    ip_b = '.'.join([bin(int(x) + 256)[3:] for x in ip_address.split('.')])

    b_string = ip_b.replace(".", "")
    host_b_string = b_string[new_cidr:]
    network_b_string = b_string[:new_cidr]
    result_network_b_string = format(int(network_b_string, 2) + part - 1, 'b').zfill(len(network_b_string))
    result_b_string = result_network_b_string + host_b_string

    result_ip = ".".join(map(str, [int(segment, 2) for segment in
                                   [result_b_string[i:i + 8] for i in range(0, len(result_b_string), 8)]]))

    return result_ip + "/" + str(new_cidr)


def calculate_broadcast_address(ip):
    ip_parts = ip.split('/')
    ip_address = ip_parts[0]
    host_b = 32 - int(ip_parts[1])

    ip_b = '.'.join([bin(int(x) + 256)[3:] for x in ip_address.split('.')])
    result_b_string = ip_b.replace(".", "")[:-host_b] + "1" * host_b

    result_ip = ".".join(map(str, [int(segment, 2) for segment in
                                   [result_b_string[i:i + 8] for i in range(0, len(result_b_string), 8)]]))
    return result_ip


def calculate_network_address(ip):
    ip_parts = ip.split('/')
    ip_address = ip_parts[0]
    host_b = 32 - int(ip_parts[1])

    ip_b = '.'.join([bin(int(x) + 256)[3:] for x in ip_address.split('.')])
    result_b_string = ip_b.replace(".", "")[:-host_b] + "0" * host_b

    result_ip = ".".join(map(str, [int(segment, 2) for segment in
                                   [result_b_string[i:i + 8] for i in range(0, len(result_b_string), 8)]]))
    return result_ip


if __name__ == '__main__':
    while True:
        print("Choose an option:")
        print("1. Divide Subnet")
        print("2. Calculate Broadcast Address")
        print("3. Calculate Network Address")
        print("4. Exit")

        choice = input("Enter your choice (1, 2, 3 or 4): ")

        if choice == '1':
            ip = input("Enter IP address and CIDR (e.g., 175.83.224.0/20): ")
            divisor = input("Enter divisor (by what is the Subnet being divided?): ")
            part = input("Enter part (which Part do you need for the result): ")

            if is_valid_ip(ip) and divisor.isdigit() and part.isdigit():
                print(f"The Subnet is {Divide_Subnet(ip, int(divisor), int(part))}\n\n")
            else:
                print("Invalid input. Please enter a valid IP address, CIDR, and numeric values for divisor and "
                      "part.\n")

        elif choice == '2':
            ip = input("Enter IP address and CIDR (e.g., 175.83.224.0/20): ")

            if is_valid_ip(ip):
                print(f"The broadcast address is: {calculate_broadcast_address(ip)}\n\n")
            else:
                print("Invalid input. Please enter a valid IP address.\n")

        elif choice == '3':
            ip = input("Enter IP address and CIDR (e.g., 175.83.224.0/20): ")

            if is_valid_ip(ip):
                print(f"The Network address is: {calculate_network_address(ip)}\n\n")
            else:
                print("Invalid input. Please enter a valid IP address.\n")

        elif choice == '4':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.\n")
