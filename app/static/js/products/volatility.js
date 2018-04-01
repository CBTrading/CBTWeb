var RenderVolatility = function(name, symbols, volatility) {

  return Highcharts.chart('volatility', {

    credits: {
      enabled: false
    },
    exporting: {
      enabled: false
    },
    legend: {
      enabled: false
    },
    title: {
        text: null,
        enabled: false
    },
    chart: {
        type: 'columnrange',
        inverted: true
    },
    xAxis: {
        categories: symbols
    },
    yAxis: {
        title: {
            text: null
        }
    },
    tooltip: {
        valueSuffix: '°C'
    },
    plotOptions: {
        columnrange: {
            dataLabels: {
                enabled: true,
                format: '{y}°C'
            }
        }
    },
    series: [{
        name: name,
        data: volatility,
        color: '#38BB9B'
    }]
  });
};
