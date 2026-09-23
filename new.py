import boto3
from bracket.aws import AwsDevice
from bracket.circuits import Circuit
from bracket.devices import Devices

device = AwsDevice(Devices.Amazon.SV1)


# cnot which gives two options for the control and target qubits

def bell_state(control, target):
    bell = Circuit().h(0).cnot(control, target)
    task = device.run(bell, shots=100)
    return task.result().measurement_counts

bell_state(0, 1)