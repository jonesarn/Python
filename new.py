import boto3
from bracket.aws import AwsDevice
from bracket.circuits import Circuit
from bracket.devices import Devices

device = AwsDevice(Devices.Amazon.SV1)


# cnot which gives two options for the control and target qubits

bell = Circuit().h(0).cnot(0,1)
task = device.run(bell, shots=100)
print(task.result().measurement_counts)