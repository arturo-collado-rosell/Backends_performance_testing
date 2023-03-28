import os
import json
import matplotlib.pyplot as plt



d_l = [10,20,30] # test duration,seconds
c_l = [10,100,500,1000, 2000,4000,10000] #connection number or clients
w_l = [0,2,4,6] #workers number

def plot_latency(flask_latency, sanic_latency, express_latency, fastapi_latency,  d_i = None, c_i = None, w_i = None):
    if d_i == None and c_i!= None and w_i!= None:
        x = []
        y_flask = []
        y_sanic = []
        y_express = []
        y_fastapi = []
        for d in d_l:
            x.append(d)
            y_flask.append(flask_latency['ave_latency_' + f'flask_{d}_{c_i}_{w_i}']) 
            y_sanic.append(sanic_latency['ave_latency_' + f'sanic_{d}_{c_i}_{w_i}'])
            y_express.append(express_latency['ave_latency_' + f'express_{d}_{c_i}_{w_i}']) 
            y_fastapi.append(fastapi_latency['ave_latency_' + f'fastapi_{d}_{c_i}_{w_i}'])     
        fig, ax = plt.subplots()
        ax.semilogy(x, y_flask, label='flask')
        ax.semilogy(x, y_sanic, label='sanic')
        ax.semilogy(x, y_express, label='express')
        ax.semilogy(x, y_fastapi, label='fastapi')
        ax.legend()
        ax.set_xlabel('Time [s]')
        ax.set_ylabel('Average latency [ms]')
        plt.show()      

    if d_i != None and c_i== None and w_i!= None:
        x = []
        y_flask = []
        y_sanic = []
        y_express = []
        y_fastapi = []
        for c in c_l:
            x.append(c)
            y_flask.append(flask_latency['ave_latency_' + f'flask_{d_i}_{c}_{w_i}']) 
            y_sanic.append(sanic_latency['ave_latency_' + f'sanic_{d_i}_{c}_{w_i}'])
            y_express.append(express_latency['ave_latency_' + f'express_{d_i}_{c}_{w_i}'])   
            y_fastapi.append(fastapi_latency['ave_latency_' + f'fastapi_{d_i}_{c}_{w_i}'])  
        fig, ax = plt.subplots()
        ax.semilogy(x, y_flask, label='flask')
        ax.semilogy(x, y_sanic, label='sanic')
        ax.semilogy(x, y_express, label='express')
        ax.semilogy(x, y_fastapi, label='fastapi')
        ax.legend()
        ax.set_xlabel('Clients [s]')
        ax.set_ylabel('Average latency [ms]')
        plt.show()          

    if d_i != None and c_i!= None and w_i== None:
        x = []
        y_flask = []
        y_sanic = []
        y_express = []
        y_fastapi = []
        for w in w_l:
            x.append(w)
            y_flask.append(flask_latency['ave_latency_' + f'flask_{d_i}_{c_i}_{w}']) 
            y_sanic.append(sanic_latency['ave_latency_' + f'sanic_{d_i}_{c_i}_{w}'])
            y_express.append(express_latency['ave_latency_' + f'express_{d_i}_{c_i}_{w}'])  
            y_fastapi.append(fastapi_latency['ave_latency_' + f'fastapi_{d_i}_{c_i}_{w}'])    
        fig, ax = plt.subplots()
        ax.semilogy(x, y_flask, label='flask')
        ax.semilogy(x, y_sanic, label='sanic')
        ax.semilogy(x, y_express, label='express')
        ax.semilogy(x, y_fastapi, label='fastapi')
        ax.legend()
        ax.set_xlabel('Workers [s]')
        ax.set_ylabel('Average latency [ms]')
        plt.show()         

