import os

# The name of the text file containing the list of computers
computer_list_file = 'computers.txt'

# The name of the program or application to check for
program_name = 'Symantec Endpoint Protection'

# Output file
output_file = 'installed_programs.txt'

# Open the output file for writing
with open(output_file, 'w') as f:
    # Open the file containing the list of computers
    with open(computer_list_file, 'r') as computer_list:
        # Read the list of computers
        computers = [line.strip() for line in computer_list.readlines()]
        for computer in computers:
            # Check if the program is installed on the current computer
            result = os.system(f'wmic /node:{computer} product get name | find "{program_name}"')
            if result == 0:
                f.write(f'{program_name} is installed on {computer}\n')
            else:
                f.write(f'{program_name} is not installed on {computer}\n')
