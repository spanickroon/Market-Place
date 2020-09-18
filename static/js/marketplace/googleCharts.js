function getStockValues() {
    fetch('stockgrowth', 
    {
        method: 'POST',
        headers: {'content-type': 'application/x-www-form-urlencoded', 'X-CSRFToken': getCookie('csrftoken') },
    })
    .then(response => {
        if (response.status !== 200) {
            return Promise.reject(); 
        }
        return response.json();
    })
    .then(response => {
        if (response['message'] === 'ok') {
            content_response = response['content'];
        } 
    })
    .catch(() => console.log('error response'));
    return content_response;
}

function getWindowSizes() {
    if (window.innerWidth >= 992) {
       return {width: 900, height: 400, fontTitle: 24, fontAxis: 22, fontValue: 16}
    } else if (window.innerWidth >= 768) {
        return {width: 500, height: 250, fontTitle: 14, fontAxis: 12, fontValue: 10}
    } else if (window.innerWidth >= 426) {
        return {width: 280, height: 125, fontTitle: 8, fontAxis: 7, fontValue: 4}
    } else {
        return {width: 250, height: 160, fontTitle: 8.5, fontAxis: 7, fontValue: 6}
    }
}

function setUpCharts() {
    var charts = [];

    getStockValues().forEach(element => {
        charts.push({
            title: `${element.name} Stock Chart`,
            chartID: `${element.name}_chart`,
            values: element.values
        })
    });

    page = document.getElementById('stockgrowth-charts');

    let resultHtml = [];

    for (var chart in charts) {
        resultHtml.push(`<div id=${charts[chart].chartID} class="stockgrowth-container"></div>`);
    }
    page.innerHTML = resultHtml.join('');

    setOnCallBack(charts);
}

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
        var sizes = getWindowSizes();
        var options = {
            width: sizes.width,
            height: sizes.height,
            title: `${charts[chart].title}.\nDate ${('0' + newDate.getDate()).slice(-2)}.${('0' + newDate.getMonth()).slice(-2)}.${newDate.getFullYear()} ${('0' + newDate.getHours()).slice(-2)}:${lastElelement[0]}. Price ${lastElelement[1].toFixed(2)}$`,
            titleTextStyle: {
                color: '#FFFFFF',
                fontSize: sizes.fontTitle,
                bold: false
            },
            hAxis: {
                title: 'Time',
                gridlines: {
                    color: '#C4C4C4'
                },
                titleTextStyle: {
                    color: '#FFFFFF',
                    fontSize: sizes.fontAxis
                },
                textStyle: {
                    color: '#FFFFFF',
                    fontSize: sizes.fontValue
                },
                slantedText: true, 
                slantedTextAngle: 45
            },
            vAxis: {
                title: 'Cost',
                minValue: 0,
                titleTextStyle: {
                    color: '#FFFFFF',
                    fontSize: sizes.fontAxis
                },
                textStyle: {
                    color: '#FFFFFF',
                    fontSize: sizes.fontValue
                },
                gridlines: {
                    count: 8,
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
