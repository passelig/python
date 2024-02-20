
import time
from pyModbusTCP.client import ModbusClient

# init modbus client
mbClient = ModbusClient(host='10.44.2.96', port=502, auto_open=True, debug=False)

# main read loop


while True:
    # 
    factoryIOrunning = mbClient.read_discrete_inputs(0)[0]
    endSensor = mbClient.read_discrete_inputs(1)[0]
  
    mbClient.write_single_coil(0, endSensor)
    print('factoryIOrunning: ' + str(factoryIOrunning) + ' endSensor: ' + str(endSensor ))

    # sleep 1s before next polling
    time.sleep(1)