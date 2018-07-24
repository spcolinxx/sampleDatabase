function check(user_lv) {
    var new_account_lv=document.getElementById('user_lv').value;
    if ((new_account_lv=='0')&&(user_lv=='3'))
    {
        alert("该账号的权限等级不允许添加超级管理员账号！");
        return false;
    }
    else if (document.getElementById('user_account').value=="")
    {
        alert("请填写新账号！");
        return false;
    }
    else if (document.getElementById(('account_owner')).value=="")
    {
        alert("请填写账号持有单位！");
        return false;
    }
    else if (document.getElementById(('user_psd')).value=="")
    {
        alert("请填写密码！");
        return false;
    }
    else if(document.getElementById('psd_rp').value=="")
    {
        alert("请再次输入密码！");
        return false;
    }
    else if(document.getElementById('user_lv').value=="")
    {
        alert("请选择用户权限！");
        return false;
    }
    else if(document.getElementById('user_psd').value!=document.getElementById('psd_rp').value)
    {
        alert("两次密码输入不一致，重新输入！");
        return false;
    }
    else
    {
        return true;
    }

}