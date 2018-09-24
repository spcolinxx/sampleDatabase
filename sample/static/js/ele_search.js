function add_ele() {
    var item=document.getElementById('select_item').value;  //要添加的项的名称
    var search_method=document.getElementById('search_method').value;  //搜索方式

    // var fm=document.getElementById('search_form');   //获得表单元素
    var and_div=document.getElementById('and_search');
    var or_div=document.getElementById('or_search');
    var nor_div=document.getElementById('nor_search');
    var target_div;

    if (search_method=="and")
    {
        target_div=and_div;
    }
    else if(search_method=="or")
    {
        target_div=or_div;
    }
    else
    {
        target_div=nor_div;
    }

    var ele_num=document.getElementById('or_search').children.length+document.getElementById('and_search').children.length+
        document.getElementById('nor_search').children.length;


    if(ele_num>99)
    {
        alert("搜索条件数量已达到上限！");
    }
    else
    {
            if (ele_num<10)
            {
                ele_num='0'+ele_num;

            }

            if (item=="库存编码")
            {
                var ele_div=document.createElement('div');
                ele_div.setAttribute('class','form-group');
                var ele_label=document.createElement('label');
                ele_label.setAttribute('class','col-md-4 lb_style');
                ele_label.innerHTML=item;
                var inner_div=document.createElement('div');
                inner_div.setAttribute('class','col-md-7');
                var ele_input=document.createElement('input');
                ele_input.setAttribute('type','text');
                ele_input.setAttribute('class','form-control');

                ele_input.setAttribute('name',search_method+'_'+ele_num+'_inv_id');
                inner_div.appendChild(ele_input);
                ele_div.appendChild(ele_label);
                ele_div.appendChild(inner_div);

                target_div.appendChild(ele_div);


            }
            else if(item=="样本类别")
            {
                var ele_div=document.createElement('div');
                ele_div.setAttribute('class','form-group');
                var ele_label=document.createElement('label');
                ele_label.setAttribute('class','col-md-4 lb_style');
                ele_label.innerHTML=item;
                var inner_div=document.createElement('div');
                inner_div.setAttribute('class','col-md-7');
                var ele_input=document.createElement('input');
                ele_input.setAttribute('type','text');
                ele_input.setAttribute('class','form-control');
                ele_input.setAttribute('name',search_method+'_'+ele_num+'_sam_cate_name');

                inner_div.appendChild(ele_input);
                ele_div.appendChild(ele_label);
                ele_div.appendChild(inner_div);

                target_div.appendChild(ele_div);


            }
            else if(item=="保存方式")
            {

                var ele_div=document.createElement('div');
                ele_div.setAttribute('class','form-group');
                var ele_label=document.createElement('label');
                ele_label.setAttribute('class','col-md-4 lb_style');
                ele_label.innerHTML=item;
                var inner_div=document.createElement('div');
                inner_div.setAttribute('class','col-md-7');
                var ele_input=document.createElement('input');
                ele_input.setAttribute('type','text');
                ele_input.setAttribute('class','form-control');
                ele_input.setAttribute('name',search_method+"_"+ele_num+'_stor_meth');

                inner_div.appendChild(ele_input);
                ele_div.appendChild(ele_label);
                ele_div.appendChild(inner_div);

                target_div.appendChild(ele_div);

            }
            else if(item=="每份样本数量")
            {
                var ele_div=document.createElement('div');
                ele_div.setAttribute('class','form-group');
                var ele_label=document.createElement('label');
                ele_label.setAttribute('class','col-md-4 lb_style');
                ele_label.innerHTML=item;
                var inner_div=document.createElement('div');
                inner_div.setAttribute('class','col-md-7');
                var ele_input=document.createElement('input');
                ele_input.setAttribute('type','text');
                ele_input.setAttribute('class','form-control');
                ele_input.setAttribute('name',search_method+'_'+ele_num+'_sam_qty');

                inner_div.appendChild(ele_input);
                ele_div.appendChild(ele_label);
                ele_div.appendChild(inner_div);

                target_div.appendChild(ele_div);


            }
            else if(item=="采集时间")
            {
                var ele_div=document.createElement('div');
                ele_div.setAttribute('class','form-group');
                var ele_label=document.createElement('label');
                ele_label.setAttribute('class','col-md-4 lb_style');
                ele_label.innerHTML=item;
                var inner_div=document.createElement('div');
                inner_div.setAttribute('class','col-md-7');

                var year_select=document.createElement('select');
                year_select.setAttribute('id',ele_num+'_acqui_year');
                year_select.setAttribute('onchange','get_acqui_time(this)');
                year_select.setAttribute('style','margin-right:5px;');
                var date=new Date();
                var this_year=date.getFullYear();
                for(var i=1949;i<=this_year;i++)
                {
                    year_select.options.add(new Option(i, i));
                }
                var year_lb=document.createElement('label');
                year_lb.innerHTML="年";
                year_lb.setAttribute('style','margin-right:5px;');

                var month_select=document.createElement('select');
                month_select.setAttribute('id',ele_num+'_acqui_month');
                month_select.setAttribute('onchange','get_acqui_time(this)');
                month_select.setAttribute('style','margin-right:5px;');
                for(var i=1;i<=12;i++)
                {
                    month_select.options.add(new Option(i,i));

                }
                var month_lb=document.createElement('label');
                month_lb.innerHTML="月";
                month_lb.setAttribute('style','margin-right:5px;');

                var day_select=document.createElement("select");
                day_select.setAttribute('id',ele_num+'_acqui_day');
                day_select.setAttribute('onchange','get_acqui_time(this)');
                day_select.setAttribute('style','margin-right:5px;');
                for(var i=1;i<=31;i++)
                {
                    day_select.options.add(new Option(i,i));

                }
                var day_lb=document.createElement('label');
                day_lb.innerHTML="日";


                var acqui_time_stor=document.createElement('input');
                acqui_time_stor.setAttribute('style','display:none;');
                acqui_time_stor.setAttribute('type','text');
                acqui_time_stor.setAttribute('name',search_method+'_'+ele_num+'_acqui_time');
                acqui_time_stor.setAttribute('id',ele_num+'_acqui_time');

                inner_div.appendChild(year_select);
                inner_div.appendChild(year_lb);
                inner_div.appendChild(month_select);
                inner_div.appendChild(month_lb);
                inner_div.appendChild(day_select);
                inner_div.appendChild(day_lb);
                inner_div.appendChild(acqui_time_stor);

                ele_div.appendChild(ele_label);
                ele_div.appendChild(inner_div);

                target_div.appendChild(ele_div);

                var year=document.getElementById(ele_num+'_acqui_year').value;
                var month=document.getElementById(ele_num+'_acqui_month').value;
                var day=document.getElementById(ele_num+'_acqui_day').value;
                if(Number(month)<10)
                {
                    month="0"+month;
                }

                if (Number(day)<10)
                {
                    day="0"+day;
                }
                var date=year+'-'+month+'-'+day;
                acqui_time_stor.value=date;
            }
            else if(item=="保存机构名称")
            {
                var ele_div=document.createElement('div');
                ele_div.setAttribute('class','form-group');
                var ele_label=document.createElement('label');
                ele_label.setAttribute('class','col-md-4 lb_style');
                ele_label.innerHTML=item;
                var inner_div=document.createElement('div');
                inner_div.setAttribute('class','col-md-7');
                var ele_input=document.createElement('input');
                ele_input.setAttribute('type','text');
                ele_input.setAttribute('class','form-control');
                ele_input.setAttribute('name',search_method+'_'+ele_num+'_org_name');

                inner_div.appendChild(ele_input);
                ele_div.appendChild(ele_label);
                ele_div.appendChild(inner_div);

                target_div.appendChild(ele_div);

            }
            else if(item=="法人机构代码")
            {
                var ele_div=document.createElement('div');
                ele_div.setAttribute('class','form-group');
                var ele_label=document.createElement('label');
                ele_label.setAttribute('class','col-md-4 lb_style');
                ele_label.innerHTML=item;
                var inner_div=document.createElement('div');
                inner_div.setAttribute('class','col-md-7');
                var ele_input=document.createElement('input');
                ele_input.setAttribute('type','text');
                ele_input.setAttribute('class','form-control');
                ele_input.setAttribute('name',search_method+'_'+ele_num+'_jur_per_id');

                inner_div.appendChild(ele_input);
                ele_div.appendChild(ele_label);
                ele_div.appendChild(inner_div);

                target_div.appendChild(ele_div);



            }
            else if(item=="法人机构类型")
            {
                var ele_div=document.createElement('div');
                ele_div.setAttribute('class','form-group');
                var ele_label=document.createElement('label');
                ele_label.setAttribute('class','col-md-4 lb_style');
                ele_label.innerHTML=item;
                var inner_div=document.createElement('div');
                inner_div.setAttribute('class','col-md-7');
                var ele_input=document.createElement('input');
                ele_input.setAttribute('type','text');
                ele_input.setAttribute('class','form-control');
                ele_input.setAttribute('name',search_method+'_'+ele_num+'_jur_per_type');

                inner_div.appendChild(ele_input);
                ele_div.appendChild(ele_label);
                ele_div.appendChild(inner_div);

                target_div.appendChild(ele_div);


            }
            else if(item=="保存机构简介")
            {
                var ele_div=document.createElement('div');
                ele_div.setAttribute('class','form-group');
                var ele_label=document.createElement('label');
                ele_label.setAttribute('class','col-md-4 lb_style');
                ele_label.innerHTML=item;
                var inner_div=document.createElement('div');
                inner_div.setAttribute('class','col-md-7');
                var ele_input=document.createElement('textarea');
                ele_input.setAttribute('name',search_method+'_'+ele_num+'_org_intro');
                ele_input.setAttribute('class','form-control');


                inner_div.appendChild(ele_input);
                ele_div.appendChild(ele_label);
                ele_div.appendChild(inner_div);

                target_div.appendChild(ele_div);
            }

            else if(item=="通讯地址")
            {
                var ele_div=document.createElement('div');
                ele_div.setAttribute('class','form-group');
                var ele_label=document.createElement('label');
                ele_label.setAttribute('class','col-md-4 lb_style');
                ele_label.innerHTML=item;
                var inner_div=document.createElement('div');
                inner_div.setAttribute('class','col-md-7');
                var ele_input=document.createElement('input');
                ele_input.setAttribute('name',search_method+'_'+ele_num+'_adr');
                ele_input.setAttribute('type','text');
                ele_input.setAttribute('class','form-control');


                inner_div.appendChild(ele_input);
                ele_div.appendChild(ele_label);
                ele_div.appendChild(inner_div);

                target_div.appendChild(ele_div);
            }
            else if(item=="邮政编码")
            {
                var ele_div=document.createElement('div');
                ele_div.setAttribute('class','form-group');
                var ele_label=document.createElement('label');
                ele_label.setAttribute('class','col-md-4 lb_style');
                ele_label.innerHTML=item;
                var inner_div=document.createElement('div');
                inner_div.setAttribute('class','col-md-7');
                var ele_input=document.createElement('input');
                ele_input.setAttribute('name',search_method+'_'+ele_num+'_post_code');
                ele_input.setAttribute('type','text');
                ele_input.setAttribute('class','form-control');


                inner_div.appendChild(ele_input);
                ele_div.appendChild(ele_label);
                ele_div.appendChild(inner_div);

                target_div.appendChild(ele_div);
            }
            else if(item=="联系人姓名")
            {
                var ele_div=document.createElement('div');
                ele_div.setAttribute('class','form-group');
                var ele_label=document.createElement('label');
                ele_label.setAttribute('class','col-md-4 lb_style');
                ele_label.innerHTML=item;
                var inner_div=document.createElement('div');
                inner_div.setAttribute('class','col-md-7');
                var ele_input=document.createElement('input');
                ele_input.setAttribute('name',search_method+'_'+ele_num+'_manager_name');
                ele_input.setAttribute('type','text');
                ele_input.setAttribute('class','form-control');


                inner_div.appendChild(ele_input);
                ele_div.appendChild(ele_label);
                ele_div.appendChild(inner_div);

                target_div.appendChild(ele_div);
            }
            else if(item=="联系电话")
            {
                var ele_div=document.createElement('div');
                ele_div.setAttribute('class','form-group');
                var ele_label=document.createElement('label');
                ele_label.setAttribute('class','col-md-4 lb_style');
                ele_label.innerHTML=item;
                var inner_div=document.createElement('div');
                inner_div.setAttribute('class','col-md-7');
                var ele_input=document.createElement('input');
                ele_input.setAttribute('name',search_method+'_'+ele_num+'_tel');
                ele_input.setAttribute('type','text');
                ele_input.setAttribute('class','form-control');


                inner_div.appendChild(ele_input);
                ele_div.appendChild(ele_label);
                ele_div.appendChild(inner_div);

                target_div.appendChild(ele_div);
            }
            else if(item=="电子邮箱")
            {
                var ele_div=document.createElement('div');
                ele_div.setAttribute('class','form-group');
                var ele_label=document.createElement('label');
                ele_label.setAttribute('class','col-md-4 lb_style');
                ele_label.innerHTML=item;
                var inner_div=document.createElement('div');
                inner_div.setAttribute('class','col-md-7');
                var ele_input=document.createElement('input');
                ele_input.setAttribute('name',search_method+'_'+ele_num+'_email');
                ele_input.setAttribute('type','text');
                ele_input.setAttribute('class','form-control');


                inner_div.appendChild(ele_input);
                ele_div.appendChild(ele_label);
                ele_div.appendChild(inner_div);

                target_div.appendChild(ele_div);
            }
            else if(item=="捐献人编号")
            {
                var ele_div=document.createElement('div');
                ele_div.setAttribute('class','form-group');
                var ele_label=document.createElement('label');
                ele_label.setAttribute('class','col-md-4 lb_style');
                ele_label.innerHTML=item;
                var inner_div=document.createElement('div');
                inner_div.setAttribute('class','col-md-7');
                var ele_input=document.createElement('input');
                ele_input.setAttribute('name',search_method+'_'+ele_num+'_don_id');
                ele_input.setAttribute('type','text');
                ele_input.setAttribute('class','form-control');


                inner_div.appendChild(ele_input);
                ele_div.appendChild(ele_label);
                ele_div.appendChild(inner_div);

                target_div.appendChild(ele_div);
            }
            else if(item=="性别")
            {
                var ele_div=document.createElement('div');
                ele_div.setAttribute('class','form-group');
                var ele_label=document.createElement('label');
                ele_label.setAttribute('class','col-md-4 lb_style');
                ele_label.innerHTML=item;
                var inner_div=document.createElement('div');
                inner_div.setAttribute('class','col-md-7');
                var sex_select=document.createElement('select');
                sex_select.setAttribute('name',search_method+'_'+ele_num+'_gender');
                sex_select.setAttribute('class','form-control');
                sex_select.options.add(new Option('男','男'));
                sex_select.options.add(new Option('女','女'));
                inner_div.appendChild(sex_select)

                ele_div.appendChild(ele_label);
                ele_div.appendChild(inner_div);

                target_div.appendChild(ele_div);
            }
            else if(item=="年龄")
            {
                var ele_div=document.createElement('div');
                ele_div.setAttribute('class','form-group');
                var ele_label=document.createElement('label');
                ele_label.setAttribute('class','col-md-4 lb_style');
                ele_label.innerHTML=item;
                var inner_div=document.createElement('div');
                inner_div.setAttribute('class','col-md-7');
                var age_select=document.createElement('select');
                age_select.setAttribute('name',search_method+'_'+ele_num+'_date_of_bir');

                age_select.setAttribute('class','form-control');
                for(var i=0;i<=150;i++)
                {
                    age_select.options.add(new Option(i,i));
                }
                inner_div.appendChild(age_select);

                ele_div.appendChild(ele_label);
                ele_div.appendChild(inner_div);

                target_div.appendChild(ele_div);
            }
            else if(item=="民族")
            {
                var ele_div=document.createElement('div');
                ele_div.setAttribute('class','form-group');
                var ele_label=document.createElement('label');
                ele_label.setAttribute('class','col-md-4 lb_style');
                ele_label.innerHTML=item;
                var inner_div=document.createElement('div');
                inner_div.setAttribute('class','col-md-7');
                var ele_input=document.createElement('input');
                ele_input.setAttribute('name',search_method+'_'+ele_num+'_eth_gro');
                ele_input.setAttribute('type','text');
                ele_input.setAttribute('class','form-control');


                inner_div.appendChild(ele_input);
                ele_div.appendChild(ele_label);
                ele_div.appendChild(inner_div);

                target_div.appendChild(ele_div);
            }
            else if(item=="籍贯")
            {
                var ele_div=document.createElement('div');
                ele_div.setAttribute('class','form-group');
                var ele_label=document.createElement('label');
                ele_label.setAttribute('class','col-md-4 lb_style');
                ele_label.innerHTML=item;
                var inner_div=document.createElement('div');
                inner_div.setAttribute('class','col-md-7');
                var ele_input=document.createElement('input');
                ele_input.setAttribute('name',search_method+'_'+ele_num+'_nativ_pla');
                ele_input.setAttribute('type','text');
                ele_input.setAttribute('class','form-control');


                inner_div.appendChild(ele_input);
                ele_div.appendChild(ele_label);
                ele_div.appendChild(inner_div);

                target_div.appendChild(ele_div);
            }
            else if(item=="出生地")
            {
                var ele_div=document.createElement('div');
                ele_div.setAttribute('class','form-group');
                var ele_label=document.createElement('label');
                ele_label.setAttribute('class','col-md-4 lb_style');
                ele_label.innerHTML=item;
                var inner_div=document.createElement('div');
                inner_div.setAttribute('class','col-md-7');
                var ele_input=document.createElement('input');
                ele_input.setAttribute('name',search_method+'_'+ele_num+'_bir_pla');
                ele_input.setAttribute('type','text');
                ele_input.setAttribute('class','form-control');


                inner_div.appendChild(ele_input);
                ele_div.appendChild(ele_label);
                ele_div.appendChild(inner_div);

                target_div.appendChild(ele_div);
            }
            else if(item=="疾病名称")
            {
                var ele_div=document.createElement('div');
                ele_div.setAttribute('class','form-group');
                var ele_label=document.createElement('label');
                ele_label.setAttribute('class','col-md-4 lb_style');
                ele_label.innerHTML=item;
                var inner_div=document.createElement('div');
                inner_div.setAttribute('class','col-md-7');
                var ele_input=document.createElement('input');
                ele_input.setAttribute('name',search_method+'_'+ele_num+'_dise_name');
                ele_input.setAttribute('type','text');
                ele_input.setAttribute('class','form-control');


                inner_div.appendChild(ele_input);
                ele_div.appendChild(ele_label);
                ele_div.appendChild(inner_div);

                target_div.appendChild(ele_div);
            }
            else if(item=="正常人群")
            {
                var ele_div=document.createElement('div');
                ele_div.setAttribute('class','form-group');
                var ele_label=document.createElement('label');
                ele_label.setAttribute('class','col-md-4 lb_style');
                ele_label.innerHTML=item;
                var inner_div=document.createElement('div');
                inner_div.setAttribute('class','col-md-7');
                var ele_input=document.createElement('input');
                ele_input.setAttribute('name',search_method+'_'+ele_num+'_normal_gro');
                ele_input.setAttribute('type','text');
                ele_input.setAttribute('class','form-control');


                inner_div.appendChild(ele_input);
                ele_div.appendChild(ele_label);
                ele_div.appendChild(inner_div);

                target_div.appendChild(ele_div);
            }
            else
            {}


    }




}

