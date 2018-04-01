var RenderVolatility = function(name, symbols, volatility) {

  return Highcharts.chart('volatility', {

    credits: {
      enabled: false
    },
    exporting: {
      enabled: false
    },
    plotOptions: {
      columnrange: {
        dataLabels: {
          enabled: true,
          format: '{y}%'
        }
      }
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
      },
      format: '{value}%'
    },
    tooltip: {
      pointFormat: '<span><b style="font-weight:bold;color:{series.color}">{point.low:,.3f} - {point.high:,.3f}%</b><br/>'
    },
    series: [{
      name: name,
      data: volatility,
      color: '#38BB9B'
    }]
  });
};
