#!/usr/bin/env python
import os, platform, subprocess, sys

# Executes a command and returns its exit code and output
def executeCommand(command):
	proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	(stdout, stderr) = proc.communicate(None)
	return proc.returncode, stdout, stderr


# Generates the wrappers for the specified set of tools
def generateWrappers(dockerImage, tools):
	
	# Determine the location of the user's home directory
	if sys.platform == 'win32':
		homeDir = os.environ['HOMEDRIVE'] + '/' + os.environ['HOMEPATH']
	else:
		homeDir = os.environ['HOME']
	
	# Create our wrappers directory if it doesn't already exist
	wrappersDir = homeDir + '/.docker-wrappers'
	if os.path.exists(wrappersDir) == False:
		os.mkdir(wrappersDir)
	
	# Pull the docker image if it doesn't already exist
	code, stdout, stderr = executeCommand(['docker', 'images', dockerImage, '--format', '{{.Repository}}:{{.Tag}}'])
	imageFound = stdout.strip()
	if (sys.version_info.major >= 3):
		imageFound = imageFound.decode('utf8')
	if imageFound != dockerImage:
		subprocess.call(['docker', 'pull', dockerImage])
	
	# Generate the wrappers for each of the tools
	for tool in tools:
		
		# Generate the shell script
		toolScript = '{}/{}'.format(wrappersDir, tool)
		with open(toolScript, 'wb') as sh:
			sh.write('#!/usr/bin/env docker-script\n'.encode('utf-8'))
			sh.write('#!{} bash\n'.format(dockerImage).encode('utf-8'))
			sh.write('{} $*\n'.format(tool).encode('utf-8'))
		
		# Determine if we are running under Windows or a POSIX-based platform
		if platform.system() != 'Windows':
			
			# Under POSIX-based platforms, set the execute bit for the shell script
			subprocess.call(['chmod', 'a+x', toolScript])
			
		else:
			
			# Under Windows, generate a batch file to wrap the shell script
			with open(toolScript + '.bat', 'wb') as bat:
				bat.write('docker-script "%~dp0{}" %*\r\n'.format(tool).encode('utf-8'))
