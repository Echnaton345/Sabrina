# CS50

CS50（Introduction to Computer Science）是一堂美國哈佛大學自1989年開始教授的計算機概論課，課程為期十二週，一週上課兩次，一次一小時。上課內容從最基本的二進位、ASCII、演算法、偽代碼、C 語言語法及應用、排序法、哈希表等，到 TCP/IP、HTTP、HTML、CSS、PHP、SQL、JavaScript、Ajax，一直到網路安全性（Cybersecurity）；不但將電腦科學裡最重要的基礎都帶了一次，還會結合歷史和新聞時事來講授，對初學者來說，內容是滿有分量的。

觀看網站：https://cs50.harvard.edu/college/2019/fall/
         http://cs50.tv/2017/fall/
  
##

# 第1支 2017 Week5 Data Structures
 

觀看網站：https://www.youtube.com/watch?v=pA-8eBZvN1E

* [Note](https://docs.cs50.net/2017/fall/notes/5/lecture5.html)

# 第2支 2017 Week8 Python
 

觀看網站：https://www.youtube.com/watch?v=n_8zxTH7SvA

* [Note](https://docs.cs50.net/2017/fall/notes/8/lecture8.html)

# 第3支 2019 Week2 Array 

觀看網站：https://cs50.harvard.edu/college/2019/fall/weeks/2/

以下為課堂整理的目錄：

* Array 陣列
* Function 函式
* Search 搜尋法
  * Linear Search
  * Binary Search
* Sort 排序法
  * Insertion Sort
  * Merge Sort
  * Selection Sort
* Command line 指令
* Debug 除錯
   
##
* Array
  * 把陣列比喻成郵局信箱，index 永遠都是從 0 開始，要非常小心數量不要數錯。
  * 陣列的宣告方式： 資料類型 名稱 數量。
  
##
* Function 
  * 當我們架構越來越多時，不可能所有都塞在主程式裡，所以需要 function 來分化，也比較好 debug。可以把 function 當成一個黑盒子，有些輸入 input 跟輸出 output。為什麼說他是黑盒子呢？因為有些常用的 function 並不是自己寫的，像是常用的 printf，引用來自 <stdio.h>，我們並不了解裡頭是怎麼實現的，但知道如何使用它。所以一個清楚的命名、及完整的文件說明是很重要的。
  
##
* Search
   * 介紹的兩種排序法，上課都有講解到。
  
##
* Sort 
  * 介紹的三種排序法，上課都有講解到。
  
##
* Command line 
  * 不管是使用 PC（cmd 命令提示字元） 或 Mac （ Terminal 終端機），如果我們要對電腦下命令，除了一般常用的圖形化介面 GUI，也可以用輸入指令對電腦說明要做什麼動作。例如說要進入桌面上的資料夾，我們習慣的操作是 對著該資料夾，使用滑鼠 double click。但也可以開啟 Terminal，輸入 cd，如果放在桌面就打Desktop，在下載就打Downloads，如果打JAVA就會使用到。
  
##
* Debug
  * help50：在發生邏輯上的衝突、導致編譯發生錯誤時使用。在下任何指令前，前面加上 help50 能夠幫助你找出錯誤的位置，或提供一些頭緒除錯。
  * eprintf(“”)：比起 printf，eprintf 會提供是哪一行的資訊，更方便除錯。
  * debug50：在編譯沒問題但結果不如預期，試圖找出設計上錯誤時使用，debug50 並無法直接幫你找出錯誤，畢竟電腦不知道你想要到結果是什麼，但可以幫助你更暸解程式運行的步驟，監控變數的變化，找出在哪一個環節出錯。
  
  





