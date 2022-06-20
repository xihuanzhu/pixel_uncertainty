1.本项目是关于像素级不确定计算的研究，主要用到dropblock和FPN

2.有效文件说明：
    model文件夹提供FPN backbone，
    DropBlock.py为dropblock模块的函数定义
    mc_dropblock_final.ipynb为训练和测试基础代码
    get_uncertainty.ipynb为计算不确定性的基础代码
    88_aug_use_dropblock_multi_output_FPN_DiceBCE_class_model文件夹均为模型存储文件
    其他文件均为工具类文件或者测试文件
    
3.数据（body）：
    训练集
        真实图片：/raid/zhuxihuan/data/body/MC_uncertainty_single_data/train_slice
        真实mask：/raid/zhuxihuan/data/body/MC_uncertainty_single_data/train_mask
    验证集
        真实图片：/raid/zhuxihuan/data/body/single_npy_data/val_slice
        真实mask：/raid/zhuxihuan/data/body/single_npy_data/val_mask
    测试集
        预测mask：/raid/zhuxihuan/data/body/test_npy_data/
        不确定性（熵为指标）：/raid/zhuxihuan/data/body/mc_dropout_entropy/
        不确定性（方差为指标）：/raid/zhuxihuan/data/body/mc_dropout_var/
        
4.训练流程：
    直接运行mc_dropblock_final.ipynb，数据文件目录需要在文件里自行调整
