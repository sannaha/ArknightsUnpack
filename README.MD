通过角色解包图像和透明通道合成角色完整立绘。

角色初始立绘存放在 `files\AB\Android\charpack` 目录下，角色皮肤立绘存放在 `files\AB\Android\skinpack` 下。请将提取到的解包图像和透明通道图像复制到该项目的 `skinpack` 目录下。

本项目已在 `skinpack` 目录中提供“前滩律动-蓝毒”皮肤的解包图像和透明通道图像用于测试，该皮肤并非官方原始立绘，角色经由 bilibili 用户 @朝雾星弦 修改。

使用：

```python
py run.py
```

注：图像处理部分参考白猫大佬的 [PIL 合并 RGB 通道图与 Alpha 通道图](https://2heng.xin/2019/06/04/pil-merge-of-two-images-with-alpha-channels/)

