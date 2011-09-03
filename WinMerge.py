import sublime, sublime_plugin
import os
from subprocess import Popen

WINMERGE = '"%s\WinMerge\WinMergeU.exe"' % os.environ['ProgramFiles']

fileA = fileB = None

def recordActiveFile(f):
	global fileA
	global fileB
	fileB = fileA
	fileA = f

class WinMergeCommand(sublime_plugin.ApplicationCommand):
	def run(self):
		cmd_line = '%s /e /ul /ur "%s" "%s"' % (WINMERGE, fileA, fileB)
		print "WinMerge command: " + cmd_line
		Popen(cmd_line)

class WinMergeFileListener(sublime_plugin.EventListener):
	def on_activated(self, view):
		if view.file_name() != fileA:
			recordActiveFile(view.file_name())
