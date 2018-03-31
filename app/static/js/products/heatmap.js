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
                return Math.abs(this.value) + '%';
            }
        }
    },
    plotOptions: {
        series: {
            stacking: 'normal'
        }
    },
    tooltip: {
        formatter: function () {
            return '<b>' + this.series.name + ', age ' + this.point.category + '</b><br/>' +
                'Population: ' + Highcharts.numberFormat(Math.abs(this.point.y), 0);
        }
    },
    series: [
      {
        name: 'Positive',
        data: positiveHeat
      },
      {
        name: 'Negative',
        data: negativeHeat
      }
    ],
    credits: {
      enabled: false
    },
    exporting: {
      enabled: false
    }
  });
};
