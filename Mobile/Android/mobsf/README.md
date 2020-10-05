# MobSF

- [MobSF](#mobsf)
  - [1. Installation](#1-installation)
  - [2. Static Analysis using MobSF](#2-static-analysis-using-mobsf)
  - [3. Solve It](#3-solve-it)
  - [References](#references)

## 1. Installation

1. If you have Docker installed in your system, run the following command

        $ sudo docker run -it -p 8000:8000 opensecurity/mobile-security-framework-mobsf:latest

    ![MobSF docker command](image/1-mobsf-docker-run.png)

2. Otherwise, follow the steps as mentioned [here](https://github.com/MobSF/Mobile-Security-Framework-MobSF/wiki/1.-Documentation) to install and run MobSF
3. Access MobSF web interface by navigating to `http://localhost:8000`

    ![MobSF](image/2-mobsf.png)

## 2. Static Analysis using MobSF

1. Upload an APK file 
2. Wait while MobSF analyzes the APK
3. Do a manual analysis of MobSF report

    ![MobSF Report](image/3-mobsf-report.png)

## 3. Solve It 

> **EXERCISE-5:**
> 1. Perform a static analysis of VyAPI APK using MobSF
> 2. Make a note of interesting findings 

## References

* [https://github.com/MobSF/Mobile-Security-Framework-MobSF/wiki/1.-Documentation](https://github.com/MobSF/Mobile-Security-Framework-MobSF/wiki/1.-Documentation)

