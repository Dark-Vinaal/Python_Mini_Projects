import platform

print()
print("=" * 60)
print("***** System Information *****")
print("=" * 60)
print()

print("Operating System:", platform.system())
print("OS Version:", platform.version())
print("Architecture:", platform.architecture()[0])
print("Processor:", platform.processor())
print("Machine:", platform.machine())
print("Python Version:", platform.python_version())
print("Node Version:", platform.node())

print()
print("=" * 60)
print("***** End of System Information *****")
print("=" * 60)
print()
