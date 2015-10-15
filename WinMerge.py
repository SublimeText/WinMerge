import sublime_plugin
import os
from subprocess import Popen
try:
    import _winreg as winreg
except:
    import winreg

WINMERGE = winreg.QueryValue(winreg.HKEY_LOCAL_MACHINE, 'SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\WinMergeU.exe')

if not WINMERGE:
    if os.path.exists("%s\WinMerge\WinMergeU.exe" % os.environ['ProgramFiles(x86)']):
        WINMERGE = '"%s\WinMerge\WinMergeU.exe"' % os.environ['ProgramFiles(x86)']
    else:
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
        print("WinMerge command: " + cmd_line)
        Popen(cmd_line)


class WinMergeFileListener(sublime_plugin.EventListener):
    def on_activated(self, view):
        if view.file_name() != fileA:
            recordActiveFile(view.file_name())
