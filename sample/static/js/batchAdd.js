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

