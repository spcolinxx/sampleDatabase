function add_ele() {
    var item=document.getElementById('select_item').value;  //要添加的项的名称
    var fm=document.getElementById('search_form');   //获得表单元素
    if (item=="样本编码")
    {
        var ele_div=document.createElement('div');
        ele_div.setAttribute('class','form-group');
        var ele_label=document.createElement('label');
        ele_label.setAttribute('class','col-md-4 lb_style');
        ele_label.innerHTML=item;
        var inner_div=document.createElement('div');
        inner_div.setAttribute('class','col-md-7');
        var ele_input=document.createElement('input');
        ele_input.setAttribute('name','inv_id');
        ele_input.setAttribute('type','text');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);


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
        ele_input.setAttribute('name','sam_cate_name');
        ele_input.setAttribute('type','text');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
    }
    else if(item=="入库日期")
    {
        var ele_div=document.createElement('div');
        ele_div.setAttribute('class','form-group');
        var ele_label=document.createElement('label');
        ele_label.setAttribute('class','col-md-4 lb_style');
        ele_label.innerHTML=item;
        var inner_div=document.createElement('div');
        inner_div.setAttribute('class','col-md-7');

        var year_select=document.createElement('select');
        year_select.setAttribute('id','in_year');
        year_select.setAttribute('style','margin-right:5px;');
        year_select.setAttribute('onchange','get_ent_date()');
        var date=new Date();
        var this_year=date.getFullYear();
        for(var i=1970;i<=this_year;i++)
        {
            year_select.options.add(new Option(i, i));
        }
        var year_lb=document.createElement('label');
        year_lb.innerHTML="年";
        year_lb.setAttribute('style','margin-right:5px;');

        var month_select=document.createElement('select');
        month_select.setAttribute('id','in_month');
        month_select.setAttribute('onchange','get_ent_date()');
        month_select.setAttribute('style','margin-right:5px;');
        for(var i=1;i<=12;i++)
        {
            month_select.options.add(new Option(i,i));

        }
        var month_lb=document.createElement('label');
        month_lb.innerHTML="月";
        month_lb.setAttribute('style','margin-right:5px;');

        var day_select=document.createElement("select");
        day_select.setAttribute('id','in_day');
        day_select.setAttribute('onchange','get_ent_date()');
        day_select.setAttribute('style','margin-right:5px;');
        for(var i=1;i<=31;i++)
        {
            day_select.options.add(new Option(i,i));

        }
        var day_lb=document.createElement('label');
        day_lb.innerHTML="日";

        var ent_date_stor=document.createElement('input');
        ent_date_stor.setAttribute('style','display:none;');
        ent_date_stor.setAttribute('type','text');
        ent_date_stor.setAttribute('name','ent_date');
        ent_date_stor.setAttribute('id','ent_date');



        inner_div.appendChild(year_select);
        inner_div.appendChild(year_lb);
        inner_div.appendChild(month_select);
        inner_div.appendChild(month_lb);
        inner_div.appendChild(day_select);
        inner_div.appendChild(day_lb);


        inner_div.appendChild(ent_date_stor);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);



        var year=document.getElementById('in_year').value;
        var month=document.getElementById('in_month').value;
        var day=document.getElementById('in_day').value;
        if(Number(month)<10)
        {
            month="0"+month;
        }

        if (Number(day)<10)
        {
            day="0"+day;
        }
        var date=year+'-'+month+'-'+day;
        ent_date_stor.value=date;




    }
    else if(item=="保存温度")
    {
        var ele_div=document.createElement('div');
        ele_div.setAttribute('class','form-group');
        var ele_label=document.createElement('label');
        ele_label.setAttribute('class','col-md-4 lb_style');
        ele_label.innerHTML=item;
        var inner_div=document.createElement('div');
        inner_div.setAttribute('class','col-md-7');

        var tempr_select=document.createElement('select');
        tempr_select.setAttribute('name','stor_meth');
        tempr_select.setAttribute('class','form-control');
        tempr_select.options.add(new Option('室温','室温'));
        tempr_select.options.add(new Option('2°C～10°C','2°C～10°C'));
        tempr_select.options.add(new Option('-35°C～-18°C','-35°C～-18°C'));
        tempr_select.options.add(new Option('-85°C～-60°C','-85°C～-60°C'));
        tempr_select.options.add(new Option('-196°C～-150°C','-196°C～-150°C'));
        tempr_select.options.add(new Option('液氮','液氮'));
        tempr_select.options.add(new Option('其它方式','其它方式'));

        inner_div.appendChild(tempr_select);

        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);


    }
    else if(item=="母本编码")
    {
        var ele_div=document.createElement('div');
        ele_div.setAttribute('class','form-group');
        var ele_label=document.createElement('label');
        ele_label.setAttribute('class','col-md-4 lb_style');
        ele_label.innerHTML=item;
        var inner_div=document.createElement('div');
        inner_div.setAttribute('class','col-md-7');
        var ele_input=document.createElement('input');
        ele_input.setAttribute('name','parent_id');
        ele_input.setAttribute('type','text');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
    }
    else if(item=="分管数")
    {
        var ele_div=document.createElement('div');
        ele_div.setAttribute('class','form-group');
        var ele_label=document.createElement('label');
        ele_label.setAttribute('class','col-md-4 lb_style');
        ele_label.innerHTML=item;
        var inner_div=document.createElement('div');
        inner_div.setAttribute('class','col-md-7');
        var ele_input=document.createElement('input');
        ele_input.setAttribute('name','batch_count');
        ele_input.setAttribute('type','text');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
    }
    else if(item=="样本量")
    {
        var ele_div=document.createElement('div');
        ele_div.setAttribute('class','form-group');
        var ele_label=document.createElement('label');
        ele_label.setAttribute('class','col-md-4 lb_style');
        ele_label.innerHTML=item;
        var inner_div=document.createElement('div');
        inner_div.setAttribute('class','col-md-7');
        var ele_input=document.createElement('input');
        ele_input.setAttribute('name','sam_qty');
        ele_input.setAttribute('type','text');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
    }
    else if(item=="量单位")
    {
        var ele_div=document.createElement('div');
        ele_div.setAttribute('class','form-group');
        var ele_label=document.createElement('label');
        ele_label.setAttribute('class','col-md-4 lb_style');
        ele_label.innerHTML=item;
        var inner_div=document.createElement('div');
        inner_div.setAttribute('class','col-md-7');
        var ele_input=document.createElement('input');
        ele_input.setAttribute('name','uni_amou');
        ele_input.setAttribute('type','text');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
    }
    else if(item=="知情同意")
    {
        var ele_div=document.createElement('div');
        ele_div.setAttribute('class','form-group');
        var ele_label=document.createElement('label');
        ele_label.setAttribute('class','col-md-4 lb_style');
        ele_label.innerHTML=item;
        var inner_div=document.createElement('div');
        inner_div.setAttribute('class','col-md-7');

        var aware_select=document.createElement('select');
        aware_select.setAttribute('name','consent');
        aware_select.setAttribute('class','form-control');
        aware_select.options.add(new Option('同意',true));
        aware_select.options.add(new Option('不同意',false));
        inner_div.appendChild(aware_select)

        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
    }
    else if(item=="样本别称")
    {
         var ele_div=document.createElement('div');
        ele_div.setAttribute('class','form-group');
        var ele_label=document.createElement('label');
        ele_label.setAttribute('class','col-md-4 lb_style');
        ele_label.innerHTML=item;
        var inner_div=document.createElement('div');
        inner_div.setAttribute('class','col-md-7');
        var ele_input=document.createElement('input');
        ele_input.setAttribute('name','sam_title')
        ele_input.setAttribute('type','text');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
    }
    else if(item=="样本描述")
    {
        var ele_div=document.createElement('div');
        ele_div.setAttribute('class','form-group');
        var ele_label=document.createElement('label');
        ele_label.setAttribute('class','col-md-4 lb_style');
        ele_label.innerHTML=item;
        var inner_div=document.createElement('div');
        inner_div.setAttribute('class','col-md-7');
        var ele_input=document.createElement('textarea');
        ele_input.setAttribute('name','sam_desc');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
    }
    else if(item=="关键词")
    {
         var ele_div=document.createElement('div');
        ele_div.setAttribute('class','form-group');
        var ele_label=document.createElement('label');
        ele_label.setAttribute('class','col-md-4 lb_style');
        ele_label.innerHTML=item;
        var inner_div=document.createElement('div');
        inner_div.setAttribute('class','col-md-7');
        var ele_input=document.createElement('input');
        ele_input.setAttribute('name','sampleinfo.keyword');

        ele_input.setAttribute('type','text');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
    }
    else if(item=="样本用途")
    {
         var ele_div=document.createElement('div');
        ele_div.setAttribute('class','form-group');
        var ele_label=document.createElement('label');
        ele_label.setAttribute('class','col-md-4 lb_style');
        ele_label.innerHTML=item;
        var inner_div=document.createElement('div');
        inner_div.setAttribute('class','col-md-7');
        var ele_input=document.createElement('input');
        ele_input.setAttribute('name','sam_uses');
        ele_input.setAttribute('type','text');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
    }
    else if(item=="采集部位")
    {
         var ele_div=document.createElement('div');
        ele_div.setAttribute('class','form-group');
        var ele_label=document.createElement('label');
        ele_label.setAttribute('class','col-md-4 lb_style');
        ele_label.innerHTML=item;
        var inner_div=document.createElement('div');
        inner_div.setAttribute('class','col-md-7');
        var ele_input=document.createElement('input');
        ele_input.setAttribute('name','acqui_pos');
        ele_input.setAttribute('type','text');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
    }
    else if(item=="分析前变量")
    {
         var ele_div=document.createElement('div');
        ele_div.setAttribute('class','form-group');
        var ele_label=document.createElement('label');
        ele_label.setAttribute('class','col-md-4 lb_style');
        ele_label.innerHTML=item;
        var inner_div=document.createElement('div');
        inner_div.setAttribute('class','col-md-7');
        var ele_input=document.createElement('input');
        ele_input.setAttribute('name','s_pre_c');
        ele_input.setAttribute('type','text');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
    }
    else if(item=="采集动因")
    {
         var ele_div=document.createElement('div');
        ele_div.setAttribute('class','form-group');
        var ele_label=document.createElement('label');
        ele_label.setAttribute('class','col-md-4 lb_style');
        ele_label.innerHTML=item;
        var inner_div=document.createElement('div');
        inner_div.setAttribute('class','col-md-7');
        var ele_input=document.createElement('input');
        ele_input.setAttribute('name','acqui_mot');
        ele_input.setAttribute('type','text');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
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
        year_select.setAttribute('id','acqui_year');
        year_select.setAttribute('onchange','get_acqui_time()');
        year_select.setAttribute('style','margin-right:5px;');
        var date=new Date();
        var this_year=date.getFullYear();
        for(var i=1970;i<=this_year;i++)
        {
            year_select.options.add(new Option(i, i));
        }
        var year_lb=document.createElement('label');
        year_lb.innerHTML="年";
        year_lb.setAttribute('style','margin-right:5px;');

        var month_select=document.createElement('select');
        month_select.setAttribute('id','acqui_month');
        month_select.setAttribute('onchange','get_acqui_time()');
        month_select.setAttribute('style','margin-right:5px;');
        for(var i=1;i<=12;i++)
        {
            month_select.options.add(new Option(i,i));

        }
        var month_lb=document.createElement('label');
        month_lb.innerHTML="月";
        month_lb.setAttribute('style','margin-right:5px;');

        var day_select=document.createElement("select");
        day_select.setAttribute('id','acqui_day');
        day_select.setAttribute('onchange','get_acqui_time()');
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
        acqui_time_stor.setAttribute('name','acqui_time');
        acqui_time_stor.setAttribute('id','acqui_time');

        inner_div.appendChild(year_select);
        inner_div.appendChild(year_lb);
        inner_div.appendChild(month_select);
        inner_div.appendChild(month_lb);
        inner_div.appendChild(day_select);
        inner_div.appendChild(day_lb);
        inner_div.appendChild(acqui_time_stor);

        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);







        var year=document.getElementById('acqui_year').value;
        var month=document.getElementById('acqui_month').value;
        var day=document.getElementById('acqui_day').value;
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
    else if(item=="采集计划")
    {
        var ele_div=document.createElement('div');
        ele_div.setAttribute('class','form-group');
        var ele_label=document.createElement('label');
        ele_label.setAttribute('class','col-md-4 lb_style');
        ele_label.innerHTML=item;
        var inner_div=document.createElement('div');
        inner_div.setAttribute('class','col-md-7');
        var ele_input=document.createElement('input');
        ele_input.setAttribute('name','acqui_plan');
        ele_input.setAttribute('type','text');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
    }
    else if(item=="采集机构")
    {
        var ele_div=document.createElement('div');
        ele_div.setAttribute('class','form-group');
        var ele_label=document.createElement('label');
        ele_label.setAttribute('class','col-md-4 lb_style');
        ele_label.innerHTML=item;
        var inner_div=document.createElement('div');
        inner_div.setAttribute('class','col-md-7');
        var ele_input=document.createElement('input');
        ele_input.setAttribute('name','acqui_org');
        ele_input.setAttribute('type','text');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
    }
    else if(item=="其他采集者")
    {
        var ele_div=document.createElement('div');
        ele_div.setAttribute('class','form-group');
        var ele_label=document.createElement('label');
        ele_label.setAttribute('class','col-md-4 lb_style');
        ele_label.innerHTML=item;
        var inner_div=document.createElement('div');
        inner_div.setAttribute('class','col-md-7');
        var ele_input=document.createElement('input');
        ele_input.setAttribute('name','acqui_assis');
        ele_input.setAttribute('type','text');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
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
        ele_input.setAttribute('name','sampleinfo.org_name');
        ele_input.setAttribute('type','text');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
    }
    else if(item=="法人机构名称")
    {
        var ele_div=document.createElement('div');
        ele_div.setAttribute('class','form-group');
        var ele_label=document.createElement('label');
        ele_label.setAttribute('class','col-md-4 lb_style');
        ele_label.innerHTML=item;
        var inner_div=document.createElement('div');
        inner_div.setAttribute('class','col-md-7');
        var ele_input=document.createElement('input');
        ele_input.setAttribute('name','jur_per_name');
        ele_input.setAttribute('type','text');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
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
        ele_input.setAttribute('name','jur_per_id');
        ele_input.setAttribute('type','text');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
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
        ele_input.setAttribute('name','jur_per_type');
        ele_input.setAttribute('type','text');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
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
        ele_input.setAttribute('name','org_intro');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
    }
    else if(item=="使用许可")
    {
        var ele_div=document.createElement('div');
        ele_div.setAttribute('class','form-group');
        var ele_label=document.createElement('label');
        ele_label.setAttribute('class','col-md-4 lb_style');
        ele_label.innerHTML=item;
        var inner_div=document.createElement('div');
        inner_div.setAttribute('class','col-md-7');
        var ele_input=document.createElement('input');
        ele_input.setAttribute('name','use_agr');
        ele_input.setAttribute('type','text');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
    }
    else if(item=="共享方式")
    {
        var ele_div=document.createElement('div');
        ele_div.setAttribute('class','form-group');
        var ele_label=document.createElement('label');
        ele_label.setAttribute('class','col-md-4 lb_style');
        ele_label.innerHTML=item;
        var inner_div=document.createElement('div');
        inner_div.setAttribute('class','col-md-7');
        var ele_input=document.createElement('input');
        ele_input.setAttribute('name','share_rule');
        ele_input.setAttribute('type','text');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
    }
    else if(item=="通信地址")
    {
        var ele_div=document.createElement('div');
        ele_div.setAttribute('class','form-group');
        var ele_label=document.createElement('label');
        ele_label.setAttribute('class','col-md-4 lb_style');
        ele_label.innerHTML=item;
        var inner_div=document.createElement('div');
        inner_div.setAttribute('class','col-md-7');
        var ele_input=document.createElement('input');
        ele_input.setAttribute('name','adr');
        ele_input.setAttribute('type','text');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
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
        ele_input.setAttribute('name','post_code');
        ele_input.setAttribute('type','text');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
    }
    else if(item=="管理员")
    {
        var ele_div=document.createElement('div');
        ele_div.setAttribute('class','form-group');
        var ele_label=document.createElement('label');
        ele_label.setAttribute('class','col-md-4 lb_style');
        ele_label.innerHTML=item;
        var inner_div=document.createElement('div');
        inner_div.setAttribute('class','col-md-7');
        var ele_input=document.createElement('input');
        ele_input.setAttribute('name','manager_name');
        ele_input.setAttribute('type','text');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
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
        ele_input.setAttribute('name','tel');
        ele_input.setAttribute('type','text');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
    }
    else if(item=="电子信箱")
    {
        var ele_div=document.createElement('div');
        ele_div.setAttribute('class','form-group');
        var ele_label=document.createElement('label');
        ele_label.setAttribute('class','col-md-4 lb_style');
        ele_label.innerHTML=item;
        var inner_div=document.createElement('div');
        inner_div.setAttribute('class','col-md-7');
        var ele_input=document.createElement('input');
        ele_input.setAttribute('name','email');
        ele_input.setAttribute('type','text');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
    }
    else if(item=="捐献者匿名编号")
    {
        var ele_div=document.createElement('div');
        ele_div.setAttribute('class','form-group');
        var ele_label=document.createElement('label');
        ele_label.setAttribute('class','col-md-4 lb_style');
        ele_label.innerHTML=item;
        var inner_div=document.createElement('div');
        inner_div.setAttribute('class','col-md-7');
        var ele_input=document.createElement('input');
        ele_input.setAttribute('name','sampelinfo.donor_id');
        ele_input.setAttribute('type','text');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
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
        sex_select.setAttribute('name','col_obj');
        sex_select.setAttribute('class','form-control');
        sex_select.options.add(new Option('男','男'));
        sex_select.options.add(new Option('女','女'));
        inner_div.appendChild(sex_select)

        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
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
        age_select.setAttribute('name','date_of_bir');

        age_select.setAttribute('class','form-control');
        for(var i=0;i<=150;i++)
        {
            age_select.options.add(new Option(i,i));
        }
        inner_div.appendChild(age_select);

        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
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
        ele_input.setAttribute('name','eth_gro');
        ele_input.setAttribute('type','text');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
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
        ele_input.setAttribute('name','nativ_pla');
        ele_input.setAttribute('type','text');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
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
        ele_input.setAttribute('name','birth_pla');
        ele_input.setAttribute('type','text');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
    }
    else if(item=="国籍")
    {
        var ele_div=document.createElement('div');
        ele_div.setAttribute('class','form-group');
        var ele_label=document.createElement('label');
        ele_label.setAttribute('class','col-md-4 lb_style');
        ele_label.innerHTML=item;
        var inner_div=document.createElement('div');
        inner_div.setAttribute('class','col-md-7');
        var ele_input=document.createElement('input');
        ele_input.setAttribute('name','nation');
        ele_input.setAttribute('type','text');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
    }
    else if(item=="职业")
    {
        var ele_div=document.createElement('div');
        ele_div.setAttribute('class','form-group');
        var ele_label=document.createElement('label');
        ele_label.setAttribute('class','col-md-4 lb_style');
        ele_label.innerHTML=item;
        var inner_div=document.createElement('div');
        inner_div.setAttribute('class','col-md-7');
        var ele_input=document.createElement('input');
        ele_input.setAttribute('name','occup');
        ele_input.setAttribute('type','text');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
    }
    else if(item=="教育程度")
    {
        var ele_div=document.createElement('div');
        ele_div.setAttribute('class','form-group');
        var ele_label=document.createElement('label');
        ele_label.setAttribute('class','col-md-4 lb_style');
        ele_label.innerHTML=item;
        var inner_div=document.createElement('div');
        inner_div.setAttribute('class','col-md-7');
        var ele_input=document.createElement('input');
        ele_input.setAttribute('name','edu_lev');
        ele_input.setAttribute('type','text');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
    }
    else if(item=="婚姻状况")
    {
        var ele_div=document.createElement('div');
        ele_div.setAttribute('class','form-group');
        var ele_label=document.createElement('label');
        ele_label.setAttribute('class','col-md-4 lb_style');
        ele_label.innerHTML=item;
        var inner_div=document.createElement('div');
        inner_div.setAttribute('class','col-md-7');
        var ele_input=document.createElement('input');
        ele_input.setAttribute('name','mari_sta');
        ele_input.setAttribute('type','text');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
    }
    else if(item=="捐献途径")
    {
        var ele_div=document.createElement('div');
        ele_div.setAttribute('class','form-group');
        var ele_label=document.createElement('label');
        ele_label.setAttribute('class','col-md-4 lb_style');
        ele_label.innerHTML=item;
        var inner_div=document.createElement('div');
        inner_div.setAttribute('class','col-md-7');
        var ele_input=document.createElement('input');
        ele_input.setAttribute('name','donate_way');
        ele_input.setAttribute('type','text');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
    }
    else if(item=="疾病类目名称")
    {
        var ele_div=document.createElement('div');
        ele_div.setAttribute('class','form-group');
        var ele_label=document.createElement('label');
        ele_label.setAttribute('class','col-md-4 lb_style');
        ele_label.innerHTML=item;
        var inner_div=document.createElement('div');
        inner_div.setAttribute('class','col-md-7');
        var ele_input=document.createElement('input');
        ele_input.setAttribute('name','dise_name');
        ele_input.setAttribute('type','text');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
    }
    else if(item=="疾病类目代码")
    {
        var ele_div=document.createElement('div');
        ele_div.setAttribute('class','form-group');
        var ele_label=document.createElement('label');
        ele_label.setAttribute('class','col-md-4 lb_style');
        ele_label.innerHTML=item;
        var inner_div=document.createElement('div');
        inner_div.setAttribute('class','col-md-7');
        var ele_input=document.createElement('input');
        ele_input.setAttribute('name','dise_id');
        ele_input.setAttribute('type','text');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
    }
    else if(item=="主要诊断")
    {
        var ele_div=document.createElement('div');
        ele_div.setAttribute('class','form-group');
        var ele_label=document.createElement('label');
        ele_label.setAttribute('class','col-md-4 lb_style');
        ele_label.innerHTML=item;
        var inner_div=document.createElement('div');
        inner_div.setAttribute('class','col-md-7');
        var ele_input=document.createElement('textarea');
        ele_input.setAttribute('name','dig_desc');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
    }
    else if(item=="现病史")
    {
        var ele_div=document.createElement('div');
        ele_div.setAttribute('class','form-group');
        var ele_label=document.createElement('label');
        ele_label.setAttribute('class','col-md-4 lb_style');
        ele_label.innerHTML=item;
        var inner_div=document.createElement('div');
        inner_div.setAttribute('class','col-md-7');
        var ele_input=document.createElement('textarea');
        ele_input.setAttribute('name','dise_his');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
    }
    else if(item=="检验记录")
    {
        var ele_div=document.createElement('div');
        ele_div.setAttribute('class','form-group');
        var ele_label=document.createElement('label');
        ele_label.setAttribute('class','col-md-4 lb_style');
        ele_label.innerHTML=item;
        var inner_div=document.createElement('div');
        inner_div.setAttribute('class','col-md-7');
        var ele_input=document.createElement('textarea');
        ele_input.setAttribute('name','exa_rec');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
    }
    else if(item=="随访记录")
    {
        var ele_div=document.createElement('div');
        ele_div.setAttribute('class','form-group');
        var ele_label=document.createElement('label');
        ele_label.setAttribute('class','col-md-4 lb_style');
        ele_label.innerHTML=item;
        var inner_div=document.createElement('div');
        inner_div.setAttribute('class','col-md-7');
        var ele_input=document.createElement('textarea');
        ele_input.setAttribute('name','inter_rec');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
    }
    else if(item=="影像资料")
    {
        var ele_div=document.createElement('div');
        ele_div.setAttribute('class','form-group');
        var ele_label=document.createElement('label');
        ele_label.setAttribute('class','col-md-4 lb_style');
        ele_label.innerHTML=item;
        var inner_div=document.createElement('div');
        inner_div.setAttribute('class','col-md-7');
        var ele_input=document.createElement('input');
        ele_input.setAttribute('name','media_rec');
        ele_input.setAttribute('type','text');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
    }
    else if(item=="病例报告")
    {
        var ele_div=document.createElement('div');
        ele_div.setAttribute('class','form-group');
        var ele_label=document.createElement('label');
        ele_label.setAttribute('class','col-md-4 lb_style');
        ele_label.innerHTML=item;
        var inner_div=document.createElement('div');
        inner_div.setAttribute('class','col-md-7');
        var ele_input=document.createElement('input');
        ele_input.setAttribute('name','medi_rep');
        ele_input.setAttribute('type','text');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
    }
    else if(item=="家系信息")
    {
        var ele_div=document.createElement('div');
        ele_div.setAttribute('class','form-group');
        var ele_label=document.createElement('label');
        ele_label.setAttribute('class','col-md-4 lb_style');
        ele_label.innerHTML=item;
        var inner_div=document.createElement('div');
        inner_div.setAttribute('class','col-md-7');
        var ele_input=document.createElement('input');
        ele_input.setAttribute('name','fam_his');
        ele_input.setAttribute('type','text');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
    }
    else if(item=="课题名称")
    {
        var ele_div=document.createElement('div');
        ele_div.setAttribute('class','form-group');
        var ele_label=document.createElement('label');
        ele_label.setAttribute('class','col-md-4 lb_style');
        ele_label.innerHTML=item;
        var inner_div=document.createElement('div');
        inner_div.setAttribute('class','col-md-7');
        var ele_input=document.createElement('input');
        ele_input.setAttribute('name','prj_name');
        ele_input.setAttribute('type','text');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
    }
    else if(item=="课题编号")
    {
        var ele_div=document.createElement('div');
        ele_div.setAttribute('class','form-group');
        var ele_label=document.createElement('label');
        ele_label.setAttribute('class','col-md-4 lb_style');
        ele_label.innerHTML=item;
        var inner_div=document.createElement('div');
        inner_div.setAttribute('class','col-md-7');
        var ele_input=document.createElement('input');
        ele_input.setAttribute('name','sampleinfo.prj_id');
        ele_input.setAttribute('type','text');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
    }
    else if(item=="课题级别")
    {
        var ele_div=document.createElement('div');
        ele_div.setAttribute('class','form-group');
        var ele_label=document.createElement('label');
        ele_label.setAttribute('class','col-md-4 lb_style');
        ele_label.innerHTML=item;
        var inner_div=document.createElement('div');
        inner_div.setAttribute('class','col-md-7');
        var ele_input=document.createElement('input');
        ele_input.setAttribute('name','prj_level');
        ele_input.setAttribute('type','text');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
    }
    else if(item=="资助机构")
    {
        var ele_div=document.createElement('div');
        ele_div.setAttribute('class','form-group');
        var ele_label=document.createElement('label');
        ele_label.setAttribute('class','col-md-4 lb_style');
        ele_label.innerHTML=item;
        var inner_div=document.createElement('div');
        inner_div.setAttribute('class','col-md-7');
        var ele_input=document.createElement('input');
        ele_input.setAttribute('name','spon_org');
        ele_input.setAttribute('type','text');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
    }
    else if(item=="纳入标准")
    {
        var ele_div=document.createElement('div');
        ele_div.setAttribute('class','form-group');
        var ele_label=document.createElement('label');
        ele_label.setAttribute('class','col-md-4 lb_style');
        ele_label.innerHTML=item;
        var inner_div=document.createElement('div');
        inner_div.setAttribute('class','col-md-7');
        var ele_input=document.createElement('input');
        ele_input.setAttribute('name','in_level');
        ele_input.setAttribute('type','text');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
    }
    else if(item=="课题关键词")
    {
        var ele_div=document.createElement('div');
        ele_div.setAttribute('class','form-group');
        var ele_label=document.createElement('label');
        ele_label.setAttribute('class','col-md-4 lb_style');
        ele_label.innerHTML=item;
        var inner_div=document.createElement('div');
        inner_div.setAttribute('class','col-md-7');
        var ele_input=document.createElement('input');
        ele_input.setAttribute('name','projectinfo.keyword');
        ele_input.setAttribute('type','text');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
    }
    else if(item=="收集目的")
    {
        var ele_div=document.createElement('div');
        ele_div.setAttribute('class','form-group');
        var ele_label=document.createElement('label');
        ele_label.setAttribute('class','col-md-4 lb_style');
        ele_label.innerHTML=item;
        var inner_div=document.createElement('div');
        inner_div.setAttribute('class','col-md-7');
        var ele_input=document.createElement('input');
        ele_input.setAttribute('name','aim');
        ele_input.setAttribute('type','text');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
    }
    else if(item=="收集方法")
    {
        var ele_div=document.createElement('div');
        ele_div.setAttribute('class','form-group');
        var ele_label=document.createElement('label');
        ele_label.setAttribute('class','col-md-4 lb_style');
        ele_label.innerHTML=item;
        var inner_div=document.createElement('div');
        inner_div.setAttribute('class','col-md-7');
        var ele_input=document.createElement('input');
        ele_input.setAttribute('name','mtd');
        ele_input.setAttribute('type','text');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
    }
    else if(item=="收集数量")
    {
        var ele_div=document.createElement('div');
        ele_div.setAttribute('class','form-group');
        var ele_label=document.createElement('label');
        ele_label.setAttribute('class','col-md-4 lb_style');
        ele_label.innerHTML=item;
        var inner_div=document.createElement('div');
        inner_div.setAttribute('class','col-md-7');
        var ele_input=document.createElement('input');
        ele_input.setAttribute('name','total_amt');
        ele_input.setAttribute('type','text');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
    }
    else if(item=="起始时间")
    {
        var ele_div=document.createElement('div');
        ele_div.setAttribute('class','form-group');
        var ele_label=document.createElement('label');
        ele_label.setAttribute('class','col-md-4 lb_style');
        ele_label.innerHTML=item;
        var inner_div=document.createElement('div');
        inner_div.setAttribute('class','col-md-7');
        var ele_input=document.createElement('input');
        ele_input.setAttribute('name','be_end_time');
        ele_input.setAttribute('type','text');
        ele_input.setAttribute('class','form-control');


        inner_div.appendChild(ele_input);
        ele_div.appendChild(ele_label);
        ele_div.appendChild(inner_div);

        fm.appendChild(ele_div);
    }
    else
    {}

    var sl=document.getElementById('select_item');
    sl.options[sl.selectedIndex]=null;

    // var bt=document.getElementById('submit_bt');
    //
    // if (bt==null)
    // {
    //     var ele_div=document.createElement('div');
    //     ele_div.setAttribute('class','form-group');
    //     var inner_div=document.createElement('div');
    //     inner_div.setAttribute('class','col-md-6 col-md-offset-3');
    //     var bt=document.createElement('button');
    //     bt.setAttribute('type','submit');
    //     bt.setAttribute('class','btn btn-primary btn-block');
    //     bt.innerHTML="搜索";
    //     bt.setAttribute('id','submit_bt');
    //     inner_div.appendChild(bt);
    //     ele_div.appendChild(inner_div);
    //     fm.appendChild(ele_div);
    //
    //
    // }
    // else
    // {
    //     alert("123");
    // }




}

function get_ent_date() {

    var ent_date=document.getElementById('ent_date');
    var year=document.getElementById('in_year').value;
    var month=document.getElementById('in_month').value;
    var day=document.getElementById('in_day').value;
    if(Number(month)<10)
    {
        month="0"+month;
    }

    if (Number(day)<10)
    {
        day="0"+day;
    }
    var date=year+'-'+month+'-'+day;
    ent_date.value=date;



}

function get_acqui_time() {

    var acqui_time=document.getElementById('acqui_time');
    var year=document.getElementById('acqui_year').value;
    var month=document.getElementById('acqui_month').value;
    var day=document.getElementById('acqui_day').value;
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


// function test() {
//
//     $.ajax({
//     type: "POST",
//     url: 'test',
//     data: {},
//     dataType: "json",
//     success: function (result) {
//         alert(result);
//     }
// })
//
//
//
// }