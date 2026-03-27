[app]

# (str) Title of your application
title = SlugRace

# (str) Package name
package.name = slugrace

# (str) Package domain (needed for android/ios packaging)
package.domain = org.slugrace

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,mp3,wav,ogg

# (list) List of inclusions using pattern matching
source.include_patterns = assets/*,*.kv

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements
requirements = python3,kivy==2.1.0,kivymd,plyer

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Bootstrap to use for android builds
# p4a = python-for-android
# The old "android" bootstrap is deprecated
p4a.bootstrap = sdl2

# (list) python-for-android branches to use, defaults to upstream (master)
#p4a.branch = master

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.arch = armeabi-v7a

# (str) filename of optional android icon file (in PNG format)
# android.icon = path/to/icon.png

# (str) filename of optional android presplash file (in PNG)
# android.presplash = path/to/presplash.png

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

[android]

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (string) Presplash background color (for android toolchain)
presplash.color = #FFFFFF

# (list) Permissions
android.permissions = VIBRATE,WAKE_LOCK

# (str) supported SDL audio formats
android.audio.formats = mp3, ogg

# (str) Android entry-point, default is ok for Kivy-based app
#android.entrypoint = org.renpy.android.PythonActivity

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

# (str) The Android API level to target, should be at least 21.
android.api = 29

# (str) The minimum API your APK / AAB will support.
android.minapi = 21

# (str) The Android SDK version to use
android.sdk = 29

# (str) The Android NDK version to use
android.ndk = 23b

# (bool) Use --private data storage (True) or --dir public storage (False)
#android.private_storage = True

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
#android.ndk_path =

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
#android.sdk_path =

# (str) ANT directory (if empty, it will be automatically downloaded.)
#android.ant_path =

# (bool) If True, then skip trying to update the Android sdk
# android.skip_update = False

# (bool) If True, then automatically accept SDK license
# agreements. This is intended for automation only. If set to False,
# the default, you will be shown the license when first running
# buildozer.
android.accept_sdk_license = True

# (str) Android logcat filters to use
#android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

# (str) The format used to package the app for debug mode. Should be either 'apk' or 'aab'.
# android.debug_artifact = apk

# (str) The format used to package the app for release mode. Should be either 'apk' or 'aab'.
# android.release_artifact = aab

[ios]

# (str) Path to a custom kivy-ios folder
#ios.kivy_ios_dir = ../kivy-ios
# Alternately, specify the URL and branch of a git checkout:
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master

# Another platform dependency: ios-deploy
# Uncomment to use a custom checkout
#ios.ios_deploy_dir = ../ios_deploy
# Or specify URL and branch
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.12.2

# (str) Name of the certificate to use for signing the debug version
# Get a list of available identities: buildozer ios list_identities
#ios.codesign.debug = "iPhone Developer: <lastname> <firstname> (<hexstring>)"

# (str) Name of the certificate to use for signing the release version
#ios.codesign.release = %(ios.codesign.debug)s