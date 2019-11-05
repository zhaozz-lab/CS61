## CS 61 A B C learn note
the note reference CS lecture and reading
## 采用sublime进行工程的编译，尝试编译通过了project2目录下的lib5
javac 的使用方式为 javac -d . -cp ;  ..\\.java
-d 表示生成package,-cp表示需要连接的文件，在windows下用;隔开，生成TileEngine需要的包
```
javac -encoding UTF-8 -d . -cp E:\Resource\skeleton-sp18\library-sp18\javalib\algs4.jar;.;E:\Resource\skeleton-sp18\library-sp18\javalib\stdlib.jar;E:\Resource\skeleton-sp18\library-sp18\javalib\stdlib-package.jar byog\TileEngine\*.java 

javac -encoding UTF-8 -d . -cp E:\Resource\skeleton-sp18\library-sp18\javalib\algs4.jar;.;E:\Resource\skeleton-sp18\library-sp18\javalib\stdlib.jar;E:\Resource\skeleton-sp18\library-sp18\javalib\stdlib-package.jar;E:\Resource\skeleton-sp18\library-sp18\javalib\junit-4.12.jar byog\lab5\*.java 
```
运行测试的结果
```
java -cp ;. byog\lab5\RandomWorldDemo.java 

```


