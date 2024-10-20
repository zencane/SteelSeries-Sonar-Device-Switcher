import subprocess
import re
import json, time

# Command to get the desired netstat output
command = 'netstat -an | findstr LISTENING | findstr 127.0.0.1 > cmdDump.txt'

# Run the command and capture the output
process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()
# Check for errors
if stderr:
    print(f"Errors: {stderr.decode('utf-8')}")
else:
    output = open('cmdDump.txt', 'r').read()
    ports = []

    # Regular expression pattern to match IP and port
    pattern = re.compile(r'127\.0\.0\.\d+:(\d+)')

    # Iterate over each line in the output
    for line in output.splitlines():
        if 'LISTENING' in line and '127.0.0.' in line:
            match = pattern.search(line)
            if match:
                ports.append(match.group(1))

for port in ports:
    # Command prefix for the PUT request
    cmd_command = (f"""curl http://127.0.0.1:{port}/streamRedirections/""")
    # Define your command as a string
    # Use subprocess.run() to execute the command
    try:
        result = subprocess.run(cmd_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, timeout=3)
        json_string = str(result.stdout)
        
        # Parse the JSON string into a Python dictionary
        data = json.loads(json_string)
        # Extract the value
        deviceId = str(data[1]['deviceId'])
        pattern = r'\{[0-9a-fA-F:.]+\}\.\{([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})\}'
        match = re.search(pattern, deviceId)
        if match:
            correctId = match.group(1)
            with open('deviceIdEarphone.txt', 'w') as file:
                file.write(correctId)
        break
    except:
        pass


x = input("press enter to exit.")
