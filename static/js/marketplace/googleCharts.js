google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

function drawChart() {
    var data = new google.visualization.DataTable();
    data.addColumn('number', 'Year');
    data.addColumn('number', 'Sales');
    data.addColumn('number', 'Expenses');
    data.addRow([2013, 1000, 400])

    var options = {
      title: 'Test',
      hAxis: {title: 'Year',  titleTextStyle: {color: '#333'}},
      vAxis: {minValue: 0, titleTextStyle: {color: '#232323'}},
      animation: {
        duration: 1000,
        easing: 'out',
        startup: true
      }
    };

    var chart = new google.visualization.AreaChart(document.getElementById('chart_div'));
    chart.draw(data, options);

    var year = 2014;

    function drawf() {
        if (year > 2020) {
            data.removeRow(0);
        }

        data.addRow([year++, Math.floor(Math.random() * 1000) + 1000, Math.floor(Math.random() * 400) + 400]);
        chart.draw(data, options);
    }
   
    var i = 1;                  

    function myLoop() {        
        setTimeout(function() {  
            drawf();
            i++;
            if (i < 30) {
                myLoop();     
            }               
        }, 2200);
    }

    myLoop();
}