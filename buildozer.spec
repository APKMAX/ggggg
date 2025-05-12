[app]
title = MiAppKivy
package.name = mi_app
package.domain = org.miapp
source.dir = .
source.include_exts = py,png,jpg,kv,ttf,json
version = 1.0
requirements = python3==3.10.13,kivy==2.3.0,android
orientation = portrait
fullscreen = 0

# Configuración Android
android.api = 34
android.minapi = 21
android.sdk = 34
android.ndk = 26.1.10909125
android.sdk_path = /usr/local/lib/android/sdk
android.ndk_path = /usr/local/lib/android/sdk/ndk/26.1.10909125
android.arch = arm64-v8a
android.p4a_dir = $HOME/.local/lib/python3.10/site-packages/pythonforandroid

# Opciones de build
[buildozer]
log_level = 2
warn_on_root = 1
target_dir = bin