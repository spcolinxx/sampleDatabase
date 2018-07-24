function check() {
    if (document.getElementById('user_account').value=="")
    {
        alert("请填写要修改的用户账号!");
        return false;
    }
    else if (document.getElementById('user_lv').value=="")
    {
        alert("请选择权限！");
        return false;

    }
    else
    {
        return true;
    }

}