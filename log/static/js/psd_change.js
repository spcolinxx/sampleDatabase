function check() {

    if(document.getElementById('pre_psd').value=="")
    {
        alert("请输入旧密码!");
        return false;
    }
    else if (document.getElementById('user_psd').value=="")
    {
         alert("请输入新密码!");
        return false;
    }
    else if(document.getElementById('psd_rp').value=="")
    {
         alert("请再次输入新密码！");
        return false;
    }
    else if(document.getElementById('user_psd').value!=document.getElementById('psd_rp').value)
    {
         alert("两次密码输入不一致，请重新输入!");

        return false;
    }
    else
    {
        return true;
    }


}