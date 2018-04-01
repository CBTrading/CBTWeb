var RenderCorrelations = function(name, symbols, negativeCorrelations, positiveCorrelations) {

  return Highcharts.chart('correlations', {

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
      pointFormat: '<span><b style="font-weight:bold;color:{series.color}">{point.y:,.3f}%</b><br/>'
    },
    series: [
      {
        name: 'Positive',
        data: positiveCorrelations,
        color: '#38BB9B'
      },
      {
        name: 'Negative',
        data: negativeCorrelations,
        color: '#D66F37'
      }
    ]
  });
};
