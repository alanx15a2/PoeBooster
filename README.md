# PoeBooster
Compress .dds file in ggpk to boost fps.
This is a python rewrite of PoeTexureResizer.

## Setup
1. Install ImageMagick-7.1.0.
1. Download and unzip PoeBooster.

## Usage
1. Run **start.bat**. (or main.py) 
1. Specific sorce path. (SSD recommended) (export from ggpk using LibGGPK2)
1. Specific an empty folder for destination path. (SSD recommended)
1. Specific how many cpu threads should use.
1. Specific resizetimes (1 means 2X smaller, 2 means 4X smaller, 3 means 8X smaller etc...)
1. Now you can drink a coffee and wait for finish. (R9-3900x is about 10 minutes, i5-8265u is about 30 minutes).

## What files should I compress?
1. Using LibGGPK2.
1. Use ```.dds$``` as regex filter. (to save times)
1. Right click on Root/Bundles2/Art and select **export**.
1. Delete Art/2DArt, Art/2Ditems, Art/Textures/Cinematic, Art/Textures/DetailMaps, Art/Textures/Interface, Art/Textures/masks in the folder.

## What should I do after finish compress?
1. Using LibGGPK2.
1. Right click on Root/Bundles2/Art and select **replace**.
1. Choose the PoeBooster output folder.

## Credits
1. demidemon - The author of PoeTexureResizer.
2. aianlinb - The author of LibGGPK2.

## Enviroments
1. python 3.9
1. ImageMagick-7.1.0