import os
import shutil
import neatoEngine
import glob

print ("neatoOperaCleaner started!")

# Cache
# Delete the web cache, which reduces time to display revisited pages

parentpath = os.environ['LocalAppData']
print (parentpath)

path = os.path.join(parentpath, "\\Opera Software\\Opera Stable\\Cache\\**")
neatoEngine.globexpander(path)
path = os.path.join(parentpath, "\\Opera Software\\Opera Stable\\Media Cache\\**")
neatoEngine.globexpander(path)
#path = os.path.join(parentpath, '\\Opera\\Opera **\\opcache\\')
#neatoEngine.globexpander(path)
#path = os.path.join(parentpath, '\\Opera\\Opera **\\thumbnails\\')
#neatoEngine.globexpander(path)
#path = os.path.join(parentpath, '\\Opera\\Opera **\\profile\\cache4\\')
#neatoEngine.globexpander(path)
#path = os.path.join(parentpath, '\\Opera\\Opera **\\profile\\opcache\\')
#neatoEngine.globexpander(path)

parentpath = os.environ['AppData']
print (parentpath)
#this is kakhe too!
path = os.path.join(parentpath, "\\Opera Software\\Opera Stable\\GPUCache\\**")
neatoEngine.globexpander(path)
path = os.path.join(parentpath, "\\Opera Software\\Opera Stable\\ShaderCache\\**")
neatoEngine.globexpander(path)
path = os.path.join(parentpath, "\\Opera Software\\Opera Stable\\File System\\**")
neatoEngine.globexpander(path)
path = os.path.join(parentpath, "\\Opera Software\\Opera Stable\\Service Worker\\**")
neatoEngine.globexpander(path)
path = os.path.join(parentpath, "\\Opera Software\\Opera Stable\\**.tmp")
neatoEngine.globexpander(path)
path = os.path.join(parentpath, "\\Opera Software\\Opera Stable\\**.**journal")
neatoEngine.globexpander(path)

# Cookies
# Delete cookies, which contain information such as web site preferences,authentication, and tracking identification

path = os.path.join(parentpath, "\\Opera Software\\Opera Stable\\Local Storage\\**")
neatoEngine.globexpander(path)
path = os.path.join(parentpath, "\\Opera Software\\Opera Stable\\IndexedDB")
neatoEngine.globexpander(path)

#History
#Clears gnenral internet history.

path = os.path.join(parentpath, "\\Opera Software\\Opera Stable\\Visited Links")
neatoEngine.globexpander(path)
path = os.path.join(parentpath, "\\Opera Software\\Opera Stable\\Top Sites")
neatoEngine.globexpander(path)
path = os.path.join(parentpath, "\\Opera Software\\Opera Stable\\History Provider Cache")
neatoEngine.globexpander(path)
path = os.path.join(parentpath, "\\Opera Software\\Opera Stable\\Network Action Predictor")
neatoEngine.globexpander(path)

#command = "delete" search = "glob" path = "$appdata\\Opera\\Opera**\\cookies4.dat" / >
#command = "delete" search = "glob" path = "$appdata\\Opera\\Opera**\\profile\\cookies4.dat" / >
#
## Current session
## Delete the current session
#
#command = "delete" search = "glob" path = "$appdata\\Opera\\Opera**\\sessions\\autosave.win" / >
#command = "delete" search = "glob" path = "$appdata\\Opera\\Opera**\\sessions\\autosave.win.bak" / >
#
## DOM Storage
## Delete HTML5 cookies
#
#command = "delete" search = "walk.all" path ="$appdata\\Opera\\Opera **\\pstorage\\"/ >
#
## Download history
## List of files downloaded
#
#command = "delete" search = "glob" path = "$appdata\\Opera\\Opera**\\download.dat" / >
#command = "delete" search = "file" path = "$appdata\\Opera\\Opera\\profile\\download.dat" / >
#
## Passwords
## A database of usernames and passwords as well as a list of sites that should not store passwords
## This option will delete your saved passwords.
#
#command = "delete" search = "file" path = "$appdata\\Opera Software\\Opera Stable\\Login Data" / >
#command = "delete" search = "file" path = "$appdata\\Opera Software\\Opera Stable\\Login Data-journal" / >
#
## Search history
## Delete the search history
#
#command = "delete" search = "glob" path = "$appdata\\Opera\\Opera**\\search_field_history.dat" / >
#
## URL history
## List of visited web pages
#
#command = "delete" search = "file" path = "$appdata\\Opera\\Opera\\profile\\global.dat" / >
#command = "delete" search = "file" path = "$appdata\\Opera\\Opera\\profile\\typed_history.xml" / >
#command = "delete" search = "file" path = "$appdata\\Opera\\Opera\\profile\\vlink4.dat" / >
#command = "delete" search = "file" path = "$localappdata\\Opera\\Opera\\profile\\vps\\????\\md.dat" / >
#command = "delete" search = "glob" path = "$appdata\\Opera\\Opera**\\global_history.dat" / >
#command = "delete" search = "glob" path = "$appdata\\Opera\\Opera**\\typed_history.xml" / >
#command = "delete" search = "glob" path = "$appdata\\Opera\\Opera**\\vlink4.dat" / >
#command = "delete" search = "glob" path = "$localappdata\\Opera\\Opera**\\icons\\**.gif" / >
#command = "delete" search = "glob" path = "$localappdata\\Opera\\Opera**\\icons\\**.ico" / >
#command = "delete" search = "glob" path = "$localappdata\\Opera\\Opera**\\icons\\**.idx" / >
#command = "delete" search = "glob" path = "$localappdata\\Opera\\Opera**\\vps\\????\\md.dat" / >

#Other Entries
#These are entries that increase the effectiveness of the cleaner.

parentpath = os.environ['LocalAppData']
print (parentpath)

path = os.path.join(parentpath, "Opera\\Opera**\\application_cache")
neatoEngine.globexpander(path)
path = os.path.join(parentpath, "Opera\\Opera**\\icons")
neatoEngine.globexpander(path)
path = os.path.join(parentpath, "Opera\\Opera**\\Logs")
neatoEngine.globexpander(path)
path = os.path.join(parentpath, "Opera\\Opera**\\temporary_downloads\\")
neatoEngine.globexpander(path)
path = os.path.join(parentpath, "Opera\\Opera**\\thumbnails\\")
neatoEngine.globexpander(path)
path = os.path.join(parentpath, "Opera\\Opera**\\vps\\")
neatoEngine.globexpander(path)

parentpath = os.environ['AppData']
print (parentpath)

path = os.path.join(parentpath, "Opera Software\\Opera Stable\\Bookmarks.bak")
neatoEngine.globexpander(path)
path = os.path.join(parentpath, "Opera Software\\Opera Stable\\Extension Cookies\\**.**")
neatoEngine.globexpander(path)
path = os.path.join(parentpath, "Opera Software\\Opera Stable\\Extension State\\LOG.old")
neatoEngine.globexpander(path)
path = os.path.join(parentpath, "Opera Software\\Opera Stable\\File System\\Origins\\LOG.old")
neatoEngine.globexpander(path)
