function confm() {

    var rst=confirm("确定要删除该样本信息？")
    if (rst==true)
    {
         to_delete();
    }

}

// function to_update() {
//
//     // alert(document.getElementById("inv_id").innerHTML+"    "+document.getElementById("org_name").innerHTML);
//
//     // $.ajax({
//     //                 type: "POST",
//     //                 url: '/sample/smpUpdate/',
//     //                 data: {inv_id:document.getElementById('inv_id').innerHTML,org_name:document.getElementById('org_name').innerHTML,
//     //                     jur_per_id:document.getElementById('jur_per_id').innerHTML},
//     //                 dataType: "json",
//     //                 success: function (result) {
//     //
//     //                 }
//     //             });
//     var url="/sample/smpUpdate/"+document.getElementById('inv_id').innerHTML+"/"+document.getElementById('org_name').innerHTML+"/"+
//         document.getElementById('jur_per_id').innerHTML;
//     alert(url)
//
//
//         // window.location="/sample/smpUpdate/"+document.getElementById('inv_id').innerHTML+"/"+document.getElementById('org_name').innerHTML+"/"+
//         // document.getElementById('jur_per_id').innerHTML;
//
//
// }

// function to_delete() {
//
//
//
//     $.ajax({
//                     type: "POST",
//                     url: '/to_delete',
//                     data: {inv_id:document.getElementById('inv_id').innerHTML,org_name:document.getElementById('org_name').innerHTML,
//                         jur_per_id:document.getElementById('jur_per_id').innerHTML},
//                     dataType: "json",
//                     success: function (result) {
//
//                     }
//                 })
//         window.location="/sample/smpdelete/";
//
// }
