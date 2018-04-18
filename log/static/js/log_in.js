function check() {

    if (document.getElementById('user_id').value=="")
    {
        alert("请填写用户名!");
        return false;

    }
    else if (document.getElementById('user_psd').value=="")
    {
        alert("请填写密码!");
        return false;
    }
    else
    {
        return true;
    }


}