// function get_ent_date() {
//
//     var ent_date=document.getElementById('ent_date');
//     var year=document.getElementById('in_year').value;
//     var month=document.getElementById('in_month').value;
//     var day=document.getElementById('in_day').value;
//     if(Number(month)<10)
//     {
//         month="0"+month;
//     }
//
//     if (Number(day)<10)
//     {
//         day="0"+day;
//     }
//     var date=year+'-'+month+'-'+day;
//     ent_date.value=date;
//
//
//
// }

function get_acqui_time(ele) {

    var acqui_time=document.getElementById(ele.id.substr(0,2)+'_acqui_time');
    var year=document.getElementById(ele.id.substr(0,2)+'_acqui_year').value;
    var month=document.getElementById(ele.id.substr(0,2)+'_acqui_month').value;
    var day=document.getElementById(ele.id.substr(0,2)+'_acqui_day').value;
    if(Number(month)<10)
    {
        month="0"+month;
    }

    if (Number(day)<10)
    {
        day="0"+day;
    }
    var date=year+'-'+month+'-'+day;
    acqui_time.value=date;

}
//
// function get_be_year() {
//
//     var be_time=document.getElementById('be_time');
//     var year=document.getElementById('be_year').value;
//     be_time.value=year;
//
//
//
// }
//
// function get_end_year() {
//
//     var end_time=document.getElementById('end_time');
//     var year=document.getElementById('end_year').value;
//     end_time.value=year;
//
//
//
// }

function reset_item() {

    window.location="/sample/ele_search";

}