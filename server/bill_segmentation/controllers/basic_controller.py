import connexion
import six
import uuid

from flask import url_for

from bill_segmentation.models.img_on_server_dto import ImgOnServerDto  # noqa: E501
from bill_segmentation import util


def upload_image(file=None):  # noqa: E501
    """上载票据图像

     # noqa: E501

    :param file: 
    :type file: str

    :rtype: ImgOnServerDto
    """
    # 检查上传文件的后缀名是否合法，并保存文件到 static 目录

    ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png", "bmp"}

    def allowed_file(filename):
        return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

    if file and allowed_file(file.filename):
        # 生成唯一 ID
        imgId = str(uuid.uuid1())
        filename = imgId + "." + file.filename.rsplit(".", 1)[1].lower()
        file.save("bill_segmentation/static/" + filename)
        return {
            "imgId": imgId,
            "imgUrl": url_for("static", filename=filename, _external=True)
        }
    return {"message": "不支持的图像格式。仅支持：.png、.jpg、.jpeg、.bmp 文件。"}, 400
