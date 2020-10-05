# Reverse Engineering

- [Reverse Engineering](#reverse-engineering)
  - [1. Identify the Supported Architecture](#1-identify-the-supported-architecture)
  - [2. Explore the APK Bundle](#2-explore-the-apk-bundle)
  - [3. Decode the APK](#3-decode-the-apk)

## 1. Identify the Supported Architecture

1. Unzip the APK

        $ unzip app-debug.apk -d vyapi_binary

2. View the contents of `lib` folder
   
        $ ls -la vyapi_binary/lib/

    ![Supported architectures](image/1-view-architecture.png)

3. If app installation is failing on an Android Virtual Device (AVD), check if the AVD supports one of the listed architectures (see step #2, above). If not, create a new AVD that supports any of the above listed architectures.

## 2. Explore the APK Bundle

1. Browse through different files and folders in the **unzipped** APK bundle. Look for interesting files.

    ![Encoded manifest file](image/2-explore-unzipped-manifest.png)

2. `AndroidManifest.xml` is an interesting place to begin with. However, the file is encoded. We shall decode it shortly.
3. What else is bundled in the Android APK? 
   
> **EXERCISE-1:**
> Make a list of all interesting files and folders that you see in the unzipped APK 

## 3. Decode the APK

1. Convert the APK into a JAR file using **Enjarify** tool

        $ enjarify app-debug.apk

    ![Enjarify](image/2b-enjarify.png)

2. Access this JAR file using **JD-GUI** java decompiler

        $ java -jar ./jd-gui-1.6.2.jar app-debug-enjarify.jar

    ![Java decompiler](image/2c-java-decompiler.png)

> **EXERCISE-2:**
> 1. Do you see any hardcoded secrets?
> 2. Can you understand the app structure and business logic?

3. Decode the APK using **APKTool**

        $ apktool d app-debug.apk 

    ![APKTool](image/2d-apktool.png)

4. Browse through different files and folders in the **decoded** APK. Look for interesting files.

    ![Decoded APK](image/2e-decoded.png)

5. `AndroidManifest.xml` is human readable now

    ![Decoded Manifest](image/2f-decoded-manifest.png)

> **EXERCISE-3:**
> Can you identify the attack surface by analyzing *AndroidManifest.xml* file and other class files?