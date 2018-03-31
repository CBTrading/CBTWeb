var RenderHeatmaps function(name, symbols, negativeHeat, positiveHeat) {

  Highcharts.chart('container', {
      chart: {
          type: 'bar'
      },
      title: {
          text: name
      },
      xAxis: [{
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
      }],
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
      series: [{
          name: 'Negative',
          data: negativeHeat
      }, {
          name: 'Positive',
          data: positiveHeat
      }],
      credits: {
        enabled: false
      },
      exporting: {
        enabled: false
      }
  });
};
