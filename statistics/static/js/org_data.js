function get_org(org_name) {

    if (org_name!="请选择保存机构")
    {
         $.ajax({
                    type: "POST",
                    url: '/return_org_info/',
                    data: {org_name:org_name},
                    async:true,
                    // dataType: "json",
                    success: function (dt) {

                        show_graph(dt);

                    }
                });

    }


}


function show_graph(dt) {

    var dom = document.getElementById("show_part");
    var myChart = echarts.init(dom);
    var app = {};
    option = null;

    option = {
        tooltip: {
            trigger: 'item',
            axisPointer: {
                type: 'cross',
                crossStyle: {
                    color: '#999'
                }
            }
        },

        legend: {
            data:['上传数据量']
        },
        xAxis: [
            {
                type: 'category',
                data: dt[0],
            }
        ],
        yAxis: [
            {
                type: 'value',

                axisLabel: {
                    formatter: '{value} '
                }
            }

        ],
        dataZoom: [{
            startValue: dt[0][0]
        }, {
            type: 'inside'
        }],
        series: [
            {
                name:'上传数据量',
                type:'bar',
                barMaxWidth: '30',
                data:dt[1],
            }
            ,
            {
                 name:'数据趋势',
                 type:'line',
                 data:dt[1],
                 smooth:true,
             }
        ]
    };
    ;
    if (option && typeof option === "object") {
        myChart.setOption(option, true);
    }


}