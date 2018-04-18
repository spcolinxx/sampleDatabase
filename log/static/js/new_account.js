function check() {
    if (document.getElementById('new_account').value=="")
    {
        alert("请填写新账号！");
        return false;
    }
    else if (document.getElementById(('psd')).value=="")
    {
        alert("请填写密码！");
        return false;
    }
    else if(document.getElementById('psd_rp').value=="")
    {
        alert("请再次输入密码！");
        return false;
    }
    else if(document.getElementById('account_lv').value=="")
    {
        alert("请选择用户权限！");
        return false;
    }
    else if(document.getElementById('psd').value!=document.getElementById('psd_rp').value)
    {
        alert("两次密码输入不一致，重新输入！");
        return false;
    }
    else
    {
        return true;
    }

}