var RenderHeatmap = function(name, symbols, negativeHeat, positiveHeat) {

  return Highcharts.chart('heatmap', {

    credits: {
      enabled: false
    },
    exporting: {
      enabled: false
    },
    plotOptions: {
      bar: {
        dataLabels: {
          enabled: true,
          format: '{y:,.3f}%'
        }
      },
      series: {
        stacking: 'normal'
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
      type: 'bar'
    },
    xAxis: [
      {
        categories: symbols,
        reversed: false,
        labels: {
          step: 1
        }
      }
    ],
    yAxis: {
      title: {
        text: null
      },
      format: '{value}%'
    },
    tooltip: {
      shared: false,
      headerFormat: '<span style="font-size: 7px">{point.key}</span><br/>',
      pointFormat: '<span><b style="font-weight:bold;color:{series.color}">{point.y:,.3f}%</b><br/>'
    },
    series: [
      {
        name: 'Positive',
        data: positiveHeat,
        color: '#38BB9B'
      },
      {
        name: 'Negative',
        data: negativeHeat,
        color: '#D66F37'
      }
    ]
  });
};
