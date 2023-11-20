# PoeBooster
壓縮 ggpk 中的 .dds 文件以提升 fps。
這是 PoeTexureResizer 的 Python 重寫版本。

## 安裝
1. 安裝 [ImageMagick-7.1.0](https://imagemagick.org/script/download.php#windows) 或直接[下載](https://github.com/alanx15a2/PoeBooster/releases/download/v0.1.3/ImageMagick-7.1.0-46-Q16-x64-dll.exe)。
2. 下載並解壓縮 [PoeBooster](https://github.com/alanx15a2/PoeBooster/releases)。

## 使用方式
1. 運行 **PoeBooster.exe**。（或 main.py）
2. 指定來源路徑。（建議使用 SSD）（使用 LibGGPK2 從 ggpk 導出）
3. 為目的地路徑指定一個空文件夾。（建議使用 SSD）
4. 指定應使用多少 CPU 線程。
5. 指定縮放次數。（1 表示縮小 2 倍，2 表示縮小 4 倍，3 表示縮小 8 倍等等……）
6. 現在你可以喝杯咖啡等待完成。

## 哪些文件應該壓縮？
1. 使用 [LibGGPK2](https://github.com/aianlinb/LibGGPK2)。
2. 使用 ```.dds$``` 作為正則表達式過濾器。（以節省時間）
3. 在 ```Root/Bundles2/Art``` 上右鍵並選擇 **Export**。
4. 在文件夾中刪除 ```Art/2DArt```、```Art/2Ditems```、```Art/Textures/Cinematic```、```Art/Textures/DetailMaps```、```Art/Textures/Interface```、```Art/Textures/masks```。

## 壓縮完成後應該做什麼？
1. 使用 [LibGGPK2](https://github.com/aianlinb/LibGGPK2)。
2. 在 Root/Bundles2/Art 上右鍵並選擇 **Replace**。
3. 選擇 PoeBooster 輸出文件夾。

## 鳴謝
1. [demidemon](https://home.gamer.com.tw/homeindex.php?owner=demidemon) - PoeTexureResizer 的作者。
2. [aianlinb](https://github.com/aianlinb) - LibGGPK2 的作者。

## 開發環境
1. python 3.9
2. ImageMagick-7.1.0