def plot_requests(flask_requests, sanic_requests, express_requests, fastapi_requests,  d_i = None, c_i = None, w_i = None):
    if d_i == None and c_i!= None and w_i!= None:
        x = []
        y_flask = []
        y_sanic = []
        y_express = []
        y_fastapi = []
        for d in d_l:
            x.append(d)
            y_flask.append(flask_requests['ave_requests_' + f'flask_{d}_{c_i}_{w_i}']) 
            y_sanic.append(sanic_requests['ave_requests_' + f'sanic_{d}_{c_i}_{w_i}'])
            y_express.append(express_requests['ave_requests_' + f'express_{d}_{c_i}_{w_i}']) 
            y_fastapi.append(fastapi_requests['ave_requests_' + f'fastapi_{d}_{c_i}_{w_i}'])    
        fig, ax = plt.subplots()
        ax.semilogy(x, y_flask, label='flask')
        ax.semilogy(x, y_sanic, label='sanic')
        ax.semilogy(x, y_express, label='express')
        ax.semilogy(x, y_fastapi, label='fastapi')
        ax.legend()
        ax.set_xlabel('Time [s]')
        ax.set_ylabel('Average requests [request/seconds]')
        plt.show()      

    if d_i != None and c_i== None and w_i!= None:
        x = []
        y_flask = []
        y_sanic = []
        y_express = []
        y_fastapi = []
        for c in c_l:
            x.append(c)
            y_flask.append(flask_requests['ave_requests_' + f'flask_{d_i}_{c}_{w_i}']) 
            y_sanic.append(sanic_requests['ave_requests_' + f'sanic_{d_i}_{c}_{w_i}'])
            y_express.append(express_requests['ave_requests_' + f'express_{d_i}_{c}_{w_i}']) 
            y_fastapi.append(fastapi_requests['ave_requests_' + f'fastapi_{d_i}_{c}_{w_i}'])    
        fig, ax = plt.subplots()
        ax.semilogy(x, y_flask, label='flask')
        ax.semilogy(x, y_sanic, label='sanic')
        ax.semilogy(x, y_express, label='express')
        ax.semilogy(x, y_fastapi, label='fastapi')
        ax.legend()
        ax.set_xlabel('Clients [s]')
        ax.set_ylabel('Average requests [request/seconds]')
        plt.show()          

    if d_i != None and c_i!= None and w_i== None:
        x = []
        y_flask = []
        y_sanic = []
        y_express = []
        y_fastapi = []
        for w in w_l:
            x.append(w)
            y_flask.append(flask_requests['ave_requests_' + f'flask_{d_i}_{c_i}_{w}']) 
            y_sanic.append(sanic_requests['ave_requests_' + f'sanic_{d_i}_{c_i}_{w}'])
            y_express.append(express_requests['ave_requests_' + f'express_{d_i}_{c_i}_{w}'])  
            y_fastapi.append(fastapi_requests['ave_requests_' + f'fastapi_{d_i}_{c_i}_{w}'])    
        fig, ax = plt.subplots()
        ax.semilogy(x, y_flask, label='flask')
        ax.semilogy(x, y_sanic, label='sanic')
        ax.semilogy(x, y_express, label='express')
        ax.semilogy(x, y_fastapi, label='fastapi')
        ax.legend()
        ax.set_xlabel('Workers [s]')
        ax.set_ylabel('Average requests [request/seconds]')
        plt.show()             

def plot_errors(flask_errors, sanic_errors, express_errors, fastapi_errors,  d_i = None, c_i = None, w_i = None):
    if d_i == None and c_i!= None and w_i!= None:
        x = []
        y_flask = []
        y_sanic = []
        y_express = []
        y_fastapi = []
        for d in d_l:
            x.append(d)
            y_flask.append(flask_errors['ave_errors_' + f'flask_{d}_{c_i}_{w_i}']) 
            y_sanic.append(sanic_errors['ave_errors_' + f'sanic_{d}_{c_i}_{w_i}'])
            y_express.append(express_errors['ave_errors_' + f'express_{d}_{c_i}_{w_i}'])
            y_fastapi.append(fastapi_errors['ave_errors_' + f'fastapi_{d}_{c_i}_{w_i}'])     
        fig, ax = plt.subplots()
        ax.semilogy(x, y_flask, label='flask')
        ax.semilogy(x, y_sanic, label='sanic')
        ax.semilogy(x, y_express, label='express')
        ax.semilogy(x, y_fastapi, label='fastapi')
        ax.legend()
        ax.set_xlabel('Time [s]')
        ax.set_ylabel('Number of errors ')
        plt.show()      

    if d_i != None and c_i== None and w_i!= None:
        x = []
        y_flask = []
        y_sanic = []
        y_express = []
        y_fastapi = []
        for c in c_l:
            x.append(c)
            y_flask.append(flask_errors['ave_errors_' + f'flask_{d_i}_{c}_{w_i}']) 
            y_sanic.append(sanic_errors['ave_errors_' + f'sanic_{d_i}_{c}_{w_i}'])
            y_express.append(express_errors['ave_errors_' + f'express_{d_i}_{c}_{w_i}'])
            y_fastapi.append(fastapi_errors['ave_errors_' + f'fastapi_{d_i}_{c}_{w_i}'])     
        fig, ax = plt.subplots()
        ax.semilogy(x, y_flask, label='flask')
        ax.semilogy(x, y_sanic, label='sanic')
        ax.semilogy(x, y_express, label='express')
        ax.semilogy(x, y_fastapi, label='fastapi')
        ax.legend()
        ax.set_xlabel('Clients [s]')
        ax.set_ylabel('Number of errors')
        plt.show()          

    if d_i != None and c_i!= None and w_i== None:
        x = []
        y_flask = []
        y_sanic = []
        y_express = []
        y_fastapi = []
        for w in w_l:
            x.append(w)
            y_flask.append(flask_errors['ave_errors_' + f'flask_{d_i}_{c_i}_{w}']) 
            y_sanic.append(sanic_errors['ave_errors_' + f'sanic_{d_i}_{c_i}_{w}'])
            y_express.append(express_errors['ave_errors_' + f'express_{d_i}_{c_i}_{w}'])
            y_fastapi.append(fastapi_errors['ave_errors_' + f'fastapi_{d_i}_{c_i}_{w}'])     
        fig, ax = plt.subplots()
        ax.semilogy(x, y_flask, label='flask')
        ax.semilogy(x, y_sanic, label='sanic')
        ax.semilogy(x, y_express, label='express')
        ax.semilogy(x, y_fastapi, label='fastapi')
        ax.legend()
        ax.set_xlabel('Workers [s]')
        ax.set_ylabel('Number of errors ')
        plt.show()                     

