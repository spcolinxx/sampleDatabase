function sub_check() {
    var ip=document.getElementById('file_input');

    if(ip.value=="")
    {
        alert("请选择要添加的样本！");
        return false;
    }
    else
    {
        return true;
    }

}

function download_alert() {


    alert("红色字段为必填字段，请勿遗漏！");

}

