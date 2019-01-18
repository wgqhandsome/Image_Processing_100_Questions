# Image Processing 100 Questions

---

This is the English version of image processing 100 questions.  The [original Japanese repository](https://github.com/yoyoyo-yo/Gasyori100knock) was created by [yoyoyo-yo](https://github.com/yoyoyo-yo).  It’s updated by him now.  To be honest, I can not speak Japanese. Since the code is language independent and I’m preparing for my interview questions about computer vision now. I decided to translate the English version of this 100 questions.

Hope this could help more people and thanks for [yoyoyo-yo's](https://github.com/yoyoyo-yo) great effort.  

## Before Reading

1. I’ll use the Google translator to help me understand his original meaning. Pretty cool, right? It’s the time for NLP.
2. I may add some additional materials and my own opinions to this repository.
3. **I’ll discard the irrelevant parts** and mainly focus on the OpenCV parts.

3. I’ll update this as soon as possible since I have to do my research project now.

## Environment Setting

 1. Go to [Miniconda](https://conda.io/miniconda.html) website, download and install it.

 2. Open your terminal, create a virtual environment using following command:

    ```bash
    $ conda create python = 3.6 -n Image_Processing_100
    ```

3. Activate your virtual environment:

   ```bash
   $ source activate Image_Processing_100
   ```

4. Install the packages:

   ```bash
   $ pip install -r requirement.txt
   ```

## Testing Your Environment

1. Clone this repository into your local computer:

   ```bash
   $ git clone git@github.com:KuKuXia/Gasyori100knock.git
   ```

2. In the Image_Processing_100_Questions folder, make a new file named sample.py, copy and paste the following code:

   ```python
   import cv2

   img = cv2.imread("assets/imori.jpg")
   cv2.imshow("imori", img)
   cv2.waitKey(0)
   cv2.destroyAllWindows()
   ```

3. Save the file and run it.
   ```bash
   python ./sample.py
   ```
4. Successful if the following image is displayed with a new window! Then if you press any button, it disappears.


![](assets/sample.png)

 4. Next, see the [Tutorial folder](https://github.com/KuKuXia/Image_Processing_100_Questions/tree/master/Tutorial) to learn `numpy `related to image processing. (Please skip this if you already know.)

 5. From now on, please solve the Question. The Question contents are included in each folder. Please use 	`assets/imori.jpg` in the question. Questions are written in the README.md of each folder.



## Content

​            Question         >>        Folder

- [x] Question 1 - 10   >> Question_01_10
- [x] Question 11 - 20 >> Question_ 11 _ 20
- [ ] Question 21 - 30 >> Question_ 21 _ 30
- [ ] Question 31 - 40 >> Question_ 31 _ 40
- [ ] Question 41 - 50 >> Question_ 41 _ 50
- [ ] Question 51 - 60 >> Question_ 51 _ 60
- [ ] Question 61 - 70 >> Question_ 61 _ 70
- [ ] Question 71 - 80 >> Quesiton_ 71 _ 80
- [ ] Question 81 - 90 >> Question_ 81 _ 90
- [ ] Question 91 - 100 >> Question_ 91 _ 100

## Note

- This paper is a teaching material to learn fundamental knowledge and theory of image processing.
- In the solution, we do not use main () etc. to simplify the code as much as possible.
- We will use numpy, but we do not post basic knowledge about numpy. Please check each one.

## Question

**Unresolved** issues are unanswered

## [Question 1-10](https://github.com/KuKuXia/Image_Processing_100_Questions/tree/master/Question_01_10)

| Number |                           Question                           | Number |                           Question                           |
| :----: | :----------------------------------------------------------: | :----: | :----------------------------------------------------------: |
|   1    |  [Channel swapping](./Question_01_10/1_Channel_Swapping.py)  |   6    | [Discretization of Color](./Question_01_10/6_Discretization_of_Color.py) |
|   2    |         [Grayscale](./Question_01_10/2_Grayscale.py)         |   7    |   [Average Pooling](./Question_01_10/7_Average_Pooling.py)   |
|   3    |      [Binarization](./Question_01_10/3_Binarization.py)      |   8    |       [Max Pooling](./Question_01_10/8_Max_Pooling.py)       |
|   4    | [Binarization of Otsu](./Question_01_10/4_Binarization_of_Otsu.py) |   9    |   [Gaussian Filter](./Question_01_10/9_Gaussian_Filter.py)   |
|   5    |    [HSV Conversion](./Question_01_10/5_HSV_Conversion.py)    |   10   |    [Median Filter](./Question_01_10/10_Median_Filter.py)     |

## [Question 11 - 20](https://github.com/KuKuXia/Image_Processing_100_Questions/tree/master/Question_11_20)

| Number |                           Question                           | Number |                           Question                           |
| :----: | :----------------------------------------------------------: | :----: | :----------------------------------------------------------: |
|   11   | [Smoothing Filter](./Question_11_20/11_Smoothing_Filter.py)  |   16   |   [Prewitt Filter](./Question_11_20/16_Prewitt_Filter.py)    |
|   12   |    [Motion Filter](./Question_11_20/12_Motion_Filter.py)     |   17   | [Laplacian Filter](./Question_11_20/17_Laplacian_Filter.py)  |
|   13   |   [MAX_MIN Filter](./Question_11_20/13_Max_Min_Filter.py)    |   18   |    [Emboss Filter](./Question_11_20/18_Emboss_Filter.py)     |
|   14   | [Differential Filter](./Question_11_20/14_Differential_Filter.py) |   19   |       [LoG Filter](./Question_11_20/19_LoG_Filter.py)        |
|   15   |     [Sobel Filter](./Question_11_20/15_Sobel_Filter.py)      |   20   | [Histogram Display](./Question_11_20/20_Histogram_Display.py) |

## [Question 21 - 30](https://github.com/KuKuXia/Image_Processing_100_Questions/tree/master/Question_21_30)

| Number |            Question            | Number |              Question               |
| :----: | :----------------------------: | :----: | :---------------------------------: |
|   21   |    Histogram normalization     |   26   |       Bi-linear interpolation       |
|   22   |      Histogram operation       |   27   |       Bi-cubic interpolation        |
|   23   |      Histogram flattening      |   28   | Affine transformation (translation) |
|   34   |        Gamma correction        |   29   |   Affine transformation (scaling)   |
|   25   | Nearest neighbor interpolation |   30   |  Affine transformation (rotation)   |

## [Question 31 - 40](https://github.com/KuKuXia/Image_Processing_100_Questions/tree/master/Question_31_40)

|     Number     |              Question              | Number |                          Question                          |
| :------------: | :--------------------------------: | :----: | :--------------------------------------------------------: |
|       31       |    Affine transformation (skew)    |   36   |    JPEG compression (Step 1) Discrete cosine transform     |
| 32 **not yet** |         Fourier transform          |   37   |                            PSNR                            |
| 33 **not yet** | Fourier transform low pass filter  |   38   |        JPEG compression (Step 2) DCT + quantization        |
| 34 **not yet** | Fourier transform high pass filter |   39   | JPEG compression (Step 3) YCbCr color specification system |
| 35 **not yet** | Fourier transform band pass filter |   40   |    JPEG compression (Step 4) YCbCr + DCT + quantization    |

## [Question 41 - 50](https://github.com/KuKuXia/Image_Processing_100_Questions/tree/master/Question_41_50)

| number |                           Question                           | number |                           Question                           |
| :----: | :----------------------------------------------------------: | :----: | :----------------------------------------------------------: |
|   41   |         Canny edge detection (Step 1) Edge intensity         |   46   | Hough conversion · Line detection (Step 3) Hough inverse transformation |
|   42   |            Canny edge detection (Step 2) thinning            |   47   |             Morphological processing (expansion)             |
|   43   | Canny edge detection (Step 3) Hysteresis threshold processing |   48   |             Morphology processing (contraction)              |
|   44   |  Hough transform · Line detection (Step 1) Hough transform   |   49   |                       Opening process                        |
|   45   |        Hough conversion · Line detection (Step 2) NMS        |   50   |                      Closing processing                      |

## [Question 51 - 60](https://github.com/KuKuXia/Image_Processing_100_Questions/tree/master/Question_51_60)

|       Question        | Number | Number |        Question         |
| :-------------------: | :----: | :----: | :---------------------: |
|  Morphology gradient  |   51   |   56   |  Template matching NCC  |
|  Top hat conversion   |   52   |   57   | Template matching ZNCC  |
| Black hat conversion  |   53   |   58   |     Labeling 4 Near     |
| Template matching SSD |   54   |   59   | Labeling 8 neighborhood |
| Template matching SAD |   55   |   60   |       Alpha Blend       |

## [Question 61 - 70](https://github.com/KuKuXia/Image_Processing_100_Questions/tree/master/Question_61_70)

|     number     |         Question          | number | Question |
| :------------: | :-----------------------: | :----: | :------: |
|       61       |    4-connected number     |        |          |
|       62       | 8 - number of connections |        |          |
|       63       |         Thinning          |        |          |
| 64 **not yet** |    Hiruditchi thinning    |        |          |


|番号|問題||番号|問題|
|:---:|:---:|:---:|:---:|:---:|
| 71 | マスキング | | 76 | 顕著性マップ
| 72 | マスキング(カラートラッキングとモルフォロジー)
| 73 | 縮小と拡大
| 74 | ピラミッド差分による高周波成分の抽出
| 74 | ガウシアンピラミッド

## TODO

Hough, Gabor, adaptivebinalizatino