def plot_info_2d(data, d_i = None, c_i = None, w_i = None):

    flask_latency = {}
    sanic_latency = {}
    express_latency = {}
    fastapi_latency = {}

    flask_requests = {}
    sanic_requests = {}
    express_requests = {}
    fastapi_requests = {}

    flask_errors = {}
    sanic_errors = {}
    express_errors = {}
    fastapi_errors = {}
    
    for d in d_l:
        for c in c_l:
            for w in w_l:
                flask_latency['ave_latency_' + f'flask_{d}_{c}_{w}'] = data[f'flask_{d}_{c}_{w}']['latency']['average'] 
                sanic_latency['ave_latency_' + f'sanic_{d}_{c}_{w}'] = data[f'sanic_{d}_{c}_{w}']['latency']['average']
                express_latency['ave_latency_' + f'express_{d}_{c}_{w}'] = data[f'express_{d}_{c}_{w}']['latency']['average']
                fastapi_latency['ave_latency_' + f'fastapi_{d}_{c}_{w}'] = data[f'fastapi_{d}_{c}_{w}']['latency']['average']

                flask_requests['ave_requests_' + f'flask_{d}_{c}_{w}'] = data[f'flask_{d}_{c}_{w}']['requests']['average'] 
                sanic_requests['ave_requests_' + f'sanic_{d}_{c}_{w}'] = data[f'sanic_{d}_{c}_{w}']['requests']['average']
                express_requests['ave_requests_' + f'express_{d}_{c}_{w}'] = data[f'express_{d}_{c}_{w}']['requests']['average']
                fastapi_requests['ave_requests_' + f'fastapi_{d}_{c}_{w}'] = data[f'fastapi_{d}_{c}_{w}']['requests']['average']

                flask_errors['ave_errors_' + f'flask_{d}_{c}_{w}'] = data[f'flask_{d}_{c}_{w}']['errors']
                sanic_errors['ave_errors_' + f'sanic_{d}_{c}_{w}'] = data[f'sanic_{d}_{c}_{w}']['errors']
                express_errors['ave_errors_' + f'express_{d}_{c}_{w}'] = data[f'express_{d}_{c}_{w}']['errors']
                fastapi_errors['ave_errors_' + f'fastapi_{d}_{c}_{w}'] = data[f'fastapi_{d}_{c}_{w}']['errors']

    plot_latency(flask_latency, sanic_latency, express_latency, fastapi_latency, d_i, c_i, w_i)
    plot_requests(flask_requests, sanic_requests, express_requests, fastapi_requests, d_i, c_i, w_i)  
    plot_errors(flask_errors, sanic_errors, express_errors, fastapi_errors, d_i, c_i, w_i)







if __name__ == '__main__':
    test_output_path = 'test_outputs'
    file_list = os.listdir(test_output_path)
    data = {}
    for file in file_list:
        file_name = file.split('.')[0]
        file_path = os.path.join(test_output_path,file)
        try:
            with open(file_path, 'r') as opened_file:
                file_info = json.load(opened_file)
                data[file_name] = file_info
        except Exception as e:
            print(f'An exception has ocurred {e}')        

    plot_info_2d(data,d_i = 20, c_i = None, w_i = 2)       

