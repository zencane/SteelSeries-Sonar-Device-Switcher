import subprocess
import json, time

# Define your command as a string
cmd_command = 'curl https://127.0.0.1:6327/subApps -k'

# Use subprocess.run() to execute the command
result = subprocess.run(cmd_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

json_string = str(result.stdout)
# Parse the JSON string into a Python dictionary
data = json.loads(json_string)
# Extract the value
port = str(data['subApps']['sonar']['metadata']['webServerAddress'])

#############

# Command prefix for the PUT request

cmd_prefix = """
curl -d '{"event":"Element Clicked","properties":{"screen_name":"mixer","mode":"stream","role":"master","current_panel":"standard","element_name":"sonar_switch_master_panel","element_type":"button"}' -H "Content-Type: application/json" -X PUT """

# Gets the device ID from the text file
with open('DeviceID/deviceIdHeadset.txt', 'r') as file:
    code = file.read()

# Generate complete command 
headset_cmd = (cmd_prefix + port + "/streamRedirections/monitoring/deviceId/%7B0.0.0.00000000%7D.%7B" + code + "%7D").strip()

# Runs the command using subprocess.Popen
activate_headset = subprocess.Popen(headset_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
