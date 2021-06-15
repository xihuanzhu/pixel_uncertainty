from model.backbone import resnet


def build_backbone(back_bone):
    if back_bone == "resnet101":
        return resnet.ResNet101(pretrained=True)
    elif back_bone == "resnet50":
        return resnet.ResNet50(pretrained=False)
