function confm() {

    var rst=confirm("确定要删除该样本信息？")
    if (rst==true)
    {
         to_delete();
    }

}

function to_update() {

    // alert(document.getElementById("inv_id").innerHTML+"    "+document.getElementById("org_name").innerHTML);

    $.ajax({
                    type: "POST",
                    url: '/to_update',
                    data: {inv_id:document.getElementById('inv_id').innerHTML,org_name:document.getElementById('org_name').innerHTML},
                    dataType: "json",
                    success: function (result) {

                    }
                })
        window.location="/sample/smpUpdate/";

}

function to_delete() {



    $.ajax({
                    type: "POST",
                    url: '/to_delete',
                    data: {sam_uni_id:document.getElementById('sam_uni_id').innerHTML},
                    dataType: "json",
                    success: function (result) {

                    }
                })
        window.location="/sample/smpdelete/";

}
