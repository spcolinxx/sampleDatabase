function check()
    {

        if (upform.smp_id.value=="")
        {
            alert("请填写样本编码！");
            return false;
        }
        else if (upform.submit_year.value=="")
        {
            alert("请填写入库年份！")
            return false;
        }
        else if (upform.submit_month.value=="")
        {
            alert("请填写入库月份！")
            return false;
        }
        else if (upform.submit_day.value=="")
        {
            alert("请填写入库日！")
            return false;
        }
        else if (upform.temperature.value=="")
        {
            alert("请填写保存温度！")
            return false;
        }
        else if (upform.smp_count.value=="")
        {
            alert("请填写样本量！")
            return false;
        }
        else if (upform.awareness.value=="")
        {
            alert("请填写知情同意！")
            return false;
        }
        else if (upform.smp_name.value=="")
        {
            alert("请填写样本别称！")
            return false;
        }
        else if (upform.part.value=="")
        {
            alert("请填写采集部位！")
            return false;
        }
        else if (upform.org_name.value=="")
        {
            alert("请填写保存机构名称！")
            return false;
        }
        else if (upform.jur_name.value=="")
        {
            alert("请填写法人机构名称！")
            return false;
        }
        else if (upform.jur_id.value=="")
        {
            alert("请填写法人机构代码！")
            return false;
        }
        else if (upform.donor_id.value=="")
        {
            alert("请填写捐献者匿名编号！")
            return false;
        }
        else if (upform.submit_month.value=="")
        {
            alert("请填写入库月份！")
            return false;
        }
        else if (upform.sex.value=="")
        {
            alert("请填写性别！")
            return false;
        }
        else if (upform.age.value=="")
        {
            alert("请填写年龄！")
            return false;
        }
        else if (upform.prj_id.value=="")
        {
            alert("请填写课题编号！")
            return false;
        }
        else
            {
                return true;
            }

        // if (upform.user.value=="")
        // {
        //     alert("请填写用户");
        //     myform.user.focus();
        //     return false;
        // }
        // if (myform.title.value.length<5)
        // {
        //     alert("标题不能少于五个字符");
        //     myform.title.focus();
        // }
    }


function cate_comb()
{
    var l1_str=document.getElementById('l1').value;
    var l2_str=document.getElementById('l2').value;
    var l3_str=document.getElementById('l3').value;
    var l4_str=document.getElementById('l4').value;

    var cate_code=l1_str+l2_str+l3_str+l4_str;
    document.getElementById('new_cate_code').readOnly=false;


    document.getElementById('new_cate_code').value=cate_code;

    document.getElementById('new_cate_code').readOnly=true;





}