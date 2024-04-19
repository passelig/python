
import time
from pyModbusTCP.client import ModbusClient

# init modbus client
mbClient = ModbusClient(host='127.0.0.1', port=502, auto_open=True, debug=False)

# main read loop


while True:
    # 
    factoryIOrunning = mbClient.read_discrete_inputs(1)[0]
    endSensor = mbClient.read_discrete_inputs(0)[0]
    #startButton = mbClient.read_discrete_inputs(2)[0]
    
    conveyor =  endSensor
    #startButtonLight = startButton
   
    #mbClient.write_single_coil(1, startButtonLight)
    mbClient.write_single_coil(0, conveyor)
    print('factoryIOrunning: ' + str(factoryIOrunning) + ' endSensor: ' + str(endSensor ))
    print(' conveyor: ' + str(conveyor) )

    # sleep 1s before next polling
    time.sleep(1)