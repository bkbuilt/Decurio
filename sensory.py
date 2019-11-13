import sys
import pyudev
import os
import daemon

def main():

	context = pyudev.Context()

	monitor = pyudev.Monitor.from_netlink(context)
	monitor.filter_by('block')
	for device in iter(monitor.poll, None):
		if 'ID_FS_TYPE' in device:
			print('{0} partition {1}'.format(device.action, device.get('ID_FS_LABEL')))

if __name__ == "__main__":
	main()
