[app]

# (str) Title of your application
title = ESP Flasher

# (str) Package name
package.name = espflasher

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests, bin, venv

# (list) List of exclusions using pattern matching
# Do not prefix with './'
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 0.1

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,pyserial,setuptools

# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
# requirements.source.kivy = ../../kivy

# (list) Garden requirements
#garden_requirements =

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (list) Supported orientations
# Valid options are: landscape, portrait, portrait-reverse or landscape-reverse
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Are you sure you want a dark theme?
# default is 0 and light mode.
#android.dark_theme = 0

#
# Android specific
#

# (list) Permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE,WIFI_STATE,CHANGE_WIFI_STATE

# (int) Target Android API, may need adjustment depending on build environment
android.api = 33

# (int) Minimum API your APK / AAB will support.
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 24

# (str) Android NDK version to use
android.ndk = 25b

# (int) Android NDK API to use. This is the minimum API your app will support, it should usually match android.minapi.
android.ndk_api = 21

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
#android.ndk_path =

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
#android.sdk_path =

# (str) ANT directory (if empty, it will be automatically downloaded.)
#ant_path =

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid excess Internet downloads or save time
# when an update is due and you just want to test compilation again.
# For production, this should remain False.
android.skip_update = False

# (bool) If True, then automatically accept SDK license agreements. Typically you really want to enable this
# only if you do not have access to the keyboard.
android.accept_sdk_license = True

# (str) Android entry point, default is ok for Kivy-based app
#android.entrypoint = org.renpy.android.PythonActivity

# (list) Pattern to whitelist for the whole project
#android.whitelist =

# (str) Path to a custom whitelist file
#android.whitelist_src =

# (str) Path to a custom blacklist file
#android.blacklist_src =

# (list) List of Java .jar files to add to the libs so that pyjnius can access
# their classes. Don't add jars that you do not need, since extra jars can slow
# down the build process. Allows wildcards matching, for example:
# OUYA-ODK/libs/*.jar
#android.add_jars = foo.jar,bar.jar,path/to/more/*.jar

# (list) List of Java files to add to the android project (can be java or a
# directory containing the files)
#android.add_src =

# (list) Android AAR archives to add (currently works only with sdl2_gradle
# bootstrap)
#android.add_aars =

# (list) Gradle dependencies to add (currently works only with sdl2_gradle
# bootstrap)
#android.gradle_dependencies =

# (list) Add java compile arguments
# This may come in handy when including certain libraries like firebase
# which require additional java compiler arguments.
#android.javac_args = -Xlint:deprecation,-Xlint:unchecked

# (list) Add java manifest entries
# Useful for adding permissions or features to the manifest
#android.manifest_entries = <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />

# (str) oculus signature key
#oculus.keyalias =

# (str) oculus keystore path
#oculus.keystore =

# (str) oculus store password
#oculus.storepass =

# (str) oculus key password
#oculus.keypass =

# (str) The command to execute after building the APK/AAB. Can be used to run
# scripts, copy files, etc...
#post_build_cmd = echo "Build finished!"

# (str) The command to execute before building the APK/AAB. Can be used to run
# scripts, clean up files, etc...
#pre_build_cmd = rm -rf dist/*

# (str) Activity class name to launch
#activity.launch_class_name = org.kivy.android.PythonActivity

# (str) Service class name to launch
#service.launch_class_name = 

# (list) Services to declare in the manifest
#services = my_service

# (list) Receivers to declare in the manifest
#receivers = my_receiver

# (list) Providers to declare in the manifest
#providers = my_provider

# (list) Meta-data to declare in the manifest
#meta_data = com.example.my_key=my_value

# (list) Intent-filters to declare in the manifest
#intent_filters = 

# (list) Features to declare in the manifest
#features = 

# (list) Libraries to link against
#libraries = 

# (str) Bootstrap name (default is sdl2)
bootstrap = sdl2

# (str) Bootstrap directory (if empty, it will be automatically downloaded.)
#bootstrap_dir =

# (str) Python installation binary for host (for cross-compilation)
#python_host_bin = python3

# (str) Python installation binary for target (for cross-compilation)
#python_target_bin = python3

# (str) Directory to install python packages into
#site_packages_dir =

# (bool) Enable debugging
debug = True

# (str) Log level
log_level = 2

# (str) Build type (release/debug)
build_type = debug