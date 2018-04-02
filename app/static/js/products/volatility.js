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
          format: '{y:,.2f}%'
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
      headerFormat: '<span style="font-size: 10px">{point.key}</span><br/>',
      pointFormat: '<span><b style="font-weight:bold;color:{series.color}">{point.low:,.2f} - {point.high:,.2f}%</b><br/>'
    },
    series: [{
      name: name,
      data: volatility,
      color: '#38BB9B'
    }]
  });
};
