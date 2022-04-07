# PoeBooster
Compress .dds file in ggpk to boost fps.
This is a python rewrite of PoeTexureResizer.

## Setup
1. Install [ImageMagick-7.1.0](https://imagemagick.org/script/download.php#windows).
1. Download and unzip [PoeBooster](https://github.com/alanx15a2/PoeBooster/releases).

## Usage
1. Run **PoeBooster.exe**. *(or main.py)*
1. Specific sorce path. *(SSD recommended) (export from ggpk using LibGGPK2)*
1. Specific an empty folder for destination path. *(SSD recommended)*
1. Specific how many cpu threads should use.
1. Specific resizetimes. *(1 means 2X smaller, 2 means 4X smaller, 3 means 8X smaller etc...)*
1. Now you can drink a coffee and wait for finish. *(R9-3900x is about 10 minutes, i5-8265u is about 30 minutes)*

## What files should I compress?
1. Using [LibGGPK2](https://github.com/aianlinb/LibGGPK2).
1. Use ```.dds$``` as regex filter. (to save times)
1. Right click on Root/Bundles2/Art and select **Export**.
1. Delete Art/2DArt, Art/2Ditems, Art/Textures/Cinematic, Art/Textures/DetailMaps, Art/Textures/Interface, Art/Textures/masks in the folder.

## What should I do after finish compress?
1. Using [LibGGPK2](https://github.com/aianlinb/LibGGPK2).
1. Right click on Root/Bundles2/Art and select **Replace**.
1. Choose the PoeBooster output folder.

## Credits
1. [demidemon](https://home.gamer.com.tw/homeindex.php?owner=demidemon) - The author of [PoeTexureResizer](https://forum.gamer.com.tw/Co.php?bsn=18966&sn=478296).
2. [aianlinb](https://github.com/aianlinb) - The author of [LibGGPK2](https://github.com/aianlinb/LibGGPK2).

## Develop Enviroments
1. python 3.9
1. ImageMagick-7.1.0
