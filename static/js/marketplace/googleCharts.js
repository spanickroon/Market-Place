google.charts.load('current', {'packages':['corechart']});

let res1 = randomValues20(3200);
let res2 = randomValues20(3200);

function setUpCharts() {
    page = document.getElementById('stockgrowth-charts');

    var charts = [{title: 'Cannabis Stock Chart', chartID: 'cannabis_chart', values: res1}, {title: 'Cannabis Stock Chart2', chartID: 'cannabis_chart2', values: res2}];
    var resultHtml = [];

    for (var chart in charts) {
        resultHtml.push(`<div id=${charts[chart].chartID} class="stockgrowth-container"></div>`);
    }
    page.innerHTML = resultHtml.join('');

    setOnCallBack(charts);

    function myLoop() {        
        setTimeout(function() {  
            var charts = [{title: 'Cannabis Stock Chart', chartID: 'cannabis_chart', values: randomValues(3200, res1)}, {title: 'Cannabis Stock Chart2', chartID: 'cannabis_chart2', values: randomValues(3200, res2)}];
            setOnCallBack(charts);
            myLoop();                  
        }, 2000);
    }
    myLoop();
}

setUpCharts();

function setOnCallBack(charts) {
    google.charts.setOnLoadCallback(function() { 
        drawChart(charts);               
    });
}

function drawChart(charts) {
    for (chart in charts) {
        var lastElelement = charts[chart].values.pop();
        charts[chart].values.push(lastElelement);

        var newDate = new Date();
        var options = {
            title: `${charts[chart].title}.\nDate ${('0' + newDate.getDate()).slice(-2)}.${('0' + newDate.getMonth()).slice(-2)}.${newDate.getFullYear()} ${('0' + newDate.getHours()).slice(-2)}:${('0' + newDate.getMinutes()).slice(-2)}:${('0' + newDate.getSeconds()).slice(-2)}. Price ${lastElelement[1]}$`,
            titleTextStyle: {
                color: '#FFFFFF',
                fontSize: 24,
                bold: false
            },
            hAxis: {
                title: 'Time',
                gridlines: {
                    color: '#C4C4C4'
                },
                titleTextStyle: {
                    color: '#FFFFFF',
                    fontSize: 22
                },
                textStyle: {
                    color: '#FFFFFF',
                    fontSize: 16
                },
                slantedText: true, 
                slantedTextAngle: 45
            },
            vAxis: {
                title: 'Cost',
                minValue: 0,
                titleTextStyle: {
                    color: '#FFFFFF',
                    fontSize: 22
                },
                textStyle: {
                    color: '#FFFFFF',
                    fontSize: 14
                },            
            },   
            legend : { position: 'none'},
            colors: ['#9C2394', '#2F048C'],
            backgroundColor: {
                fill: '#232323',
                fillOpacity: 0.9
            },
        };

        var data = new google.visualization.DataTable();
        var areaChart = new google.visualization.AreaChart(document.getElementById(charts[chart].chartID));

        data.addColumn('string', 'Date');
        data.addColumn('number', 'Cost');
        data.addRows(charts[chart].values);

        areaChart.draw(data, options);
    }
}

/* Testing */

function randomValues(startNumber, res) {
    var newDate = new Date();
    res.push(
        [`${('0' + newDate.getMinutes()).slice(-2)}:${('0' + newDate.getSeconds()).slice(-2)}`, 
        Math.floor(Math.random() * 1000) + startNumber]);
    res.shift();
    return res;
}

function randomValues20(startNumber) {
    var newDate = new Date();
    var res = [];

    for (var i=0; i<20; i++) {
        newDate.setSeconds(newDate.getSeconds() + 5);
        res.push(
            [`${('0' + newDate.getMinutes()).slice(-2)}:${('0' + (newDate.getSeconds())).slice(-2)}`, 
            Math.floor(Math.random() * 1000) + startNumber]);
    }

    return res;
}