function confm() {

    var rst=confirm("确定要删除该样本信息？")
    if (rst==true)
    {
        window.location.href='/sample/smpdelete/'
    }

}