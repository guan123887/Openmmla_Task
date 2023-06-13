# Openmmla_Task2

1.创建虚拟环境 activate new_env

2.选择mmpretrain\configs\resnet\resnet50_8xb32_in1k.py, 然后将四个文件的代码复制到新建立的文件resnet50_finetune.py

3.根据需求修改resnet50_finetune.py配置

4.在mmpretrain目录下使用虚拟环境, mim train pretrain resnet50_finetune.py --work-dir=./exp进行训练

