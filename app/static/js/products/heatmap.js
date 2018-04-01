var RenderHeatmap = function(name, symbols, negativeHeat, positiveHeat) {

  return Highcharts.chart('heatmap', {

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
        type: 'bar'
    },
    xAxis: [
      {
        categories: symbols,
        reversed: false,
        labels: {
            step: 1
        }
      },
      {
        opposite: true,
        reversed: false,
        categories: symbols,
        linkedTo: 0,
        labels: {
            step: 1
        }
      }
    ],
    yAxis: {
        title: {
            text: null
        },
        labels: {
            formatter: function () {
                return this.value + '%';
            }
        }
    },
    plotOptions: {
        series: {
            stacking: 'normal'
        }
    },
    tooltip: {
      shared: false,
      pointFormat: '<span><b style="color:{series.color}">{point.y:,.3f}</b><br/>'
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
