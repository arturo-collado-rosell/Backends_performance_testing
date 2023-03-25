import subprocess
import os
import pprint
import json
import time

servers = {'flask':5000, 'sanic':5001, 'express':3000}

if __name__ == '__main__':
    d_l = [10,20,30] # test duration,seconds
    c_l = [10,100,1000] #connection number or clients
    w_l = [0,2,4,6] #workers number
    output_dir ='test_outputs' 
    os.makedirs(output_dir, exist_ok=True)

    for d in d_l:
        for c in c_l:
            for w in w_l:

                for server_name, server_port in servers.items():
                    output_file = os.path.abspath(f'{server_name}_result.json')
                    # Run the autocannon command and capture its output
                    result = subprocess.run(['autocannon', f'http://{server_name}:{server_port}', '-d', f'{d}', '-c', f'{c}', '-w', f'{w}', '--output', output_file, '--json'], capture_output=True, text=True)
                    # Save the output to a file
                    with open(output_dir + '/' + f'{server_name}_{d}_{c}_{w}.json', 'w') as f:
                        json.dump(json.loads(result.stdout), f)