from django.db import models
from django_jsonfield_backport import models as json_models

# Create your models here.
class Awards(models.Model):
    award_name = models.CharField(max_length=128, verbose_name="奖项名称")
    award_level = models.CharField(max_length=128, verbose_name="奖项级别")
    award_description = models.CharField(max_length=512, verbose_name="奖项描述")
    award_consultant = models.CharField(max_length=128, verbose_name="奖项顾问")
    award_image = models.ImageField(max_length=1000, upload_to='img')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    start_time = models.DateTimeField(verbose_name="开始申请时间")
    end_time = models.DateTimeField(verbose_name="截止申请时间")
    APPROVAL_STATE = [
        (0, "未开始"),
        (1, "已开始"),
        (2, "已结束"),
    ]
    approval_state = models.IntegerField(choices=APPROVAL_STATE, default=3, verbose_name="评审状态")

    def to_json(self):
        return {
            "id": self.id,
            "award_name": self.award_name,
            "award_level": self.award_level,
            "award_description": self.award_description,
            "award_consultant": self.award_consultant,
            "award_image": self.award_image.name,
            "create_time": str(self.create_time).split('+')[0],
            "start_time": str(self.start_time).split('+')[0],
            "end_time": str(self.end_time).split('+')[0],
            "approval_state": self.approval_state,
        }

class Secretary(models.Model):
    group_id = models.IntegerField(max_length=128, verbose_name="组id")
    secretaries = json_models.JSONField(verbose_name="组内秘书", default=list)
