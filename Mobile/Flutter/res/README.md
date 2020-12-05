# Pre-event Promotion

## 1. Find the hardcoded secret

1. Download APK
2. Decode APK: `apktool d app-arm64-v8a-release.apk` 
3. Test if a known string is present: `grep -r -Pio "Did you find" app-arm64-v8a-release/`
4. Find the secret: `strings app-arm64-v8a-release/lib/arm64-v8a/libapp.so | grep "Did you find" -C5`